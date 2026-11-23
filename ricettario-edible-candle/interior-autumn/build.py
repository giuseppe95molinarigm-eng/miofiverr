"""Interior sample of The Edible Candle Cookbook, styled to match the autumn cover.

Pages: title, contents, introduction, chapter 1 opener, recipes 01-02,
chapter 2 opener, recipes 03-04 (recipe text and photos supplied by the client,
see ../ricette-cliente/).

Trim 8 x 10 in + 0.125 in bleed (page 8.125 x 10.25 in), KDP premium colour.
Run from this folder:  python3 build.py && node render.js && node check.js
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTS = (HERE.parent.parent / "assets" / "fonts").as_uri()
IMG = (HERE / "img").as_uri()


# ---------------------------------------------------------------- ornaments
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
    return f'<div class="folio {side}{c}"><b>{n}</b><span>The Edible Candle Cookbook</span></div>'


# ---------------------------------------------------------------- recipes (client text, verbatim)
RECIPES = [
    dict(
        num="01", chapter="Savory Butter Candles", page=13, side="recto", img="r1.jpg", pos="50% 55%",
        title="Roasted Garlic &amp; Rosemary Butter Candle",
        intro="Sweet roasted garlic and fragrant rosemary turn a simple butter spread into a "
              "centerpiece for warm, crusty bread.",
        meta=[("Makes", "1 candle"), ("Serves", "about 8"), ("Prep", "10 min"),
              ("Roast", "35–45 min"), ("Chill", "2 hr")],
        ingredients=["1 small head garlic", "1 tsp olive oil",
                     "½ cup (113 g) unsalted butter, softened",
                     "1 tsp finely chopped fresh rosemary", "¼ tsp fine sea salt",
                     "⅛ tsp freshly ground black pepper", "Toasted baguette slices, for serving"],
        need="a small food-grade silicone spiral mold (about ½ cup capacity) and a short piece "
             "of plain, undyed cotton kitchen twine for the decorative wick.",
        method=[
            ("Roast the garlic.", "Heat the oven to 400°F (200°C). Slice the top off the garlic "
             "head to expose the cloves. Drizzle with olive oil, wrap in foil, and roast for "
             "35–45 minutes, until soft and golden. Let cool."),
            ("Mix the butter.", "Squeeze 4 roasted cloves into a bowl and mash until smooth. "
             "Stir in the softened butter, rosemary, salt, and pepper."),
            ("Fill the mold.", "Press the butter into the mold with the back of a spoon to push "
             "it into the grooves. Smooth the exposed surface and refrigerate for about 2 hours, "
             "until firm."),
            ("Add the wick.", "Unmold onto a small ceramic plate. Use a skewer to make a shallow "
             "hole in the center of the top, then insert the cotton twine so a short length "
             "stands upright."),
            ("Serve.", "Let the butter soften for about 10 minutes. Keep the wick unlit and remove "
             "it before serving. Spread the butter over warm baguette slices."),
        ]),
    dict(
        num="02", chapter="Savory Butter Candles", page=14, side="verso", img="r2.jpg", pos="50% 50%",
        title="Smoked Paprika &amp; Sea Salt Butter Candle",
        intro="Sweet smoked paprika gives this butter its copper color and a woodsmoke aroma. "
              "A pinch of flaky sea salt adds crunch to each bite of grilled sourdough.",
        meta=[("Makes", "1 candle"), ("Serves", "about 8"), ("Prep", "10 min"), ("Chill", "2 hr")],
        ingredients=["½ cup (113 g) unsalted butter, softened", "1½ tsp sweet smoked paprika",
                     "½ tsp finely grated lemon zest", "¼ tsp fine sea salt",
                     "1 pinch flaky sea salt, to finish", "Grilled sourdough slices, for serving"],
        need="a small cylindrical food-grade silicone mold (about ½ cup capacity) and a short "
             "piece of plain, undyed cotton kitchen twine for the decorative wick.",
        method=[
            ("Season the butter.", "Mix the softened butter with the paprika, lemon zest, and "
             "fine sea salt until the color is uniform."),
            ("Fill the mold.", "Press the butter into the mold a spoonful at a time to minimize "
             "air pockets. Level the exposed surface and refrigerate for about 2 hours, until firm."),
            ("Add the wick.", "Unmold the butter onto a small ceramic plate. Make a shallow hole "
             "in the center of the top with a skewer and insert the twine so a short length "
             "stands upright. Sprinkle the flaky salt around it."),
            ("Serve.", "Let the butter soften for about 10 minutes. Keep the wick unlit and remove "
             "it before serving. Spread the butter on warm grilled sourdough."),
        ]),
    dict(
        num="03", chapter="Sweet Butter Candles", page=26, side="verso", img="r3.jpg", pos="50% 45%",
        title="Fig &amp; Honey Butter Candle",
        intro="Fig preserves leave little flecks of fruit in this honey-sweetened butter. Serve it "
              "with warm brioche, fresh figs, and toasted walnuts for crunch.",
        meta=[("Makes", "1 candle"), ("Serves", "about 8"), ("Prep", "10 min"), ("Chill", "2 hr")],
        ingredients=["½ cup (113 g) unsalted butter, softened", "1 tbsp thick fig preserves",
                     "1 tsp honey", "1 pinch fine sea salt",
                     "Toasted brioche, quartered fresh figs, and toasted walnuts, to serve"],
        need="a small fluted food-grade silicone mold (about ⅔ cup capacity) and a short piece "
             "of plain, undyed cotton kitchen twine for the decorative wick.",
        method=[
            ("Mix the butter.", "Stir the softened butter, honey, and salt until smooth. Fold in "
             "the fig preserves, leaving a few streaks and flecks of fruit."),
            ("Fill the mold.", "Press the butter into the fluted mold with the back of a spoon to "
             "fill the grooves. Smooth the exposed surface and refrigerate for about 2 hours, "
             "until firm."),
            ("Add the wick.", "Unmold onto a small ceramic plate. Make a shallow hole in the "
             "center of the top with a skewer and insert the twine so a short length stands upright."),
            ("Serve.", "Let the butter soften for about 10 minutes. Keep the wick unlit and remove "
             "it before serving. Spread the butter on warm brioche and serve with the fresh figs "
             "and toasted walnuts."),
        ]),
    dict(
        num="04", chapter="Sweet Butter Candles", page=27, side="recto", img="r4.jpg", pos="50% 60%",
        title="Maple &amp; Cinnamon Butter Candle",
        intro="Maple syrup and cinnamon make a soft, lightly sweet butter that melts into the "
              "pockets of a hot waffle.",
        meta=[("Makes", "1 candle"), ("Serves", "about 8"), ("Prep", "10 min"), ("Chill", "2 hr")],
        ingredients=["½ cup (113 g) unsalted butter, softened", "1 tbsp pure maple syrup",
                     "½ tsp ground cinnamon", "1 pinch fine sea salt",
                     "Warm waffles and extra maple syrup, to serve"],
        need="a small round food-grade silicone mold (about ⅔ cup capacity) and a short piece of "
             "plain, undyed cotton kitchen twine for the decorative wick.",
        method=[
            ("Mix the butter.", "Stir the softened butter with the cinnamon and salt until evenly "
             "speckled. Add the maple syrup a teaspoon at a time, stirring well after each addition."),
            ("Shape and chill.", "Press the butter into the mold with the back of a spoon. Smooth "
             "the surface and refrigerate for about 2 hours, until firm enough to unmold."),
            ("Add the wick.", "Turn the butter out onto a small saucer. Make a shallow hole in the "
             "center with a skewer and insert the twine so a short length stands upright."),
            ("Serve.", "Let the butter soften for about 10 minutes. Keep the wick unlit and remove "
             "it before serving. Spoon the butter over hot waffles and finish with a drizzle of "
             "maple syrup."),
        ]),
]


def recipe_page(r):
    meta = "".join(f"<div><b>{k}</b><i>{v}</i></div>" for k, v in r["meta"])
    ings = "".join(f"<li>{i}</li>" for i in r["ingredients"])
    steps = "".join(f"<li><span>{n}</span><p><strong>{h}</strong> {t}</p></li>"
                    for n, (h, t) in enumerate(r["method"], 1))
    return f"""
