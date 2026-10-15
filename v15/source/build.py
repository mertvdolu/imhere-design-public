from pathlib import Path
import json,re,sys,shutil
B=Path(__file__).resolve().parents[1]; bank=json.loads((B/'source/copy-bank.json').read_text());states=json.loads((B/'source/states.json').read_text())
keys=set()
def collect(o):
 if isinstance(o,dict):
  for k,v in o.items():
   if k=='keys' and isinstance(v,dict):keys.update(v.values())
   if k in ['key','title','description','placeholder','help','error','reason','a11y'] and isinstance(v,str):keys.add(v)
   collect(v)
 elif isinstance(o,list):
  for v in o:collect(v)
collect(states)
# Renderer common references remain explicit.
keys.update(k for k in ['viewBack','loading','navProfile','navMessages','navNearby','navEvents','communityActiveLabel','communityPickerA11yLabel','communityPickerA11yHint','mapShowMyArea','occupationOther','occupationShowHelp','occupationNetworkingNote','profileLinkedinCheckRequired','nearbyFiltersCountMany','eventV1CategoryNetworking','eventV1CategorySocial','eventV1CategoryActivity','communityOptionNetworking','communityOptionFriendship'] if k in bank)
missing=keys-bank.keys()
if missing:raise SystemExit('Missing: '+str(missing))
copy={k:bank[k] for k in sorted(keys)}
(B/'data.js').write_text('window.V15 = '+json.dumps({'states':states,'copy':copy,'occupations':json.loads((B/'source/occupation-catalog.json').read_text()) if (B/'source/occupation-catalog.json').exists() else None},ensure_ascii=False)+';\n')
(B/'catalog.json').write_text(json.dumps({'version':'1.0','theme':'2.3','featureGate':'V15.ENABLED except d0 (1.4.2)','states':states},ensure_ascii=False,indent=2)+'\n')
for group in dict.fromkeys(s['group'] for s in states):
 d=B/group;d.mkdir(exist_ok=True);(d/'screens/png').mkdir(parents=True,exist_ok=True);(d/'evidence').mkdir(exist_ok=True)
 ss=[s for s in states if s['group']==group]
 (d/'catalog.json').write_text(json.dumps({'theme':'2.3','states':ss},ensure_ascii=False,indent=2)+'\n')
 (d/'ONIZLEME.html').write_text('<!doctype html><html lang="tr"><meta charset="utf-8"><title>IM HERE '+group+'</title><script>location.replace("../ONIZLEME.html?scene='+ss[0]['id']+'"+location.search.replace("?","&"));</script><a href="../ONIZLEME.html?scene='+ss[0]['id']+'">Önizleme</a></html>')
 localkeys=set();old=keys;keys=localkeys;collect(ss);keys=old
 cc=[bank[k] for k in sorted(localkeys)]
 for e in cc:e['screens']=[s['id'] for s in ss if e['key'] in json.dumps(s,ensure_ascii=False)]
 (d/'copy.proposed.json').write_text(json.dumps({'status':'APPROVED COPY — HB-37 r5 / existing approved reuse; UI decisions proposed ★','entries':cc,'proposals':[]},ensure_ascii=False,indent=2)+'\n')
 (d/'COPY-REVIEW.md').write_text('# '+group+' — copy review\n\nOnaylı kaynak değerleri aynen. Dosya adı teslim standardı gereği `proposed`; metin onayı HB-37 r5 ve atıf yapılan mevcut anahtarlarla sınırlıdır. Ana ARB üzerine yazılmaz.\n\n| KEY | EN | TR | SCREEN / STATE | SOURCE |\n|---|---|---|---|---|\n'+''.join('| '+e['key']+' | '+e['en']+' | '+e['tr']+' | '+', '.join(e['screens'])+' | '+e['source']+' |\n' for e in cc)+'\n## ÖNERİ\n\nYok. Metin yeniden yazılmadı.\n')
 (d/'SCREEN-STATE-MATRIX.md').write_text('# '+group+' — durum matrisi\n\nHer durum: EN/TR × %100/%200 × 390×844 / 412×915; 4× opak PNG. `--full` yalnız kaydırılan içerikte. Dar ekran: 320/%200 iOS + Android ölçümü.\n\n| State | Davranış |\n|---|---|\n'+''.join('| '+s['id']+' | '+s.get('notes','')+' |\n' for s in ss))
(B/'copy.proposed.json').write_text(json.dumps({'status':'APPROVED COPY — HB-37 r5 / approved reuse; proposed UI decisions separate','entries':list(copy.values()),'proposals':[]},ensure_ascii=False,indent=2)+'\n')
print(len(states),'states',len(copy),'keys')
