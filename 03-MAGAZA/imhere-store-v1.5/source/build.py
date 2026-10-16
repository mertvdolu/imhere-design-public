"""1.4 store composition, exact 1.5 copy, intact native screenshots. No retouching."""
from pathlib import Path
import base64, hashlib, html, json

ROOT = Path(__file__).resolve().parents[1]
def load(name): return json.loads((ROOT/name).read_text())
def data(path, mime): return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()
def txt(value, x, y, size, weight=400, colour='#191A17', anchor='start', tracking=0):
    return f'<text x="{x}" y="{y}" font-family="Geist" font-size="{size}" font-weight="{weight}" fill="{colour}" text-anchor="{anchor}" letter-spacing="{tracking}">{html.escape(value)}</text>'

def main():
    copy=load('source/copy.en-GB.json'); provenance=load('source/capture-provenance.json')
    sources={c['file']:c for c in provenance['captures']}
    css=''.join('@font-face{font-family:Geist;font-weight:'+str(weight)+';src:url('+data(ROOT/f'assets/Geist-{style}.woff2','font/woff2')+')}' for weight,style in [(400,'Regular'),(500,'Medium')])
    mark=data(ROOT/'assets/imhere-mark-icon-weight.svg','image/svg+xml')
    assets=[]
    for folder,width,height,platform in [('ios-15-1206x2622',1206,2622,'ios'),('ios-15-1320x2868',1320,2868,'ios'),('play-15-phone',1080,1920,'android')]:
        ios=platform=='ios'; w=1320 if ios else 1080; h=height*w/width
        sy=500 if ios else 330; sh=h-sy-(158 if ios else 84)
        pad=22 if ios else 16; radius=62 if ios else 44; shadow=10 if ios else 8
        defs=f'<defs><filter id="soft-surface" x="-30%" y="-20%" width="160%" height="140%" color-interpolation-filters="sRGB"><feDropShadow dx="{shadow}" dy="{shadow}" stdDeviation="{shadow}" flood-color="#D6D2C8"/><feDropShadow dx="-{shadow}" dy="-{shadow}" stdDeviation="{shadow}" flood-color="#FFFEFA"/></filter></defs>'
        for shot in copy['shots']:
            nativepath=f'source/native/{platform}/{shot["source"]}'; src=ROOT/nativepath; meta=sources[nativepath]
            digest=hashlib.sha256(src.read_bytes()).hexdigest(); assert digest==meta['sha256']
            nw,nh=meta['width'],meta['height']; sw=sh*nw/nh; sx=(w-sw)/2
            ops=[f'<rect width="{w}" height="{h}" fill="#F4F1E9"/>']
            if ios:
                ops += [f'<image x="86" y="67" width="54" height="34.245" href="{mark}"/>',txt(copy['brand'],169,96,28,500,tracking=2),txt(shot['lines'][0],82,238,112,500,tracking=-4),txt(shot['lines'][1],82,356,112,500,tracking=-4),txt(shot['subtitle'],86,426,34,colour='#696A62')]
            else:
                ops += [f'<image x="82" y="36" width="44" height="27.903" href="{mark}"/>',txt(copy['brand'],149,61,24,500,tracking=1.7),txt(shot['lines'][0],78,146,82,500,tracking=-3),txt(shot['lines'][1],78,235,82,500,tracking=-3),txt(shot['subtitle'],82,287,28,colour='#696A62')]
            ops += [f'<rect x="{sx-pad}" y="{sy-pad}" width="{sw+pad*2}" height="{sh+pad*2}" rx="{radius}" fill="#F4F1E9" stroke="#B7B3A9" stroke-width="1.5" filter="url(#soft-surface)"/>',f'<svg x="{sx}" y="{sy}" width="{sw}" height="{sh}" viewBox="0 0 {nw} {nh}"><image width="{nw}" height="{nh}" href="{data(src,"image/png")}"/></svg>']
            disclosure=copy['filterDisclosure'] if shot['id']=='03-filters' else copy['disclosure']
            ops.append(txt(disclosure,w/2,h-41 if ios else 1887,28 if ios else 23,colour='#696A62',anchor='middle'))
            svg=f'source/svg/{folder}/{shot["id"]}.svg'; dest=ROOT/svg;dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{html.escape(shot["title"])}</title><desc id="desc">{html.escape(shot["subtitle"]+" "+disclosure)}</desc><style>{css}</style>{defs}'+''.join(ops)+'</svg>\n')
            assets.append({'file':f'{folder}/{shot["id"]}.png','sourceSvg':svg,'shot':shot['id'],'platform':platform,'width':width,'height':height,'nativeSource':nativepath,'nativeSha256':digest,'geometry':{'x':sx,'y':sy,'width':sw,'height':sh,'designWidth':w,'designHeight':h,'sourceWidth':nw,'sourceHeight':nh},'portraitOverlays':0,'crop':'none','disclosure':disclosure})
    (ROOT/'DELIVERY.json').write_text(json.dumps({'package':'IM HERE store 1.5','theme':'Cream & Ink v2.3','date':'2026-10-16','copyStatus':copy['status'],'assets':assets,'feature':provenance['feature']},ensure_ascii=False,indent=2)+'\n')
    print('Built 18 SVGs. All native frames unchanged; no portrait or status bar overlays.')
if __name__=='__main__':main()
