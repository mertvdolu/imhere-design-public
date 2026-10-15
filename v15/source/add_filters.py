from pathlib import Path
import json
B=Path(__file__).resolve().parents[1];p=B/'source/states.json';ss=json.loads(p.read_text());ss=[x for x in ss if x['group']!='filtre'];cat=json.loads((B/'source/occupation-catalog.json').read_text());jobs=[x for x in cat['occupations'] if not x['id'].startswith('other-')][:6]
def P(k,**kw):return dict(type='text',key=k,**kw)
def N(k,**kw):return dict(type='notice',key=k,**kw)
def A(k,**kw):return dict(key=k,**kw)
def AS(*a,**kw):return dict(type='actions',items=list(a),**kw)
def add(mode,b,**kw):ss.append(dict(id='filters-'+mode,group='filtre',title='nearbyFilters',blocks=b,notes='Networking only. Counts are explicit design fixtures, never live. Each visible option≥3, cap50+. OR among≤5 jobs, AND with LinkedIn Everyone. Panel order frozen while open; 0/1/2 same state; no saved filters.',**kw))
for mode in ['loading','options','selected','max-five','no-options','linkedin-only','failed','offline']:
 b=[P('nearbyFiltersJobHelp')]
 if mode=='loading':b+=[dict(type='skeleton',key='nearbyLoading',count=4)]
 elif mode in ['failed','offline']:b+=[N('offline' if mode=='offline' else 'errorStateChanged',error=True),AS(A('checkInRetry',to='filters-loading'))]
 elif mode=='no-options':b+=[P('nearbyFiltersNoOptions')]
 else:
  items=[]
  for i,j in enumerate(jobs):
   count=[51,24,12,8,6,3][i];items.append(dict(label={'en':j['en'],'tr':j['tr']},value=j['id'],count=count,selected=(mode=='max-five' and i<5)or(mode=='selected' and i<2),disabled=mode=='max-five' and i>=5,a11y='nearbyFiltersOptionManyA11y' if count>50 else 'nearbyFiltersOptionA11y'))
  b+=[dict(type='choices',key='nearbyFiltersJobTitles',name='jobs',multiple=True,items=items)]
  if mode=='max-five':b+=[P('nearbyFiltersMaxReached',helper=True)]
 if mode not in ['loading','failed','offline']:b+=[dict(type='switch',key='nearbyFiltersLinkedinOnly',checked=mode=='linkedin-only',to='filters-linkedin-only')]
 b+=[P('nearbyFiltersThresholdNote',helper=True),P('nearbyFiltersPrivacyNote',helper=True),P('nearbyFiltersUpdateNote',helper=True)]
 if mode not in ['loading','failed','offline']:b+=[AS(A('nearbyFiltersClear',to='filters-options'),A('nearbyFiltersShowResults',primary=True,to='filters-list'))]
 add(mode,b,back='nearby-networking')
for mode in ['not-enough','no-longer-enough']:
 add(mode,[P('nearbyFiltersOnBadge',params={'count':2}),N('nearbyFiltersNotEnough' if mode=='not-enough' else 'nearbyFiltersNoLongerEnough'),P('nearbyFiltersNotEnoughBody'),AS(A('nearbyFilters',to='filters-selected'),A('nearbyFiltersClear',to='nearby-networking'))],nav='Nearby')
add('friendship',[P('nearbyFiltersFriendshipNote'),AS(A('viewBack',to='nearby-friendship'))],back='nearby-friendship')
add('list',[dict(type='community',community='Networking'),AS(A('nearbyFiltersOnBadge',params={'count':2},icon='filter',to='filters-selected')),*[dict(type='person',name=n) for n in ['Maya','Alex','Sam']]],nav='Nearby')
p.write_text(json.dumps(ss,ensure_ascii=False,indent=2)+'\n')
m=Path('v15/source/group-notes.json');z=json.loads(m.read_text());z['filtre']={'spec':'Tam ekran kaydırılan alt sayfa (★), back48. Checkbox meslek satırı + sayım;6 tasarım örneği51/24/12/8/6/3,51→50+. Liste sunucu snapshot sırasıyla açılır; seçimde yer değişmez.5 seçildiğinde seçilmemiş satırlar pasif ve MaxReached görünür. LinkedIn switch yanında hiçbir sayı yok. 0/1/2 TEK not-enough görünümü. Threshold ve privacy notları aynen.','handoff':'Only Networking. Max5 OR, LinkedIn AND. active-count=#selected jobs+LinkedIn flag. Seçili grup eşik altına düştüğünde filtreler korunur; kullanıcı değiştirene kadar başka listeye düşülmez. Son kullanılan filtreler yok. 50+ a11y OptionManyA11y. UpdateNote yalnız backend sayımı yaklaşık60sn ise; bu örnekte koşul true, Code teyidi olmadan söz uygulanmaz. Önizlemedeki sayılar yalnız yerleşim fixture; canlı veri değildir.','decisions':'★ Tam sayfa: %200 ve uzun TR uyarılarda sheet yüksekliğiyle mücadele etmeden tüm satırlar erişilir. ★ Görünen sıra panel açıkken sabit. YENİ BİLEŞEN — ONAY GEREKİR: counted filter row (mevcut checkbox+etiket+tabular sayı birleşimi).'};m.write_text(json.dumps(z,ensure_ascii=False,indent=2)+'\n');print('filters',12)