<section class="page {r['side']} recipe">
  <figure class="r-photo"><img src="{IMG}/{r['img']}" style="object-position:{r['pos']}" alt=""></figure>
  <div class="live">
    <div class="r-head">
      <p class="kicker"><span class="num">{r['num']}</span> {r['chapter']}</p>
      <h1 class="r-title">{r['title']}</h1>
      {rule()}
      <p class="r-intro">{r['intro']}</p>
    </div>
    <div class="meta" style="grid-template-columns: repeat({len(r['meta'])}, 1fr)">{meta}</div>
    <div class="r-body">
      <div class="ing">
        <h3>Ingredients</h3><ul>{ings}</ul>
        <aside class="need"><b>You’ll also need</b> {r['need']}</aside>
      </div>
      <div class="met"><h3>Method</h3><ol>{steps}</ol></div>
    </div>
  </div>
  {folio(r['page'], r['side'])}
</section>"""


def chapter_page(side, num, title, blurb, items, photo):
    rows = "".join(f"<li>{t} <b>{p}</b></li>" for t, p in items)
    return f"""
<section class="page {side} chapter dark-bg {photo['cls']}">
  <div class="ch-text">
    <p class="ch-num">Chapter {num}</p>
    <h1 class="ch-title">{title}</h1>
    {laurel_pair()}
    <p class="ch-blurb">{blurb}</p>
    {photo.get('inline', '')}
    <ul class="ch-list">{rows}</ul>
  </div>
  {photo.get('band', '')}
