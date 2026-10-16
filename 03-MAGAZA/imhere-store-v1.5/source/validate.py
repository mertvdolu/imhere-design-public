"""Read-only artwork/source audit. --write saves evidence before manifest generation."""
from pathlib import Path
import base64,hashlib,json,sys,xml.etree.ElementTree as ET
from PIL import Image,ImageFont
R=Path(__file__).resolve().parents[1];NS={'s':'http://www.w3.org/2000/svg'}
def load(p):return json.loads((R/p).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
copy=load('source/copy.en-GB.json');d=load('DELIVERY.json');p=load('source/capture-provenance.json')
brief=(R/'source/evidence/FOUNDER-BRIEF.txt').read_text();results=[]
assert len(d['assets'])==18 and len(p['captures'])==12
for s in copy['shots']:
    assert s['title'] in brief and s['subtitle'] in brief
    assert ' '.join(s['lines'])==s['title']
    assert 'linkedin' not in (s['title']+s['subtitle']).lower()
for s in p['captures']:
    assert sha(R/s['file'])==s['sha256']
    with Image.open(R/s['file']) as im:assert im.size==(s['width'],s['height'])
for a in d['assets']:
    im=Image.open(R/a['file']);assert im.mode=='RGB' and im.format=='PNG' and im.size==(a['width'],a['height'])
    tree=ET.parse(R/a['sourceSvg']);images=tree.findall('.//s:image',NS)
    assert len(images)==2,'Only brand mark and intact native image permitted'
    native=[n for n in images if n.get('href','').startswith('data:image/png;base64,')];assert len(native)==1
    n=native[0];assert hashlib.sha256(base64.b64decode(n.get('href').split(',',1)[1])).hexdigest()==a['nativeSha256']
    assert n.get('clip-path') is None and n.get('filter') is None
    g=a['geometry'];assert float(n.get('width'))==g['sourceWidth'] and float(n.get('height'))==g['sourceHeight']
    assert abs(g['width']/g['height']-g['sourceWidth']/g['sourceHeight'])<1e-10
    assert g['x']>=0 and g['x']+g['width']<=g['designWidth'] and g['y']+g['height']<g['designHeight']-60
    shot=next(s for s in copy['shots'] if s['id']==a['shot']);texts=tree.findall('.//s:text',NS)
    strings=[''.join(n.itertext()) for n in texts]
    footer=copy['filterDisclosure'] if a['shot']=='03-filters' else copy['disclosure']
    assert strings==[copy['brand'],*shot['lines'],shot['subtitle'],footer],a['file']
    fits=[]
    for n,s in zip(texts,strings):
        size=float(n.get('font-size'));style='Medium' if n.get('font-weight')=='500' else 'Regular'
        font=ImageFont.truetype(str(R/f'assets/Geist-{style}.ttf'),round(size));length=font.getlength(s)+(len(s)-1)*float(n.get('letter-spacing','0'))
        x=float(n.get('x'));y=float(n.get('y'));left=x-length/2 if n.get('text-anchor')=='middle' else x
        assert left>=0 and left+length<=g['designWidth'] and y-size>=0 and y<=g['designHeight'],s
        if s==shot['subtitle']:assert y+size*.25<g['y']-(22 if a['platform']=='ios' else 16)
        if s==footer:assert y-size>g['y']+g['height']+(22 if a['platform']=='ios' else 16)
        fits.append({'text':s,'width':round(length,2),'fits':True})
    results.append({'file':a['file'],'size':im.size,'opaqueRGB':True,'embeddedNativeHashMatches':True,'fullFrameUniformScale':True,'nativeOverlays':0,'exactCopy':True,'textFit':fits})
feature=p['feature'];assert sha(R/feature['file'])==feature['sha256']
with Image.open(R/feature['file']) as im:assert im.mode=='RGB' and im.size==(1024,500)
featuretexts=' '.join(''.join(x.itertext()) for x in ET.parse(R/feature['sourceSvg']).findall('.//s:text',NS))
assert 'purpose' not in featuretexts.lower() and 'amaç' not in featuretexts.lower()
def lum(h):
    v=[int(h[i:i+2],16)/255 for i in (1,3,5)];v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in v]
    return sum(x*y for x,y in zip(v,[.2126,.7152,.0722]))
def contrast(a,b):
    lo,hi=sorted([lum(a),lum(b)]);return (hi+.05)/(lo+.05)
ratios={c:round(contrast(c,'#F4F1E9'),3) for c in ['#191A17','#696A62']};assert min(ratios.values())>=4.5
report={'status':'PASS','screenshots':18,'nativeSources':12,'featureGraphics':1,'allOpaqueRGB':True,'nativeContentUnchanged':True,'featureByteIdenticalTo14':True,'marketingTextContrast':ratios,'assets':results,'limits':['Artwork audit, not native application QA or store acceptance.','Native clocks, battery icons, UI wording, people and counts retained as supplied.','1.4 request-profile sources retained independently for iOS and Android.']}
if '--write' in sys.argv:(R/'evidence/artwork-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
else:
    manifest=load('MANIFEST.json');actual={str(f.relative_to(R)) for f in R.rglob('*') if f.is_file() and f.name not in ['MANIFEST.json','.DS_Store'] and '__pycache__' not in f.parts}
    assert actual=={f['file'] for f in manifest['files']}
    assert all(sha(R/f['file'])==f['sha256'] and (R/f['file']).stat().st_size==f['bytes'] for f in manifest['files'])
print('PASS: 18 RGB screenshots, 12 intact native sources, exact supplied copy, no crop/overlay, text fit, contrast; unchanged 1024x500 feature.'+(' Manifest verified.' if '--write' not in sys.argv else ''))
