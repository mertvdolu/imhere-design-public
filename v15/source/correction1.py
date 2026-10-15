"""Apply Manager V15-TASARIM-DUZELTME-1 to its accepted baseline, design repository only."""
from pathlib import Path
import json,copy,subprocess,hashlib
B=Path(__file__).resolve().parents[1];R=B.parent;BASE='0aaa981d83241d30e24b28fcdc70a76ca48563bf'
S=json.loads(subprocess.check_output(['git','show',BASE+':v15/source/states.json'],cwd=R,text=True));old=copy.deepcopy(S);idx={s['id']:s for s in S}
def clone(id,new):
 s=copy.deepcopy(idx[id]);s['id']=new;S.append(s);idx[new]=s;return s
def actions(s):return [a for b in s['blocks'] if b['type']=='actions' for a in b['items']]
def choices(s):return next(b for b in s['blocks'] if b['type']=='choices')
# 1 / 7. Existing first-transition values stay unchanged; standalone changed-link has stored Nobody.
for s in S:
 if s['id'].startswith('migration-linkedin-'):
  choices(s)['hideLegend']=True
  s['storedVisibility']='Everyone';s['transitionReason']='FIRST'
  s['notes']='Shown only when linkedinTransitionNeeded=true. FIRST uses v15LinkedinBody. Dismiss keeps the stored setting; first-transition fixture is Everyone. Failure restores the stored setting and stays here. Group legend is visually hidden but accessible.'
for suffix,source,value in [('default','everyone','Nobody'),('other','connections','Connections'),('saving','saving','Connections'),('failed','failed','Nobody'),('offline','offline','Nobody')]:
 s=clone('migration-linkedin-'+source,'migration-linkedin-changed-'+suffix)
 s['transitionReason']='LINK_CHANGED';s['storedVisibility']='Nobody'
 next(b for b in s['blocks'] if b.get('key')=='v15LinkedinBody')['key']='v15LinkedinChangedBody'
 for o in choices(s)['items']:o['selected']=o['value']==value
 for a in actions(s):
  if a['key']=='v15LinkedinContinue':a['to']='migration-linkedin-changed-saving'
  if a['key']=='cancel':a['to']='nearby-networking'
 if suffix=='saving':s['ack']='nearby-networking';s['reject']='migration-linkedin-changed-failed'
 s['notes']='Standalone LINK_CHANGED review, no intro/community steps. Stored setting Nobody; other-selection example Connections. Dismiss and failure retain stored Nobody; success only after server ack returns to the existing app. No transition if linkedinTransitionNeeded=false.'
# 2. Connection viewer is in chat, not the inbox list. Rename without retaining a misleading active state.
s=idx['linkedin-connection'];s['id']='linkedin-chat-connection';s['title']=None;s['fixtureTitle']={'en':'Maya','tr':'Maya'};s['layout']='subpage'
s['blocks']=[b for b in s['blocks'] if b['type']!='person']
for b in s['blocks']:
 if b.get('to')=='linkedin-connection':b['to']='linkedin-chat-connection'
s['notes']='Decision 56(5): LinkedIn row and ViewerNote in the connected conversation screen, never in the Connections/inbox list. Maya is the fictional conversation title. Visibility still follows the stored preference; this is a focused row-placement drawing, not a replacement for the full chat composer.'
s=idx['linkedin-chat'];s['title']=None;s['fixtureTitle']={'en':'Maya','tr':'Maya'};s['layout']='subpage';s['blocks']=[b for b in s['blocks'] if b['type']!='person'];s['notes']='Same conversation-surface placement as linkedin-chat-connection. Historical connection entry routes to this conversation; no LinkedIn field is added to readInbox/Connections list. Existing chat controls remain outside this focused specimen.'
# 3 / 4 / 5. Operation-specific failure and progress.
s=clone('settings-failed','settings-switch-failed');next(b for b in s['blocks'] if b.get('key')=='communitySettingsChangeFailed')['key']='communitySwitchFailed';s['notes']='Switch failed: old membership and active community remain. Uses communitySwitchFailed; join/leave failure remains settings-failed / communitySettingsChangeFailed.'
idx['settings-switching']['reject']='settings-switch-failed'
for id in ['settings-joining','settings-leaving']:
 s=idx[id];s['blocks'][0]={'type':'progress'};s['notes']='Pending join/leave response, no visible progress text. Reuse 24×24 loading arc, stroke1.8; progressbar labelled by screen title for accessibility. Failure uses communitySettingsChangeFailed; no premature success.'
