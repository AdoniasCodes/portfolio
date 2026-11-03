import { chromium } from 'playwright';
import fs from 'fs';
const OUT='/Users/eyoel/vibecoding/job/websites-portfolio/media';
const b=await chromium.launch({channel:'chrome',headless:true});
const dir='raw/amore';fs.rmSync(dir,{recursive:true,force:true});
const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true,recordVideo:{dir,size:{width:390,height:844}}});
const tc=Date.now();
const p=await c.newPage();
const w=ms=>p.waitForTimeout(ms);
const hide=()=>p.addStyleTag({content:'nextjs-portal,[data-nextjs-dev-tools-button]{display:none!important}'}).catch(()=>{});
const shot=async n=>{await hide();await p.screenshot({path:`${OUT}/${n}.png`})};
const nav=async n=>{await p.getByRole('link',{name:n,exact:true}).click();await w(2500);await hide()};
await p.goto('http://localhost:3111/',{waitUntil:'load'});await hide();await w(2500);
await p.getByText('Get in').click();await w(1000);
await p.getByText('Panda',{exact:true}).click();await w(4000);await hide();
const startSec=(Date.now()-tc)/1000;
await shot('amore-1');
await p.mouse.wheel(0,500);await w(1500);await p.mouse.wheel(0,-500);await w(800);
await nav('Discover');
await w(1500);
await p.getByText('Mood match').click();await w(1200);
for(const o of ['Curious','Together','Mind.blowing','Modern','Movie','Moderate']){
  await p.getByRole('button',{name:new RegExp(o)}).first().click({timeout:8000}).catch(async e=>{await p.screenshot({path:'frames/amore-fail.png'});throw e});await w(600);
}
await w(1800);
await shot('amore-2');
for(let i=0;i<4;i++){await p.touchscreen.tap(195,616);await w(700);}
let matched=false;
for(let i=0;i<4&&!matched;i++){
  await p.touchscreen.tap(322,616);await w(1100);
  matched=await p.getByText(/A MATCH/i).first().isVisible().catch(()=>false);
}
console.log('matched',matched);
await w(1200);
if(!matched){await p.getByText('Tap for details').first().click({force:true}).catch(()=>{});await w(2200);}
await shot('amore-3');
if(!matched){await p.touchscreen.tap(359,115);await w(900);}
if(matched){await p.screenshot({path:'frames/amore-matchstate.png'});}
await nav('Watchlist').catch(async()=>{await p.touchscreen.tap(195,780);await w(1000);await nav('Watchlist')});
await w(600);await p.getByRole('button',{name:/Saved/}).first().click().catch(e=>console.log('savedfail'));await w(1500);await shot('amore-4');
await nav('Us');await w(1500);await shot('amore-5');
await nav('Tonight');await w(1500);
fs.writeFileSync('raw/amore/start.txt',String(startSec));
const vp=await p.video().path();
await c.close();await b.close();
console.log('start',startSec);
fs.renameSync(vp,'raw/amore/raw.webm');
