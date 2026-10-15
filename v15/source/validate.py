"""Read-only structural/artifact/copy audit; --write saves evidence before final manifest refresh."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
from PIL import Image
B=Path(__file__).resolve().parents[1];R=B.parent
states=json.loads((B/'catalog.json').read_text())['states'];errs=[];checks=[]
def check(name,ok,detail=None):
 checks.append({'check':name,'pass':bool(ok),'detail':detail})
 if not ok:errs.append(name)
req=['README.md','SPEC.md','HANDOFF.md','SCREEN-STATE-MATRIX.md','VALIDATION.md','COPY-REVIEW.md','copy.proposed.json','catalog.json','OVERVIEW.png','evidence']
groups=list(dict.fromkeys(s['group'] for s in states))+['italik-acilis']
check('12 delivery folders',len(groups)==12)
for g in ['']+groups:check('required files '+(g or 'root'),all((B/g/x).exists() for x in req))
main=full=measurecount=0
for s in states:
 d=B/s['group'];ms=json.loads((d/'evidence'/f"{s['id']}.json").read_text());measurecount+=len(ms)
 check('layout '+s['id'], all(not(x['horizontalOverflow'] or x['smallTargets'] or x['clippedText'] or x.get('verticalOverlaps') or x.get('verticalTextOverflow') or x.get('unreachableContent')) and x.get('measurementVersion')==2 and x['h1']==1 and x['fonts']=='loaded' for x in ms))
 check('320 iOS/Android '+s['id'],all(any(x['width']==320 and x['scale']==200 and x['locale']==l and x['platform']==p for x in ms) for l in ['en','tr'] for p in ['ios','android']))
 for w,h in [(390,844),(412,915)]:
  for l in ['en','tr']:
   for scale in [100,200]:
    stem=f"{s['id']}--{l}--{scale}"+('--412' if w==412 else '')
    p=d/'screens/png'/f'{stem}.png';im=Image.open(p);main+=1
    check('PNG '+str(p.relative_to(B)),im.size==(w*4,h*4) and im.mode=='RGB',{'size':im.size,'mode':im.mode})
    m=next(x for x in ms if x['width']==w and x['locale']==l and x['scale']==scale and x['position']=='top')
    f=d/'screens/png'/f'{stem}--full.png'
    check('full coverage '+stem,f.exists()==m['fullNeeded'])
    if f.exists():
     im=Image.open(f);full+=1
     check('full PNG '+stem,im.width==w*4 and im.height>h*4 and im.height%4==0 and im.mode=='RGB')
check('PNG totals',main==len(states)*8 and full==sum(1 for p in B.glob('*/screens/png/*--full.png')),{'main':main,'full':full})
# Independently recover authoritative values; never use the generated copy bank as truth.
expected={};L=R/'02-SON-EKLER/imhere-cream-complete-v2.2/l10n'
def addarb(en,tr):
 for k,v in en.items():
  if not k.startswith('@') and isinstance(v,str) and k in tr:expected[k]=(v,tr[k])
addarb(json.loads((L/'app_en.arb').read_text()),json.loads((L/'app_tr.arb').read_text()))
for stem in ['contact-card-complete-patch','contact-card-v1-patch','v6-final-copy-patch','compact-v10-patch','release8-approved-patch']:
 addarb(json.loads((L/f'{stem}_en.arb').read_text()),json.loads((L/f'{stem}_tr.arb').read_text()))
G=Path('/Users/velio/Desktop/here/ops/V15/graph/_kaynak/app/lib/l10n')
for k,v in json.loads((G/'app_en.arb').read_text()).items():
 if k not in expected and not k.startswith('@') and isinstance(v,str):expected[k]=(v,json.loads((G/'app_tr.arb').read_text()).get(k))
old=Path('/Users/velio/Desktop/here/harbor/profil-al-metin-son.md').read_text()
for line in old.splitlines():
 p=[x.strip() for x in line.split('|')[1:-1]]
 if len(p)>=4 and p[0].isdigit():expected[p[1]]=(p[2],p[3])
hb=Path('/Users/velio/Desktop/here/harbor/v15-uygulama-metinleri.md').read_text()
for line in hb.splitlines():
 p=[x.strip() for x in line.split('|')[1:-1]]
 if len(p)<3:continue
 k=p[0].split(' ')[0]
 if not re.fullmatch('[a-z][A-Za-z0-9]+',k) or p[1].startswith('~~') or 'EMEKLİ' in p[1]:continue
 if k in ['eventV1CategoryNetworking','y1CategoryNetworking']:expected[k]=(p[2],p[3])
 elif k=='occupation':expected[k]=('Job title','Meslek')
 elif k=='showOccupation':expected[k]=('Show my job title','Mesleğim görünsün')
 else:expected[k]=(p[1],p[2])
for k,l,v in re.findall(r'`(\w+)` (EN|TR)[^\n]*\n```\n([^\n]+)\n```',hb):
 if k in expected:
  pair=list(expected[k]);pair[0 if l=='EN' else 1]=v;expected[k]=tuple(pair)
r6=re.search(r'\| r6-10[^\n]*EN `([^`]+)` · TR `([^`]+)`',hb)
assert r6, 'Approved r6 key missing'
expected['v15LinkedinChangedBody']=r6.groups()
copy=json.loads((B/'copy.proposed.json').read_text())['entries'];deviations=[]
for e in copy:
 if expected.get(e['key'])!=(e['en'],e['tr']):deviations.append({'key':e['key'],'expected':expected.get(e['key']),'delivered':(e['en'],e['tr'])})
check('copy exact authoritative EN/TR',not deviations,{'keys':len(copy),'deviations':deviations})
retired=['occupationPlaceholder','profileOccupationRequired','profileLinkedinShow','profileLinkedinShowHelp','profileLinkedinPausedResumeNote']
baseline=json.loads(subprocess.check_output(['git','show','0aaa981d83241d30e24b28fcdc70a76ca48563bf:v15/copy.proposed.json'],cwd=R,text=True))['entries']
now={e['key']:e for e in copy}
check('195 existing approved values unchanged',all(e['key'] in now and (e['en'],e['tr'])==(now[e['key']]['en'],now[e['key']]['tr']) for e in baseline))
check('retired copy absent',not any(e['key'] in retired or e['key'].startswith('profilePurpose') for e in copy))
alltext=json.dumps(states,ensure_ascii=False)
check('only placeholder LinkedIn URL',not re.search(r'linkedin\.com/in/(?!…)',alltext))
check('no real portraits',not any(p.suffix.lower() in ['.jpg','.jpeg','.webp'] for p in (B/'assets').rglob('*')))
t=json.loads((B/'tokens.json').read_text())
check('text and control contrast',t['contrastOnCream']['text']>=4.5 and t['contrastOnCream']['textSecondary']>=4.5 and t['contrastOnCream']['inputBorder']>=3)
check('community contrast',all(t['contrastOnCream'][k]>=4.5 and t['communityOnRatios'][k]>=4.5 and t['communityLightRatios'][k]>=4.5 for k in ['community.networking','community.friendship']))
check('contrast stress',all(not (x['horizontalOverflow'] or x['smallTargets'] or x['clippedText']) for x in json.loads((B/'evidence/contrast-stress.json').read_text())))
inter=json.loads((B/'evidence/interaction-results.json').read_text());check('observed interactions',len(inter['checks'])==14 and all(x['status']=='PASS' for x in inter['checks']))
check('SVG icon count',len(list((B/'ikonlar/assets/svg').glob('*.svg')))==15)
baseline_tokens=json.loads(subprocess.check_output(['git','show','0aaa981d83241d30e24b28fcdc70a76ca48563bf:v15/tokens.json'],cwd=R,text=True))
check('approved appearance tokens unchanged',all(t[k]==baseline_tokens[k] for k in ['colors','space','radius','iconStroke','targetMin','motion']))
cat=json.loads((R/'EKRAN-KATALOGU.json').read_text());matches=[x for x in cat if x.get('id')=='match-different']
check('match-different flag-off only',bool(matches) and all(x.get('visibilityCondition')=='V15.ENABLED == false' for x in matches))
check('state matrix header','| Bölüm | State | Görsel |' in (B/'SCREEN-STATE-MATRIX.md').read_text())
# Manager correction requirements, separately from generic layout checks.
byid={x['id']:x for x in states}
def walk(x):
 if isinstance(x,dict):
  yield x
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
def keys(id):return [n['key'] for n in walk(byid[id]) if 'key' in n]
changed=['migration-linkedin-changed-'+x for x in ['default','other','saving','failed','offline']]
check('R1 standalone changed-link states',all(x in byid and 'v15LinkedinChangedBody' in keys(x) and 'v15LinkedinBody' not in keys(x) and byid[x]['storedVisibility']=='Nobody' for x in changed))
check('R1 stored selection restored',all(next(n for n in walk(byid[x]) if n.get('type')=='choices')['items'][0]['selected'] for x in [changed[0],changed[3],changed[4]]))
check('R1 conversation placement', 'linkedin-connection' not in byid and 'linkedin-chat-connection' in byid and byid['linkedin-chat-connection']['fixtureTitle']['en']=='Maya')
check('R1 operation failures','communitySwitchFailed' in keys('settings-switch-failed') and 'communitySettingsChangeFailed' in keys('settings-failed') and byid['settings-switching']['reject']=='settings-switch-failed')
check('R1 textless progress',all('communitySwitching' not in keys(x) and any(n.get('type')=='progress' for n in walk(byid[x])) for x in ['settings-joining','settings-leaving']))
check('R1 check-in notice',all(any(n.get('type')=='notice' and n.get('key')=='communityCheckInEndsNote' for n in walk(byid[x])) for x in ['settings-switch-checkin','settings-switch-going']))
edit=[x for x in states if x.get('context')=='profile-edit']
check('R1 profile job editing',bool(edit) and all(x['title']=='occupation' and x.get('back') and 'occupationSkip' not in keys(x['id']) for x in edit))
check('R1 Other title inline',all(any(n.get('type')=='occupations' and n.get('inlineTitle',{}).get('key')=='occupationOwnTitleLabel' for n in walk(byid[x])) for x in ['occupation-other','occupation-signup-other']))
check('R1 hidden duplicate legend',all(n.get('hideLegend') for x in states if x['id'].startswith('migration-linkedin-') for n in x['blocks'] if n.get('type')=='choices'))
check('R1 Continue after saved','signupLinkedinSkip' not in keys('linkedin-saved') and 'v15LinkedinContinue' in keys('linkedin-saved'))
check('R1 settings first add default note','profileLinkedinVisibilityDefaultNote' in keys('linkedin-settings-empty') and 'signupLinkedinSkip' not in keys('linkedin-settings-empty'))
check('R1 settings read gates',all(x in byid for x in ['settings-loading','settings-read-failed','linkedin-settings-loading','linkedin-settings-read-failed']))
check('R1 filtered Nearby context',all(byid[x]['title']=='navNearby' and any(b.get('type')=='community' for b in byid[x]['blocks']) and 'nearbyFiltersOnBadge' in keys(x) for x in ['filters-not-enough','filters-no-longer-enough']))
check('R1 forbidden colour pair',any(x['foreground']=='#696A62' and x['background']=='#E5E9EF' and x['contrast']<4.5 for x in t['forbiddenPairings']))
# Actual tracked and untracked scope, including currently uncommitted delivery work.
changed=subprocess.check_output(['git','diff','--name-only','58bf8c4380c9e2b8487b32d5d94f6f1e683ad649'],cwd=R,text=True).splitlines()
changed+=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=R,text=True).splitlines()
check('design-only scope',all(x.startswith('v15/') or x=='EKRAN-KATALOGU.json' for x in changed))
m=json.loads((B/'MANIFEST.json').read_text());actual={str(p.relative_to(B)) for p in B.rglob('*') if p.is_file() and p.name!='MANIFEST.json' and '__pycache__' not in p.parts};listed={e['file'] for e in m['files']}
# During --write this script and its first report may not be in the previous manifest; final readonly audit is strict.
if '--write' not in sys.argv:
 check('manifest path coverage',actual==listed,{'actual':len(actual),'listed':len(listed)})
 check('manifest bytes/SHA256',all((B/e['file']).stat().st_size==e['bytes'] and hashlib.sha256((B/e['file']).read_bytes()).hexdigest()==e['sha256'] for e in m['files']))
 check('manifest counts',m['counts']['states']==len(states) and m['counts']['mainPng']==main and m['counts']['fullPng']==full and m['counts']['filesExcludingManifest']==len(actual))
result={'status':'PASS' if not errs else 'FAIL','states':len(states),'mainPng':main,'fullPng':full,'measuredLayouts':measurecount,'approvedCopyKeys':len(copy),'copyDeviations':len(deviations),'failedChecks':errs,'checks':checks,'scope':'Browser design and artifact audit; not native/backend/accessibility-service/release evidence.'}
if '--write' in sys.argv:(B/'evidence/final-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False))
sys.exit(1 if errs else 0)
