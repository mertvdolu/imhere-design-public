"""Rebuild editable store artwork with Pillow font metrics. No network or native app access.
Run: python source/build.py; then node source/render.cjs (Pillow + sharp required).
"""
from pathlib import Path
import json, base64, html, math, re, hashlib
from PIL import ImageFont
R=Path(__file__).resolve().parents[1]
A=R/'assets'; C=json.loads((R/'source/theme.tokens.json').read_text())['colors']; UI=json.loads((R/'source/ui-copy.en.json').read_text())
INK=C['text']; PAPER=C['background']; CARD=C['card']; MUTED=C['textSecondary']; LINE=C['border']
FONTS={}
def font(size,weight=400):
 key=(size,weight)
 if key not in FONTS:FONTS[key]=ImageFont.truetype(str(A/('Geist-Medium.ttf' if weight==500 else 'Geist-SemiBold.ttf' if weight==600 else 'Geist-Regular.ttf')),round(size*4))
 return FONTS[key]
def width(text,size,weight=400,tracking=0):return font(size,weight).getlength(text)/4+max(0,len(text)-1)*tracking
def data(path,mime):return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()
CSS=''.join('@font-face{font-family:Geist;font-weight:'+str(w)+';src:url('+data(A/f.replace('.ttf','.woff2'),'font/woff2')+')}' for w,f in [(400,'Geist-Regular.ttf'),(500,'Geist-Medium.ttf'),(600,'Geist-SemiBold.ttf')])
ICONS={
 'nearby':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3"/>',
 'profile':'<circle cx="12" cy="7" r="3.5"/><path d="M5 21v-3a7 7 0 0 1 14 0v3"/>',
 'messages':'<path d="M4 4h16v12H9l-5 4z"/>',
 'events':'<rect x="4" y="5" width="16" height="16" rx="2"/><path d="M8 3v4m8-4v4M4 10h16"/>',
 'arrow':'<path d="M7 17 17 7M7 7h10v10"/>',
 'chevron':'<path d="m9 5 7 7-7 7"/>',
 'back':'<path d="m15 5-7 7 7 7"/>',
 'map':'<path d="m3 6 6-3 6 3 6-3v15l-6 3-6-3-6 3zM9 3v15m6-12v15"/>',
 'lock':'<rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
 'more':'<circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/>',
 'settings':'<circle cx="12" cy="12" r="3"/><path d="m10 3 4 0 .6 3 2 .9 2.8-1 2 3.4-2.2 2v2.4l2.2 2-2 3.4-2.8-1-2 .9-.6 3h-4l-.6-3-2-.9-2.8 1-2-3.4 2.2-2v-2.4l-2.2-2 2-3.4 2.8 1 2-.9z"/>'}
