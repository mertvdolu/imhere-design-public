"""Compose Google Play SVG artwork from unchanged Android captures.

Native captures stay complete and uniformly scaled. Synthetic portraits cover
only the two existing photo slots; no app UI, clock or system element is drawn.
"""
from pathlib import Path
import base64
import hashlib
import html
import json

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    return json.loads((ROOT / name).read_text())

def data(path, mime):
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()

def txt(value, x, y, size, weight=400, colour='#191A17', anchor='start', tracking=0):
    return (f'<text x="{x}" y="{y}" font-family="Geist" font-size="{size}" '
            f'font-weight="{weight}" fill="{colour}" text-anchor="{anchor}" '
            f'letter-spacing="{tracking}">{html.escape(value)}</text>')

def main():
    copy = load('source/copy.en-GB.json')
    placements = load('source/portrait-placements.json')
    expected = {c['file']: c['sha256'] for c in load('source/capture-provenance.json')['captures']}
    shots = {s['id']: s for s in copy['shots']}
    css = ''.join('@font-face{font-family:Geist;font-weight:' + str(weight) + ';src:url(' +
                  data(ROOT / f'assets/Geist-{style}.woff2', 'font/woff2') + ')}'
                  for weight, style in [(400, 'Regular'), (500, 'Medium')])
    defs = ('<defs><filter id="soft-surface" x="-30%" y="-20%" width="160%" height="140%" color-interpolation-filters="sRGB">'
            '<feDropShadow dx="8" dy="8" stdDeviation="8" flood-color="#D6D2C8"/>'
            '<feDropShadow dx="-8" dy="-8" stdDeviation="8" flood-color="#FFFEFA"/>'
            '</filter></defs>')
    mark = data(ROOT / 'assets/imhere-mark-icon-weight.svg', 'image/svg+xml')
    deliveries = []

    def native(shot_id, x, y, height, padding=16, radius=44):
        shot = shots[shot_id]
        path = 'source/native/android/' + shot['source']
        digest = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        assert digest == expected[path], path
        width = height * 1080 / 2400
        image = f'<image width="1080" height="2400" href="{data(ROOT / path, "image/png")}"/>'
        pos = placements['placements'].get(shot_id)
        if pos:
            px, py, pw, ph, r = [pos[k] for k in ('x', 'y', 'width', 'height', 'radius')]
            image += (f'<defs><clipPath id="portrait-{shot_id}"><rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="{r}"/></clipPath></defs>'
                      f'<image x="{px}" y="{py}" width="{pw}" height="{ph}" preserveAspectRatio="xMidYMid slice" '
                      f'clip-path="url(#portrait-{shot_id})" href="{data(ROOT / placements["asset"], "image/jpeg")}"/>')
        markup = (f'<rect x="{x-padding}" y="{y-padding}" width="{width+padding*2}" height="{height+padding*2}" '
                  f'rx="{radius}" fill="#F4F1E9" stroke="#B7B3A9" stroke-width="1.5" filter="url(#soft-surface)"/>'
                  f'<svg x="{x}" y="{y}" width="{width}" height="{height}" viewBox="0 0 1080 2400">{image}</svg>')
        return markup, {'shot': shot_id, 'nativeSource': path, 'sha256': digest, 'portrait': pos,
                        'geometry': {'x': x, 'y': y, 'width': width, 'height': height, 'sourceWidth': 1080, 'sourceHeight': 2400},
                        'crop': 'none; full Android native frame uniformly scaled'}

    def save(id, width, height, title, alt, ops, captures, file):
        source = 'source/svg/' + id + '.svg'
        (ROOT / source).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">'
                                  f'<title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(alt)}</desc><style>{css}</style>{defs}' + ''.join(ops) + '</svg>\n')
        deliveries.append({'file': file, 'sourceSvg': source, 'id': id, 'width': width, 'height': height,
                           'captures': captures, 'copyStatus': copy['status']})

    for shot in copy['shots']:
        ops = ['<rect width="1080" height="1920" fill="#F4F1E9"/>',
               f'<image x="82" y="36" width="44" height="27.903" href="{mark}"/>',
               txt(copy['brand'], 149, 61, 24, 500, tracking=1.7),
               txt(shot['lines'][0], 78, 146, 82, 500, tracking=-3),
               txt(shot['lines'][1], 78, 235, 82, 500, tracking=-3)]
        markup, capture = native(shot['id'], 189, 276, 1560)
        ops.append(markup)
        if shot['id'] == '06-area-activity':
            ops.append(txt(copy['mapCredit'], 540, 1870, 19, colour='#696A62', anchor='middle'))
        ops.append(txt(copy['disclosure'], 540, 1900 if shot['id'] == '06-area-activity' else 1887,
                       23, colour='#696A62', anchor='middle'))
        save(shot['id'], 1080, 1920, shot['title'], shot['alt'], ops, [capture], 'google-play/phone/' + shot['id'] + '.png')

    feature = copy['feature']
    ops = ['<rect width="1024" height="500" fill="#F4F1E9"/>',
           f'<image x="64" y="97" width="68" height="43.125" href="{mark}"/>',
           txt(copy['brand'], 158, 133, 27, 500, tracking=1.7),
           txt(feature['lines'][0], 64, 236, 54, 500, tracking=-1.7),
           txt(feature['lines'][1], 64, 300, 54, 500, tracking=-1.7)]
    captures = []
    for shot_id, x in [('02-nearby', 566), ('04-chat', 777)]:
        markup, capture = native(shot_id, x, 62, 380, padding=10, radius=28)
        ops.append(markup); captures.append(capture)
    ops.append(txt(copy['disclosure'], 512, 480, 16, colour='#696A62', anchor='middle'))
    save('feature-graphic', 1024, 500, feature['title'], feature['alt'], ops, captures, 'google-play/feature-graphic.png')
    (ROOT / 'DELIVERY.json').write_text(json.dumps({'package':'STORE-IOS-14 EK1', 'theme':'Cream & Ink v2.3',
        'appVersion':'1.4.0 (19)', 'platform':'Android / Google Play', 'status':'DESIGN EXPORTED — PLAY COPY REVIEW',
        'copyStatus':copy['status'], 'assets':deliveries}, ensure_ascii=False, indent=2)+'\n')
    print('Built 6 phone SVGs + feature SVG from 6 hash-verified Android captures.')

if __name__ == '__main__':
    main()
