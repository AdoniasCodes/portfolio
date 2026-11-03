import { chromium } from 'playwright';
import fs from 'fs';
const OUT='/Users/eyoel/vibecoding/job/websites-portfolio/media';
const sites={
 hermella:['https://adoniascodes.github.io/hermella/',1],
 adoniascodes:['https://adoniascodes.github.io/',1],
 inteltech:['https://inteltech.et/',1],
 nucleus:['https://nucleusinternationalschoolsystem.com/',0],
 agc:['https://advancedgeneralcontractor.com/',0],
 mekaneselam:['https://mekaneselamss.com/',0],
 cribcrm:['https://cribcrm.com/',0],
 intelmotion:['https://intelmotionlifts.com/',0],
 ethiolifecare:['https://ethiolifecare.com/',0],
};
const only=process.argv.slice(2);
const browser=await chromium.launch({channel:'chrome',headless:false,args:['--use-angle=metal','--enable-gpu','--ignore-gpu-blocklist','--enable-unsafe-swiftshader','--window-position=0,0']});
for(const [slug,[url,is3d]] of Object.entries(sites)){
 if(only.length&&!only.includes(slug))continue;
 const dir=`/Users/eyoel/vibecoding/job/websites-portfolio/capture/raw/${slug}`;
 fs.rmSync(dir,{recursive:true,force:true});
 const ctx=await browser.newContext({viewport:{width:1440,height:900},recordVideo:{dir,size:{width:1440,height:900}}});
 const page=await ctx.newPage();
 const t0=Date.now();
 try{await page.goto(url,{waitUntil:'load',timeout:45000});}catch(e){console.log(slug,'goto',e.message)}
 await page.waitForTimeout(4000);
 // cookie banners
 for(const sel of ['button:has-text("Accept all")','button:has-text("Accept")','button:has-text("Got it")','button:has-text("I agree")','button:has-text("Allow all")']){
  try{const b=page.locator(sel).first(); if(await b.isVisible({timeout:200})){await b.click({timeout:1000});break}}catch{}
 }
 await page.waitForTimeout(500);
 await page.screenshot({path:`${OUT}/${slug}-top.png`});
 const startMs=Date.now()-t0-600; // approx start of meaningful content
 await page.mouse.move(700,400);
 const H=await page.evaluate(()=>document.documentElement.scrollHeight-innerHeight);
 const total=is3d?13000:11000, steps=total/40;
 const target=Math.min(H, is3d?H:H);
 const ease=t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
 const s=Date.now();
 for(let i=1;i<=steps;i++){
  const p=ease(i/steps);
  await page.mouse.move(700+Math.sin(i/6)*160,400+Math.cos(i/8)*90);
  await page.evaluate(y=>window.scrollTo(0,y),target*p);
  await page.waitForTimeout(40);
 }
 await page.waitForTimeout(500);
 console.log(slug,'H',H,'startMs',startMs);
 const vp=await page.video().path();
 await ctx.close();
 fs.writeFileSync(`${dir}/start.txt`,String(Math.max(0,startMs)/1000));
 fs.renameSync(vp,`${dir}/raw.webm`);
}
await browser.close();