class SVG:
 def __init__(self,w,h,title):self.w=w;self.h=h;self.title=title;self.ops=[];self.texts=[];self.uid=0;self.prefix=hashlib.sha1(title.encode()).hexdigest()[:8]
 def rect(self,x,y,w,h,fill=PAPER,r=0,stroke=None,sw=1):self.ops.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
 def line(self,x1,y1,x2,y2,color=LINE,sw=1):self.ops.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{sw}"/>')
 def text(self,text,x,y,size=16,color=INK,weight=400,tracking=0,anchor='start'):
  tw=width(text,size,weight,tracking);left=x-tw/2 if anchor=='middle' else x-tw if anchor=='end' else x
  self.texts.append(dict(text=text,x=left,y=y-size,width=tw,height=size*1.25,size=size))
  self.ops.append(f'<text x="{x}" y="{y}" font-family="Geist" font-size="{size}" fill="{color}" font-weight="{weight}" letter-spacing="{tracking}" text-anchor="{anchor}">{html.escape(text)}</text>')
 def para(self,text,x,y,w,size=16,color=INK,weight=400,leading=1.5):
  yy=y
  for para in text.split('\n'):
   line=''
   for word in para.split():
    if line and width(line+' '+word,size,weight)>w:self.text(line,x,yy,size,color,weight);yy+=size*leading;line=word
    else:line=(line+' '+word).strip()
   self.text(line,x,yy,size,color,weight);yy+=size*leading
  return yy
 def image(self,path,x,y,w,h,r=0,mime=None):
  mime=mime or ('image/svg+xml' if path.suffix=='.svg' else 'image/jpeg' if path.suffix=='.jpg' else 'image/png');self.uid+=1;clip=f'{self.prefix}-clip-{self.uid}'
  self.ops.append(f'<defs><clipPath id="{clip}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath></defs><image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#{clip})" href="{data(path,mime)}"/>')
 def icon(self,name,x,y,size=22,color=INK):self.ops.append(f'<g transform="translate({x} {y}) scale({size/24})" fill="none" stroke="{color}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')
 def logo(self,x,y,w=40):self.image(A/'imhere-mark-icon-weight.svg',x,y,w,w*91.32/144)
 def pill(self,label,x,y,w=None,selected=False):
  w=w or width(label,12)+24;self.rect(x,y,w,28,INK if selected else CARD,14,INK if selected else LINE);self.text(label,x+w/2,y+18,12,CARD if selected else INK,anchor='middle');return w
 def button(self,label,x,y,w,primary=False,disabled=False):
  self.rect(x,y,w,50,INK if primary and not disabled else CARD,14,INK if not disabled else '#8A8B81');self.text(label,x+w/2,y+31,14,CARD if primary and not disabled else MUTED if disabled else INK,500,anchor='middle')
 def embed(self,content,x,y,w,h,r=32):
  self.uid+=1;clip=f'{self.prefix}-view-{self.uid}'
  self.ops.append(f'<defs><clipPath id="{clip}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath></defs><g clip-path="url(#{clip})"><svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {content.w} {content.h}">{"".join(content.ops)}</svg></g>')
 def render(self):return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{html.escape(self.title)}"><title>{html.escape(self.title)}</title><style>{CSS}</style>'+''.join(self.ops)+'</svg>'

def status(s,platform):
 s.text('9:41',25,28,12,weight=500)
 s.ops.append(f'<g transform="translate({s.w-76} 18)" fill="{INK}"><path d="M0 10V7h2v3M4 10V5h2v5M8 10V3h2v7M12 10V0h2v10"/></g>')
 s.rect(s.w-51,18,23,11,'none',2,INK);s.rect(s.w-48,21,16,5,INK,1);s.rect(s.w-27,21,2,5,INK,1)

def nav(s,active,platform):
 y=s.h-86;s.rect(0,y,s.w,86,CARD);s.line(0,y,s.w,y)
 for i,(k,n) in enumerate([('navProfile','profile'),('navMessages','messages'),('navNearby','nearby'),('navEvents','events')]):
  x=s.w*(i+.5)/4;on=n==active
  if on:s.line(x-14,y+2,x+14,y+2,INK,2)
  s.icon(n,x-10,y+16,20,INK if on else MUTED);s.text(UI[k],x,y+55,11,INK if on else MUTED,500 if on else 400,anchor='middle')
 s.rect(s.w/2-46,s.h-13,92,4,INK,2)

def top(s,title,icon='settings'):
 s.logo(37,67);s.icon(icon,s.w-52,70,22);s.text(title,24,158,36,weight=500,tracking=-1.8)

def photo(s,who,x,y,w,h,r=16):s.image(A/f'{who}-synthetic.jpg',x,y,w,h,r)

