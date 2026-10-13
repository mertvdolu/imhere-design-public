"""Build editable store SVGs from complete, unchanged iOS captures.

Only the two authorised native portrait slots receive an SVG image overlay.
No native text, control, colour, frame, timestamp or scroll position is repainted.
Python 3 standard library; render.cjs uses sharp and included Geist fonts.
"""
from pathlib import Path
import base64
import hashlib
import html
import json

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'

def read_json(path):
    return json.loads((ROOT / path).read_text())

def data(path, mime):
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()

def txt(value, x, y, size, weight=400, colour='#191A17', anchor='start', tracking=0):
    return (f'<text x="{x}" y="{y}" font-family="Geist" font-size="{size}" '
            f'font-weight="{weight}" fill="{colour}" text-anchor="{anchor}" '
            f'letter-spacing="{tracking}">{html.escape(value)}</text>')

def main():
    copy = read_json('source/copy.en-GB.json')
    portraits = read_json('source/portrait-placements.json')
    provenance = read_json('source/capture-provenance.json')
    expected = {x['file']: x['sha256'] for x in provenance['captures']}
    css = ''.join('@font-face{font-family:Geist;font-weight:' + str(weight) +
                  ';src:url(' + data(ASSETS / f'Geist-{style}.woff2', 'font/woff2') + ')}'
                  for weight, style in [(400, 'Regular'), (500, 'Medium')])
    sets = [('iphone-6.9', 1320, 2868), ('iphone-6.5', 1242, 2688),
            ('iphone-dynamic-island-medium', 1206, 2622)]
    deliveries = []
    for folder, width, height in sets:
        # A 1320-wide design coordinate space; export geometry adapts to aspect ratio.
        w, h = 1320, height * 1320 / width
        screen_y = 444
        screen_h = h - screen_y - 158
        screen_w = screen_h * 1206 / 2622
        screen_x = (w - screen_w) / 2
        padding = 22
        for shot in copy['shots']:
            native_path = 'source/native/ios/' + shot['source']
            src = ROOT / native_path
            digest = hashlib.sha256(src.read_bytes()).hexdigest()
            if digest != expected[native_path]:
                raise ValueError('Source hash changed: ' + native_path)
            ops = [f'<rect width="{w}" height="{h}" fill="#F4F1E9"/>',
                f'<image x="86" y="67" width="54" height="34.245" href="{data(ASSETS / "imhere-mark-icon-weight.svg", "image/svg+xml")}"/>',
                txt(copy['brand'], 169, 96, 28, 500, tracking=2),
                txt(shot['lines'][0], 82, 238, 112, 500, tracking=-4),
                txt(shot['lines'][1], 82, 356, 112, 500, tracking=-4)]
            # Cream-and-Ink raised surround is outside all original native pixels.
            ops.append(f'<rect x="{screen_x-padding}" y="{screen_y-padding}" width="{screen_w+padding*2}" height="{screen_h+padding*2}" rx="62" fill="#F4F1E9" stroke="#B7B3A9" stroke-width="1.5" filter="url(#soft-surface)"/>')
            native = f'<image width="1206" height="2622" href="{data(src,"image/png")}"/>'
            pos = portraits['placements'].get(shot['id'])
            if pos:
                x,y,pw,ph,r = [pos[k] for k in ('x','y','width','height','radius')]
                native += (f'<defs><clipPath id="portrait-slot"><rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="{r}"/></clipPath></defs>'
                           f'<image x="{x}" y="{y}" width="{pw}" height="{ph}" preserveAspectRatio="xMidYMid slice" clip-path="url(#portrait-slot)" href="{data(ROOT/portraits["asset"],"image/jpeg")}"/>')
            ops.append(f'<svg x="{screen_x}" y="{screen_y}" width="{screen_w}" height="{screen_h}" viewBox="0 0 1206 2622">{native}</svg>')
            if shot['id'] == '06-area-activity':
                ops.append(txt(copy['mapCredit'], w/2, h-84, 25, colour='#696A62', anchor='middle'))
            ops.append(txt(copy['disclosure'], w/2, h-41, 28, colour='#696A62', anchor='middle'))
            defs = ('<defs><filter id="soft-surface" x="-20%" y="-10%" width="150%" height="130%" color-interpolation-filters="sRGB">'
                    '<feDropShadow dx="10" dy="10" stdDeviation="10" flood-color="#D6D2C8"/>'
                    '<feDropShadow dx="-10" dy="-10" stdDeviation="10" flood-color="#FFFEFA"/>'
                    '</filter></defs>')
            output = f'app-store/{folder}/{shot["id"]}.png'
            svg_path = f'source/svg/{folder}/{shot["id"]}.svg'
            target = ROOT / svg_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{html.escape(shot["title"])}</title><desc id="desc">{html.escape(shot["alt"])}</desc><style>{css}</style>{defs}' + ''.join(ops) + '</svg>\n')
            deliveries.append({'file':output, 'sourceSvg':svg_path, 'shot':shot['id'],
                'width':width,'height':height,'nativeSource':native_path,
                'nativeSourceSha256':digest, 'portrait':pos,
                'nativeGeometry':{'x':screen_x,'y':screen_y,'width':screen_w,'height':screen_h,'designWidth':w,'designHeight':h,'sourceWidth':1206,'sourceHeight':2622},
                'crop':'none; entire source uniformly scaled', 'copyStatus':copy['status']})
    (ROOT/'DELIVERY.json').write_text(json.dumps({'package':'STORE-IOS-14','theme':'Cream & Ink v2.3','appVersion':'1.4.0 (19)',
       'status':'DESIGN EXPORTED — '+copy['status'], 'revision':'R2',
       'platform':'iPhone only','copyStatus':copy['status'],'assets':deliveries},ensure_ascii=False,indent=2)+'\n')
    print('Built',len(deliveries),'editable SVG compositions from 6 verified native sources.')

if __name__ == '__main__':
    main()
