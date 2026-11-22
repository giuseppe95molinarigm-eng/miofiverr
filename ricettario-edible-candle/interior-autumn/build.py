"""Six interior pages matching the autumn cover of The Edible Candle Cookbook.

Trim 8 x 10 in + 0.125 in bleed (page 8.125 x 10.25 in), KDP premium colour.
Photos are crops of the approved cover image, all >= 220 DPI at placed size.
Run:  python3 interior-autumn/build.py && node interior-autumn/render.js
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTS = (HERE.parent.parent / "assets" / "fonts").as_uri()
IMG = (HERE / "img").as_uri()


def sprig(flip=False, color="#C9963E"):
    t = ' transform="scale(-1,1) translate(-120,0)"' if flip else ""
    leaves = "".join(
        f'<path d="M{x},20 q-6,-14 -18,-16 q4,12 18,16 Z" fill="{color}"/>'
        f'<path d="M{x},20 q-6,14 -18,16 q4,-12 18,-16 Z" fill="{color}"/>'
        for x in (40, 62, 84))
    return (f'<svg class="sprig" viewBox="0 0 120 40" xmlns="http://www.w3.org/2000/svg"><g{t}>'
            f'<path d="M14,20 H112" stroke="{color}" stroke-width="2.2" stroke-linecap="round"/>{leaves}'
            f'<circle cx="112" cy="20" r="3" fill="{color}"/></g></svg>')


def laurel_pair(color="#C9963E"):
    return f'<div class="laurel">{sprig(True, color)}<span></span>{sprig(False, color)}</div>'


def rule(color="#C9963E"):
    return (f'<svg class="rule" viewBox="0 0 300 14" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="M0,7 H128 M172,7 H300" stroke="{color}" stroke-width="1"/>'
            f'<path d="M150,0 L157,7 L150,14 L143,7 Z" fill="{color}"/>'
            f'<circle cx="136" cy="7" r="2" fill="{color}"/><circle cx="164" cy="7" r="2" fill="{color}"/></svg>')


def folio(n, side, dark=False):
    c = " dark" if dark else ""
    return (f'<div class="folio {side}{c}"><b>{n}</b><span>The Edible Candle Cookbook</span></div>')


def ing_list(items):
    out = []
    for it in items:
        if it.startswith("#"):
            out.append(f'<li class="sub">{it[1:]}</li>')
        else:
            out.append(f"<li>{it}</li>")
    return "<ul>" + "".join(out) + "</ul>"


def steps(items):
    return "<ol>" + "".join(f"<li><span>{i}</span><p>{s}</p></li>" for i, s in enumerate(items, 1)) + "</ol>"


def meta(pairs):
    return '<div class="meta">' + "".join(f"<div><b>{k}</b><i>{v}</i></div>" for k, v in pairs) + "</div>"


pages = []

# ------------------------------------------------------------ 1  title (recto)
pages.append(f"""
<section class="page recto title">
  {laurel_pair()}
  <p class="t-the">The</p>
  <h1 class="t-main">Edible<br>Candle</h1>
  <p class="t-cook">Cookbook</p>
  {rule()}
  <p class="t-sub">Artisan Butter Candles, Savory Dips<br>&amp; Sweet Delights for Every Table</p>
  <div class="t-author">
    <p class="name">Lauren Whitmore</p>
    <p class="role">Food Stylist &amp; Recipe Developer</p>
  </div>
  <p class="t-pub">Hearth &amp; Harvest Press</p>
</section>""")

# ------------------------------------------------------------ 2  contents (verso, dark)
toc = [
    ("Introduction", "Welcome to the Autumn Table", "1"),
    ("Before You Light", "Wicks, Molds &amp; Safety", "4"),
    ("The Base Method", "Four Steps to Every Candle", "8"),
    ("Chapter One", "Savory Butter Candles", "12"),
    ("Chapter Two", "Tallow &amp; Ghee Candles", "34"),
    ("Chapter Three", "Sweet Dessert Candles", "56"),
    ("Chapter Four", "Harvest &amp; Holiday Boards", "78"),
    ("Reference", "Conversions &amp; Index", "102"),
]
rows = "".join(f'<li><small>{a}</small><span>{b}</span><i></i><b>{n}</b></li>' for a, b, n in toc)
pages.append(f"""
<section class="page verso contents dark-bg">
  <div class="live">
    {laurel_pair()}
    <h1 class="c-title">Contents</h1>
    {rule()}
    <ul class="toc">{rows}</ul>
  </div>
  {folio("iv", "verso", True)}
