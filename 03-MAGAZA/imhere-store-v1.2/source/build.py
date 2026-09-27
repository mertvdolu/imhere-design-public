"""Compose unchanged native captures and authorised synthetic portraits as SVG layers.
Run with Python/Pillow, then node source/render.cjs (sharp).
"""
from pathlib import Path
from PIL import Image
import json,base64,html,hashlib
R=Path(__file__).resolve().parents[1];A=R/'assets'
def data(p,mime):return 'data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()
css=''.join('@font-face{font-family:Geist;font-weight:'+str(w)+';src:url('+data(A/f,'font/woff2')+')}' for w,f in [(400,'Geist-Regular.woff2'),(500,'Geist-Medium.woff2')])
copy=json.loads((R/'source/marketing-copy.en.json').read_text());positions=json.loads((R/'source/portrait-placements.json').read_text());delivery=[]
def text(t,x,y,size,weight=400,color='#191A17',anchor='start',tracking=0):return f'<text x="{x}" y="{y}" font-family="Geist" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}" letter-spacing="{tracking}">{html.escape(t)}</text>'
for folder,W,H,plat in [('app-store/iphone-6.9',1320,2868,'ios'),('app-store/iphone-6.5',1242,2688,'ios'),('google-play/phone',1080,1920,'android')]:
 for shot in copy['shots']:
  id=shot['id'];src=R/'source/native'/plat/(id+'.png')
  if id=='06-profile' or not src.exists():continue
  nw,nh=Image.open(src).size;w,h=W/2,H/2;android=plat=='android';yy=145 if android else 330 if W==1320 else 310;sh=h-194 if android else h-399;sw=sh*nw/nh;xx=(w-sw)/2
  ops=[f'<rect width="{w}" height="{h}" fill="#F4F1E9"/>']
  if android:
   ops+=[text('IM HERE',32,36,12,500,tracking=1.1),text(shot['playTitle'][0],32,100,35,500,tracking=-1.1)]
   if id in ['02-nearby','05-chat','06-profile']:ops.append(text(shot['sub'],32,128,14,color='#696A62'))
  else:
   ops.append(f'<image x="49" y="36" width="32" height="20.293333" href="{data(A/"imhere-mark-icon-weight.svg","image/svg+xml")}"/>');ops.append(text('IM HERE',103,53,13,500,tracking=1.1));sz=62 if W==1320 else 58
   for i,line in enumerate(shot['title']):ops.append(text(line,48,143+i*sz*1.02,sz,500,tracking=-2.6))
   ops.append(text(shot['sub'],49,258 if W==1320 else 250,17,color='#696A62'))
  ops.append(f'<rect x="{xx-3}" y="{yy-3}" width="{sw+6}" height="{sh+6}" rx="0" fill="#191A17"/>')
  # Capture is kept whole, aspect ratio intact; only portrait area is overlaid.
  inner=f'<image width="{nw}" height="{nh}" href="{data(src,"image/png")}"/>'
  pos=positions.get(plat+'/'+id)
  if pos:
   x,y,pw,ph,rad=[pos[k] for k in ['x','y','width','height','radius']]
   inner+=f'<defs><clipPath id="portrait"><rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="{rad}"/></clipPath></defs><image x="{x}" y="{y}" width="{pw}" height="{ph}" preserveAspectRatio="xMidYMid slice" clip-path="url(#portrait)" href="{data(A/pos["portrait"],"image/jpeg")}"/>'
  ops.append(f'<svg x="{xx}" y="{yy}" width="{sw}" height="{sh}" viewBox="0 0 {nw} {nh}">{inner}</svg>')
  label='Illustrative map · Not live data' if id=='03-full-screen-map' else 'Fictional profiles · Illustrative content'
  if id=='03-full-screen-map':ops.append(text('© OpenMapTiles',w/2,h-44,12,color='#696A62',anchor='middle'))
  ops.append(text(label,w/2,h-24,14,color='#696A62',anchor='middle'))
  f=R/folder/(id+'.svg');f.parent.mkdir(parents=True,exist_ok=True);f.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {w} {h}"><title>{html.escape(" ".join(shot["title"]))}</title><style>{css}</style>'+''.join(ops)+'</svg>')
  delivery.append({'file':str(f.relative_to(R)).replace('.svg','.png'),'width':W,'height':H,'platform':plat,'shot':id,'nativeSource':str(src.relative_to(R)),'nativeSourceSha256':hashlib.sha256(src.read_bytes()).hexdigest(),'nativeSourceSize':[nw,nh],'syntheticPortrait':pos,'crop':'none; uniform scaling','sourceType':'native capture with disclosed synthetic portrait overlay' if pos else 'native capture'})
(R/'DELIVERY.json').write_text(json.dumps({'version':'1.2','status':'partial native delivery; Android02/03 and photo-enabled06 pending','assets':delivery,'pending':['google-play/phone/02-nearby','google-play/phone/03-full-screen-map','app-store/iphone-6.9/06-profile','app-store/iphone-6.5/06-profile','google-play/phone/06-profile'],'featureGraphic':'Use existing v1.0 feature graphic; illustrative marketing composition, not native capture','profileDisclosure':'Fictional profiles · Illustrative content'},ensure_ascii=False,indent=2)+'\n')
print('Built',len(delivery),'native compositions')
