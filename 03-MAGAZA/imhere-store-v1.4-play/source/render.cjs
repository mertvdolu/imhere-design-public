// Rasterise the editable artwork; never repaint native pixels or reflow app UI.
const fs=require('fs'),path=require('path'),os=require('os');
const root=path.resolve(__dirname,'..');
const config=path.join(os.tmpdir(),`imhere-play14-fonts-${process.pid}.conf`);
fs.writeFileSync(config,`<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>${root}/assets</dir><cachedir>${os.tmpdir()}/imhere-play14-font-cache</cachedir></fontconfig>`);
process.env.FONTCONFIG_FILE=config;
const sharp=require('sharp');
async function main(){
  const delivery=JSON.parse(fs.readFileSync(path.join(root,'DELIVERY.json')));
  const evidence=[];
  for(const a of delivery.assets){
    const dest=path.join(root,a.file);
    await sharp(path.join(root,a.sourceSvg),{limitInputPixels:false}).flatten({background:'#F4F1E9'}).removeAlpha().toColourspace('srgb').png({compressionLevel:9,palette:false}).toFile(dest);
    const m=await sharp(dest).metadata();
    if(m.width!==a.width||m.height!==a.height||m.channels!==3||m.hasAlpha)throw Error('Bad export: '+a.file);
    evidence.push({file:a.file,width:m.width,height:m.height,format:m.format,channels:m.channels,hasAlpha:m.hasAlpha,space:m.space});
  }
  const layers=[],w=324,h=576,margin=36,gap=24,top=110;
  const width=margin*2+w*3+gap*2,height=1744;
  for(let i=0;i<6;i++) layers.push({input:await sharp(path.join(root,delivery.assets[i].file)).resize(w,h).png().toBuffer(),left:margin+(i%3)*(w+gap),top:top+Math.floor(i/3)*(h+gap)});
  layers.push({input:await sharp(path.join(root,'google-play/feature-graphic.png')).resize(768,375).png().toBuffer(),left:162,top:1310});
  layers.push({input:Buffer.from(`<svg width="${width}" height="100"><text x="36" y="40" font-family="Geist" font-size="28" font-weight="500" fill="#191A17">IM HERE · Google Play 1.4.0 (19)</text><text x="36" y="69" font-family="Geist" font-size="17" fill="#696A62">Cream &amp; Ink v2.3 · 6 Android screens + feature graphic</text><text x="36" y="92" font-family="Geist" font-size="14" fill="#696A62">DRAFT — HARBOR + FOUNDER PLAY COPY APPROVAL REQUIRED</text></svg>`),left:0,top:0});
  await sharp({create:{width,height,channels:3,background:'#E8E4DA'}}).composite(layers).removeAlpha().png().toFile(path.join(root,'review/contact-sheet.png'));
  fs.writeFileSync(path.join(root,'evidence/export-validation.json'),JSON.stringify({result:'PASS',count:7,allRGB:true,allOpaque:true,exports:evidence},null,2)+'\n');
  console.log('PASS: 7 opaque RGB PNGs + review contact sheet.');
}
main().catch(e=>{console.error(e);process.exitCode=1}).finally(()=>fs.rmSync(config,{force:true}));
