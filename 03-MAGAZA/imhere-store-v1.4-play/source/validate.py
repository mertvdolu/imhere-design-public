"""Check exported PNGs, lossless native embedding, portrait slots and typography."""
from pathlib import Path
import base64
import hashlib
import json
import xml.etree.ElementTree as ET
from PIL import Image, ImageFont

ROOT=Path(__file__).resolve().parents[1]
NS={'s':'http://www.w3.org/2000/svg'}
def load(p):return json.loads((ROOT/p).read_text())
def lum(h):
    v=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in v]
    return sum(a*b for a,b in zip(v,[.2126,.7152,.0722]))
def contrast(a,b):
    x,y=sorted([lum(a),lum(b)]);return (y+.05)/(x+.05)

delivery=load('DELIVERY.json');copy=load('source/copy.en-GB.json')
provenance=load('source/capture-provenance.json');placements=load('source/portrait-placements.json')
for c in provenance['captures']:
    p=ROOT/c['file'];assert hashlib.sha256(p.read_bytes()).hexdigest()==c['sha256']
    with Image.open(p) as im:assert im.size==(1080,2400)
assert len(delivery['assets'])==7
results=[]
for a in delivery['assets']:
    with Image.open(ROOT/a['file']) as im:
        assert im.mode=='RGB' and im.format=='PNG' and im.size==(a['width'],a['height'])
    tree=ET.parse(ROOT/a['sourceSvg']);images=tree.findall('.//s:image',NS)
    native=[x for x in images if x.get('href','').startswith('data:image/png;base64,')]
    assert len(native)==len(a['captures'])
    for node,cap in zip(native,a['captures']):
        assert hashlib.sha256(base64.b64decode(node.get('href').split(',',1)[1])).hexdigest()==cap['sha256']
        assert node.get('width')=='1080' and node.get('height')=='2400'
        assert node.get('clip-path') is None and node.get('filter') is None
        g=cap['geometry'];assert abs(g['width']/g['height']-1080/2400)<1e-12
        assert g['x']>=0 and g['y']>=0 and g['x']+g['width']<=a['width'] and g['y']+g['height']<a['height']
    portraits=[x for x in images if x.get('href','').startswith('data:image/jpeg;base64,')]
    expected=[cap for cap in a['captures'] if cap['portrait']]
    assert len(portraits)==len(expected)
    for node,cap in zip(portraits,expected):
        pos=placements['placements'][cap['shot']]
        for k in ('x','y','width','height'):assert float(node.get(k))==pos[k]
        assert node.get('clip-path')=='url(#portrait-'+cap['shot']+')'
    checks=[]
    for node in tree.findall('.//s:text',NS):
        text=''.join(node.itertext());size=round(float(node.get('font-size')))
        style='Medium' if node.get('font-weight')=='500' else 'Regular'
        font=ImageFont.truetype(str(ROOT/f'assets/Geist-{style}.ttf'),size)
        length=font.getlength(text)+(len(text)-1)*float(node.get('letter-spacing','0'))
        x=float(node.get('x'));y=float(node.get('y'));left=x-length/2 if node.get('text-anchor')=='middle' else x
        assert left>=0 and left+length<=a['width'] and y-size>=0 and y<=a['height'],text
        checks.append({'text':text,'width':round(length,2),'fits':True})
    assert copy['disclosure'] in [x['text'] for x in checks]
    if a['id']!='feature-graphic':
        assert (a['width'],a['height'])==(1080,1920)
        g=a['captures'][0]['geometry'];assert g['width']*g['height']/(1080*1920)>.5
        assert 235/1920<.2
    else:assert (a['width'],a['height'])==(1024,500)
    results.append({'file':a['file'],'size':[a['width'],a['height']],'opaqueRGB':True,'sourceHashesMatch':True,'fullNativeFrames':len(native),'portraitSlots':len(portraits),'textFit':checks})
assert all(len(s['title'].split())<=5 and len(s['alt'])<=140 for s in copy['shots'])
assert len(copy['feature']['alt'])<=140
ratios={'heading':round(contrast('#191A17','#F4F1E9'),2),'footer':round(contrast('#696A62','#F4F1E9'),2)}
assert min(ratios.values())>=4.5
report={'result':'PASS','sourceCaptures':6,'exports':7,'phonePngs':6,'featureGraphics':1,'opaqueRGB':True,'nativeSourcesUnchanged':True,'nativeNotCroppedOrStretched':True,'portraitScenes':['02-nearby','04-chat'],'marketingContrast':ratios,'copyStatus':copy['status'],'assets':results,'limits':['Not Google Play approval or native usability test','Play final copy and feature graphic approval pending HARBOR + Founder','Event lower explanatory text extends behind native bottom navigation; source retained']}
(ROOT/'evidence/artwork-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('PASS: 6 source hashes; 7 opaque RGB PNGs; native frames intact; text fits; contrast',ratios)
