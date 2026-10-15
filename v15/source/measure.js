(async()=>{
 await document.fonts.ready;
 await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
 const p=document.getElementById('phone'),r=p.getBoundingClientRect(),sc=p.querySelector('.scroll');
 const smallTargets=[],clippedText=[],verticalOverlaps=[],verticalTextOverflow=[],unreachableContent=[];
 const label=e=>(e.getAttribute('data-key')||e.getAttribute('aria-label')||e.className||e.tagName).toString().slice(0,100);
 const visible=e=>e.getBoundingClientRect().width>0&&e.getBoundingClientRect().height>0&&getComputedStyle(e).visibility!=='hidden'&&!e.closest('.sr-only,[aria-hidden=true]');
 for(const e of p.querySelectorAll('button,a,input,summary')){
  if(!e.getBoundingClientRect().width||getComputedStyle(e).visibility==='hidden')continue;
  const z=e.matches('input[type=radio],input[type=checkbox]')?e.closest('label'):e,b=z.getBoundingClientRect();
  if(b.width<47.9||b.height<47.9)smallTargets.push({tag:e.tagName,label:(e.getAttribute('aria-label')||z.innerText).slice(0,90),w:b.width,h:b.height});
 }
 const walker=document.createTreeWalker(p,4);
 while(walker.nextNode()){
  const n=walker.currentNode,e=n.parentElement;
  if(!n.textContent.trim()||!visible(e))continue;
  const range=document.createRange();range.selectNodeContents(n);
  const block=e.closest('p,h1,h2,label,legend,.face,a'),bb=block?.getBoundingClientRect(),tolerance=block?Math.max(1,parseFloat(getComputedStyle(block).fontSize)*.1):1;
  for(const b of range.getClientRects()){
   if(b.width&&(b.left<r.left-.8||b.right>r.right+.8))clippedText.push({text:n.textContent.slice(0,90),left:b.left-r.left,right:b.right-r.right});
   if(b.width&&bb&&(b.top<bb.top-tolerance||b.bottom>bb.bottom+tolerance))verticalTextOverflow.push({text:n.textContent.slice(0,90),container:label(block),above:Math.max(0,bb.top-b.top),below:Math.max(0,b.bottom-bb.bottom)});
  }
 }
 // Normal-flow sibling regions; map background, visually hidden legends and nested controls are excluded.
 for(const parent of p.querySelectorAll('.body-content,.actions,.options,.field,.notice')){
  const nodes=[...parent.children].filter(e=>visible(e)&&getComputedStyle(e).position!=='absolute');
  for(let i=0;i<nodes.length;i++)for(let j=i+1;j<nodes.length;j++){
   const a=nodes[i].getBoundingClientRect(),b=nodes[j].getBoundingClientRect();
   const dx=Math.min(a.right,b.right)-Math.max(a.left,b.left),dy=Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top);
   if(dx>1&&dy>1)verticalOverlaps.push({parent:label(parent),first:label(nodes[i]),second:label(nodes[j]),overlapY:dy,overlapX:dx});
  }
 }
 const top=sc.getBoundingClientRect().top;
 for(const e of p.querySelector('.body-content').children)if(visible(e)&&getComputedStyle(e).position!=='absolute'&&e.getBoundingClientRect().top+sc.scrollTop<top-.8)unreachableContent.push({element:label(e),aboveScrollStart:top-e.getBoundingClientRect().top-sc.scrollTop});
 return{measurementVersion:2,scene:new URLSearchParams(location.search).get('scene'),locale:p.lang,scale:p.classList.contains('large')?200:100,width:r.width,height:r.height,platform:p.classList.contains('android')?'android':'ios',position:p.classList.contains('full')?'full':'top',horizontalOverflow:Math.max(0,p.scrollWidth-p.clientWidth,sc.scrollWidth-sc.clientWidth),smallTargets,clippedText,verticalOverlaps,verticalTextOverflow,unreachableContent,h1:p.querySelectorAll('h1').length,fonts:document.fonts.status,contentHeight:sc.scrollHeight,visibleHeight:sc.clientHeight,fullNeeded:sc.scrollHeight>sc.clientHeight+1,keys:[...new Set([...p.querySelectorAll('[data-key]')].map(x=>x.dataset.key))]};
})()