def ui(kind,platform):
 w,h=(390,844) if platform=='ios' else (412,915);s=SVG(w,h,kind+' / illustrative Cream & Ink v2.2 screen');s.rect(0,0,w,h,PAPER);status(s,platform)
 if kind=='map':
  # The accepted catalog fixture already includes the full-screen layout, four aggregate
  # colours, snapshot caveat and required attribution. It is not a live map capture.
  src=(A/f'map-ready-{platform}.svg').read_text();body=src[src.index('</style>')+8:src.rfind('</svg>')]
  s.ops=[body];s.texts=[];return s
 if kind=='opening':
  s.icon('back',24,64);photo(s,'maya',24,110,54,65,12);s.text('Maya',94,137,21,weight=500);s.text('Designer',94,162,14,MUTED)
  yy=s.para(UI['intentQuestion'],24,224,w-48,31,weight=500,leading=1.12)
  s.text(UI['intentHint'],24,yy+16,14,MUTED)
  y=yy+46
  for k in ['intentFriendship','intentNetworking']:
   s.rect(24,y,w-48,70,CARD,15,'#8A8B81');s.rect(44,y+24,22,22,'none',4,INK);s.text(UI[k],82,y+43,18);y+=86
  s.button(UI['requestSend'],24,y+16,w-48,disabled=True)
  s.rect(w/2-46,h-13,92,4,INK,2)
 elif kind=='nearby':
  top(s,UI['navNearby'],'map');s.text('A hello can start here.',24,188,14,MUTED)
  s.rect(24,217,w-48,77,CARD,15,LINE);s.text(UI['checkInTitle'],40,243,12,MUTED);s.text(UI['checkInStatusActive'].replace('{time}','10:10'),40,269,13)
  s.text(UI['nearbyPeople'],24,329,12,MUTED,500)
  photo(s,'maya',24,348,w-48,215,16);s.text('Maya',24,602,26,weight=500);s.text('Designer',24,627,14,MUTED);s.icon('arrow',w-57,588,24)
  x=24
  for label in ['Design','Coffee','Walking']:x+=s.pill(label,x,649)+8
  nav(s,'nearby',platform)
 elif kind=='connections':
  top(s,UI['navMessages']);s.text(UI['messagesConnections'],24,189,14,MUTED)
  s.text(UI['messagesConnections'],24,235,14,weight=500);s.text(UI['messagesRequests'],196,235,14,MUTED);s.line(24,249,139,249,INK,2);s.line(151,249,w-24,249)
  photo(s,'maya',24,285,56,67,12);s.text('Maya',96,307,18,weight=500);s.para('It’s nice to talk about new ideas.',96,333,w-150,14,MUTED,leading=1.4);s.icon('chevron',w-47,306,19);s.line(24,378,w-24,378)
  photo(s,'alex',24,408,56,67,12);s.text('Alex',96,429,18,weight=500);s.icon('lock',96,446,14,MUTED);s.para(UI['connectionEndedNeutral'],117,458,w-153,12,MUTED,leading=1.4);s.icon('chevron',w-47,431,19,MUTED);s.line(24,497,w-24,497)
  nav(s,'messages',platform)
 elif kind=='chat':
  s.icon('back',18,70,22);photo(s,'maya',52,58,42,48,12);s.text('Maya',108,79,17,weight=500);s.text(UI['intentFriendship'],108,100,12,MUTED);s.icon('more',w-44,70,21);s.line(0,123,w,123)
  y=165
  for msg,own in [('Hello, I noticed you’re interested in design.',False),('Hello. I am! Especially the little details.',True),('Same here. The simple things take the most thought.',False),('It’s nice to talk about new ideas.',True)]:
   bw=276;lines=math.ceil(width(msg,16)/(bw-32));bh=32+lines*25;x=w-24-bw if own else 24
   s.rect(x,y,bw,bh,INK if own else CARD,17, None if own else LINE);s.para(msg,x+16,y+29,bw-32,16,CARD if own else INK,leading=1.56);y+=bh+17
  foot=h-151;s.rect(0,foot,w,151,CARD);s.line(0,foot,w,foot);s.text(UI['chatRemaining'].replace('{remaining}','18'),24,foot+29,12,MUTED);s.text(UI['continueTitle'],w-24,foot+52,12,MUTED,anchor='end')
  s.rect(24,foot+65,w-118,48,C['input'],13,'#8A8B81');s.text(UI['chatPlaceholder'],38,foot+94,14,MUTED);s.button(UI['chatSend'],w-84,foot+65,60,disabled=True);s.text('0 / 500',24,foot+133,11,MUTED);s.rect(w/2-46,h-10,92,4,INK,2)
 elif kind=='profile':
  top(s,UI['navProfile']);s.text(UI['profileEditTitle'],24,189,14,MUTED)
  photo(s,'alex',24,219,w-48,257,16);s.text('Alex',24,518,29,weight=500);s.text('Designer',24,544,14,MUTED)
  s.para('Coffee, design and new ideas.\nAlways up for a good conversation.',24,580,w-48,15,leading=1.5)
  x=24
  for label in ['Design','Coffee','Walking']:x+=s.pill(label,x,632)+8
  s.button(UI['profileEditTitle'],24,683,w-48,primary=True);nav(s,'profile',platform)
 else:raise ValueError(kind)
 return s

