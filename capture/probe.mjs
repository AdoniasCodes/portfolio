import { chromium } from 'playwright';
const b=await chromium.launch({channel:'chrome',headless:true});
const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
const p=await c.newPage();
await p.goto('http://localhost:3111/',{waitUntil:'load'});await p.waitForTimeout(3000);
await p.getByText('Get in').click();await p.waitForTimeout(2500);
await p.screenshot({path:'frames/amore-probe.png'});
console.log(await p.evaluate(()=>[...document.querySelectorAll('nav a,nav button,[role=tab]')].map(e=>e.innerText.replace(/\n/g,' ')+'|'+(e.getAttribute('href')||''))));
await b.close();
