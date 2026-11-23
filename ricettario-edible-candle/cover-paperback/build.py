"""Full paperback cover wrap (back + spine + front) for KDP.

Book: 8.5 x 11 in trim, 150 pages, premium colour paper (0.002347 in/page)
  spine  = 150 x 0.002347 = 0.352 in
  cover  = 0.125 + 8.5 + 0.352 + 8.5 + 0.125 = 17.602 in  x  11.25 in
Run from this folder:  python3 build.py && node render.js
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTS = (HERE.parent.parent / "assets" / "fonts").as_uri()
IMG = (HERE / "img").as_uri()

BLEED, TRIM_W, TRIM_H, PAGES, PPI = 0.125, 8.5, 11.0, 150, 0.002347
SPINE = round(PAGES * PPI, 3)                      # 0.352
W = round(2 * BLEED + 2 * TRIM_W + SPINE, 3)       # 17.602
H = TRIM_H + 2 * BLEED                             # 11.25
BACK_W = BLEED + TRIM_W                            # 8.625
SPINE_X = BACK_W
FRONT_X = BACK_W + SPINE
# KDP barcode zone: 2 x 1.2 in, 0.25 in from the trim, bottom-right of the back cover
BAR = dict(x=BACK_W - 0.25 - 2.0, y=H - BLEED - 0.25 - 1.2, w=2.0, h=1.2)


def sprig(flip=False, color="#C9963E"):
    t = ' transform="scale(-1,1) translate(-120,0)"' if flip else ""
    leaves = "".join(
        f'<path d="M{x},20 q-6,-14 -18,-16 q4,12 18,16 Z" fill="{color}"/>'
        f'<path d="M{x},20 q-6,14 -18,16 q4,-12 18,-16 Z" fill="{color}"/>' for x in (40, 62, 84))
    return (f'<svg class="sprig" viewBox="0 0 120 40" xmlns="http://www.w3.org/2000/svg"><g{t}>'
            f'<path d="M14,20 H112" stroke="{color}" stroke-width="2.2" stroke-linecap="round"/>{leaves}'
            f'<circle cx="112" cy="20" r="3" fill="{color}"/></g></svg>')


def laurel():
    return f'<div class="laurel">{sprig(True)}<span></span>{sprig()}</div>'


def rule(w="2.6in"):
    return (f'<svg class="rule" style="width:{w}" viewBox="0 0 300 14" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M0,7 H128 M172,7 H300" stroke="#C9963E" stroke-width="1"/>'
            '<path d="M150,0 L157,7 L150,14 L143,7 Z" fill="#C9963E"/>'
            '<circle cx="136" cy="7" r="2" fill="#C9963E"/><circle cx="164" cy="7" r="2" fill="#C9963E"/></svg>')


inside = [
    "Sweet &amp; savory butter candles for every season",
    "A simple four-step base method",
    "Make-ahead, storage and serving notes",
    "Pairings for boards, breads, brunch &amp; holidays",
    "Easy silicone-mold shaping, no special skills",
    "Full-color photography throughout",
]
inside_html = "".join(f"<li>{t}</li>" for t in inside)

photos = [("back-r1.jpg", "Roasted Garlic &amp; Rosemary"),
          ("back-r3.jpg", "Fig &amp; Honey"),
          ("back-r4.jpg", "Maple &amp; Cinnamon")]
photos_html = "".join(
    f'<figure><div class="arch"><img src="{IMG}/{f}" alt=""></div><figcaption>{c}</figcaption></figure>'
    for f, c in photos)

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>The Edible Candle Cookbook — Paperback Cover</title><style>
@font-face {{ font-family: 'Cinzel'; src: url('{FONTS}/static/Cinzel-500.ttf'); font-weight: 500; }}
@font-face {{ font-family: 'Cinzel'; src: url('{FONTS}/static/Cinzel-600.ttf'); font-weight: 600; }}
@font-face {{ font-family: 'Cinzel'; src: url('{FONTS}/static/Cinzel-700.ttf'); font-weight: 700; }}
@font-face {{ font-family: 'Cormorant'; src: url('{FONTS}/static/CormorantGaramond-500.ttf'); font-weight: 500; }}
@font-face {{ font-family: 'Cormorant'; src: url('{FONTS}/static/CormorantGaramond-Italic-500.ttf'); font-style: italic; font-weight: 500; }}
@font-face {{ font-family: 'Jost'; src: url('{FONTS}/static/Jost-400.ttf'); font-weight: 400; }}
@font-face {{ font-family: 'Jost'; src: url('{FONTS}/static/Jost-500.ttf'); font-weight: 500; }}
@page {{ size: {W}in {H}in; margin: 0; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}in; height: {H}in; background: #1E140E; }}
body {{ position: relative; overflow: hidden; -webkit-print-color-adjust: exact; print-color-adjust: exact; color: #F3E6CF; }}
.abs {{ position: absolute; }}
.back-bg {{ left: 0; top: 0; width: {BACK_W}in; height: {H}in; }}
.back-bg img, .front img, .spine img {{ width: 100%; height: 100%; display: block; }}
.back-shade {{ left: 0; top: 0; width: {BACK_W}in; height: {H}in;
   background: radial-gradient(ellipse 70% 45% at 50% 24%, rgba(80,48,22,.35), rgba(20,13,9,0) 70%),
               linear-gradient(rgba(20,13,9,.88), rgba(20,13,9,.62) 45%, rgba(20,13,9,.2) 78%, rgba(20,13,9,.4)); }}
.spine {{ left: {SPINE_X - 0.003:.3f}in; top: 0; width: {SPINE + 0.006:.3f}in; height: {H}in; }}
.front {{ left: {FRONT_X}in; top: 0; width: {W - FRONT_X:.3f}in; height: {H}in; }}

/* back cover content: safe area 0.5in inside the trim */
.back {{ left: {BLEED + 0.55}in; width: {TRIM_W - 1.1}in; top: {BLEED + 0.6}in; text-align: center; }}
.sprig {{ width: .95in; height: .32in; }}
.laurel {{ display: flex; align-items: center; justify-content: center; gap: 10px; }}
.laurel span {{ width: 6px; height: 6px; background: #C9963E; transform: rotate(45deg); }}
.rule {{ display: block; height: 12px; margin: 12px auto; }}
h1 {{ font-family: 'Cinzel'; font-weight: 600; font-size: 27pt; line-height: 1.15; color: #E2B865; letter-spacing: .03em; margin-top: 10px; }}
.blurb {{ font-family: 'Cormorant'; font-size: 15pt; line-height: 1.42; color: #F1E4CC; max-width: 6.5in; margin: 0 auto; text-wrap: balance; }}
.blurb em {{ color: #E2B865; }}
.photos {{ display: flex; justify-content: center; gap: .3in; margin-top: .38in; }}
.photos figure {{ width: 1.95in; }}
.photos .arch {{ width: 1.95in; height: 2.4in; border-radius: .975in .975in 5px 5px; overflow: hidden; outline: 1px solid #C9963E; outline-offset: 5px; }}
.photos img {{ object-fit: cover; width: 100%; height: 100%; }}
.photos figcaption {{ font-family: 'Cinzel'; font-size: 6.8pt; letter-spacing: .1em; color: #E2B865; margin-top: 12px; text-transform: uppercase; white-space: nowrap; }}
h2 {{ font-family: 'Cinzel'; font-weight: 600; font-size: 11pt; letter-spacing: .3em; color: #E2B865; margin-top: .4in; }}
.inside {{ list-style: none; columns: 2; column-gap: .35in; text-align: left; margin: 12px auto 0; max-width: 6.6in; }}
.inside li {{ font-family: 'Jost'; font-size: 10.2pt; line-height: 1.4; color: #EFE2CA; padding: 4px 0 4px 16px; position: relative; break-inside: avoid; }}
.inside li::before {{ content: ''; position: absolute; left: 0; top: 10px; width: 6px; height: 6px; background: #C9963E; transform: rotate(45deg); }}

.bio {{ left: {BLEED + 0.55}in; top: {BAR['y'] - 0.45:.3f}in; width: {BAR['x'] - BLEED - 0.55 - 0.3:.3f}in;
        display: grid; grid-template-columns: 1.1in 1fr; gap: .22in; align-items: center;
        border-top: 1px solid rgba(201,150,62,.55); padding-top: .2in; }}
.mono {{ width: .95in; height: .95in; border-radius: 50%; border: 1.5px solid #C9963E; display: flex; align-items: center; justify-content: center;
         font-family: 'Cinzel'; font-weight: 600; font-size: 22pt; color: #E2B865; letter-spacing: .02em; position: relative; }}
.portrait {{ width: 1.1in; height: 1.1in; border-radius: 50%; overflow: hidden; outline: 1.5px solid #C9963E; outline-offset: 4px; }}
.portrait img {{ width: 100%; height: 100%; object-fit: cover; }}
.mono::after {{ content: ''; position: absolute; inset: 5px; border-radius: 50%; border: 1px solid rgba(201,150,62,.45); }}
.bio h3 {{ font-family: 'Cinzel'; font-weight: 600; font-size: 9pt; letter-spacing: .26em; color: #E2B865; margin-bottom: 4px; }}
.bio p {{ font-family: 'Cormorant'; font-size: 11.3pt; line-height: 1.36; color: #EADCC3; text-wrap: pretty; }}
.bio p b {{ font-weight: 500; color: #F6EBD8; }}
.pub {{ left: {BAR['x']:.3f}in; width: {BAR['w']}in; top: {BAR['y'] - 0.62:.3f}in; text-align: center; }}
.pub p {{ font-family: 'Cinzel'; font-weight: 500; font-size: 7.5pt; letter-spacing: .28em; color: #C9A46A; }}
.pub small {{ display: block; font-family: 'Jost'; font-size: 6.5pt; letter-spacing: .2em; color: #A88F75; margin-top: 4px; }}

/* spine: reads top to bottom (US convention) */
.spine-text {{ left: {SPINE_X}in; width: {SPINE}in; top: {BLEED + 0.45}in; height: {TRIM_H - 0.9}in;
               writing-mode: vertical-rl; display: flex; align-items: center; justify-content: space-between; }}
.spine-text .t {{ font-family: 'Cinzel'; font-weight: 700; font-size: 12.5pt; letter-spacing: .16em; color: #E2B865; white-space: nowrap; }}
.spine-text .t span {{ color: #F6EBD8; font-weight: 600; }}
.spine-text .a {{ font-family: 'Cinzel'; font-weight: 600; font-size: 10pt; letter-spacing: .2em; color: #F3E6CF; white-space: nowrap; }}
.spine-text .d {{ width: 6px; height: 6px; background: #C9963E; transform: rotate(45deg); }}
</style></head><body>
<div class="abs back-bg"><img src="{IMG}/back-bg.jpg" alt=""></div>
<div class="abs back-shade"></div>
<div class="abs spine"><img src="{IMG}/spine.jpg" alt=""></div>
<div class="abs front"><img src="{IMG}/front-panel.jpg" alt=""></div>

<div class="abs back">
  {laurel()}
  <h1>The Centerpiece You Can<br>Spread on Warm Bread</h1>
  {rule()}
  <p class="blurb">Shaped like elegant pillar candles but made entirely of flavored butter,
  edible candles are the easiest way to turn an ordinary meal into an occasion. In this
  beautifully photographed collection, food stylist <em>Lauren Whitmore</em> shows you how to
  make them with a simple silicone mold, a few pantry ingredients and ten minutes of hands-on
  time, from roasted garlic and smoked paprika to fig, honey and maple cinnamon.</p>
  <div class="photos">{photos_html}</div>
  <h2>Inside You’ll Find</h2>
  <ul class="inside">{inside_html}</ul>
</div>

<div class="abs bio">
  <div class="portrait"><img src="{IMG}/author.jpg" alt=""></div>
  <div>
    <h3>About the Author</h3>
    <p><b>Lauren Whitmore</b> is a food stylist and recipe developer from Vermont, where
    autumn is the longest and most delicious season of the year. She has spent more than a
    decade styling harvest tables, brunches and holiday menus, and believes every gathering
    deserves one dish everyone remembers.</p>
  </div>
</div>
<div class="abs pub"><p>Hearth &amp; Harvest Press</p><small>COOKING / SEASONAL</small></div>

<div class="abs spine-text">
  <div class="t">The Edible <span>Candle</span> Cookbook</div>
  <div class="d"></div>
  <div class="a">Lauren Whitmore</div>
</div>
</body></html>"""