SHOTS=[
 {'id':'01-opening','kind':'opening','title':['A hello','starts here.'],'sub':'Friendship and networking, nearby.','playTitle':['A hello starts here.']},
 {'id':'02-nearby','kind':'nearby','title':['People.','Closer to you.'],'sub':'Find a shared interest. Send a hello.','playTitle':['People. Closer to you.']},
 {'id':'03-full-screen-map','kind':'map','title':['A wider view','of nearby.'],'sub':'Explore activity on a full-screen map.','playTitle':['Explore nearby.']},
 {'id':'04-connections','kind':'connections','title':['Connections,','in one place.'],'sub':'Your connections and requests, together.','playTitle':['Your connections.']},
 {'id':'05-chat','kind':'chat','title':['Start with','a conversation.'],'sub':'Text, emoji and links. Keep it simple.','playTitle':['Start a conversation.']},
 {'id':'06-profile','kind':'profile','title':['A little','about you.'],'sub':'Your photo. Your interests. Your choice.','playTitle':['A little about you.']},
]
SETS=[('app-store/iphone-6.9',1320,2868,'ios'),('app-store/iphone-6.5',1242,2688,'ios'),('google-play/phone',1080,1920,'android')]
DIS='Fictional profiles · Illustrative content'
BOUNDS=[];DELIVER=[]
for folder,W,H,platform in SETS:
 ww,hh=W/2,H/2;play=platform=='android'
 for shot in SHOTS:
  s=SVG(ww,hh,'IM HERE — '+ ' '.join(shot['title']));s.rect(0,0,ww,hh,PAPER)
  if play:
   s.text('IM HERE',32,36,12,weight=500,tracking=1.1);s.text(shot['playTitle'][0],32,100,35,weight=500,tracking=-1.1)
   frameH=hh-194;app=ui(shot['kind'],platform);scale=frameH/app.h;frameW=app.w*scale;xx=(ww-frameW)/2;yy=145
  else:
   s.logo(49,36,32);s.text('IM HERE',103,53,13,weight=500,tracking=1.1)
   sz=62 if W==1320 else 58
   for i,line in enumerate(shot['title']):s.text(line,48,143+i*sz*1.02,sz,weight=500,tracking=-2.6)
   s.text(shot['sub'],49,258 if W==1320 else 250,17,MUTED)
   app=ui(shot['kind'],platform);frameH=hh-399;scale=frameH/app.h;frameW=app.w*scale;xx=(ww-frameW)/2;yy=330 if W==1320 else 310
  s.rect(xx-3,yy-3,frameW+6,frameH+6,INK,34 if not play else 24)
  s.embed(app,xx,yy,frameW,frameH,31 if not play else 21)
  disclosure='Illustrative map · Not live data' if shot['kind']=='map' else DIS
  s.text(disclosure,ww/2,hh-24,14,MUTED,anchor='middle')
  p=R/folder/(shot['id']+'.svg');p.parent.mkdir(parents=True,exist_ok=True)
  svg=s.render().replace(f'width="{ww}" height="{hh}"',f'width="{W}" height="{H}"',1);p.write_text(svg)
  errors=[t for t in s.texts if t['x']<0 or t['x']+t['width']>ww or t['y']<0 or t['y']+t['height']>hh]
  errors += [t for t in app.texts if t['x']<0 or t['x']+t['width']>app.w or t['y']<0 or t['y']+t['height']>app.h]
  assert not errors,(p,errors)
  BOUNDS.append({'file':str(p.relative_to(R)),'textBoundsPass':True,'artboard':[W,H],'appViewport':[app.w,app.h],'deviceFrameFullyVisible':yy+frameH<hh-35})
  DELIVER.append({'file':str(p.with_suffix('.png').relative_to(R)),'width':W,'height':H,'platform':platform,'shot':shot['id'],'title':' '.join(shot['playTitle'] if play else shot['title']),'sourceType':'design-render','nativeCaptureVerified':False})
  if folder=='app-store/iphone-6.9':
   d=R/'source/screens';d.mkdir(exist_ok=True);(d/(shot['kind']+'-ios.svg')).write_text(app.render())
