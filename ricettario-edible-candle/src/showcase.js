// Builds the Fiverr portfolio images (1280x769 @2x) from the rendered page PNGs.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const root = path.resolve(__dirname, '..');
const P = (n) => 'file://' + path.join(root, 'build', 'pages', `p${String(n).padStart(2, '0')}.png`);
const fonts = 'file://' + path.resolve(root, '..', 'assets', 'fonts');

const base = `
@font-face{font-family:'Cormorant';src:url('${fonts}/CormorantGaramond.ttf');font-weight:300 700}
@font-face{font-family:'Cormorant';src:url('${fonts}/CormorantGaramond-Italic.ttf');font-style:italic;font-weight:300 700}
@font-face{font-family:'Jost';src:url('${fonts}/Jost.ttf');font-weight:100 900}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1280px;height:769px;overflow:hidden;font-family:'Jost';color:#F6EAD3;
 background:radial-gradient(circle at 70% 45%,#5A3522 0%,#2A1A12 60%,#1C110B 100%)}
.kick{font-size:13px;letter-spacing:.32em;text-transform:uppercase;color:#E7C47A}
h1{font-family:'Cormorant';font-weight:600;line-height:1.0}
.spread{display:flex;filter:drop-shadow(0 30px 40px rgba(0,0,0,.55))}
.spread img{display:block}
.spread .l{box-shadow:inset -30px 0 30px -20px rgba(0,0,0,.25)}
.spread .shade{position:relative}
.spread .shade::after{content:'';position:absolute;top:0;bottom:0;width:60px;pointer-events:none}
.spread .L::after{right:0;background:linear-gradient(to right,rgba(0,0,0,0),rgba(0,0,0,.18))}
.spread .R::after{left:0;background:linear-gradient(to left,rgba(0,0,0,0),rgba(0,0,0,.22))}
.tags{display:flex;gap:10px;flex-wrap:wrap}
.tags span{border:1px solid rgba(231,196,122,.5);border-radius:99px;padding:7px 14px;font-size:13px;color:#F3E3C3}
`;

const spread = (a, b, h) => `<div class="spread">
  <div class="shade L"><img src="${P(a)}" style="height:${h}px"></div>
  <div class="shade R"><img src="${P(b)}" style="height:${h}px"></div></div>`;

const slides = {
  '01-hero': `
   <div style="position:absolute;left:70px;top:0;bottom:0;width:380px;display:flex;flex-direction:column;justify-content:center;gap:22px">
     <div class="kick">Cookbook design · Amazon KDP</div>
     <h1 style="font-size:58px">The Edible<br>Candle Cookbook</h1>
     <p style="font-family:'Cormorant';font-style:italic;font-size:22px;color:#E9D9BC;line-height:1.35">
       Recipe writing, illustrated layout and print-ready interior formatting for a niche cookbook.</p>
     <div class="tags"><span>8 × 10 in</span><span>Full bleed</span><span>KDP print-ready PDF</span><span>Vector art</span></div>
   </div>
   <div style="position:absolute;right:-250px;top:50%;transform:translateY(-50%) perspective(1600px) rotateY(-14deg)">${spread(8, 9, 590)}</div>`,
  '02-recipe-spread': `
   <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px">
     ${spread(12, 13, 610)}
     <div class="kick">Consistent recipe template · ingredients, method, timings, chef’s notes</div></div>`,
  '03-chapter': `
   <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px">
     ${spread(10, 11, 610)}
     <div class="kick">Full-bleed chapter openers · feature pages</div></div>`,
  '04-front-matter': `
   <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px">
     <div style="display:flex;gap:26px">${spread(1, 2, 300)}${spread(3, 4, 300)}</div>
     <div style="display:flex;gap:26px">${spread(5, 6, 300)}${spread(7, 14, 300)}</div></div>`,
};

(async () => {
  const out = path.join(root, 'fiverr');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1280, height: 769 }, deviceScaleFactor: 2 });
  for (const [name, body] of Object.entries(slides)) {
    const f = path.join(root, 'build', `showcase-${name}.html`);
    fs.writeFileSync(f, `<!doctype html><html><head><meta charset="utf-8"><style>${base}</style></head><body>${body}</body></html>`);
    await pg.goto('file://' + f, { waitUntil: 'networkidle' });
    await pg.evaluate(() => document.fonts.ready);
    await pg.screenshot({ path: path.join(out, `${name}.jpg`), type: 'jpeg', quality: 90 });
  }
  await b.close();
  console.log('ok');
})();
