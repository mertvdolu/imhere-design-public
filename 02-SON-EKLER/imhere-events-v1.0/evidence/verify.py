"""Read-only consistency checks for the design handoff. No app/backend execution."""
from pathlib import Path
import json
import re
import hashlib

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / 'catalog.json').read_text())
states = catalog['states']
assert len(states) == catalog['stateCount'] == 36
assert len({s['id'] for s in states}) == 36
for mode in ('locked', 'cancelled', 'changed'):
    assert {s['myRsvp'] for s in states if s['screen'] == 'detail' and s['mode'] == mode} == {'NONE', 'INTERESTED', 'GOING'}
assert {s['category'] for s in states} == {'NETWORKING', 'SOCIAL', 'ACTIVITY'}
assert all(s['copyStatus'] == 'PROPOSED' and s['minTouchTarget'] == 48 for s in states)

arbs = [json.loads((root / 'l10n' / f'events-v1-proposed_{lang}.arb').read_text()) for lang in ('en', 'tr')]
keys = [{k for k in arb if not k.startswith('@')} for arb in arbs]
assert keys[0] == keys[1] and len(keys[0]) == 52
for key in keys[0]:
    assert re.findall(r'\{(\w+)\}', arbs[0][key]) == re.findall(r'\{(\w+)\}', arbs[1][key]), key
    for arb in arbs:
        assert 'PROPOSED' in arb['@' + key]['description'], key
        assert 'anonim' not in arb[key].lower()

assert json.loads((root / 'catalog.js').read_text().removeprefix('window.EVENT_CATALOG=').rstrip(';\n')) == catalog
preview_copy = json.loads((root / 'copy.js').read_text().split('window.EVENT_COPY=', 1)[1].rstrip(';\n'))
for index, locale in enumerate(('en', 'tr')):
    assert all(preview_copy[locale][key] == arbs[index][key] for key in keys[0])

for file in ('SPEC.md', 'HANDOFF.md', 'SCREEN-STATE-MATRIX.md', 'COPY-REVIEW.md', 'tokens.components.json', 'ONIZLEME.html', 'style.css', 'preview.js'):
    assert (root / file).is_file(), file
html = (root / 'ONIZLEME.html').read_text()
for target in re.findall(r'(?:src|href)="([^"]+)"', html):
    if not target.startswith(('http:', 'https:', '#')):
        assert (root / target.split('?')[0]).exists(), target
js = (root / 'preview.js').read_text()
assert not re.search(r'\b(fetch|XMLHttpRequest|localStorage|sessionStorage)\b', js)
assert 'window.open' not in js and 'mailto:' not in js
assert all((root / 'assets' / f'event-art-{c.lower()}.svg').exists() for c in ('NETWORKING', 'SOCIAL', 'ACTIVITY'))

manifest_path = root / 'MANIFEST.json'
if manifest_path.exists():
    manifest = json.loads(manifest_path.read_text())
    actual = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p != manifest_path and '__pycache__' not in str(p)}
    assert actual == {e['file'] for e in manifest['entries']}
    for item in manifest['entries']:
        b = (root / item['file']).read_bytes()
        assert len(b) == item['bytes'] and hashlib.sha256(b).hexdigest() == item['sha256'], item['file']
print('PASS: 36 states, RSVP coverage, 52 EN/TR proposed keys, placeholders, preview parity, files, no network/storage, manifest (when present)')