</section>"""


pages = []

# 1  title (recto)
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

# 2  contents (verso, dark)
toc = [
    ("Introduction", "Welcome to the Autumn Table", "1"),
    ("Before You Begin", "Molds, Twine &amp; Storage", "4"),
    ("The Base Method", "Four Steps to Every Candle", "8"),
    ("Chapter One", "Savory Butter Candles", "12"),
    ("Chapter Two", "Sweet Butter Candles", "25"),
    ("Chapter Three", "Holiday &amp; Party Boards", "41"),
    ("Chapter Four", "Breads, Crackers &amp; Dippers", "57"),
    ("Reference", "Conversions &amp; Index", "74"),
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

# 3  introduction (recto)
pages.append(f"""
<section class="page recto intro">
  <div class="live">
    <p class="kicker">Introduction</p>
    <h1 class="h-page">Welcome to the<br>Autumn Table</h1>
    {rule()}
    <figure class="arch"><img src="{IMG}/intro.jpg" alt=""></figure>
    <div class="intro-text">
      <p class="lead">When the leaves turn copper and the evenings draw in, there is no better
      reason to gather friends around the table than a candle you can eat.</p>
      <p>A butter candle looks like a beautiful pillar candle, but it is made entirely of
      flavored butter, shaped in a simple silicone mold and finished with a short length of
      plain cotton twine. Set it on a small plate in the middle of the table and it becomes
      the conversation piece of the evening, until someone reaches for the bread.</p>
      <p>The wick is purely decorative: it stays unlit and comes out before serving. Let the
      candle soften for about ten minutes, then spread it over warm toast, waffles or brioche.</p>
      <p>Every recipe in this book takes about ten minutes of hands-on time, a few everyday
      ingredients and a couple of hours in the fridge. Start with the base method on page 8,
      then let the season guide your flavors.</p>
      <p class="sig">With warmth from my kitchen to yours,<br><span>Lauren</span></p>
    </div>
  </div>
  {folio("1", "recto")}
