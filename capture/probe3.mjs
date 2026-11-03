import { chromium } from 'playwright';
const b=await chromium.launch({channel:'chrome',headless:true});
const c=await b.newContext({viewport:{width:1440,height:900}});
const p=await c.newPage();
await p.goto('http://localhost:8000/jobs',{waitUntil:'load'});await p.waitForTimeout(2500);
await p.screenshot({path:'frames/jp-jobs.png'});
console.log(await p.evaluate(()=>[...document.querySelectorAll('a')].slice(0,60).map(a=>a.innerText.trim().replace(/\n/g,' ').slice(0,40)+' -> '+a.getAttribute('href'))));
await b.close();
