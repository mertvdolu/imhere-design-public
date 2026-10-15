// Called only through CUA's documented tab/CDP API; no separate browser driver.
import fs from 'node:fs/promises';
export async function capture(tab,cdp,base,group,ids){
 const ms=await fs.readFile(base+'/source/measure.js','utf8'),results=[];
 const measure=async()=>{const x=await cdp.send('Runtime.evaluate',{expression:ms,awaitPromise:true,returnByValue:true});if(x.exceptionDetails)throw Error(JSON.stringify(x.exceptionDetails));return x.result.value};
 const save=async(path,width,height)=>{let data;try{data=await cdp.send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,fromSurface:true,clip:{x:0,y:0,width,height,scale:1}})}catch(e){await measure();data=await cdp.send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,fromSurface:true,clip:{x:0,y:0,width,height,scale:1}})}await fs.writeFile(path,Buffer.from(data.data,'base64'))};
 for(const id of ids){let cur=[];
  for(const width of [390,412])for(const locale of ['en','tr'])for(const scale of [100,200]){
   const height=width===412?915:844,stem=id+'--'+locale+'--'+scale+(width===412?'--412':'');
   await cdp.send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:4,mobile:false});
   await tab.goto('http://127.0.0.1:8823/ONIZLEME.html?'+new URLSearchParams({scene:id,width,locale,scale,export:'1',position:'top'}));
   const m=await measure();cur.push(m);await save(base+'/'+group+'/screens/png/'+stem+'.png',width,height);
   if(m.fullNeeded){await tab.goto('http://127.0.0.1:8823/ONIZLEME.html?'+new URLSearchParams({scene:id,width,locale,scale,export:'1',position:'full'}));const fm=await measure();cur.push(fm);await save(base+'/'+group+'/screens/png/'+stem+'--full.png',width,Math.ceil(fm.height));}
  }
  for(const platform of ['ios','android'])for(const locale of ['en','tr']){
   await cdp.send('Emulation.setDeviceMetricsOverride',{width:320,height:844,deviceScaleFactor:1,mobile:false});
   await tab.goto('http://127.0.0.1:8823/ONIZLEME.html?'+new URLSearchParams({scene:id,width:320,locale,scale:200,export:'1',platform}));
   cur.push(await measure());await save(base+'/'+group+'/evidence/'+id+'--'+locale+'--200--320--'+platform+'.png',320,844);
  }
  await fs.writeFile(base+'/'+group+'/evidence/'+id+'.json',JSON.stringify(cur,null,2));results.push(...cur);
 }
 return{group,states:ids.length,checks:results.length,issues:results.filter(m=>m.horizontalOverflow||m.smallTargets.length||m.clippedText.length||m.h1!==1)};
}
