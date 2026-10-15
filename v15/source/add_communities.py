from pathlib import Path
import json,copy
B=Path(__file__).resolve().parents[1];p=B/'source/states.json';states=json.loads(p.read_text());groups=['topluluk-kayit','gecis','ayarlar-topluluk','secici'];states=[s for s in states if s['group'] not in groups]
def P(k,**kw):return dict(type='text',key=k,**kw)
def N(k,**kw):return dict(type='notice',key=k,**kw)
def A(k,**kw):return dict(key=k,**kw)
def AS(*a,**kw):return dict(type='actions',items=list(a),**kw)
def S(id,g,t,blocks,notes='',**kw):states.append(dict(id=id,group=g,title=t,blocks=blocks,notes=notes,**kw))
def opt(c,selected=False,to=None):return dict(key='communityOption'+c,description='communityOption'+c+'Desc',community=c if c!='Both' else None,selected=selected,value=c,**({'to':to} if to else {}))
def picker(v='',start=False):return dict(type='choices',key='communityBothStartWith' if start else 'communityChooseTitle',hideLegend=not start,name='community',cards=True,items=[opt(c,c==v,('community-both-'+c.lower() if start else 'community-'+c.lower())) for c in (['Networking','Friendship'] if start else ['Networking','Friendship','Both'])])
for mode in ['none','networking','friendship','both','both-start','both-networking','both-friendship','saving','failed']:
 start=mode.startswith('both-');val=mode.replace('both-','').title() if start else mode.title();selected=mode not in ['none','both-start'];blocks=[] if start else [P('communityChooseBody')]
 blocks+=[picker(val,start),P('communityNotDating',helper=True)]
 if mode=='failed':blocks+=[N('communityChooseSaveFailed',error=True)]
 blocks+=[AS(A('v15LinkedinContinue',primary=True,disabled=not selected or mode=='saving',busy=mode=='saving',reason='errorGenderRequired' if not selected else None,to='community-both-start' if mode=='both' else 'community-saving'))]
 S('community-'+mode,'topluluk-kayit','communityBothStartWith' if start else 'communityChooseTitle',blocks,'No preselection. Both requires explicit starting community. Initial selection does not consume a change. Friendship-only skips job/LinkedIn; card step still appears. Error retains chosen community.',layout='onboarding',ack='migration-occupation' if mode=='saving' else None,reject='community-failed' if mode=='saving' else None)
# preserve Networking selected in saving / failure
for s in states:
 if s['id'] in ['community-saving','community-failed']:s['blocks'][1]=picker('Networking')

def visibility(selected='Everyone',disabled=False):return dict(type='choices',key='profileLinkedinVisibilityTitle',name='visibility',items=[dict(key='profileLinkedinVisibility'+v,description='profileLinkedinVisibility'+v+'Desc',selected=v==selected,disabled=disabled,value=v) for v in ['Nobody','Connections','Everyone']])
S('migration-intro','gecis','v15IntroTitle',[P('v15IntroBody'),P('v15IntroNoGuess'),dict(type='link',key='v15WhatChanged',href='https://useimhere.com/privacy'),AS(A('v15LinkedinContinue',primary=True,to='migration-community'))],'No inferred choice. Not visible in discovery until community selection.',layout='onboarding')
S('migration-community','gecis','communityChooseTitle',[P('communityChooseBody'),picker(),P('communityNotDating',helper=True),AS(A('v15LinkedinContinue',disabled=True,reason='errorGenderRequired'))],'Reuses registration selection component. Initial selection ends previous check-in; no rate-limit cost. LinkedIn step only if stored.',layout='onboarding')
for mode in ['everyone','connections','nobody','saving','failed','offline']:
 val='Everyone' if mode in ['everyone','failed','offline'] else 'Nobody' if mode=='nobody' else 'Connections';blocks=[P('v15LinkedinBody'),visibility(val,mode=='saving'),P('v15LinkedinChangeLater',helper=True)]
 if mode in ['failed','offline']:blocks+=[N('offline' if mode=='offline' else 'profileLinkedinVisibilitySaveFailed',error=True)]
 blocks+=[AS(A('v15LinkedinContinue',primary=True,to='migration-linkedin-saving',disabled=mode=='saving',busy=mode=='saving'),A('cancel',to='migration-intro'))]
 S('migration-linkedin-'+mode,'gecis','v15LinkedinTitle',blocks,'Only for stored LinkedIn. Everyone is existing value; no extra visual emphasis. Dismiss keeps Everyone and repeats next launch. Save failure restores Everyone and stays on screen. Body uses HB-37 r5.',layout='dialog',ack='migration-occupation' if mode=='saving' else None,reject='migration-linkedin-failed' if mode=='saving' else None)
