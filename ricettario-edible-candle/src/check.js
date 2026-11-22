// flags any page whose live content runs into the folio zone
const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.resolve(__dirname,'../build/edible-candle-cookbook.html'));await p.evaluate(()=>document.fonts.ready);
const r=await p.$$eval('.page',ps=>ps.map((pg,i)=>{const live=pg.querySelector('.live');const lb=live.getBoundingClientRect();let max=0;
live.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();if(r.height)max=Math.max(max,r.bottom)});return [i+1,Math.round(lb.bottom-max)]}));
console.log(r.map(x=>x.join(':')).join(' '));await b.close();})();