</section>""")

# ------------------------------------------------------------ 3  introduction (recto)
pages.append(f"""
<section class="page recto intro">
  <div class="live">
    <p class="kicker">Introduction</p>
    <h1 class="h-page">Welcome to the<br>Autumn Table</h1>
    {rule()}
    <figure class="arch"><img src="{IMG}/left.jpg" alt=""></figure>
    <div class="intro-text">
      <p class="lead">When the leaves turn copper and the evenings draw in, there is no better
      reason to gather friends around the table than a candle you can eat.</p>
      <p>An edible candle is shaped from butter, tallow or cocoa butter and set around a
      food-safe cotton wick. Light it as your guests sit down, and within minutes a warm,
      fragrant pool forms at the top, ready for torn bread, roasted vegetables or crisp
      slices of apple. What starts as the centerpiece quietly becomes the first course.</p>
      <p>I began making them for our family’s Thanksgiving table, and they have been the
      most talked-about dish every year since. Every recipe in this book has been tested in
      my own kitchen for flavor, for a clean and steady burn, and for how beautiful it looks
      in candlelight.</p>
      <p>You will find burn times, make-ahead notes and seasonal pairings alongside each
      recipe. Start with the base method on page 8, then let the season guide you.</p>
      <p class="sig">With warmth from my kitchen to yours,<br><span>Lauren</span></p>
    </div>
    <p class="caption">Wildflower Honey Butter Candle, page 18</p>
  </div>
  {folio("1", "recto")}
</section>""")

# ------------------------------------------------------------ 4  chapter opener (verso, dark)
pages.append(f"""
<section class="page verso chapter dark-bg">
  <div class="ch-text">
    <p class="ch-num">Chapter One</p>
    <h1 class="ch-title">Savory<br>Butter Candles</h1>
    {laurel_pair()}
    <p class="ch-blurb">Garlic, woodland herbs, smoked salt and a whisper of chili. These are the
    candles that bring everyone to the table and keep them there, bread in hand, long after the
    last log has burned down.</p>
    <ul class="ch-list">
      <li>Herbed Garlic Butter Crown Candle <b>13</b></li>
      <li>Smoky Chili &amp; Mustard Seed Candle <b>14</b></li>
      <li>Brown Butter, Sage &amp; Walnut Candle <b>16</b></li>
      <li>Wildflower Honey Butter Candle <b>18</b></li>
      <li>Roasted Garlic &amp; Fig Candle <b>20</b></li>
    </ul>
  </div>
  <div class="ch-photo"><img src="{IMG}/still.jpg" alt=""></div>