S('migration-occupation','gecis','v15OccupationTitle',[P('v15OccupationBody'),AS(A('v15OccupationChoose',to='occupation-empty'),A('v15OccupationNotNow',action='skip-occupation'),equal=True)],'Optional one-time invitation. Equal button treatment. Existing free text is not mapped automatically.',layout='onboarding')
S('migration-offline','gecis','v15IntroTitle',[P('v15IntroBody'),N('offline',error=True),AS(A('checkInRetry',to='migration-intro'))],'Network failure keeps route and avoids inferred membership.',layout='onboarding')

def row(c,active,member,limited=False):
 b=[]
 if active:b+=[dict(type='tag',key='communitySettingsInUse',community=c)]
 if not limited:
  acts=[]
  if member:
   if not active:acts.append(A('communitySwitchConfirm',to='settings-switch-confirm'))
   if active and not both: b+=[P('communitySettingsLastOne',helper=True)]
   else:acts.append(A('communitySettingsLeave',community=c,to='settings-leave-active' if active else 'settings-leave-inactive'))
  else:acts.append(A('communitySettingsJoin',community=c,to='settings-join-confirm'))
  if acts:b+=[AS(*acts)]
 return dict(type='row',key='communityOption'+c,community=c,blocks=b)
for mode in ['one','both','checked-in','going','limit','last-one','failed','switch-done','join-done','leave-done']:
 both=mode not in ['one','last-one','leave-done'];active='Friendship' if mode=='switch-done' else 'Networking';blocks=[P('communitySettingsHelp'),row('Networking',active=='Networking',True,mode=='limit'),row('Friendship',active=='Friendship',both,mode=='limit'),P('communitySettingsLimitRule',helper=True)]
 if mode in ['checked-in','going']:blocks+=[N('communityCheckInEndsNote')]
 if mode=='going':blocks+=[P('communitySwitchGoingNote',helper=True)]
 if mode=='limit':blocks+=[N('communitySwitchLimitReached')]
 if mode=='failed':blocks+=[N('communitySettingsChangeFailed',error=True)]
 if mode.endswith('-done'):blocks+=[N({'switch-done':'communitySwitchDone','join-done':'communitySettingsJoined','leave-done':'communitySettingsLeft'}[mode],community='Friendship')]
 S('settings-'+mode,'ayarlar-topluluk','communitySettingsTitle',blocks,'Only own membership. Join/leave/switch count separately in rolling24h; first selection free. '+('Server acknowledgement received.' if mode.endswith('done') else 'No optimistic membership change.'),back='nearby-networking')
