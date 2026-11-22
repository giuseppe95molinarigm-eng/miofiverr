// Reports free space (px) at the bottom of each page's live area; negative = overflow.
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'build', 'interior.html')); await p.evaluate(() => document.fonts.ready);
  console.log((await p.$$eval('.page', ps => ps.map((pg, i) => {
    const l = pg.querySelector('.live'); if (!l) return (i + 1) + ':-';
    const lb = l.getBoundingClientRect(); let m = 0;
    l.querySelectorAll('*').forEach(e => { const r = e.getBoundingClientRect(); if (r.height) m = Math.max(m, r.bottom); });
    const a = pg.querySelector('.rA-top'), c = pg.querySelector('.rA-method'), ph = pg.querySelector('.photo-col');
    const x = a ? ` top-ends=${Math.round(a.getBoundingClientRect().bottom)} photo-ends=${Math.round(ph.getBoundingClientRect().bottom)} method-top=${Math.round(c.getBoundingClientRect().top)} method-end=${Math.round(c.getBoundingClientRect().bottom)}` : '';
    return (i + 1) + ':' + Math.round(lb.bottom - m) + x;
  }))).join('\n'));
  await b.close();
})();