for id in ['settings-switch-checkin','settings-switch-going']:
 idx[id]['blocks'].insert(1,{'type':'notice','key':'communityCheckInEndsNote'})
# 6. Keep signup context and explicitly separate profile editing.
for suffix,source in [('selected','selected'),('other','other'),('saving','saving'),('saved','saved'),('failed','failed')]:
 s=clone('occupation-'+source,'occupation-signup-'+suffix);s['layout']='onboarding';s['context']='signup'
 s['blocks']=[b for b in s['blocks'] if not(b['type']=='actions' and any(a['key']=='occupationRemove' for a in b['items']))]
 for a in actions(s):
  if a.get('to')=='occupation-saving':a['to']='occupation-signup-saving'
 if s.get('ack')=='occupation-saved':s['ack']='occupation-signup-saved'
 if s.get('reject')=='occupation-failed':s['reject']='occupation-signup-failed'
 s['notes']='Optional signup job step; Skip stays available. Separate from Profile editing. Save waits for server acknowledgement; no forced occupation. Other title is directly under the selected Other row.'
s=clone('occupation-empty','occupation-edit-empty');s['layout']='subpage'
for s in S:
 if s['group']=='meslek' and s.get('title')=='occupationStepTitle':
  if s.get('layout')=='subpage' or s['id']=='occupation-removing':
   s['context']='profile-edit';s['title']='occupation';s['layout']='subpage';s['back']='occupation-profile-networking'
   s['blocks']=[b for b in s['blocks'] if b.get('key') not in ['occupationStepBody','occupationStepBodyF']]
   for b in s['blocks']:
    if b['type']=='actions':b['items']=[a for a in b['items'] if a['key']!='occupationSkip'];b.pop('equal',None)
   s['notes']='Profile editing: Job title label/H1, Back and Save; no Skip. Return to the existing Profile editor. Other title immediately follows the selected Other row. Save/remove success only after server response; existing visibility preserved.'
  else:s.setdefault('context','signup')
  job=next((b for b in s['blocks'] if b['type']=='occupations'),None)
  if job:
   job['selectedTo']='occupation-signup-selected' if s.get('context')=='signup' else 'occupation-selected'
   job['otherTo']='occupation-signup-other' if s.get('context')=='signup' else 'occupation-other'
   title=next((b for b in s['blocks'] if b.get('key')=='occupationOwnTitleLabel'),None)
   if title:job['inlineTitle']=title;s['blocks'].remove(title)
# 8. Signup saved state can continue after ack; never skip a completed server-confirmed step.
for a in actions(idx['linkedin-saved']):
 if a['key']=='signupLinkedinSkip':a.clear();a.update({'key':'v15LinkedinContinue','to':'card-empty'})
idx['linkedin-saved']['notes']+=' Server-confirmed saved state: Continue replaces Skip and opens the optional card step.'
# 9. First add from Settings, with explicit default note, no signup Skip.
s=clone('linkedin-empty','linkedin-settings-empty');s['title']='profileLinkedin';s['layout']='subpage';s['context']='settings';s['back']='occupation-profile-networking'
s['blocks'][0]={'type':'text','key':'profileLinkedinHelp'}
for a in actions(s):
 if a['key']=='signupLinkedinSkip':a.clear();a.update({'key':'cancel','action':'existing-back'})