for mode in ['switch-confirm','switch-checkin','switch-going','join-confirm','leave-inactive','leave-active','leave-active-going']:
 join=mode.startswith('join');leave=mode.startswith('leave');active=mode.startswith('leave-active');com='Networking' if active else 'Friendship';title='communitySettingsJoinTitle' if join else 'communitySettingsLeaveTitle' if leave else 'communitySwitchTitle';blocks=[]
 if join:blocks=[P('communitySettingsJoinBody')]
 elif leave:
  if active:blocks+=[P('communitySettingsLeaveActiveNote',community=com,other='Friendship'),N('communityCheckInEndsNote')]
  if mode=='leave-active-going':blocks+=[P('communitySwitchGoingNote',helper=True)]
  blocks+=[P('communitySettingsLeaveBody',community=com)]
 else:
  blocks=[P('communitySwitchBodyCheckedIn' if mode in ['switch-checkin','switch-going'] else 'communitySwitchBody',community=com)]
  if mode=='switch-going':blocks+=[P('communitySwitchGoingNote',helper=True)]
 blocks+=[P('communitySwitchRemaining',params={'remaining':2},helper=True),AS(A('communitySettingsJoinConfirm' if join else 'communitySettingsLeaveConfirm' if leave else 'communitySwitchConfirm',primary=True,to='settings-'+('joining' if join else 'leaving' if leave else 'switching')),A('cancel',to='settings-both'))]
 S('settings-'+mode,'ayarlar-topluluk',title,blocks,'Confirmation before mutation. Inactive leave/join does not change active community or end check-in. Active leave order: active note, check-in, Going, leave body, remaining. No reset time or countdown.',community=com,other='Friendship',layout='dialog')
for mode in ['joining','leaving','switching']:
 S('settings-'+mode,'ayarlar-topluluk','communitySettingsTitle',[N('communitySwitching',busy=True),P('communitySettingsLimitRule',helper=True)],'Pending server response, no premature success. Controls replaced by status; completion restores action availability.',layout='dialog',ack='settings-'+{'joining':'join','leaving':'leave','switching':'switch'}[mode]+'-done',reject='settings-failed')
# Indicator surfaces: own active community only. Fictional map geometry, no location marks.
for mode in ['networking','friendship','single','loading','empty','failed','offline']:
 c='Friendship' if mode=='friendship' else 'Networking';b=[dict(type='community',community=c)]
 if c=='Networking' and mode not in ['loading','failed','offline']:b+=[AS(A('nearbyFilters',icon='filter',to='filters-options'))]
 if mode=='loading':b+=[N('nearbyLoading',busy=True)]
 elif mode=='empty':b+=[P('nearbyEmpty')]
 elif mode in ['failed','offline']:b+=[N('nearbyOffline' if mode=='offline' else 'nearbyFailed',error=True),AS(A('checkInRetry',to='nearby-loading'))]
 else:b+=[dict(type='person',name='Maya',blocks=[])]
 S('nearby-'+mode,'secici','nearbyPeople',b,'Indicator only: opens Settings → Communities. Single community is also actionable. Other person community label absent. Switching removes old content before new load.',nav='Nearby')
for mode in ['networking','friendship','single','empty','loading','failed','offline']:
 c='Friendship' if mode=='friendship' else 'Networking';b=[dict(type='map',empty=mode in ['empty','loading','failed','offline']),dict(type='maptools',community=c)]
 if mode=='loading':b+=[N('mapLoading',busy=True)]
 if mode=='empty':b+=[P('mapNoActivity',helper=True)]
 if mode in ['failed','offline']:b+=[N('mapOffline' if mode=='offline' else 'mapUnavailable',error=True),AS(A('checkInRetry',to='map-loading'))]
 b+=[P('mapBody',helper=True)]
 S('map-'+mode,'secici','mapOpen',b,'Full-area map. Own community pill top-left and Show my area top-right, attribution separate above bottom nav. K=2 suppression empty result; no inference about people. Geometry is a fictional design fixture; no precise locations.',layout='map',nav='Nearby')
S('events-community','secici','navEvents',[dict(type='community',community='Networking'),P('nearbyEmpty')],'Indicator opens Settings. Empty fixture uses neutral existing text; Events-specific empty copy is resolved before final capture.',nav='Events')
for c in ['Networking','Friendship']:
 S('connection-'+c.lower(),'secici','messagesConnections',[dict(type='person',name='Maya',blocks=[dict(type='tag',key='connectionCommunityBadge',community=c)])],'Historical connection community from the connection record only. Not the other person’s current membership.',nav='Messages')
p.write_text(json.dumps(states,ensure_ascii=False,indent=2)+'\n');print(len(states),'states')
