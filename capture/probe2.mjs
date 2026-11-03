import { chromium } from 'playwright';
const b=await chromium.launch({channel:'chrome',headless:true});
const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
const p=await c.newPage();const w=ms=>p.waitForTimeout(ms);
await p.goto('http://localhost:3111/',{waitUntil:'load'});await w(2500);
await p.getByText('Get in').click();await w(1000);await p.getByText('Panda',{exact:true}).click();await w(3000);
await p.getByRole('link',{name:'Discover',exact:true}).click();await w(2000);
await p.getByText('Mood match').click();await w(1500);
for(let i=0;i<8;i++){
 const t=await p.innerText('body');console.log('---',i,t.replace(/\n+/g,' | ').slice(0,300));
 await p.screenshot({path:`frames/amore-m${i}.png`});
 const btns=await p.$$('button');
 let clicked=false;
 for(const bt of btns){const tx=(await bt.innerText()).trim();if(tx&&!/Browse|Mood match|back|skip|Tonight|Discover|Watchlist|^Us$|Profile/i.test(tx)&&await bt.isVisible()){await bt.click();clicked=true;break}}
 if(!clicked)break;await w(1500);
}
await b.close();
