from pathlib import Path
import json
B=Path(__file__).resolve().parents[1];p=B/'source/states.json';s=json.loads(p.read_text());s=[x for x in s if x['group']!='kart-adimi']
def P(k,**kw):return dict(type='text',key=k,**kw)
def N(k,**kw):return dict(type='notice',key=k,**kw)
def A(k,**kw):return dict(key=k,**kw)
def AS(*a,**kw):return dict(type='actions',items=list(a),**kw)
for mode in ['empty','filled','invalid','saving','saved','failed','skipped']:
 if mode=='skipped':
  b=[dict(type='community',community='Friendship'),P('nearbyBody'),AS(A('checkInStart',primary=True,action='existing-checkin'))]
  s.append(dict(id='card-'+mode,group='kart-adimi',title='nearbyTitle',blocks=b,nav='Nearby',notes='No skipped confirmation screen in production. Shown destination after optional onboarding completes; Friendship-only also gets card step. No card is created by skipping. Other pending onboarding steps take precedence.'))
  continue
 b=[P('contactCardStepBody'),dict(type='field',key='contactPhone',inputType='tel',value='',disabled=mode=='saving'),dict(type='field',key='contactEmail',inputType='email',value='maya' if mode=='invalid' else 'maya@example.invalid' if mode in ['filled','saving','saved','failed'] else '',disabled=mode=='saving',help='contactCardStepEmailNote',error='contactFieldInvalid' if mode=='invalid' else None),dict(type='field',key='contactInstagram',value='',disabled=mode=='saving')]
 if mode=='invalid':b+=[P('contactCardStepEmailNote',helper=True)]
 if mode=='saved':b+=[N('contactCardSaved')]
 if mode=='failed':b+=[N('contactCardSaveFailed',error=True)]
 b+=[P('contactCardStepLater',helper=True),AS(A('contactCardSave',disabled=mode in ['invalid','saving'],busy=mode=='saving',to='card-skipped' if mode=='empty' else 'card-saving'),A('contactCardNotNow',to='card-skipped',disabled=mode=='saving'),equal=True)]
 s.append(dict(id='card-'+mode,group='kart-adimi',title='contactCardStepTitle',blocks=b,layout='onboarding',notes='Optional for both communities. Sign-in email not prefilled. Example.invalid is reserved fictional layout data. Fields only shared when sent in a chat, never on profile. Blank Save behaves as Not now. Equal action treatment; invalid input reason inline. Saved only after server acknowledgement.',ack='card-saved' if mode=='saving' else None,reject='card-failed' if mode=='saving' else None))
p.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n');m=Path('v15/source/group-notes.json');z=json.loads(m.read_text());z['kart-adimi']={'spec':'İsteğe bağlı kayıt adımı: telefon/e-posta/Instagram. E-posta boş; giriş e-postasından türetilmez. StepBody aynen, EmailNote e-posta altında. StepLater düğmelerin üstünde. Save/Not now aynı ikincil krem yüzey, aynı14/500, en az48 hedef; wrap/flex ile büyük yazıda alt alta. Boş Save etkin; Send bu ekranda yok.','handoff':'Tüm topluluklarda yeni kayıt için. Mevcut kullanıcılara zorunlu adım yok. Kaydetme yalnız kart sahibinin verisini günceller; sohbete gönderim değildir. CardSaved sadece server-ack; hata alanları korur. Boş Save=skip; tamamlanan onboarding ardından normalNearby, kalan adım varsa önce o. skipped PNG hedef görünümüdür, yeni ürün onay ekranı değil.','decisions':'★ Boş Save, Not now ile aynı ilerlemeyi yapar; boş kart kaydı/başarı mesajı üretmez. ★ Eşit ağırlık için iki düğme de aynı kabartmalı krem. YENİ BİLEŞEN — ONAY GEREKİR: yok. Kurmaca e-posta example.invalid; iletişim kurulmaz.'};m.write_text(json.dumps(z,ensure_ascii=False,indent=2)+'\n');print('card states',7)