guides = f"""<style>
.g {{ position: absolute; pointer-events: none; }}
.trim {{ border: 1.5px solid #00B7FF; }}
.safe {{ border: 1px dashed #FF3EA5; }}
.bar {{ background: rgba(255,255,255,.92); color: #333; font: 600 9pt/1 'Jost'; display: flex; align-items: center; justify-content: center; }}
.lbl {{ font: 600 8pt/1 'Jost'; color: #00B7FF; background: rgba(0,0,0,.6); padding: 3px 6px; }}
</style>
<div class="g trim" style="left:{BLEED}in;top:{BLEED}in;width:{TRIM_W}in;height:{TRIM_H}in"></div>
<div class="g trim" style="left:{FRONT_X}in;top:{BLEED}in;width:{TRIM_W}in;height:{TRIM_H}in"></div>
<div class="g trim" style="left:{SPINE_X}in;top:{BLEED}in;width:{SPINE}in;height:{TRIM_H}in;border-color:#FFD400"></div>
<div class="g safe" style="left:{BLEED + 0.125}in;top:{BLEED + 0.125}in;width:{TRIM_W - 0.25}in;height:{TRIM_H - 0.25}in"></div>
<div class="g safe" style="left:{FRONT_X + 0.125}in;top:{BLEED + 0.125}in;width:{TRIM_W - 0.25}in;height:{TRIM_H - 0.25}in"></div>
<div class="g safe" style="left:{SPINE_X + 0.0625}in;top:{BLEED + 0.125}in;width:{SPINE - 0.125}in;height:{TRIM_H - 0.25}in"></div>
<div class="g bar" style="left:{BAR['x']}in;top:{BAR['y']}in;width:{BAR['w']}in;height:{BAR['h']}in">KDP barcode area</div>
<div class="g lbl" style="left:{BLEED + 0.2}in;top:{BLEED + 0.15}in">BACK · trim 8.5 × 11 in</div>
<div class="g lbl" style="left:{FRONT_X + 0.2}in;top:{BLEED + 0.15}in">FRONT · trim 8.5 × 11 in</div>
<div class="g lbl" style="left:{SPINE_X - 0.9}in;top:{H - 0.45}in">SPINE {SPINE} in · {PAGES} pp</div>
"""

out = HERE / "build"
out.mkdir(exist_ok=True)
(out / "cover.html").write_text(html, encoding="utf-8")
(out / "cover-guides.html").write_text(html.replace("</body>", guides + "</body>"), encoding="utf-8")
(out / "dims.txt").write_text(f"{W} {H} {SPINE}\n")
print(f"cover {W} x {H} in, spine {SPINE} in")
