/* Design-only preview. Sign out is simulated outside the screen; copying the public email is real. */
(() => {
  'use strict';
  const $=id=>document.getElementById(id), q=new URLSearchParams(location.search);
  const keys=['state','locale','scale','width','platform','position'];
  for(const k of keys)if([...$(k).options].some(o=>o.value===q.get(k)))$(k).value=q.get(k);
  $('contrast').checked=q.get('contrast')==='1';
  document.body.classList.toggle('export',q.get('export')==='1');
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  function render(){
    const state=$('state').value,locale=$('locale').value,c=window.ERT098_COPY[state][locale];
    const screen=$('screen');screen.lang=locale;screen.style.width=$('width').value+'px';
    screen.className='screen '+$('platform').value+($('scale').value==='200'?' large':'')+($('position').value==='full'?' full':'')+($('contrast').checked?' contrast':'');
    const body=esc(c.body).replace('info@useimhere.com','<span class="email">info@useimhere.com</span>');
    screen.innerHTML='<div class="reading" tabindex="0" role="region" aria-labelledby="account-heading"><h1 id="account-heading">'+esc(c.title)+'</h1><p id="account-body">'+body+'</p></div><div class="actions"><button type="button" class="tap primary" id="signout"><span class="paint">'+esc(c.primary)+'</span></button>'+(c.secondary?'<button type="button" class="tap secondary" id="copy"><span class="paint">'+esc(c.secondary)+'</span></button><p id="copied" class="notice" role="status" hidden><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 4 4L19 6"/></svg><span>'+esc(c.copied)+'</span></p>':'')+'</div>';
    $('signout').onclick=()=>{$('review-feedback').textContent='Önizleme: Çıkış yap eylemi seçildi. Gerçek oturum işlemi yapılmadı.';};
    if(c.secondary)$('copy').onclick=async()=>{
      $('copied').hidden=true;
      try{await navigator.clipboard.writeText('info@useimhere.com');$('copied').hidden=false;}
      catch{$('review-feedback').textContent='Önizlemede kopyalama tamamlanamadı; başarı geri bildirimi gösterilmedi. Gövdedeki adres seçilebilir.';}
    };
    $('review-feedback').textContent='';
    const params=new URLSearchParams(keys.map(k=>[k,$(k).value]));params.set('contrast',$('contrast').checked?'1':'0');if(q.get('export')==='1')params.set('export','1');
    history.replaceState(null,'','?'+params);
    if($('position').value==='end')document.fonts.ready.then(()=>{const reading=screen.querySelector('.reading');reading.scrollTop=reading.scrollHeight;});
  }
  for(const k of [...keys,'contrast'])$(k).onchange=render;
  render();
})();
