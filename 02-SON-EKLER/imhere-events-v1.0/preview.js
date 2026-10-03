/* Local design simulation. No backend, permissions, storage, calendar writes or map launches. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const states = window.EVENT_CATALOG.states;
  const q = new URLSearchParams(location.search);
  const settings = { locale:q.get('locale')||'en', platform:q.get('platform')||'ios', width:q.get('width')||'390', scale:q.get('scale')||'100' };
  let current = {...(states.find(s=>s.id===q.get('scene'))||states.find(s=>s.id==='list-populated'))};
  let announcement = '';
  const paths = {
    back:'m14 6-6 6 6 6', calendar:'M5 5h14v15H5zM8 3v4M16 3v4M5 10h14', arrow:'m8 5 7 7-7 7', check:'m5 12 4 4L19 6', clock:'M12 7v5l3 2M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0', pin:'M19 10c0 5-7 11-7 11S5 15 5 10a7 7 0 1 1 14 0ZM14 10a2 2 0 1 1-4 0 2 2 0 0 1 4 0', map:'m3 5 6-2 6 2 6-2v16l-6 2-6-2-6 2ZM9 3v16M15 5v16', info:'M12 11v6M12 7h.01M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0', lock:'M6 10h12v10H6zM8 10V7a4 4 0 0 1 8 0v3', cancel:'M6 6l12 12M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0', star:'m12 3 3 6 6 1-4.5 4.5 1 6.5L12 18l-5.5 3 1-6.5L3 10l6-1Z', image:'M3 4h18v16H3zM3 16l6-6 5 5 3-3 4 4M17 8h.01', profile:'M20 21v-2a7 7 0 0 0-14 0v2M16 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0', messages:'M4 4h16v12H9l-5 4z', nearby:'M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0', networking:'M9 7a4 4 0 1 1 0 8 4 4 0 0 1 0-8ZM15 7a4 4 0 1 1 0 8', social:'M4 6h12v10a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4ZM16 8h2a3 3 0 0 1 0 6h-2', activity:'m4 17 5-8 4 5 3-9 4 12', loading:'M12 3a9 9 0 1 1-9 9', offline:'m3 3 18 18M5 9a12 12 0 0 1 14-1M8 13a6 6 0 0 1 7-1M11 17h2'
  };
  const esc = s => String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const t=(key,args={})=>{let v=window.EVENT_COPY[settings.locale][key];if(v===undefined)throw new Error('Missing copy: '+key);for(const [k,val] of Object.entries(args))v=v.replaceAll('{'+k+'}',val);return esc(v);};
  const ico=(name,cls='')=>`<svg class="${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="${paths[name]||paths.info}"/></svg>`;
  const rsKey=state=>state==='NONE'?'eventV1None':state==='INTERESTED'?'eventV1Interested':'eventV1Going';
  const choiceText=state=>window.EVENT_COPY[settings.locale][rsKey(state)];
  const button=(key,action,{primary=false,disabled=false,icon=''}={})=>`<button class="tap ${primary?'primary':''}" data-action="${action}" ${disabled?'disabled':''}><span class="paint">${icon?ico(icon):''}<span>${t(key)}</span></span></button>`;
  const note=(title,body,icon='info')=>`<div class="notice">${ico(icon)}<div>${title?`<p class="notice-title">${t(title)}</p>`:''}<p>${t(body)}</p></div></div>`;
  const category=cat=>`<div class="category" aria-label="${t('eventV1CategoryLabel',{category:window.EVENT_COPY[settings.locale]['eventV1Category'+cat[0]+cat.slice(1).toLowerCase()]})}">${ico(cat.toLowerCase())}<span>${t('eventV1Category'+cat[0]+cat.slice(1).toLowerCase())}</span></div>`;
  const data={
    NETWORKING:{title:['An evening of ideas','Fikirlerle bir akşam'],venue:['Example Studio','Örnek Stüdyo'],description:['A relaxed evening to exchange ideas about design and independent work. Come with a question, a project, or simply a little curiosity.','Tasarım ve bağımsız çalışma üzerine fikir paylaşmak için sakin bir akşam. Bir soru, bir proje veya yalnızca biraz merakla gelebilirsin.'],date:['Sat, 24 Oct 2026','24 Eki 2026, Cmt'],time:'18:00–20:00'},
    SOCIAL:{title:['Coffee & conversation','Kahve ve sohbet'],venue:['Example Café','Örnek Kafe'],description:['An unhurried afternoon for a coffee and a conversation.','Bir kahve ve sohbet için telaşsız bir öğleden sonra.'],date:['Sun, 25 Oct 2026','25 Eki 2026, Paz'],time:'14:00–16:00'},
    ACTIVITY:{title:['A creative afternoon','Yaratıcı bir öğleden sonra'],venue:['Example Workshop','Örnek Atölye'],description:['A simple creative session. Explore an idea and enjoy making something with your hands.','Sade bir yaratıcı çalışma. Bir fikri keşfet, kendi ellerinle bir şeyler yapmanın keyfini çıkar.'],date:['Sun, 25 Oct 2026','25 Eki 2026, Paz'],time:'16:00–18:00'}
  };
  const fixture=cat=>{const x=data[cat],i=settings.locale==='en'?0:1;return {title:x.title[i],venue:x.venue[i],description:x.description[i],date:x.date[i],time:x.time,address:i===0?'Sample Street, London':'Örnek Sokak, Londra'};};
  const art=(cat,cls='hero',failed=false)=>failed?`<div class="${cls} image-fallback" role="img" aria-label="${t('eventV1ImageUnavailable')}">${ico('image')}</div>`:`<img class="${cls}" src="assets/event-art-${cat.toLowerCase()}.svg" alt="">`;
  function card(cat,rsvp='NONE',status='ready',failed=false){
    const e=fixture(cat);let footer='';
    if(status==='cancelled')footer=`${ico('cancel')}<span class="status-label cancelled">${t('eventV1Cancelled')}</span>`;
    else if(status==='started')footer=`${ico('lock')}<span>${t('eventV1Started')}</span>${rsvp!=='NONE'?`<span>· ${t('eventV1ListChoice',{choice:choiceText(rsvp)})}</span>`:''}`;
    else if(rsvp!=='NONE')footer=`${ico('check')}<span>${t('eventV1ListChoice',{choice:choiceText(rsvp)})}</span>`;
    return `<button class="event-card ${status==='cancelled'?'cancelled':''}" data-event="${cat}" data-rsvp="${rsvp}" data-status="${status}"><span class="card-main">${art(cat,'card-image',failed)}<span>${category(cat)}<span class="card-title">${esc(e.title)}</span><span class="card-meta">${esc(e.date)}<br>${esc(e.time)} · Europe/London</span><span class="card-meta">${esc(e.venue)}</span></span></span>${footer?`<span class="card-foot">${footer}</span>`:''}</button>`;
  }
  function blank(mode,list){
    const loading=mode==='loading';if(loading)return `<div role="status" class="loading-status">${ico('loading','spinner')}<span>${t(list?'eventsV1Loading':'eventV1Loading')}</span></div><div aria-hidden="true" class="skeleton"></div><div aria-hidden="true" class="skeleton"></div>`;
    const map={empty:['eventsV1EmptyTitle','eventsV1EmptyBody','calendar'],error:['eventsV1ErrorTitle','eventsV1ErrorBody','info'],offline:['eventsV1OfflineTitle','eventsV1OfflineBody','offline'],'not-found':['eventV1UnavailableTitle','eventV1UnavailableBody','calendar']};
    const [a,b,icon]=map[mode];return `<div class="empty-state"><div class="empty-art">${ico(icon)}</div><h2>${t(a)}</h2><p>${t(b)}</p>${mode==='error'||mode==='offline'?button('retry','retry',{icon:'arrow'}):mode==='not-found'?button('eventV1Back','back'):''}</div>`;
  }
  function list(){
    const mode=current.mode;let body='';
    if(['loading','empty','error','offline'].includes(mode))body=blank(mode,true);
    else body=`<div class="event-list">${card('NETWORKING',mode==='populated'?'INTERESTED':'GOING',mode==='cancelled'?'cancelled':mode==='started'?'started':'ready',mode==='image-failed')}${card('SOCIAL','NONE')}${mode==='populated'?card('ACTIVITY','GOING'):''}</div>`;
    return `<h1 class="screen-title">${t('navEvents')}</h1><p class="lede">${t('eventsV1Intro')}</p>${body}`;
  }
  function detail(){
    if(['loading','error','offline','not-found'].includes(current.mode))return blank(current.mode,false);
    const {mode,myRsvp,category:cat}=current;const e=fixture(cat);
    const cancelled=mode==='cancelled',locked=mode==='locked',busy=mode==='updating';
    const disabled=cancelled||locked||busy;
    const banner=cancelled?note('eventV1Cancelled','eventV1CancelledBody','cancel'):locked?note('eventV1Started','eventV1LockedBody','lock'):mode==='changed'?note('eventV1ChangedTitle','eventV1ChangedBody'):'';
    let title=e.title,description=e.description;
    if(mode==='long-content'){
      title=settings.locale==='en'?'An evening of ideas about creative work, thoughtful design and everyday connection':'Yaratıcı çalışma, düşünceli tasarım ve günlük hayattaki bağlantılar üzerine bir akşam';
      description=Array(7).fill(e.description).join('\n\n');
    }
    let rsvp=`<p class="status-label">${t(cancelled&&myRsvp!=='NONE'?'eventV1CancelledChoice':'eventV1ListChoice',{choice:choiceText(myRsvp)})}</p>`;
    rsvp+=`<div class="rsvp-controls" role="group" aria-busy="${busy}" aria-label="${t('eventV1YourChoice')}">${['INTERESTED','GOING'].map(rs=>{const selected=!cancelled&&myRsvp===rs;return `<button class="tap ${selected?'selected':''}" data-select="${rs}" aria-pressed="${selected}" ${disabled?'disabled':''}><span class="paint">${ico(selected?'check':rs==='INTERESTED'?'star':'calendar')}<span>${t(rsKey(rs))}</span></span></button>`;}).join('')}</div>`;
    if(myRsvp!=='NONE')rsvp+=`<button class="quiet" data-select="NONE" ${disabled?'disabled':''}>${t('eventV1Withdraw')}</button>`;
    if(busy)rsvp+=`<p class="inline-status" role="status">${ico('loading','spinner')}${t('eventV1Saving')}</p>`;
    if(mode==='save-failed')rsvp+=`<p class="inline-status error" role="alert">${t('eventV1SaveFailed')}</p>${button('retry','retry-rsvp')}`;
    if(mode==='changed'&&myRsvp!=='NONE')rsvp+=`<p class="helper">${t('eventV1ChoiceKept')}</p>`;
    let actionStatus='';
    for(const a of ['calendar','map'])if(mode.startsWith(a+'-'))actionStatus=`<p class="inline-status ${mode.endsWith('failed')?'error':''}" role="${mode.endsWith('failed')?'alert':'status'}">${mode.endsWith('opening')?ico('loading','spinner'):''}${t('eventV1'+(a==='map'?'Map':'Calendar')+(mode.endsWith('failed')?'Failed':'Opening'))}</p>`;
    const times=e.time.split('–');
    return `${banner}${art(cat,'hero',mode==='image-failed')}${category(cat)}<h1 class="detail-title">${esc(title)}</h1><dl class="facts"><div class="fact">${ico('calendar')}<div><dt>${t('eventV1Start')}</dt><dd>${esc(e.date)} · ${times[0]}</dd></div></div><div class="fact">${ico('clock')}<div><dt>${t('eventV1End')}</dt><dd>${esc(e.date)} · ${times[1]}</dd><div class="zone">${t('eventV1TimeZone',{zone:'Europe/London'})}</div></div></div><div class="fact">${ico('pin')}<div><dt>${t('eventV1Venue')}</dt><dd>${esc(e.venue)}<br>${esc(e.address)}</dd></div></div></dl><section class="section"><h2 class="section-title">${t('eventV1YourChoice')}</h2>${rsvp}<p class="helper">${t('eventV1ChoiceHelp')}</p></section><section class="section"><h2 class="section-title">${t('eventV1Plan')}</h2><div class="action-list">${button('eventV1Calendar','calendar',{icon:'calendar',disabled:cancelled||mode==='calendar-opening'})}${button('eventV1Map','map',{icon:'map',disabled:cancelled||mode==='map-opening'})}</div>${actionStatus}<p class="helper">${t('eventV1CalendarHelp')}</p></section><section class="section"><h2 class="section-title">${t('eventV1About')}</h2><p class="description">${esc(description)}</p></section>`;
  }
  function nav(){return `<div class="navslot"><nav class="nav" aria-label="${settings.locale==='en'?'Main navigation':'Ana gezinme'}">${['Profile','Messages','Nearby','Events'].map((s,i)=>`<button class="${i===3?'active':''}" ${i===3?'aria-current="page"':''} data-tab="${s}">${ico(i===3?'calendar':s.toLowerCase())}<span>${t('nav'+s)}</span></button>`).join('')}</nav></div>`;}
  function render(reset=true){
    const scroll=$('phone').querySelector('.scroll')?.scrollTop||0;
    $('phone').className=`phone ${settings.platform} ${settings.scale==='200'?'large':''} ${$('contrast').checked?'contrast':''} ${$('solid').checked?'solid':''} ${$('motion').checked?'reduce-motion':''}`;
    $('phone').style.width=settings.width+'px';$('phone').lang=settings.locale;
    const isList=current.screen==='list';
    $('phone').innerHTML=`<div class="statusbar" aria-hidden="true"><span>9:41</span><span>▰ ▰</span></div><div class="appbar">${isList?'<img class="mark" src="../imhere-cream-complete-v2.2/assets/imhere-mark.svg" alt="IM HERE">':`<button class="icon" data-action="back" aria-label="${t('eventV1Back')}"><span class="face">${ico('back')}</span></button><span class="bar-title">${t('navEvents')}</span>`}</div><div class="scroll" tabindex="0" aria-label="${t('navEvents')}">${isList?list():detail()}</div>${nav()}<div class="home-indicator" aria-hidden="true"></div><span class="sr-only" role="status">${esc(announcement)}</span>`;
    if(!reset)$('phone').querySelector('.scroll').scrollTop=scroll;
    $('scenario-note').textContent=current.id+' · '+current.label+' · Son doğrulanmış tercih: '+current.myRsvp+'. Bu görünüm ürün verisi değildir.';
    const params=new URLSearchParams({...settings,scene:current.id,contrast:$('contrast').checked?'1':'0',solid:$('solid').checked?'1':'0',motion:$('motion').checked?'1':'0'});history.replaceState(null,'','?'+params);
    $('phone').querySelectorAll('[data-event]').forEach(el=>el.onclick=()=>{const mode=el.dataset.status==='started'?'locked':el.dataset.status;current={...states.find(s=>s.id==='detail-'+(mode==='ready'?el.dataset.rsvp.toLowerCase():mode+'-'+el.dataset.rsvp.toLowerCase())),category:el.dataset.event};$('scene').value=current.id;render();});
    $('phone').querySelectorAll('[data-select]').forEach(el=>el.onclick=()=>{if(el.dataset.select===current.myRsvp)return;current={...current,id:el.dataset.select==='NONE'?'detail-withdrawing':'detail-updating-'+el.dataset.select.toLowerCase(),mode:'updating',pending:el.dataset.select};render(false);$('preview-feedback').textContent='Örnek istek bekliyor. Sonuç için önizlemenin yanıt düğmelerini kullan.';});
    $('phone').querySelectorAll('[data-action]').forEach(el=>el.onclick=()=>act(el.dataset.action));
    $('phone').querySelectorAll('[data-tab]').forEach(el=>el.onclick=()=>{if(el.dataset.tab==='Events')setScene('list-populated');else $('preview-feedback').textContent='Diğer ana sekmeler mevcut uygulama akışını kullanır; bu pakette yeniden tasarlanmıyor.';});
  }
  function act(a){
    if(a==='back')return setScene('list-populated');
    if(a==='retry'){current={...current,mode:'loading'};render();$('preview-feedback').textContent='Yeniden yükleme örneği: yanıtı dış kontrolle seç.';return;}
    if(a==='retry-rsvp'){current={...current,mode:'updating'};return render(false);}
    current={...current,mode:a+'-opening'};render(false);$('preview-feedback').textContent='Sistem '+(a==='calendar'?'takvim':'harita')+' açılışı tasarımda örnekleniyor; gerçek uygulama açılmadı. Dönüş için başarılı/hata yanıtını seç.';
  }
  function setScene(id){current={...states.find(s=>s.id===id)};announcement='';$('preview-feedback').textContent='';$('scene').value=id;render();}
  $('scene').innerHTML=states.map(s=>`<option value="${s.id}">${esc(s.label)}</option>`).join('');$('scene').value=current.id;$('scene').onchange=()=>setScene($('scene').value);
  for(const k of ['locale','platform','width','scale']){if([...$(k).options].some(o=>o.value===settings[k]))$(k).value=settings[k];else settings[k]=$(k).value;$(k).onchange=()=>{settings[k]=$(k).value;render();};}
  for(const k of ['contrast','solid','motion']){$(k).checked=q.get(k)==='1';$(k).onchange=()=>render(false);}
  $('ack').onclick=()=>{
    if(current.mode==='updating'){
      current={...current,myRsvp:current.pending,mode:'ready'};
      announcement=current.myRsvp==='NONE'?window.EVENT_COPY[settings.locale].eventV1WithdrawnAnnouncement:window.EVENT_COPY[settings.locale].eventV1SavedAnnouncement.replace('{choice}',choiceText(current.myRsvp));
      current.id='detail-'+current.myRsvp.toLowerCase();$('scene').value=current.id;render(false);
    }else if(current.mode==='loading')setScene(current.screen==='list'?'list-populated':'detail-none');
    else if(current.mode.endsWith('-opening')){current={...current,mode:'ready'};render(false);}
    $('preview-feedback').textContent='Örnek yanıt gösterildi. Bu bir gerçek işlem veya takvime kaydetme onayı değildir.';
  };
  $('reject').onclick=()=>{if(current.mode==='updating')current={...current,mode:'save-failed'};else if(current.mode.endsWith('-opening'))current={...current,mode:current.mode.replace('opening','failed')};else current={...current,mode:'error'};render(false);};
  $('lock').onclick=()=>{if(current.screen==='detail'){current={...current,id:'detail-locked-'+current.myRsvp.toLowerCase(),mode:'locked'};$('scene').value=current.id;render(false);}else setScene('list-started');};
  render();
})();
