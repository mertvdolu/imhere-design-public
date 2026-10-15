from pathlib import Path
import json,hashlib,sys,math
from PIL import Image,ImageDraw,ImageFont
B=Path(__file__).resolve().parents[1];R=B.parent;states=json.loads((B/'catalog.json').read_text())['states'];bank=json.loads((B/'source/copy-bank.json').read_text()); meta=json.loads((B/'source/group-notes.json').read_text()) if (B/'source/group-notes.json').exists() else {}
def write(p,s):p.write_text(s+'\n')
def lum(h):
 rgb=[int(h[i:i+2],16)/255 for i in (1,3,5)];v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in rgb];return sum(a*b for a,b in zip(v,[.2126,.7152,.0722]))
def ratio(a,b):l=sorted([lum(a),lum(b)]);return round((l[1]+.05)/(l[0]+.05),3)
colors={'background':'#F4F1E9','surface':'#F4F1E9','onInk':'#FCFAF5','text':'#191A17','textSecondary':'#696A62','inputBorder':'#7C7D73','cardBorder':'#B7B3A9','community.networking':'#344E78','community.networking.on':'#FCFAF5','community.networking.surface':'#E5E9EF','community.friendship':'#315C46','community.friendship.on':'#FCFAF5','community.friendship.surface':'#E5EBE4','densityBlue':'#64A8FF','densityYellow':'#F7D46A','densityGreen':'#7DDEAC','densityRed':'#EE8985'}
contrasts={k:ratio(v,colors['background']) for k,v in colors.items()}
write(B/'tokens.json',json.dumps({'theme':'2.3','status':'Community additions: DESIGN RECOMMENDATION — FOUNDER APPROVAL REQUIRED','colors':colors,'contrastOnCream':contrasts,'communityOnRatios':{k:ratio(colors[k],colors[k+'.on']) for k in ['community.networking','community.friendship']},'communityLightRatios':{k:ratio(colors[k],colors[k+'.surface']) for k in ['community.networking','community.friendship']},'space':[4,8,12,16,20,24,32,40,48],'radius':{'input':12,'button':12,'card':15,'sheet':24,'pill':999},'iconStroke':1.8,'targetMin':48,'motion':{'reduced':{'durationMs':150,'curve':'linear','property':'opacity','spatial':False}},'precedence':'v2.3 surface spec uses cream raised and inset surfaces. Brief #FCFAF5 remains on-ink. Decorative borders are not control boundaries.'},ensure_ascii=False,indent=2))
write(B/'TOKENS.md','# V15 token kararları (★)\n\nCream & Ink v2.3 yüzeyleri korunur. Krem kabartma / iç yüzey #F4F1E9; yeni renk yalnız topluluk kimliği.\n\n| Rol | Hex | Krem ile oran |\n|---|---|---|\n'+''.join(f'| {k} | {v} | {contrasts[k]}:1 |\n' for k,v in colors.items())+'\nMetin: Ink/cream '+str(contrasts['text'])+':1; yardımcı '+str(contrasts['textSecondary'])+':1; kontrol kenarı '+str(contrasts['inputBorder'])+':1. Açık topluluk yüzeyi/dekoratif kenar tek başına kontrol veya anlam taşımaz; Ink/radyo/etiket ve belirgin kontrol kenarı korunur. Harita renkleri metin rengi değildir.\n\n★ Networking #344E78, Friendship #315C46. İkisi koyu, bastırılmış ton; yoğunluk renklerinin parlak/pastel lekelerinden ayrılır. Logo tek renk; LinkedIn logosu yok.\n\n★ Seçici: üst solda 48 hedefli hap, yalnız Ayarlar bağlantısı; harita konum düğmesi sağda. Tek toplulukta da açılır. %200 satır sarar, atıf menü üstünde ayrı akışta kalır.\n\n★ Filtre: tam ekran alt sayfa, 24 kenar, kaydırılan gövde. Sabit seçim sırası; 5 sınırı metinle.\n\n★ İkonlar: 3 kategori + 2 topluluk yeterli; Professional=çanta, Networking=bağlı kareler. Kategori Ink; topluluk yalnız etiketli topluluk kontrolünde kendi rengi.\n\n★ İtalik ve yeni açılış: isteğe bağlı bölümde karar verilir. Yeni font/bağımlılık eklenmez.\n')
allmeasure=[];pngcount=fullcount=0
for g in dict.fromkeys(s['group'] for s in states):
 d=B/g;ss=[s for s in states if s['group']==g];ms=[]
 for s in ss:
  p=d/'evidence'/f"{s['id']}.json"
  if p.exists():ms+=json.loads(p.read_text())
 allmeasure+=ms
 issues=[x for x in ms if x['horizontalOverflow'] or x['smallTargets'] or x['clippedText'] or x['h1']!=1]
 main=list((d/'screens/png').glob('*.png'));full=[p for p in main if '--full' in p.name];pngcount+=len(main)-len(full);fullcount+=len(full)
 for p in list((d/'screens/png').glob('*.png'))+list((d/'evidence').glob('*.png')):
  im=Image.open(p)
  if im.mode!='RGB':im.convert('RGB').save(p,optimize=True)
 # Contact sheet: all states, main EN100 at 390; bounded columns.
 thumbs=[]
 font=ImageFont.truetype(str(B/'assets/Geist-Regular.ttf'),17)
 for s in ss:
  p=d/'screens/png'/f"{s['id']}--en--100.png"
  if p.exists():thumbs.append((s['id'],Image.open(p).resize((195,422))))
 if thumbs:
  cols=min(4,len(thumbs));rows=math.ceil(len(thumbs)/cols);sheet=Image.new('RGB',(cols*227+32,rows*478+32),'#E7E3DA');draw=ImageDraw.Draw(sheet)
  for i,(name,im) in enumerate(thumbs):x=32+(i%cols)*227;y=24+(i//cols)*478;sheet.paste(im,(x,y));draw.text((x,y+430),name[:26],fill='#191A17',font=font)
  sheet.save(d/'OVERVIEW.png',optimize=True)
 measure={'states':len(ss),'expectedMainPng':len(ss)*8,'mainPng':len(main)-len(full),'fullPng':len(full),'measuredLayouts':len(ms),'horizontalOverflow':sum(x['horizontalOverflow']>0 for x in ms),'smallTargets':sum(len(x['smallTargets']) for x in ms),'clippedText':sum(len(x['clippedText']) for x in ms),'issues':issues,'status':'PASS' if ms and not issues and len(main)-len(full)==len(ss)*8 else 'PENDING / FAIL'}
 write(d/'evidence/summary.json',json.dumps(measure,ensure_ascii=False,indent=2))
 info=meta.get(g,{})
 write(d/'README.md',f'# V15 / {g}\n\nCream & Ink v2.3 · Tasarım teslimi, canlı uygulama değildir.\n\n1. [SPEC](SPEC.md)\n2. [HTML önizleme](ONIZLEME.html)\n3. [Durum matrisi](SCREEN-STATE-MATRIX.md)\n4. [Copy review](COPY-REVIEW.md)\n5. [Ölçüm](VALIDATION.md)\n\n{len(ss)} durum · {measure["mainPng"]} ana PNG · {len(full)} uzun içerik PNG. Dosyalar `screens/png/`; her durum EN/TR, %100/%200, 390 ve 412 mantıksal genişlikte 4× opak RGB.\n\nDurum: {measure["status"]}. Görseller tasarım önizlemesidir; native cihaz/backend kanıtı değildir.')
 write(d/'SPEC.md',f'# {g} — SPEC\n\n## Bileşenler / ölçü\n\nMevcut v2.3 başlık, küçük düğme, bilgi kartı, input, radyo ve satır desenleri. Kenar 24 dp. Başlık 28/600, gövde 16/400, yardım 14/400; satır aralığı 1.18/1.5/1.5. Bölüm başlığı 18/500. Ölçek %200: punto 2×, sabit satır sınırı yok. Küçük düğme görünen yüzey en az 36, bağımsız hedef en az 48×48; radius12. Kart radius15.\n\n'+info.get('spec','D0: tek ekran, geri/alt menü yok. Logo mevcut splash-mark SVG; yeni ikon veya renk yok. Başlık/gövde/Update/delete-account link okuma sırası. Gövde normalde dikey ortalı; büyük metinde doğal akış ve kaydırma. Açılış beklerken Update devre dışı ve aria-busy; etiketi korunur, spinner durumun görsel işaretidir. Mağaza açma hata metni Update üstünde, eylem yeniden kullanılabilir. Silme notunun tamamı en az48 hedefli gerçek web bağlantısıdır; uygulama içinde silme vaadi yok.')+'\n\n## Durumlar\n\n'+''.join('- **'+s['id']+'**: '+s.get('notes','')+'\n' for s in ss)+'\n## Erişilebilirlik / native\n\nHer durum tek H1, doğal üstten alta okuma; %200 ve320 genişlikte yatay kaydırma yok. En az48 hedef, renk yanında metin/ikon. Pasif kontrolün koşulu mevcut metin veya işlem durumu ile görünür. Varsa radyo grup etiketi, checkbox çoklu seçim, switch görünür etiketle. Focus visible 2 px Ink +3 offset. `Reduce Motion`: 150 ms doğrusal opaklık, mekânsal hareket yok. Yüksek kontrastta gölge yok, belirgin Ink kenar; şeffaflığı azaltmada menü opak.\n\n## ★ / yeni bileşen\n\n'+info.get('decisions','★ Tekrar açma eylemi aynı Update düğmesiyle; ikinci bir mağaza düğmesi eklenmedi. YENİ BİLEŞEN — ONAY GEREKİR: yok; mevcut başlangıç engeli ve form/info desenleri.'))
 write(d/'HANDOFF.md',f'# {g} — Code handoff\n\nÖnce SPEC + SCREEN-STATE-MATRIX. Copy dosyası inceleme/eşleme kaynağıdır; canonical ARB üzerine yazılmaz. Anahtarın onaylı kaynağı COPY-REVIEW’de. Başarı yalnız sunucu/işlem sonucu onayından sonra.\n\n'+info.get('handoff','D0 bağımsız 1.4.2 kapısıdır; V15.ENABLED arkasına alınmaz. Store URL platform yapılandırmasından; tahmini URL yok. Güncelleme mağazayı açmayı dener, hata sonrası aynı ekranda kalır. Hesap silme notu https://useimhere.com/delete-account bağlantısıdır. Web önizleme Update yalnız opening durumuna geçer; hata üst inceleme kontrolüyle simüle edilir.\n\nD0 iOS ürün kapısı: mağaza URL’si olmayan eski yapıya kapı yükseltilmez; Manager karar42 Code tarafında doğrulanır.')+'\n\nFlutter: SafeArea + ScrollView, doğal metin ölçüsü, yerleşik animasyon/CustomPainter. Yeni bağımlılık yok. Ekran okuyucuda H1 header, link link, tek seçim radiogroup; decorative icon excludeSemantics. Önizleme kabuğu OS cihaz testi değildir. Code VoiceOver/TalkBack, native Dynamic Type, Android font ölçeği, gerçek URL açıcı/ağ/yanıtları ayrıca ölçer.')
 write(d/'VALIDATION.md',f'# {g} — validation\n\n**{measure["status"]} — browser design preview**\n\n- {len(ss)} durum / {measure["mainPng"]} ana PNG / {len(full)} full PNG.\n- {len(ms)} gerçek DOM yerleşim ölçümü, EN/TR, %100/%200,390/412; ek320/%200 iOS+Android kabuğu.\n- Yatay taşma: {measure["horizontalOverflow"]}; <48 hedef: {measure["smallTargets"]}; yatay kesilen metin: {measure["clippedText"]}.\n- Her ekran tek H1; bütün fontlar yerel Geist.\n- Ink/cream {contrasts["text"]}:1; secondary/cream {contrasts["textSecondary"]}:1; kontrol kenarı/cream {contrasts["inputBorder"]}:1. Metin≥4.5 ve kontrol≥3.\n- PNG opak RGB, ana boyutlar1560×3376 ve1648×3660. Uzun metin için full kare ayrı; üst ekranın tek başına tüm içeriği göstermesi beklenmez.\n\nÖlçüm: `evidence/<state>.json`, `evidence/summary.json`. Ürün, cihaz, VoiceOver/TalkBack, ağ ve backend doğrulaması değildir. Dikey kaydırma yetkili; font küçültme ve ellipsis yok.')
# Root cumulative index.
write(B/'README.md','# IM HERE · V15 tasarım teslimi\n\nCream & Ink v2.3. Başlangıç: remote main58bf8c4; yalnız design/v15-cream-ink-v23. D0 ayrı1.4.2; diğer ekranlar V15.ENABLED. Uygulama deposuna dokunulmaz.\n\n'+''.join(f'- [{g}]({g}/README.md)\n' for g in dict.fromkeys(s['group'] for s in states))+'\n[Önizleme](ONIZLEME.html) · [Tokenlar](TOKENS.md) · [MANIFEST](MANIFEST.json)')
write(B/'SPEC.md','# V15 — ortak SPEC\n\nKaynak önceliği: Founder15Eki brief + karar1–52; copyHB-37 r5 §14.1>§13>önceki tablolar; yüzeyv2.3, düzenv10. `source/provenance.json` kaynak özet/hash.\n\n'+''.join(f'- [{g} ekran kuralları]({g}/SPEC.md)\n' for g in dict.fromkeys(s['group'] for s in states))+'\n[★ kararlar ve renkler](TOKENS.md). Onaylı metinler yeniden yazılmaz; ayrı öneriler copy review içindedir. Native ve backend değişikliği bu teslim değildir.')
write(B/'HANDOFF.md','# TASARIMCIDAN MANAGERE MESAJ\n\nV15 tasarımının parça teslimleri aynı dalda birikir. D0 ilk commit ve ayrı1.4.2 kapsamıdır. Sonraki gruplar kapalıV15 bayrağı için hazırlanır.\n\nOkuma: README → grupSPEC → ONIZLEME → COPY-REVIEW → VALIDATION → MANIFEST. SHA/push kanıtı teslim mesajında; MANIFEST kendini listelemez.\n\nHB-37 dosyası r5 olarak güncellenmiş: 3 LinkedIn değeri §14.1’den AYNEN. METİN-EKİ BEKLİYOR durumu kaynakta kapanmış; ek söz uydurulmadı.\n\n'+''.join(f'- [{g}]({g}/HANDOFF.md)\n' for g in dict.fromkeys(s['group'] for s in states))+'\nTasarım, native uygulama/test/yayın değildir. Main birleşimi, deploy veya mağaza işlemi yok.')
write(B/'SCREEN-STATE-MATRIX.md','# V15 — toplam durum matrisi\n\n'+''.join(f'| {s["group"]} | {s["id"]} | [PNG]({s["group"]}/screens/png/{s["id"]}--en--100.png) |\n' for s in states))
write(B/'COPY-REVIEW.md','# V15 — Copy review\n\nAPPROVED COPY — HB-37 r5 + existing approved references. Dosya adı proposed teslim standardıdır; tasarım önerileri onaylı metinlerden ayrıdır. Canonical ARB’ye otomatik merge yok. Anahtar bazlı ekran/EN/TR/kaynak listeleri:\n\n'+''.join(f'- [{g}]({g}/COPY-REVIEW.md)\n' for g in dict.fromkeys(s['group'] for s in states))+'\n## ÖNERİ\n\nOnaylı metinlerde söz değişikliği yok. Geçerli LinkedIn üç değeri HB-37 r5§14.1; eksik ek metin kalmadı.')
write(B/'VALIDATION.md',f'# V15 — doğrulama özeti\n\n{len(states)} durum · {pngcount} ana PNG · {fullcount} full PNG · {len(allmeasure)} DOM yerleşim ölçümü.\n\nYatay taşma: {sum(x["horizontalOverflow"]>0 for x in allmeasure)}; <48 hedef: {sum(len(x["smallTargets"]) for x in allmeasure)}; kesilen metin: {sum(len(x["clippedText"]) for x in allmeasure)}. Detay grupların VALIDATION/evidence dosyalarında. Renk oranları TOKENS.md’de.\n\nNative cihaz, backend veya yayımlanmış ürün doğrulaması değildir.')
write(B/'evidence/summary.json',json.dumps({'states':len(states),'mainPng':pngcount,'fullPng':fullcount,'measurements':len(allmeasure),'horizontalOverflow':sum(x['horizontalOverflow']>0 for x in allmeasure),'smallTargets':sum(len(x['smallTargets']) for x in allmeasure),'clippedText':sum(len(x['clippedText']) for x in allmeasure)},indent=2))
# Root overview uses first state from each completed group.
thumbs=[]
for g in dict.fromkeys(s['group'] for s in states):
 representative={'secici':'map-networking','filtre':'filters-options','meslek':'occupation-search','linkedin':'linkedin-confirmed','kart-adimi':'card-filled','ayarlar-topluluk':'settings-both','professional':'professional-list'}
 s=next(s for s in states if s['id']==representative[g]) if g in representative else next(s for s in states if s['group']==g);p=B/g/'screens/png'/f"{s['id']}--en--100.png"
 if p.exists():thumbs.append((g,Image.open(p).resize((195,422))))
if thumbs:
 cols=min(4,len(thumbs));im=Image.new('RGB',(cols*227+32,math.ceil(len(thumbs)/cols)*478+32),'#E7E3DA');draw=ImageDraw.Draw(im);font=ImageFont.truetype(str(B/'assets/Geist-Regular.ttf'),17)
 for i,(n,p) in enumerate(thumbs):x=32+(i%cols)*227;y=24+(i//cols)*478;im.paste(p,(x,y));draw.text((x,y+430),n,fill='#191A17',font=font)
 im.save(B/'OVERVIEW.png',optimize=True)
# Main catalog extends only this file; historical states remain intact.
p=R/'EKRAN-KATALOGU.json';cat=json.loads(p.read_text());cat=[x for x in cat if x.get('source')!='v15']
for s in states:
 for lang in ['en','tr']:
  for scale in ['100','200']:
   for width in [390,412]:cat.append({'id':s['id'],'lang':lang,'scale':scale,'width':width,'source':'v15','themeVersion':'2.3','active':True,'beta':True,'featureGate':'minimum-supported-version (1.4.2)' if s['group']=='d0' else 'V15.ENABLED','file':f'v15/{s["group"]}/screens/png/{s["id"]}--{lang}--{scale}'+('--412' if width==412 else '')+'.png','spec':f'v15/{s["group"]}/SPEC.md'})
for row in cat:
 if row.get('source')!='v15' and row.get('id','').startswith(('intent-send-','intent-accept-')):
  row['visibilityCondition']='V15.ENABLED == false'
  row['v15Retirement']='Session purpose selection removed. Keep historical asset for flag-off only.'
cat=[r for r in cat if r.get('id')!='v15-retirement-rules']
cat.append({'id':'v15-retirement-rules','kind':'conditional-component-retirement','source':'v15-policy','active':False,'beta':False,'when':'V15.ENABLED == true','hide':['Y2 Why are you here / session purpose selection','nearby person purpose badge','Send anyway / new 10-day mismatch flow','Profile default purpose'],'flagOff':'Existing behaviour remains unchanged','retainExistingExpiry':'Existing 10-day records expire on their existing date; no new ones','replacement':'v15/topluluk-kayit + v15/ayarlar-topluluk','reference':'Founder 15 Oct decisions32,36; earlier y1-y2/profil-al packages retained in their Git history'})
write(p,json.dumps(cat,ensure_ascii=False,indent=2))
# Optional direction kept as an explicit no-change decision.
from optional import prepare
prepare(B)
from delivery import prepare as prepare_delivery
prepare_delivery(B)
# Manifest files exclude itself, generated last.
files=[{'file':str(p.relative_to(B)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(B.rglob('*')) if p.is_file() and p.name!='MANIFEST.json' and '__pycache__' not in p.parts]
write(B/'MANIFEST.json',json.dumps({'theme':'2.3','counts':{'states':len(states),'mainPng':pngcount,'fullPng':fullcount,'filesExcludingManifest':len(files)},'files':files},ensure_ascii=False,indent=2))
print(json.dumps({'states':len(states),'main':pngcount,'full':fullcount,'files':len(files),'checks':len(allmeasure),'issues':sum(bool(x['horizontalOverflow']or x['smallTargets']or x['clippedText']) for x in allmeasure)}))
