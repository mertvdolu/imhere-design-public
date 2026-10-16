from pathlib import Path
import json,hashlib
from PIL import Image
R=Path(__file__).resolve().parents[1]
uploads=[x['file'] for x in json.loads((R/'DELIVERY.json').read_text())['assets']]+['play-feature/feature-graphic.png']
(R/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256((R/p).read_bytes()).hexdigest()+'  '+p+'\n' for p in uploads))
files=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or p.name in ['MANIFEST.json','.DS_Store'] or '__pycache__' in p.parts:continue
    rel=str(p.relative_to(R));v={'file':rel,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'role':'store-upload-candidate' if rel in uploads else 'source-or-review'}
    if p.suffix=='.png':
        with Image.open(p) as im:v.update(width=im.width,height=im.height,mode=im.mode)
    files.append(v)
(R/'MANIFEST.json').write_text(json.dumps({'package':'imhere-store-v1.5','date':'2026-10-16','theme':'Cream & Ink v2.3','storePngCount':19,'screenshots':18,'featureGraphics':1,'fileCount':len(files),'hashAlgorithm':'SHA256','selfExclusion':'MANIFEST.json','files':files},ensure_ascii=False,indent=2)+'\n')
print('MANIFEST:',len(files),'files; 19 store PNGs.')