s['blocks'].insert(-1,{'type':'text','key':'profileLinkedinNetworkingNote','helper':True})
s['notes']='Settings → LinkedIn, first add with no stored link. Everyone standard radio selection; profileLinkedinVisibilityDefaultNote below options. Back/Cancel, not Skip. Open/check and own confirmation still required before Save.'
# 10. Read gates show neither a guessed stored value nor stale membership.
for group,title,prefix,ready in [('ayarlar-topluluk','communitySettingsTitle','settings','settings-both'),('linkedin','profileLinkedin','linkedin-settings','linkedin-stored')]:
 for kind in ['loading','read-failed']:
  id=prefix+'-'+kind
  s={'id':id,'group':group,'title':title,'layout':'subpage','context':'settings','back':'nearby-networking','blocks':[], 'notes':'Settings read gate. No guessed membership, link, default visibility, or stale controls until current server data is read. Existing generic error + Retry; no mutation is attempted.'}
  if kind=='loading':s['blocks']=[{'type':'progress'}];s['ack']=ready;s['reject']=prefix+'-read-failed'
  else:s['blocks']=[{'type':'notice','key':'errorStateChanged','error':True},{'type':'actions','items':[{'key':'checkInRetry','to':prefix+'-loading'}]}]
  S.append(s)
# 11. Both threshold outcomes are the filtered Nearby list, not the filter editor.
for id in ['filters-not-enough','filters-no-longer-enough']:
 s=idx[id];s['title']='navNearby';s['blocks']=s['blocks'][1:]
 s['blocks'][:0]=[{'type':'community','community':'Networking'},{'type':'actions','items':[{'key':'nearbyFiltersOnBadge','params':{'count':2},'icon':'filter','to':'filters-selected'}]}]
 for b in s['blocks'][2:]:
  if b['type']=='actions':b['items']=[a for a in b['items'] if a['key']!='nearbyFilters']
 s['notes']='Filtered Nearby list: Nearby H1, own community indicator, 2 filters on button, selected filters retained. 0/1/2 share this threshold state; no hidden count shown. Edit via count button or explicitly clear.'
# Stable group ordering, keeping new states in their existing section.
order=list(dict.fromkeys(s['group'] for s in old));S.sort(key=lambda s:order.index(s['group']))
(B/'source/states.json').write_text(json.dumps(S,ensure_ascii=False,indent=2)+'\n')
bank=json.loads((B/'source/copy-bank.json').read_text());bank['v15LinkedinChangedBody']={'key':'v15LinkedinChangedBody','en':'Your LinkedIn link has changed. Check who can see it.','tr':'LinkedIn bağlantın değişti. Kimin görebileceğini kontrol et.','source':'HB-37 r6 / HB-41 §15 r6-10; decision58','status':'APPROVED — Manager (Founder delegation), decision58'}
(B/'source/copy-bank.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n')
# Fresh screenshots only for changed visual state definitions; all states get the new vertical audit.
oldidx={s['id']:s for s in old}
def vis(s):return {k:v for k,v in s.items() if k not in ['notes','context','storedVisibility','transitionReason','ack','reject','back']}
affected=[s['id'] for s in S if s['id'] not in oldidx or vis(s)!=vis(oldidx[s['id']]) or s['group']=='d0']
(B/'source/correction1-plan.json').write_text(json.dumps({'base':BASE,'task':'V15-TASARIM-DUZELTME-1','changedStates':affected,'removedIds':['linkedin-connection'],'totalStates':len(S),'scope':'v15 + EKRAN-KATALOGU only; existing appearance tokens unchanged'},ensure_ascii=False,indent=2)+'\n')
# Retire old generated assets for renamed state; history remains in baseline commit.
for folder in [B/'linkedin/screens/png',B/'linkedin/evidence']:
 for p in list(folder.glob('linkedin-connection--*'))+list(folder.glob('linkedin-connection.json')):
  if p.is_file():p.unlink()
prov=json.loads((B/'source/provenance.json').read_text());hb=Path('/Users/velio/Desktop/here/harbor/v15-uygulama-metinleri.md');prompt=Path('/Users/velio/Desktop/here/ops/designer/PROMPT-V15-DUZELTME-1.md');prov['correction1']={'baseline':BASE,'task':prompt.name,'promptSha256':hashlib.sha256(prompt.read_bytes()).hexdigest(),'copyRevision':'HB-37 r6 / HB-41 §15','copySha256':hashlib.sha256(hb.read_bytes()).hexdigest(),'approvedExistingValuesChanged':0};(B/'source/provenance.json').write_text(json.dumps(prov,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'states':len(S),'capture':len(affected),'byGroup':{g:sum(s['id'] in affected and s['group']==g for s in S) for g in order}}))
