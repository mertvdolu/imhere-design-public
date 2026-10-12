"""List every package file except MANIFEST.json itself. Run last after any edit."""
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p.name in ('MANIFEST.json','.DS_Store') or '__pycache__' in p.parts: continue
    rel=p.relative_to(ROOT).as_posix()
    item={'file':rel,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    if p.suffix.lower() in ('.png','.jpg','.jpeg'):
        with Image.open(p) as im: item.update(width=im.width,height=im.height,mode=im.mode)
    elif p.suffix.lower()=='.svg':
        node=ET.parse(p).getroot()
        for k in ('width','height'):
            value=node.get(k)
            if value:
                try: item[k]=float(value)
                except ValueError: item[k]=value
        if node.get('viewBox'):item['viewBox']=node.get('viewBox')
    if rel.startswith('app-store/') and p.suffix=='.png': item['role']='store-upload-candidate-copy-approval-pending'
    elif rel.startswith('source/native/'):item['role']='unaltered-native-source'
    elif rel.startswith('review/'):item['role']='review-only-not-for-store'
    else:item['role']='source-or-documentation'
    files.append(item)
out={'package':'imhere-store-v1.4-ios','theme':'Cream & Ink v2.3','appVersion':'1.4.0 (19)','date':'2026-10-13','status':'DESIGN EXPORTED — HARBOR + FOUNDER COPY APPROVAL REQUIRED','hashAlgorithm':'SHA256','selfExclusion':'MANIFEST.json','storePngCount':sum(x['role']=='store-upload-candidate-copy-approval-pending' for x in files),'fileCount':len(files),'files':files}
(ROOT/'MANIFEST.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'MANIFEST: {len(files)} files; {out["storePngCount"]} store PNG candidates; SHA256 recorded.')
