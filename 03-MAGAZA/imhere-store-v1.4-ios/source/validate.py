"""Validate exported artwork, actual source hashes, editable SVGs and text fit."""
from pathlib import Path
import base64
import hashlib
import json
import xml.etree.ElementTree as ET
from PIL import Image, ImageFont

ROOT=Path(__file__).resolve().parents[1]
NS={'s':'http://www.w3.org/2000/svg'}
def load(p): return json.loads((ROOT/p).read_text())
def luminance(h):
    vals=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    vals=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in vals]
    return sum(a*b for a,b in zip(vals,[.2126,.7152,.0722]))
def contrast(a,b):
    x,y=sorted([luminance(a),luminance(b)])
    return (y+.05)/(x+.05)

delivery=load('DELIVERY.json');copy=load('source/copy.en-GB.json');provenance=load('source/capture-provenance.json')
expected=load('source/portrait-placements.json')['placements'];results=[]
for src in provenance['captures']:
    assert hashlib.sha256((ROOT/src['file']).read_bytes()).hexdigest()==src['sha256'],src['file']
    assert Image.open(ROOT/src['file']).size==(1206,2622)
for a in delivery['assets']:
    p=ROOT/a['file'];im=Image.open(p)
    assert im.format=='PNG' and im.mode=='RGB' and im.size==(a['width'],a['height']),a['file']
    tree=ET.parse(ROOT/a['sourceSvg']); images=tree.findall('.//s:image',NS)
    native=[i for i in images if i.get('href','').startswith('data:image/png;base64,')]
    assert len(native)==1
    assert hashlib.sha256(base64.b64decode(native[0].get('href').split(',',1)[1])).hexdigest()==a['nativeSourceSha256']
    assert native[0].get('width')=='1206' and native[0].get('height')=='2622'
    assert native[0].get('clip-path') is None and native[0].get('filter') is None
    portrait=[i for i in images if i.get('href','').startswith('data:image/jpeg;base64,')]
    expected_pos=expected.get(a['shot'])
    assert len(portrait)==(1 if expected_pos else 0)
    if expected_pos:
        for k in ['x','y','width','height']: assert float(portrait[0].get(k))==expected_pos[k]
        assert portrait[0].get('clip-path')=='url(#portrait-slot)'
    g=a['nativeGeometry']
    assert abs(g['width']/g['height']-1206/2622)<1e-10
    assert g['x']>=0 and g['y']>=0 and g['x']+g['width']<=g['designWidth'] and g['y']+g['height']<g['designHeight']-100
    text_checks=[]
    for node in tree.findall('.//s:text',NS):
        s=''.join(node.itertext()); size=round(float(node.get('font-size')))
        style='Medium' if node.get('font-weight')=='500' else 'Regular'
        font=ImageFont.truetype(str(ROOT/'assets'/f'Geist-{style}.ttf'),size)
        length=font.getlength(s)+(len(s)-1)*float(node.get('letter-spacing','0'))
        x=float(node.get('x'));y=float(node.get('y'));left=x-length/2 if node.get('text-anchor')=='middle' else x
        assert left>=0 and left+length<=g['designWidth'] and y-size>=0 and y<=g['designHeight'],s
        text_checks.append({'text':s,'widthInDesignUnits':round(length,2),'fits':True})
    results.append({'file':a['file'],'size':[im.width,im.height],'mode':im.mode,'nativeEmbeddedHashMatches':True,'nativeFullFrame':True,'portraitSlots':len(portrait),'textFit':text_checks})
assert len(results)==18 and sum(x['portraitSlots'] for x in results)==6
assert all(len(s['title'].split())<=5 for s in copy['shots'])
ratios={'heading':round(contrast('#191A17','#F4F1E9'),2),'footer':round(contrast('#696A62','#F4F1E9'),2)}
assert min(ratios.values())>=4.5
report={'result':'PASS','sourceCaptures':6,'exports':18,'sets':3,'opaqueRGB':True,'nativeSourcesUnchanged':True,'nativeNotCroppedOrStretched':True,'portraitScenes':['02-nearby','04-chat'],'marketingContrast':ratios,'copyStatus':copy['status'],'assets':results,'limits':['Not App Store approval','Not a native usability or build test','Source event actions partly behind native bottom navigation; source is preserved']}
(ROOT/'evidence/artwork-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('PASS: 6 source hashes; 18 RGB PNGs; embedded native images intact; 2 portrait slots per set; text fits; contrast',ratios)
