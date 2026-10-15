from pathlib import Path
import json
B=Path(__file__).resolve().parents[1];p=B/'source/states.json';ss=json.loads(p.read_text());ss=[x for x in ss if x['group'] not in ['meslek','linkedin']];cat=json.loads(Path('/Users/velio/Desktop/here/ops/V15/meslek-katalogu-uygulama.json').read_text());(B/'source/occupation-catalog.json').write_text(json.dumps(cat,ensure_ascii=False,indent=2)+'\n')
def P(k,**kw):return dict(type='text',key=k,**kw)
def N(k,**kw):return dict(type='notice',key=k,**kw)
def A(k,**kw):return dict(key=k,**kw)
def AS(*a,**kw):return dict(type='actions',items=list(a),**kw)
def S(id,g,t,b,notes='',**kw):ss.append(dict(id=id,group=g,title=t,blocks=b,notes=notes,**kw))
def field(k,**kw):return dict(type='field',key=k,**kw)
def vis(v='Everyone',disabled=False):return dict(type='choices',key='profileLinkedinVisibilityTitle',name='visibility',items=[dict(key='profileLinkedinVisibility'+x,description='profileLinkedinVisibility'+x+'Desc',selected=x==v,value=x,disabled=disabled) for x in ['Nobody','Connections','Everyone']])
for mode in ['empty','search','no-match','selected','other','hidden','legacy','replace','saving','saved','removed','failed','catalog-failed','loading']:
 b=[P('occupationStepBody'),P('occupationStepBodyF',helper=True)]
 if mode=='legacy':b+=[dict(type='fixture',en='Product designer',tr='Ürün tasarımcısı'),P('occupationLegacyNote'),P('occupationReplaceNote',helper=True)]
 if mode=='replace':b+=[P('occupationReplaceNote')]
 b+=[field('occupationSearchHint',value='designer' if mode=='search' else 'zzzzz' if mode=='no-match' else '',inputType='search',placeholder='occupationSearchHint')]
 if mode=='loading':b+=[dict(type='skeleton',key='profileLoading')]
 elif mode=='catalog-failed':b+=[N('errorStateChanged',error=True),AS(A('checkInRetry',to='occupation-loading'))]
 elif mode=='no-match':b+=[P('occupationNoMatch'),dict(type='occupations',query='none',otherOnly=True)]
 else:b+=[dict(type='occupations',query='designer' if mode=='search' else '',selected='software-engineer' if mode in ['selected','hidden','saving','saved','failed','replace'] else 'other-technology' if mode=='other' else '',expanded='technology' if mode in ['selected','hidden','saving','saved','failed','replace','other'] else '',disabled=mode=='saving')]
 if mode=='other':b+=[field('occupationOwnTitleLabel',en='Creative technologist',tr='Yaratıcı teknoloji uzmanı',help='occupationOwnTitleHelp')]
 if mode not in ['empty','no-match','search','removed','loading','catalog-failed']:
  b+=[dict(type='switch',key='showOccupation',checked=mode!='hidden',disabled=mode=='saving',help='occupationShowHelp'),P('occupationNetworkingNote',helper=True)]
 if mode=='saving':b+=[N('profileSaving',busy=True)]
 if mode=='saved':b+=[N('profileSaved')]
 if mode=='removed':b+=[N('occupationRemoved')]
 if mode=='failed':b+=[N('profileSaveFailed',error=True)]
 b+=[AS(A('profileSave',disabled=mode in ['loading','saving','catalog-failed'],busy=mode=='saving',to='occupation-saving'),A('occupationSkip',action='skip-job'),equal=True)]
 if mode in ['selected','other','hidden','legacy','saved','failed']:b+=[AS(A('occupationRemove',to='occupation-removing'))]
 S('occupation-'+mode,'meslek','occupationStepTitle',b,'Optional catalogue selection; labels from Manager catalogue1.0.1. No sensitive occupations invented. Group disclosure reuses existing expandable list. Show defaults on for first new selection, existing false preserved. Other custom title excluded from filters. Saving waits for server acknowledgement.',layout='onboarding' if mode in ['empty','loading','search','no-match'] else 'subpage',ack='occupation-saved' if mode=='saving' else None,reject='occupation-failed' if mode=='saving' else None)
S('occupation-removing','meslek','occupationStepTitle',[P('occupationNetworkingNote'),AS(A('occupationRemove',disabled=True,busy=True))],'Pending remove; no removed status until server confirms. Failure returns selected old title.',ack='occupation-removed',reject='occupation-failed')
for c in ['networking','friendship']:
 blocks=[dict(type='person',name='Maya',blocks=[dict(type='fixture',en='Software engineer',tr='Yazılım mühendisi')] if c=='networking' else [])]
 S('occupation-profile-'+c,'meslek','navProfile',blocks,'Other profile: community never displayed. Occupation only in Networking, omitted entirely in Friendship; no blank line. Fixture uses catalogue title.')