</section>""")

# ------------------------------------------------------------ 5  recipe A (recto)
pages.append(f"""
<section class="page recto recipe rA">
  <div class="photo-col"><img src="{IMG}/center.jpg" alt=""></div>
  <div class="live">
    <div class="rA-top">
      <p class="kicker">Savory Butter Candles</p>
      <h1 class="r-title">Herbed Garlic<br>Butter Crown<br>Candle</h1>
      {rule()}
      <p class="r-intro">Shaped in a fluted mini bundt mold, this golden crown of garlic butter is
      flecked with thyme, rosemary and pink peppercorns. As it melts, finish the pool with a
      thread of warm honey and dip in thick slices of rustic bread.</p>
      {meta([("Serves", "6–8"), ("Prep", "20 min"), ("Set", "4 hrs"), ("Burn", "1 hr")])}
      <h3>Ingredients</h3>
      {ing_list([
        "1 cup (225 g) salted butter, softened",
        "3 garlic cloves, finely grated",
        "1 tbsp fresh thyme leaves",
        "2 tsp fresh rosemary, minced",
        "1 tsp pink peppercorns, crushed",
        "½ tsp flaky sea salt",
        "#To finish",
        "2 tbsp warm honey",
        "Rustic bread, torn, for dipping",
        "#To assemble",
        "1 food-safe cotton wick, 6 in, oiled",
        "1 silicone mini bundt mold, 1 cup",
      ])}
    </div>
    <div class="rA-method">
      <h3>Method</h3>
      {steps([
        "Beat the softened butter until smooth and glossy, then fold in the garlic, herbs, peppercorns and salt.",
        "Thread the oiled wick through the center tube of the mold and secure it straight with a clothespin across the top.",
        "Pack the butter into the mold in three layers, pressing into every flute and tapping out air pockets.",
        "Chill for 4 hours, or freeze for 1 hour, until completely firm. Peel the mold away gently.",
        "Set the crown on a rimmed stoneware dish, trim the wick to ¼ in and light 10 minutes before serving. Drizzle the melted pool with honey.",
      ])}
      <aside class="tip"><b>Lauren’s tip</b> Chill the mold for 10 minutes before filling: the
      flutes stay crisp and the crown releases cleanly every time.</aside>
    </div>
  </div>
  {folio("13", "recto")}
</section>""")

# ------------------------------------------------------------ 6  recipe B (verso)
pages.append(f"""
<section class="page verso recipe rB">
  <div class="live">
    <div class="rB-head">
      <figure class="rB-photo"><img src="{IMG}/right.jpg" alt=""></figure>
      <div class="rB-title">
        <p class="kicker">Savory Butter Candles</p>
        <h1 class="r-title">Smoky Chili &amp;<br>Mustard Seed<br>Candle</h1>
        {rule()}
        <p class="r-intro">Golden with smoked paprika and studded with crunchy mustard seeds,
        this slow-burning tallow candle is crowned with chili flakes and toasted seeds. Pair it
        with roasted squash, pretzel bites and a glass of hard cider.</p>
        {meta([("Serves", "6"), ("Prep", "25 min"), ("Set", "2 hrs"), ("Burn", "90+ min")])}
      </div>
    </div>
    <div class="rB-body">
      <div class="ing"><h3>Ingredients</h3>
      {ing_list([
        "¾ cup (150 g) rendered beef tallow",
        "¼ cup (55 g) unsalted butter",
        "1 tsp smoked paprika",
        "¼ tsp ground turmeric",
        "1 tbsp whole yellow mustard seeds",
        "½ tsp smoked sea salt",
        "#Seed crown",
        "1 tsp red chili flakes",
        "1 tsp toasted pumpkin seeds, chopped",
        "½ tsp black mustard seeds",
        "#To assemble",
        "1 food-safe wick with metal tab",
        "1 straight-sided 8 oz pillar mold",
      ])}</div>
      <div class="met"><h3>Method</h3>
      {steps([
        "Melt the tallow and butter over low heat. Whisk in the paprika, turmeric and salt until evenly golden. Do not let it smoke.",
        "Toast the yellow mustard seeds in a dry pan for 1 minute until they pop, then stir them into the fat.",
        "Fix the wick tab to the base of the mold with a drop of warm fat and hold the wick upright.",
        "Cool the mixture, stirring often, until it turns thick and opaque, so the seeds stay suspended. Pour into the mold.",
        "Chill for 2 hours, unmold and press the seed crown gently into the top. Trim the wick to ¼ in and light at the table.",
      ])}
      <aside class="tip"><b>Make ahead</b> Wrapped tightly, the candle keeps for 2 weeks in the
      fridge. Bring it to room temperature for 30 minutes before lighting.</aside></div>
    </div>
  </div>
  {folio("14", "verso")}