# Feature graphic: separate storytelling composition, not a pretend device capture.
s=SVG(1024,500,'IM HERE — Common interests. New connections.');s.rect(0,0,1024,500,PAPER)
s.text('IM HERE',66,72,16,weight=500,tracking=1.5);s.text('Common',64,181,62,weight=500,tracking=-2.5);s.text('interests.',64,245,62,weight=500,tracking=-2.5);s.text('New connections.',66,302,29,weight=400,tracking=-.7)
s.text('Friendship and networking, nearby.',67,365,17,MUTED)
s.rect(622,42,327,330,CARD,22,LINE);s.text(UI['navNearby'],646,81,22,weight=500)
photo(s,'maya',646,105,96,119,13);s.text('Maya',764,145,25,weight=500);s.text('Designer',764,175,15,MUTED);s.icon('arrow',883,185,23)
x=646
for label in ['Design','Coffee','Walking']:x+=s.pill(label,x,247)+8
s.text('Coffee, design and new ideas.',646,313,16,MUTED)
s.rect(714,341,211,78,INK,20);s.text('Hello.',740,391,30,CARD,weight=500)
s.text(DIS,66,457,12,MUTED)
p=R/'google-play/feature-graphic.svg';p.write_text(s.render());DELIVER.append({'file':'google-play/feature-graphic.png','width':1024,'height':500,'platform':'android','shot':'feature','title':'Common interests. New connections.','sourceType':'marketing-composition','nativeCaptureVerified':False})
errors=[t for t in s.texts if t['x']<0 or t['x']+t['width']>1024 or t['y']<0 or t['y']+t['height']>500];assert not errors,errors
BOUNDS.append({'file':str(p.relative_to(R)),'textBoundsPass':True,'artboard':[1024,500]})
(R/'source/marketing-copy.en.json').write_text(json.dumps({'version':'1.0','shots':SHOTS,'feature':{'title':'Common interests. New connections.','sub':'Friendship and networking, nearby.'},'profileDisclosure':DIS,'mapDisclosure':'Illustrative map · Not live data'},indent=2,ensure_ascii=False)+'\n')
(R/'evidence/layout-validation.json').write_text(json.dumps(BOUNDS,indent=2)+'\n')
(R/'DELIVERY.json').write_text(json.dumps({'version':'1.0','themeVersion':'2.2','sourceCommit':'f3dbd40bdedad4ec0b3ed06f38b72d1c1cfcebf2','language':'en','assets':DELIVER,'status':'design-complete; native-capture comparison required before store submission'},indent=2)+'\n')
print('Created 19 editable artworks and six standalone screen sources. All text fits.')