for mode in ['empty','invalid','unconfirmed','opening','confirmed','nobody','connections','saving','saved','save-failed','stored','offline','open-failed','paused','removed']:
 confirmed=mode in ['confirmed','nobody','connections','saving','saved','save-failed','stored','paused'];busy=mode in ['opening','saving'];v='Nobody' if mode=='nobody' else 'Connections' if mode in ['connections','saving'] else 'Everyone';onboard=mode not in ['stored','paused','removed']
 b=[P('signupLinkedinBody' if onboard else 'profileLinkedinHelp')]
 if mode=='paused':b+=[N('profileLinkedinPausedNote')]
 b+=[field('profileLinkedinFieldLabel',value='' if mode in ['empty','removed'] else 'linkedin.com/…' if mode=='invalid' else 'linkedin.com/in/…',placeholder='profileLinkedinHint',error='profileLinkedinInvalid' if mode=='invalid' else None,disabled=busy)]
 b+=[AS(A('profileLinkedinOpenCheck',icon='external',to='linkedin-opening',disabled=mode in ['empty','invalid','opening','saving'],busy=mode=='opening'))]
 if mode=='opening':b+=[N('profileLinkedinOpening',busy=True)]
 b+=[P('profileLinkedinOutsideAppNote',helper=True),P('profileLinkedinNoCheck',helper=True),vis(v,busy)]
 if onboard:b+=[P('profileLinkedinVisibilityDefaultNote',helper=True)]
 else:b+=[P('profileLinkedinNetworkingNote',helper=True)]
 if not confirmed:b+=[P('profileLinkedinCheckRequired',helper=True)]
 if mode in ['offline','open-failed','save-failed']:b+=[N({'offline':'offline','open-failed':'linkOpenFailed','save-failed':'profileLinkedinVisibilitySaveFailed'}[mode],error=True)]
 if mode=='saved':b+=[N('profileLinkedinSaved')]
 if mode=='removed':b+=[N('profileLinkedinRemoved')]
 if mode=='saving':b+=[N('profileLinkedinSaving',busy=True)]
 b+=[AS(A('profileLinkedinSave',to='linkedin-saving',disabled=not confirmed or busy or mode=='offline',busy=mode=='saving'),A('signupLinkedinSkip',action='skip-linkedin'),equal=True)]
 if mode in ['stored','paused','saved']:b+=[AS(A('profileLinkedinRemove',to='linkedin-remove-confirm'))]
 S('linkedin-'+mode,'linkedin','signupLinkedinTitle' if onboard else 'profileLinkedin',b,'Optional. Form → external Open/check → return own-profile confirmation → Save. Return/Yes only enables Save, not verification. No success tick or green state. Three equal radios, only dot selected. Failure restores old Everyone; source body HB-37r5. URL is fictional placeholder.',layout='onboarding' if onboard else 'subpage',ack='linkedin-confirm-return' if mode=='opening' else 'linkedin-saved' if mode=='saving' else None,reject='linkedin-open-failed' if mode=='opening' else 'linkedin-save-failed' if mode=='saving' else None)
S('linkedin-confirm-return','linkedin','profileLinkedinConfirmTitle',[dict(type='fixture',text='linkedin.com/in/…'),P('profileLinkedinHelp'),P('profileLinkedinOutsideAppNote'),P('profileLinkedinNoCheck'),AS(A('profileLinkedinConfirmYes',to='linkedin-confirmed'),A('profileLinkedinConfirmNo',to='linkedin-unconfirmed'),equal=True)],'Shown only after successful external opening and app return. Yes confirms ownership declaration only; next Save still required. Editing URL invalidates confirmation.',layout='dialog')
for mode in ['confirm','busy','failed']:
 b=[P('profileLinkedinRemoveBody'),P('contactSeenNote')]
 if mode=='busy':b+=[N('profileLinkedinRemoving',busy=True)]
 if mode=='failed':b+=[N('profileLinkedinRemoveFailed',error=True)]
 b+=[AS(A('profileLinkedinRemove',to='linkedin-remove-busy',primary=True,disabled=mode=='busy',busy=mode=='busy'),A('cancel',to='linkedin-stored',disabled=mode=='busy'))]
 S('linkedin-remove-'+mode,'linkedin','profileLinkedinRemoveConfirm',b,'Removal keeps seen-information warning. Failed removal keeps stored link. Acknowledge before Removed.',layout='dialog',ack='linkedin-removed' if mode=='busy' else None,reject='linkedin-remove-failed' if mode=='busy' else None)
for context in ['connection','chat','networking-before','friendship-before','hidden','viewer-offline','viewer-failed']:
 b=[dict(type='person',name='Maya')]
 if context not in ['friendship-before','hidden']:
  b+=[dict(type='link',key='profileLinkedin',icon=True,to='linkedin-'+context),P('profileLinkedinViewerNote',helper=True)]
 if context in ['viewer-offline','viewer-failed']:b+=[N('offline' if context=='viewer-offline' else 'linkOpenFailed',error=True),AS(A('checkInRetry',action='retry-external'))]
 S('linkedin-'+context,'linkedin','navProfile',b,'Link plain text + generic external icon. Connections/chat profile can see according to visibility across communities. Before connection Networking only. Hidden/no link identical omission; no placeholder or community field. Viewer notice immediately below link.')
p.write_text(json.dumps(ss,ensure_ascii=False,indent=2)+'\n');print(len(ss),'states')
