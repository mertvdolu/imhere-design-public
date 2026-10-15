from pathlib import Path
import json,re,hashlib
BASE=Path(__file__).resolve().parents[1]; REPO=BASE.parent
HB=Path('/Users/velio/Desktop/here/harbor/v15-uygulama-metinleri.md')
OLD=Path('/Users/velio/Desktop/here/harbor/profil-al-metin-son.md')
entries={}
def put(k,en,tr,src):
    if re.fullmatch(r'[a-z][A-Za-z0-9]+',k) and not en.startswith('~~') and not 'EMEKLİ' in en:
        entries[k]={'key':k,'en':en,'tr':tr,'source':src,'status':'APPROVED — source / existing design reference'}
# Existing shipped design copy, without rewriting any canonical ARB.
L=REPO/'02-SON-EKLER/imhere-cream-complete-v2.2/l10n'
common={l:json.loads((L/f'app_{l}.arb').read_text()) for l in ['en','tr']}
for k,en in common['en'].items():
    if not k.startswith('@') and isinstance(en,str) and k in common['tr']:put(k,en,common['tr'][k],'v2.3 l10n/app_*.arb')
for stem in ['contact-card-complete-patch','contact-card-v1-patch','v6-final-copy-patch','compact-v10-patch','release8-approved-patch']:
    a={l:json.loads((L/f'{stem}_{l}.arb').read_text()) for l in ['en','tr']}
    for k,en in a['en'].items():
        if not k.startswith('@') and isinstance(en,str) and k in a['tr']:put(k,en,a['tr'][k],f'v2.3 {stem}')
for n,line in enumerate(OLD.read_text().splitlines(),1):
    p=[s.strip() for s in line.split('|')[1:-1]]
    if len(p)>=4 and p[0].isdigit():put(p[1],p[2],p[3],f'HB-20 final §3 line {n}; reused by HB-37 §7')
for n,line in enumerate(HB.read_text().splitlines(),1):
    p=[s.strip() for s in line.split('|')[1:-1]]
    if len(p)>=3:
        k=p[0].split(' ')[0]
        if k in ['eventV1CategoryNetworking','y1CategoryNetworking']:put(k,p[2],p[3],f'HB-37 r5 §5 line {n}')
        elif k=='occupation':put(k,'Job title','Meslek','HB-37 r5 §6')
        elif k=='showOccupation':put(k,'Show my job title','Mesleğim görünsün','HB-37 r5 §6')
        else:put(k,p[1],p[2],f'HB-37 r5 line {n}')
for k,locale,val in re.findall(r'`(\w+)` (EN|TR)[^\n]*\n```\n([^\n]+)\n```',HB.read_text()):
    if k in entries:entries[k][locale.lower()]=val;entries[k]['source']='HB-37 r5 §14.1 FINAL'
for k in list(entries):
    if k.startswith('profilePurpose') or k in ['profileLinkedinShow','profileLinkedinShowHelp','occupationPlaceholder','profileOccupationRequired','profileLinkedinPausedResumeNote']:
        entries.pop(k)
(BASE/'source/copy-bank.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
(BASE/'source/provenance.json').write_text(json.dumps({'theme':'Cream & Ink v2.3','baseCommit':'58bf8c4380c9e2b8487b32d5d94f6f1e683ad649','copy':[{'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [HB,OLD]],'precedence':'HB-37 r5 §14.1 > §13 > earlier tables. Latest approved source resolves METİN-EKİ BEKLİYOR.','privacy':'No real profile or contact data. Fictional labels and layout fixtures only.'},ensure_ascii=False,indent=2)+'\n')
print(len(entries),'reference keys')
