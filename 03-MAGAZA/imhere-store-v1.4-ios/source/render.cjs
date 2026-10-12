// Render native screenshot compositions and contact sheets, without browser capture.
// Requirements: Node.js + sharp. Fonts and source imagery are included in this package.
const fs=require('fs'),path=require('path'),os=require('os');
const root=path.resolve(__dirname,'..');
const config=path.join(os.tmpdir(),`imhere-store14-fonts-${process.pid}.conf`);
fs.writeFileSync(config,`<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>${root}/assets</dir><cachedir>${os.tmpdir()}/imhere-store14-font-cache</cachedir></fontconfig>`);
process.env.FONTCONFIG_FILE=config;
const sharp=require('sharp');
const escape=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
async function main(){
  const delivery=JSON.parse(fs.readFileSync(path.join(root,'DELIVERY.json')));
  const copy=JSON.parse(fs.readFileSync(path.join(root,'source/copy.en-GB.json')));
  const evidence=[];
  for(const item of delivery.assets){
    const dest=path.join(root,item.file); fs.mkdirSync(path.dirname(dest),{recursive:true});
    await sharp(path.join(root,item.sourceSvg),{limitInputPixels:false}).flatten({background:'#F4F1E9'}).removeAlpha().toColourspace('srgb').png({compressionLevel:9,palette:false}).toFile(dest);
    const m=await sharp(dest).metadata();
    if(m.width!==item.width||m.height!==item.height||m.channels!==3||m.hasAlpha||m.format!=='png') throw Error('Invalid export '+item.file);
    evidence.push({file:item.file,width:m.width,height:m.height,channels:m.channels,hasAlpha:m.hasAlpha,space:m.space,format:m.format,bytes:fs.statSync(dest).size});
  }
  // Editorial review sheet carries draft status outside the six store-upload PNGs.
  const review=path.join(root,'review');fs.mkdirSync(review,{recursive:true});
  for(const folder of ['iphone-6.9','iphone-6.5','iphone-dynamic-island-medium']){
    const shots=delivery.assets.filter(x=>x.file.startsWith('app-store/'+folder+'/'));
    const W=352,H=Math.round(W*shots[0].height/shots[0].width),gap=26,margin=34,top=118;
    const ww=margin*2+W*3+gap*2,hh=top+2*H+gap+margin;
    const layers=[];
    for(let i=0;i<shots.length;i++) layers.push({input:await sharp(path.join(root,shots[i].file)).resize(W,H).png().toBuffer(),left:margin+(i%3)*(W+gap),top:top+Math.floor(i/3)*(H+gap)});
    layers.push({input:Buffer.from(`<svg width="${ww}" height="${top}"><text x="34" y="42" font-family="Geist" font-size="28" font-weight="500" fill="#191A17">IM HERE · App Store 1.4.0 (19)</text><text x="34" y="74" font-family="Geist" font-size="17" fill="#696A62">Cream &amp; Ink v2.3 · ${folder} · 6 native iPhone scenes</text><text x="34" y="99" font-family="Geist" font-size="14" fill="#696A62">COPY DRAFT — HARBOR + FOUNDER APPROVAL REQUIRED</text></svg>`),left:0,top:0});
    await sharp({create:{width:ww,height:hh,channels:3,background:'#E8E4DA'}}).composite(layers).removeAlpha().png().toFile(path.join(review,folder+'-contact-sheet.png'));
  }
  fs.mkdirSync(path.join(root,'evidence'),{recursive:true});
  fs.writeFileSync(path.join(root,'evidence/export-validation.json'),JSON.stringify({count:evidence.length,allOpaque:evidence.every(x=>!x.hasAlpha),allRGB:evidence.every(x=>x.channels===3),exports:evidence},null,2)+'\n');
  console.log('PASS: '+evidence.length+' opaque RGB PNGs; 3 review contact sheets.');
}
main().catch(e=>{console.error(e);process.exitCode=1}).finally(()=>{fs.rmSync(config,{force:true})});