</section>""")

CSS = f"""
@font-face {{ font-family: 'Cinzel'; src: url('{FONTS}/Cinzel.ttf'); font-weight: 400 900; }}
@font-face {{ font-family: 'Cormorant'; src: url('{FONTS}/CormorantGaramond.ttf'); font-weight: 300 700; }}
@font-face {{ font-family: 'Cormorant'; src: url('{FONTS}/CormorantGaramond-Italic.ttf'); font-style: italic; font-weight: 300 700; }}
@font-face {{ font-family: 'Jost'; src: url('{FONTS}/Jost.ttf'); font-weight: 100 900; }}
@font-face {{ font-family: 'Vibes'; src: url('{FONTS}/GreatVibes-Regular.ttf'); }}
@page {{ size: 8.125in 10.25in; margin: 0; }}
:root {{ --choc:#1E140E; --choc2:#2C1D14; --gold:#C9963E; --gold2:#E2B865; --cream:#FBF5EA; --sand:#F2E6D2;
        --ink:#2B1B12; --soft:#6E5646; --pumpkin:#C8641F; --fig:#7B2A2A; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: #777; }}
body {{ font-family: 'Jost', sans-serif; color: var(--ink); -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ width: 8.125in; height: 10.25in; position: relative; overflow: hidden; background: var(--cream);
        break-after: page; }}
.live {{ position: absolute; top: .8in; bottom: 1in; left: .875in; right: .875in; }}
.dark-bg {{ background: radial-gradient(ellipse at 50% 30%, #3A2618 0%, var(--choc) 62%, #140D09 100%); color: var(--sand); }}
.folio {{ position: absolute; bottom: .55in; display: flex; gap: 12px; align-items: baseline;
          font-family: 'Cinzel'; font-size: 7.5pt; letter-spacing: .22em; color: var(--soft); }}
.folio b {{ font-size: 10.5pt; color: var(--pumpkin); letter-spacing: 0; }}
.folio.recto {{ right: .875in; flex-direction: row-reverse; }}
.folio.verso {{ left: .875in; }}
.folio.dark {{ color: #A88F75; }} .folio.dark b {{ color: var(--gold); }}

.sprig {{ width: .9in; height: .3in; }}
.laurel {{ display: flex; align-items: center; justify-content: center; gap: 10px; }}
.laurel span {{ width: 5px; height: 5px; background: var(--gold); transform: rotate(45deg); }}
.rule {{ display: block; width: 2.4in; height: 12px; margin: 10px auto; }}
.kicker {{ font-family: 'Cinzel'; font-size: 8pt; letter-spacing: .32em; text-transform: uppercase; color: var(--pumpkin); font-weight: 600; }}
h1, h3 {{ font-weight: 600; }}

/* 1 title */
.title {{ text-align: center; padding-top: 1.55in; }}
.title .laurel .sprig {{ width: 1.1in; height: .37in; }}
.t-the {{ font-family: 'Cinzel'; font-size: 22pt; letter-spacing: .3em; color: var(--ink); margin-top: 14px; }}
.t-main {{ font-family: 'Cinzel'; font-size: 66pt; line-height: .98; color: var(--gold); letter-spacing: .02em;
           background: linear-gradient(180deg, #D8A851 0%, #B07A2A 100%); -webkit-background-clip: text; background-clip: text;
           -webkit-text-fill-color: transparent; margin-top: 4px; }}
.t-cook {{ font-family: 'Cinzel'; font-size: 30pt; letter-spacing: .14em; margin-top: 4px; }}
.t-sub {{ font-family: 'Cormorant'; font-style: italic; font-size: 17pt; line-height: 1.3; color: var(--soft); margin-top: 6px; }}
.t-author {{ margin-top: 1.45in; }}
.t-author .name {{ font-family: 'Cinzel'; font-size: 19pt; letter-spacing: .12em; color: var(--gold); font-weight: 600; }}
.t-author .role {{ font-size: 8.5pt; letter-spacing: .3em; text-transform: uppercase; color: var(--soft); margin-top: 6px; }}
.t-pub {{ position: absolute; bottom: .8in; left: 0; right: 0; font-family: 'Cinzel'; font-size: 8.5pt; letter-spacing: .3em; color: var(--soft); }}

/* 2 contents */
.contents .live {{ text-align: center; top: 1.05in; }}
.c-title {{ font-family: 'Cinzel'; font-size: 46pt; color: var(--gold2); letter-spacing: .08em; margin-top: 10px; font-weight: 500; }}
.toc {{ list-style: none; margin-top: .45in; text-align: left; }}
.toc li {{ display: grid; grid-template-columns: 1.6in auto 1fr auto; align-items: baseline; gap: 12px;
           padding: 13px 0; border-bottom: 1px solid rgba(201,150,62,.22); }}
.toc small {{ font-family: 'Cinzel'; font-size: 7.5pt; letter-spacing: .24em; text-transform: uppercase; color: var(--gold); }}
.toc span {{ font-family: 'Cormorant'; font-size: 18.5pt; color: #F6EBD8; font-weight: 500; }}
.toc i {{ border-bottom: 1px dotted rgba(226,184,101,.35); transform: translateY(-5px); }}
.toc b {{ font-family: 'Cinzel'; font-size: 13pt; color: var(--gold2); font-weight: 600; }}

/* 3 intro */
.h-page {{ font-family: 'Cinzel'; font-size: 30pt; line-height: 1.12; margin-top: 8px; font-weight: 500; }}
.intro .kicker, .intro .h-page {{ text-align: left; }}
.intro .rule {{ margin: 12px 0 14px; }}
.arch {{ float: right; width: 2.45in; height: 3.75in; margin: 0 0 12px .3in; border-radius: 1.3in 1.3in 6px 6px;
         overflow: hidden; outline: 1px solid var(--gold); outline-offset: 6px; }}
.arch img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 30%; }}
.intro-text p {{ font-family: 'Cormorant'; font-size: 13.4pt; line-height: 1.45; margin-bottom: 10px; text-align: justify; hyphens: auto; }}
.intro-text .lead {{ font-size: 16pt; font-style: italic; color: var(--fig); line-height: 1.35; text-align: left; }}
.intro-text .lead::first-letter {{ font-family: 'Cinzel'; font-style: normal; float: left; font-size: 46pt; line-height: .9;
     padding: 2px 8px 0 0; color: var(--pumpkin); }}
.sig {{ font-style: italic; text-align: left !important; margin-top: 6px; }}
.sig span {{ font-family: 'Vibes'; font-style: normal; font-size: 32pt; color: var(--pumpkin); display: inline-block; margin-top: 4px; }}
.caption {{ position: absolute; right: 0; top: 2.05in; width: 2.45in; text-align: center; font-family: 'Cormorant';
            font-style: italic; font-size: 10pt; color: var(--soft); display: none; }}

/* 4 chapter */
.chapter .ch-text {{ position: absolute; top: .95in; left: .875in; right: .875in; text-align: center; }}
.ch-num {{ font-family: 'Cinzel'; font-size: 10pt; letter-spacing: .45em; text-transform: uppercase; color: var(--gold); }}
.ch-title {{ font-family: 'Cinzel'; font-size: 44pt; line-height: 1.05; color: #F6EBD8; margin: 12px 0 14px; font-weight: 500; }}
.ch-blurb {{ font-family: 'Cormorant'; font-style: italic; font-size: 14.5pt; line-height: 1.42; color: #E6D4B8; max-width: 5in; margin: 14px auto 0; }}
.ch-list {{ list-style: none; max-width: 4.4in; margin: .3in auto 0; text-align: left; }}
.ch-list li {{ display: flex; justify-content: space-between; font-family: 'Cormorant'; font-size: 13.5pt; color: #F3E6CF;
               padding: 6px 0; border-bottom: 1px solid rgba(201,150,62,.25); }}
.ch-list b {{ font-family: 'Cinzel'; color: var(--gold2); font-size: 11pt; }}
.ch-photo {{ position: absolute; left: 0; right: 0; bottom: 0; height: 3.15in; }}
.ch-photo img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%; }}
.ch-photo::before {{ content: ''; position: absolute; inset: 0 0 auto 0; height: 1.1in;
                    background: linear-gradient(#1A110C, rgba(26,17,12,0)); z-index: 1; }}

/* recipes shared */
.r-title {{ font-family: 'Cinzel'; font-size: 25pt; line-height: 1.1; margin-top: 6px; font-weight: 600; color: var(--ink); }}
.recipe .rule {{ margin: 10px 0; width: 2in; }}
.r-intro {{ font-family: 'Cormorant'; font-style: italic; font-size: 12.3pt; line-height: 1.38; color: var(--soft); }}
.meta {{ display: grid; grid-template-columns: repeat(4, 1fr); margin: 12px 0 14px; border-top: 1px solid var(--gold); border-bottom: 1px solid var(--gold); }}
.meta div {{ text-align: center; padding: 6px 0; }}
.meta div + div {{ border-left: 1px solid #E6D3B0; }}
.meta b {{ display: block; font-family: 'Cinzel'; font-size: 6.5pt; letter-spacing: .2em; color: var(--pumpkin); }}
.meta i {{ font-style: normal; font-family: 'Cormorant'; font-size: 13pt; font-weight: 600; }}
.recipe h3 {{ font-family: 'Cinzel'; font-size: 12.5pt; letter-spacing: .12em; margin-bottom: 6px; color: var(--fig); }}
.recipe ul {{ list-style: none; }}
.recipe ul li {{ font-size: 9.1pt; line-height: 1.35; padding: 3.2px 0 3.2px 13px; position: relative; border-bottom: 1px dotted #DCC9AA; }}
.recipe ul li::before {{ content: ''; position: absolute; left: 0; top: 8.5px; width: 5px; height: 5px; background: var(--gold); transform: rotate(45deg); }}
.recipe ul li.sub {{ font-family: 'Cormorant'; font-style: italic; font-weight: 700; font-size: 12pt; color: var(--pumpkin); border: 0; padding: 7px 0 1px; }}
.recipe ul li.sub::before {{ display: none; }}
.recipe ol {{ list-style: none; }}
.recipe ol li {{ display: grid; grid-template-columns: 24px 1fr; gap: 6px; margin-bottom: 7px; }}
.recipe ol li span {{ font-family: 'Cinzel'; font-weight: 700; font-size: 13pt; color: var(--pumpkin); line-height: 1.05; }}
.recipe ol li p {{ font-size: 9.1pt; line-height: 1.45; }}
.tip {{ margin-top: 8px; background: var(--sand); border-left: 3px solid var(--gold); padding: 9px 13px; font-size: 8.8pt; line-height: 1.45; }}
.tip b {{ font-family: 'Cormorant'; font-style: italic; font-size: 12.5pt; color: var(--fig); margin-right: 4px; }}

/* 5 recipe A: photo bleeds off top + outer (right) edge */
.rA .photo-col {{ position: absolute; top: 0; right: 0; width: 3.6in; height: 5.3in; overflow: hidden;
                  border-bottom-left-radius: 1.6in; }}
.rA .photo-col img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 30%; }}
.rA .rA-top {{ width: 2.95in; }}
.rA .rA-method {{ position: absolute; right: 0; width: 3.3in; top: 4.75in; }}

.rA .rA-method ol li {{ break-inside: avoid; }}
.rA .tip {{ break-inside: avoid; }}

/* 6 recipe B: photo bleeds off outer (left) edge */
.rB .rB-head {{ display: grid; grid-template-columns: 2.95in 1fr; gap: .3in; }}
.rB .rB-photo {{ margin-left: -1in; margin-top: -.925in; height: 4.85in; overflow: hidden; border-bottom-right-radius: 1.4in; }}
.rB .rB-photo img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 35%; }}
.rB .rB-body {{ display: grid; grid-template-columns: 2.25in 1fr; gap: .3in; margin-top: .2in; }}
@media screen {{ .page {{ margin: 20px auto; box-shadow: 0 4px 30px rgba(0,0,0,.3); }} }}
"""

html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>The Edible Candle Cookbook — '
        f'Interior Sample</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
out = HERE / "build"
out.mkdir(exist_ok=True)
(out / "interior.html").write_text(html, encoding="utf-8")
print("pages", len(pages))
