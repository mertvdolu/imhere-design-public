// Rebuild opaque sRGB PNG exports from editable SVGs. Requires sharp.
// Usage: node source/render.cjs. Set NODE_PATH if sharp is not installed locally.
const fs=require('fs'),path=require('path'),os=require('os');
const root=path.resolve(__dirname,'..');
const config=path.join(os.tmpdir(),'imhere-store-fonts-'+process.pid+'.conf');
fs.writeFileSync(config,`<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>${root}/assets</dir><cachedir>${os.tmpdir()}/imhere-store-font-cache</cachedir></fontconfig>`);
process.env.FONTCONFIG_FILE=config;
const sharp=require('sharp');
(async()=>{
 const d=JSON.parse(fs.readFileSync(path.join(root,'DELIVERY.json')));
 const evidence=[];
 for(const f of d.assets){
  const input=path.join(root,f.file.replace('.png','.svg')),output=path.join(root,f.file);
  await sharp(input,{limitInputPixels:false}).flatten({background:'#F4F1E9'}).removeAlpha().toColourspace('srgb').png({compressionLevel:9,palette:false}).toFile(output);
  const m=await sharp(output).metadata();
  if(m.width!==f.width||m.height!==f.height||m.hasAlpha||m.channels!==3)throw Error('Invalid export '+f.file);
  evidence.push({file:f.file,width:m.width,height:m.height,channels:m.channels,hasAlpha:m.hasAlpha,format:m.format,space:m.space,bytes:fs.statSync(output).size});
 }
 const preview=path.join(root,'review');fs.mkdirSync(preview,{recursive:true});
 for(const [folder,name,W,H]of [['app-store/iphone-6.9','app-store-contact-sheet',360,782],['google-play/phone','google-play-contact-sheet',360,640]]){
  const files=d.assets.filter(x=>x.file.startsWith(folder+'/'));const columns=3,gap=22,margin=32,titleH=82;
  const ww=columns*W+(columns-1)*gap+margin*2,hh=2*H+gap+margin*2+titleH;
  const images=[];
  for(let i=0;i<files.length;i++)images.push({input:await sharp(path.join(root,files[i].file)).resize(W,H).png().toBuffer(),left:margin+(i%columns)*(W+gap),top:margin+titleH+Math.floor(i/columns)*(H+gap)});
  const label=`<svg width="${ww}" height="${titleH}"><text x="32" y="40" fill="#191A17" font-family="Geist" font-size="24">IM HERE / Store artwork v1.0</text><text x="32" y="66" fill="#696A62" font-family="Geist" font-size="14">${folder} · Cream &amp; Ink v2.2 · Design renders</text></svg>`;
  images.push({input:Buffer.from(label),left:0,top:0});
  await sharp({create:{width:ww,height:hh,channels:3,background:'#E5E0D5'}}).composite(images).removeAlpha().png().toFile(path.join(preview,name+'.png'));
 }
 fs.writeFileSync(path.join(root,'evidence/export-validation.json'),JSON.stringify({exports:evidence,allOpaque:true,allRGB:true,count:evidence.length},null,2)+'\n');
 fs.unlinkSync(config);console.log('PASS: '+evidence.length+' opaque RGB PNGs; two contact sheets.');
})().catch(e=>{console.error(e);process.exit(1)});
