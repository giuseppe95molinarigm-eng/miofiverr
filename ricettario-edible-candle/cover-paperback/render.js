// Renders the cover wrap to a KDP print PDF plus JPG previews (with and without guides).
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const { execFileSync } = require('child_process');

(async () => {
  const out = path.join(__dirname, 'build');
  const [W, H] = fs.readFileSync(path.join(out, 'dims.txt'), 'utf8').trim().split(' ').map(Number);
  const b = await chromium.launch();

  const p = await b.newPage();
  await p.goto('file://' + path.join(out, 'cover.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const pdf = path.join(out, 'edible-candle-cookbook-paperback-cover.pdf');
  await p.pdf({ path: pdf, width: `${W}in`, height: `${H}in`, printBackground: true, preferCSSPageSize: true });
  // snap the page box to the exact KDP size (Chromium rounds to whole pixels)
  execFileSync('python3', ['-c', `
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
r = PdfReader(${JSON.stringify(pdf)}); w = PdfWriter()
for pg in r.pages:
    box = RectangleObject([0, 0, ${W * 72}, ${H * 72}]); pg.mediabox = box; pg.cropbox = box; w.add_page(pg)
w.add_metadata({'/Title': 'The Edible Candle Cookbook - Paperback Cover'})
w.write(${JSON.stringify(pdf)})
`]);

  for (const [file, name] of [['cover.html', 'preview-cover.jpg'], ['cover-guides.html', 'preview-cover-guides.jpg']]) {
    const s = await b.newPage({ viewport: { width: Math.round(W * 96), height: Math.round(H * 96) }, deviceScaleFactor: 1.5 });
    await s.goto('file://' + path.join(out, file), { waitUntil: 'networkidle' });
    await s.evaluate(() => document.fonts.ready);
    await s.screenshot({ path: path.join(out, name), type: 'jpeg', quality: 90 });
  }
  await b.close();
  console.log('done');
})();
