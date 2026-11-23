// Renders build/edible-candle-cookbook.html to a KDP-ready PDF + PNG page previews.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const root = __dirname;
  const html = 'file://' + path.join(root, 'build', 'interior.html');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(html, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: path.join(root, 'build', 'edible-candle-cookbook-interior.pdf'),
    width: '8.125in', height: '10.25in', printBackground: true, preferCSSPageSize: true,
  });

  // per-page PNGs (used for previews and the Fiverr showcase images)
  const dir = path.join(root, 'build', 'pages');
  fs.mkdirSync(dir, { recursive: true });
  const shot = await browser.newPage({ viewport: { width: 780, height: 984 }, deviceScaleFactor: 2 });
  await shot.goto(html, { waitUntil: 'networkidle' });
  await shot.addStyleTag({ content: 'html,body{background:#fff} .page{margin:0!important;box-shadow:none!important}' });
  await shot.evaluate(() => document.fonts.ready);
  const els = await shot.$$('.page');
  for (let i = 0; i < els.length; i++) {
    await els[i].screenshot({ path: path.join(dir, `p${String(i + 1).padStart(2, '0')}.png`) });
  }
  await browser.close();
  console.log('done', els.length);
})();