</section>""")

# 4  chapter one (verso, dark, photo band from the cover)
pages.append(chapter_page(
    "verso", "One", "Savory<br>Butter Candles",
    "Roasted garlic, woodland herbs, smoked paprika and flaky salt. These are the candles that "
    "bring everyone to the table and keep them there, warm bread in hand.",
    [("Roasted Garlic &amp; Rosemary Butter Candle", 13),
     ("Smoked Paprika &amp; Sea Salt Butter Candle", 14),
     ("Brown Butter, Sage &amp; Walnut Candle", 16),
     ("Parmesan &amp; Black Pepper Candle", 18),
     ("Everything Bagel Butter Candle", 20)],
    {"cls": "with-band", "band": f'<div class="ch-photo"><img src="{IMG}/still.jpg" alt=""></div>'}))

pages.append(recipe_page(RECIPES[0]))
pages.append(recipe_page(RECIPES[1]))

# 7  chapter two (recto, dark, arch photo)
pages.append(chapter_page(
    "recto", "Two", "Sweet<br>Butter Candles",
    "Fig and honey, maple and cinnamon, and the warm spices of the season. Made for slow "
    "weekend breakfasts, brunch boards and the last course of an autumn dinner.",
    [("Fig &amp; Honey Butter Candle", 26),
     ("Maple &amp; Cinnamon Butter Candle", 27),
     ("Pumpkin Spice &amp; Brown Sugar Candle", 28),
     ("Salted Caramel Apple Candle", 30),
     ("Chai &amp; Vanilla Bean Candle", 32)],
    {"cls": "with-arch", "inline": f'<figure class="ch-arch"><img src="{IMG}/ch2.jpg" alt=""></figure>'}))

pages.append(recipe_page(RECIPES[2]))
pages.append(recipe_page(RECIPES[3]))

# ---------------------------------------------------------------- css
CSS = f"""
@font-face {{ font-family: 'Cinzel'; src: url('{FONTS}/Cinzel.ttf'); font-weight: 400 900; }}
@font-face {{ font-family: 'Cormorant'; src: url('{FONTS}/CormorantGaramond.ttf'); font-weight: 300 700; }}
@font-face {{ font-family: 'Cormorant'; src: url('{FONTS}/CormorantGaramond-Italic.ttf'); font-style: italic; font-weight: 300 700; }}
@font-face {{ font-family: 'Jost'; src: url('{FONTS}/Jost.ttf'); font-weight: 100 900; }}
@font-face {{ font-family: 'Vibes'; src: url('{FONTS}/GreatVibes-Regular.ttf'); }}
@page {{ size: 8.125in 10.25in; margin: 0; }}
:root {{ --choc:#1E140E; --gold:#C9963E; --gold2:#E2B865; --cream:#FBF5EA; --sand:#F2E6D2;
        --ink:#2B1B12; --soft:#6E5646; --pumpkin:#C8641F; --fig:#7B2A2A; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: #777; }}
body {{ font-family: 'Jost', sans-serif; color: var(--ink); -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ width: 8.125in; height: 10.25in; position: relative; overflow: hidden; background: var(--cream); break-after: page; }}
/* live area: 0.125 bleed + 0.75 outer/0.875 gutter, safe on both sides */
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

/* title */
.title {{ text-align: center; padding-top: 1.55in; }}
.title .laurel .sprig {{ width: 1.1in; height: .37in; }}
.t-the {{ font-family: 'Cinzel'; font-size: 22pt; letter-spacing: .3em; margin-top: 14px; }}
.t-main {{ font-family: 'Cinzel'; font-size: 66pt; line-height: .98; letter-spacing: .02em; font-weight: 600;
           background: linear-gradient(180deg, #D8A851 0%, #B07A2A 100%); -webkit-background-clip: text; background-clip: text;
           -webkit-text-fill-color: transparent; margin-top: 4px; }}
.t-cook {{ font-family: 'Cinzel'; font-size: 30pt; letter-spacing: .14em; margin-top: 4px; }}
.t-sub {{ font-family: 'Cormorant'; font-style: italic; font-size: 17pt; line-height: 1.3; color: var(--soft); margin-top: 6px; }}
.t-author {{ margin-top: 1.45in; }}
.t-author .name {{ font-family: 'Cinzel'; font-size: 19pt; letter-spacing: .12em; color: var(--gold); font-weight: 600; }}
.t-author .role {{ font-size: 8.5pt; letter-spacing: .3em; text-transform: uppercase; color: var(--soft); margin-top: 6px; }}
.t-pub {{ position: absolute; bottom: .8in; left: 0; right: 0; font-family: 'Cinzel'; font-size: 8.5pt; letter-spacing: .3em; color: var(--soft); }}

/* contents */
.contents .live {{ text-align: center; top: 1.05in; }}
.c-title {{ font-family: 'Cinzel'; font-size: 46pt; color: var(--gold2); letter-spacing: .08em; margin-top: 10px; font-weight: 500; }}
.toc {{ list-style: none; margin-top: .45in; text-align: left; }}
.toc li {{ display: grid; grid-template-columns: 1.6in auto 1fr auto; align-items: baseline; gap: 12px;
           padding: 13px 0; border-bottom: 1px solid rgba(201,150,62,.22); }}
.toc small {{ font-family: 'Cinzel'; font-size: 7.5pt; letter-spacing: .24em; text-transform: uppercase; color: var(--gold); }}
.toc span {{ font-family: 'Cormorant'; font-size: 18.5pt; color: #F6EBD8; font-weight: 500; }}
.toc i {{ border-bottom: 1px dotted rgba(226,184,101,.35); transform: translateY(-5px); }}
.toc b {{ font-family: 'Cinzel'; font-size: 13pt; color: var(--gold2); font-weight: 600; }}

/* intro */
.h-page {{ font-family: 'Cinzel'; font-size: 30pt; line-height: 1.12; margin-top: 8px; font-weight: 500; }}
.intro .rule {{ margin: 12px 0 16px; }}
.arch {{ float: right; width: 2.45in; height: 3.75in; margin: 0 0 12px .3in; border-radius: 1.3in 1.3in 6px 6px;
         overflow: hidden; outline: 1px solid var(--gold); outline-offset: 6px; }}
.arch img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%; }}
.intro-text p {{ font-family: 'Cormorant'; font-size: 13.6pt; line-height: 1.46; margin-bottom: 11px; text-align: justify; hyphens: auto; }}
.intro-text .lead {{ font-size: 16pt; font-style: italic; color: var(--fig); line-height: 1.35; text-align: left; }}
.intro-text .lead::first-letter {{ font-family: 'Cinzel'; font-style: normal; float: left; font-size: 46pt; line-height: .9;
     padding: 2px 8px 0 0; color: var(--pumpkin); }}
.sig {{ font-style: italic; text-align: left !important; margin-top: 6px; }}
.sig span {{ font-family: 'Vibes'; font-style: normal; font-size: 32pt; color: var(--pumpkin); display: inline-block; margin-top: 4px; }}

/* chapter openers */
.chapter .ch-text {{ position: absolute; top: .95in; left: .875in; right: .875in; text-align: center; }}
.ch-num {{ font-family: 'Cinzel'; font-size: 10pt; letter-spacing: .45em; text-transform: uppercase; color: var(--gold); }}
.ch-title {{ font-family: 'Cinzel'; font-size: 44pt; line-height: 1.05; color: #F6EBD8; margin: 12px 0 14px; font-weight: 500; }}
.ch-blurb {{ font-family: 'Cormorant'; font-style: italic; font-size: 14.5pt; line-height: 1.42; color: #E6D4B8; max-width: 5in; margin: 14px auto 0; }}
.ch-list {{ list-style: none; max-width: 4.5in; margin: .3in auto 0; text-align: left; }}
.ch-list li {{ display: flex; justify-content: space-between; gap: 12px; font-family: 'Cormorant'; font-size: 13.5pt; color: #F3E6CF;
               padding: 6px 0; border-bottom: 1px solid rgba(201,150,62,.25); }}
.ch-list b {{ font-family: 'Cinzel'; color: var(--gold2); font-size: 11pt; }}
.ch-photo {{ position: absolute; left: 0; right: 0; bottom: 0; height: 3.15in; }}
.ch-photo img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%; }}
.ch-photo::before {{ content: ''; position: absolute; inset: 0 0 auto 0; height: 1.1in; background: linear-gradient(#1A110C, rgba(26,17,12,0)); }}
.ch-arch {{ width: 2.1in; height: 2.6in; margin: .3in auto 0; border-radius: 1.05in 1.05in 6px 6px; overflow: hidden;
            outline: 1px solid var(--gold); outline-offset: 6px; }}
.ch-arch img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 45%; }}
.with-arch .ch-list {{ margin-top: .35in; }}

/* recipe template */
.recipe .live {{ top: 3.62in; }}
.r-photo {{ position: absolute; top: 0; left: 0; right: 0; height: 3.32in; overflow: hidden; border-bottom: 4px solid var(--gold); }}
.r-photo img {{ width: 100%; height: 100%; object-fit: cover; }}
.r-head {{ text-align: center; }}
.r-head .kicker .num {{ display: inline-block; border: 1px solid var(--pumpkin); border-radius: 50%; width: 22px; height: 22px;
                        line-height: 20px; letter-spacing: 0; margin-right: 6px; font-size: 7.5pt; }}
.r-title {{ font-family: 'Cinzel'; font-size: 19pt; line-height: 1.1; margin-top: 6px; font-weight: 600; }}
.recipe .rule {{ margin: 6px auto; width: 2in; }}
.r-intro {{ font-family: 'Cormorant'; font-style: italic; font-size: 12.8pt; line-height: 1.36; color: var(--soft); max-width: 6.3in; margin: 0 auto; text-wrap: balance; }}
.meta {{ display: grid; margin: 10px 0 12px; border-top: 1px solid var(--gold); border-bottom: 1px solid var(--gold); }}
.meta div {{ text-align: center; padding: 6px 0; }}
.meta div + div {{ border-left: 1px solid #E6D3B0; }}
.meta b {{ display: block; font-family: 'Cinzel'; font-size: 6.5pt; letter-spacing: .2em; color: var(--pumpkin); }}
.meta i {{ font-style: normal; font-family: 'Cormorant'; font-size: 12.5pt; font-weight: 600; }}
.r-body {{ display: grid; grid-template-columns: 2.1in 1fr; gap: .28in; }}
.recipe h3 {{ font-family: 'Cinzel'; font-size: 12pt; letter-spacing: .12em; margin-bottom: 5px; color: var(--fig); font-weight: 600; }}
.recipe ul {{ list-style: none; }}
.recipe ul li {{ font-size: 9pt; line-height: 1.35; padding: 3.5px 0 3.5px 13px; position: relative; border-bottom: 1px dotted #DCC9AA; }}
.recipe ul li::before {{ content: ''; position: absolute; left: 0; top: 8.5px; width: 5px; height: 5px; background: var(--gold); transform: rotate(45deg); }}
.need {{ margin-top: 8px; background: var(--sand); border-left: 3px solid var(--gold); padding: 8px 11px; font-size: 8.4pt; line-height: 1.42; }}
.need b {{ display: block; font-family: 'Cormorant'; font-style: italic; font-size: 12pt; color: var(--fig); margin-bottom: 1px; }}
.recipe ol {{ list-style: none; }}
.recipe ol li {{ display: grid; grid-template-columns: 22px 1fr; gap: 6px; margin-bottom: 5px; }}
.recipe ol li span {{ font-family: 'Cinzel'; font-weight: 700; font-size: 13pt; color: var(--pumpkin); line-height: 1.05; }}
.recipe ol li p {{ font-size: 9pt; line-height: 1.4; }}
.recipe ol li strong {{ font-weight: 600; color: var(--ink); }}
@media screen {{ .page {{ margin: 20px auto; box-shadow: 0 4px 30px rgba(0,0,0,.3); }} }}
"""

html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>The Edible Candle Cookbook — '
        f'Interior Sample</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
out = HERE / "build"
out.mkdir(exist_ok=True)
(out / "interior.html").write_text(html, encoding="utf-8")
print("pages", len(pages))
