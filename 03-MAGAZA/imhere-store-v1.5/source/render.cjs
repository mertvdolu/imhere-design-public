// Same 1.4 SVG/sharp/Geist route. Native pixels are never repainted.
const fs=require('fs'),path=require('path'),os=require('os');
const root=path.resolve(__dirname,'..'),config=path.join(os.tmpdir(),`imhere-store15-${process.pid}.conf`);
fs.writeFileSync(config,`<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>${root}/assets</dir><cachedir>${os.tmpdir()}/imhere-store15-font-cache</cachedir></fontconfig>`);
process.env.FONTCONFIG_FILE=config;
const sharp=require('sharp');
async function main(){
  const delivery=JSON.parse(fs.readFileSync(path.join(root,'DELIVERY.json'))),evidence=[];
  for(const a of delivery.assets){
    const dest=path.join(root,a.file);fs.mkdirSync(path.dirname(dest),{recursive:true});
    await sharp(path.join(root,a.sourceSvg),{limitInputPixels:false}).flatten({background:'#F4F1E9'}).removeAlpha().toColourspace('srgb').png({compressionLevel:9,palette:false}).toFile(dest);
    const m=await sharp(dest).metadata();
    if(m.width!==a.width||m.height!==a.height||m.channels!==3||m.hasAlpha)throw Error('Bad export '+a.file);
    evidence.push({file:a.file,width:m.width,height:m.height,channels:m.channels,hasAlpha:m.hasAlpha});
  }
  for(const folder of ['ios-15-1206x2622','ios-15-1320x2868','play-15-phone']){
    const assets=delivery.assets.filter(x=>x.file.startsWith(folder+'/'));
    const W=352,H=Math.round(W*assets[0].height/assets[0].width),gap=26,margin=34,top=100;
    const width=margin*2+W*3+gap*2,height=top+H*2+gap+margin,layers=[];
    for(let i=0;i<assets.length;i++)layers.push({input:await sharp(path.join(root,assets[i].file)).resize(W,H).png().toBuffer(),left:margin+(i%3)*(W+gap),top:top+Math.floor(i/3)*(H+gap)});
    layers.push({input:Buffer.from(`<svg width="${width}" height="100"><text x="34" y="40" font-family="Geist" font-size="28" font-weight="500" fill="#191A17">IM HERE · Store 1.5</text><text x="34" y="72" font-family="Geist" font-size="18" fill="#696A62">${folder} · 6 unchanged native screens · Founder-supplied copy</text></svg>`),left:0,top:0});
    await sharp({create:{width,height,channels:3,background:'#E8E4DA'}}).composite(layers).removeAlpha().png().toFile(path.join(root,'review',folder+'-contact-sheet.png'));
  }
  fs.writeFileSync(path.join(root,'evidence/export-validation.json'),JSON.stringify({status:'PASS',count:18,allRGB:true,allOpaque:true,exports:evidence},null,2)+'\n');
  console.log('PASS: 18 opaque RGB PNGs + 3 contact sheets. Existing feature graphic untouched.');
}
main().catch(e=>{console.error(e);process.exitCode=1}).finally(()=>fs.rmSync(config,{force:true}));
