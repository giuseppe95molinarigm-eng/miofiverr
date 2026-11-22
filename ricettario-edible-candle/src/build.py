"""Builds the Edible Candle Cookbook sample interior (HTML -> PDF via Chromium).

Trim 8 x 10 in, full bleed -> page 8.125 x 10.25 in (KDP spec).
Run:  python3 src/build.py
"""
from pathlib import Path
import illustrations as il

ROOT = Path(__file__).resolve().parent.parent
FONTS = (ROOT.parent / "assets" / "fonts").as_uri()

# ---------------------------------------------------------------- recipes
RECIPES = [
    dict(
        key="garlic", art=il.garlic_herb, chapter="Savory Butter Candles", page=12,
        title="Garlic & Herb Butter Candle",
        intro="The candle that started the trend. Light it ten minutes before guests sit down "
              "and a warm pool of garlicky butter collects at the top, ready for torn bread. "
              "By the end of the meal, the candle has quietly become the appetizer.",
        meta=[("Serves", "6–8"), ("Prep", "15 min"), ("Set", "3 hrs"), ("Burn", "45–60 min")],
        ingredients=[
            ("", "1 cup (2 sticks / 225 g) salted butter, softened"),
            ("", "3 garlic cloves, finely grated"),
            ("", "2 tbsp fresh parsley, minced"),
            ("", "1 tbsp fresh chives, minced"),
            ("", "1 tsp fresh thyme leaves"),
            ("", "½ tsp flaky sea salt"),
            ("", "¼ tsp cracked black pepper"),
            ("To assemble", ""),
            ("", "1 food-safe cotton wick, 6 in"),
            ("", "1 tsp olive oil, to prime the wick"),
            ("", "1 tall 8 oz paper cup, as mold"),
        ],
        method=[
            "Prime the wick by rubbing it with olive oil until fully coated. Set aside on a paper towel.",
            "In a bowl, beat the softened butter with a spatula until smooth and glossy. "
            "Fold in garlic, herbs, salt and pepper until evenly speckled.",
            "Line the mold with parchment. Hold the wick upright in the center with a clothespin "
            "and pack in the butter in three layers, tapping out any air pockets.",
            "Refrigerate for at least 3 hours, or freeze for 1 hour, until completely firm.",
            "Unmold onto a rimmed plate, trim the wick to ¼ in and finish with flaky salt. "
            "Light 10 minutes before serving and dip warm bread into the melted pool.",
        ],
        tip=("Chef’s note", "Make the candle up to 5 days ahead and keep it wrapped in the "
             "fridge. Always blow it out before scooping the last of the butter."),
    ),
    dict(
        key="tallow", art=il.tallow, chapter="Savory Butter Candles", page=13,
        title="Hot Honey Beef Tallow Candle",
        intro="Tallow burns slower and cleaner than butter, so this candle lasts the whole "
              "dinner. As it melts, swirl in a ribbon of chili-spiked honey for a sweet-heat "
              "dip that disappears faster than the bread basket can be refilled.",
        meta=[("Serves", "6"), ("Prep", "20 min"), ("Set", "2 hrs"), ("Burn", "90+ min")],
        ingredients=[
            ("", "1 cup (200 g) rendered beef tallow"),
            ("", "1 sprig fresh rosemary"),
            ("", "1 garlic clove, smashed"),
            ("", "½ tsp smoked sea salt"),
            ("Hot honey", ""),
            ("", "⅓ cup (110 g) runny honey"),
            ("", "1–2 tsp red chili flakes"),
            ("", "1 tsp apple cider vinegar"),
            ("To assemble", ""),
            ("", "1 food-safe cotton wick with metal tab"),
            ("", "1 oven-safe 8 oz ramekin"),
        ],
        method=[
            "Gently melt the tallow with the rosemary and garlic over low heat for 10 minutes "
            "to infuse. Do not let it smoke. Strain and stir in the smoked salt.",
            "Fix the wick tab to the center of the ramekin with a drop of the warm tallow. "
            "Let it set for one minute, then pour in the infused tallow.",
            "Leave at room temperature for 2 hours, or chill for 45 minutes, until opaque and firm.",
            "Meanwhile, warm honey, chili flakes and vinegar for 3 minutes. Cool slightly.",
            "Light the candle at the table. Once a melted pool forms, drizzle in the hot honey "
            "and dip toasted sourdough straight into the ramekin.",
        ],
        tip=("Swap it", "No tallow? Use ghee for a nutty, vegetarian version with the same "
             "long, steady burn."),
    ),
    dict(
        key="cocoa", art=il.cocoa, chapter="Sweet Dipping Candles", page=34,
        title="Vanilla Bean Cocoa Butter Candle",
        intro="A dessert you light instead of plate. Pure cocoa butter melts into a silky, "
              "white-chocolate-scented dip for strawberries, shortbread and salted pretzels. "
              "Flecked with real vanilla, it looks as good on the table as it tastes.",
        meta=[("Serves", "4–6"), ("Prep", "15 min"), ("Set", "2 hrs"), ("Burn", "40–50 min")],
        ingredients=[
            ("", "¾ cup (150 g) food-grade cocoa butter wafers"),
            ("", "2 tbsp refined coconut oil"),
            ("", "1 vanilla bean, seeds scraped"),
            ("", "Pinch of flaky sea salt"),
            ("For dipping", ""),
            ("", "1 lb (450 g) fresh strawberries"),
            ("", "Shortbread, pretzels or biscotti"),
            ("To assemble", ""),
            ("", "1 food-safe cotton wick, 6 in"),
            ("", "1 short 6 oz glass or silicone mold"),
        ],
        method=[
            "Melt the cocoa butter and coconut oil in a heatproof bowl set over barely "
            "simmering water, stirring until clear and fluid.",
            "Remove from the heat and whisk in the vanilla seeds and salt. Let cool for "
            "8–10 minutes, stirring often, until slightly thickened so the seeds stay suspended.",
            "Center the wick in the mold and pour in the mixture. Tap gently to settle.",
            "Chill for 2 hours until completely firm, then unmold onto a serving board.",
            "Light the candle and arrange the fruit and biscuits around it. Dip once a "
            "warm pool has formed, about 8 minutes.",
        ],
        tip=("Keep it neat", "Trim the wick to ¼ in before every lighting. A short flame "
             "melts the cocoa butter gently without scorching the vanilla."),
    ),
    dict(
        key="banana", art=il.banana, chapter="Sweet Dipping Candles", page=35,
        title="Banana & Almond Trick Candles",
        intro="The party trick every kid (and grown-up) asks for again. A banana “candle” "
              "with a sliver of almond as its wick really does burn for a minute or two, "
              "thanks to the natural oil in the nut. Blow it out, then eat the whole thing.",
        meta=[("Serves", "4"), ("Prep", "10 min"), ("Set", "None"), ("Burn", "1–2 min")],
        ingredients=[
            ("", "2 firm, just-ripe bananas"),
            ("", "4 raw almond slivers (not toasted)"),
            ("", "½ lemon, juiced"),
            ("Chocolate drizzle", ""),
            ("", "3 oz (85 g) dark chocolate, chopped"),
            ("", "3 tbsp heavy cream"),
            ("", "Pinch of cinnamon"),
        ],
        method=[
            "Peel the bananas and cut each into two pieces with flat ends, 3–4 in tall. "
            "Brush with lemon juice to keep them bright.",
            "Stand the pieces upright on a serving plate. With a skewer, make a small hole "
            "in the top of each and press in an almond sliver, leaving ¼ in exposed.",
            "Warm the cream until steaming, pour over the chocolate and cinnamon, wait "
            "1 minute and stir until glossy.",
            "Dim the lights, light the almond “wicks” with a long match and let them flicker. "
            "Blow out, drizzle with chocolate and serve immediately.",
        ],
        tip=("Allergy note", "Contains tree nuts. For a nut-free version, use a thin strip "
             "of coconut flesh, which burns briefly in the same way."),
    ),
]

TOC = [
    ("Welcome to the Edible Candle Table", 4),
    ("Before You Light: Tools & Safety", 5),
    ("The Base Method in Four Steps", 6),
    ("Savory Butter Candles", 11),
    ("Sweet Dipping Candles", 33),
    ("Cheese, Tallow & Holiday Candles", 55),
    ("Boards, Breads & Pairings", 77),
    ("Measurement Conversions", 96),
    ("Index", 98),
]


# ---------------------------------------------------------------- helpers
def folio(n, side):
    return f'<div class="folio {side}"><span>{n}</span><em>The Edible Candle Cookbook</em></div>'


def page(content, side, cls="", n=None):
    f = folio(n, side) if n else ""
    return f'<section class="page {side} {cls}"><div class="live">{content}</div>{f}</section>'


def recipe_page(r, side):
    n = r["page"]
    ings = []
    for head, txt in r["ingredients"]:
        if head:
            ings.append(f'<li class="sub">{head}</li>')
        else:
            ings.append(f"<li>{txt}</li>")
    steps = "".join(f"<li><span>{i}</span><p>{s}</p></li>" for i, s in enumerate(r["method"], 1))
    meta = "".join(f"<div><b>{k}</b><i>{v}</i></div>" for k, v in r["meta"])
    body = f"""
    <div class="r-head">
      <p class="kicker">{r['chapter']}</p>
      <h2>{r['title']}</h2>
      {il.ornament()}
    </div>
    <figure class="r-art">{r['art']()}</figure>
    <p class="r-intro">{r['intro']}</p>
    <div class="meta">{meta}</div>
    <div class="r-body">
      <div class="ing"><h3>Ingredients</h3><ul>{''.join(ings)}</ul></div>
      <div class="met"><h3>Method</h3><ol>{steps}</ol>
        <aside class="tip"><b>{r['tip'][0]}</b> {r['tip'][1]}</aside></div>
    </div>"""
    return page(body, side, "recipe", n)


def chapter_page(num, title, blurb, recipes, art):
    items = "".join(f"<li><span>{t}</span><i></i><b>{p}</b></li>" for t, p in recipes)
    body = f"""
    <div class="ch-num">Chapter {num}</div>
    <h1 class="ch-title">{title}</h1>
    {il.ornament('#E7C47A')}
    <p class="ch-blurb">{blurb}</p>
    <div class="ch-art">{art}</div>
    <ul class="ch-list">{items}</ul>"""
    return page(body, "recto", "chapter")


# ---------------------------------------------------------------- pages
pages = []

# 1  title page (recto)
pages.append(page(f"""
  <div class="tp">
    <p class="tp-pre">Light it. Dip it. Devour it.</p>
    <div class="tp-art">{il.candle_small()}</div>
    <h1>The Edible<br>Candle<br><span>Cookbook</span></h1>
    {il.ornament()}
    <p class="tp-sub">60 Butter, Chocolate &amp; Tallow Candles<br>to Light Up Every Table</p>
    <p class="tp-author">Eleanor Hart</p>
  </div>""", "recto", "title"))

# 2  copyright (verso)
pages.append(page("""
  <div class="copy">
    <p><b>The Edible Candle Cookbook</b><br>60 Butter, Chocolate &amp; Tallow Candles to Light Up Every Table</p>
    <p>Copyright © 2026 Eleanor Hart. All rights reserved.</p>
    <p>No part of this publication may be reproduced, distributed or transmitted in any form or by any
    means, including photocopying, recording or other electronic or mechanical methods, without the prior
    written permission of the publisher, except for brief quotations in reviews.</p>
    <p><b>Safety disclaimer.</b> Edible candles involve an open flame. Never leave a lit candle unattended,
    keep it away from children, pets and flammable materials, and always place it on a heat-resistant
    plate. Use only untreated, food-safe cotton wicks and remove the wick before eating. The author and
    publisher accept no liability for injury or damage arising from the use of this book.</p>
    <p>Paperback ISBN: 000-0-00000-000-0<br>Hardcover ISBN: 000-0-00000-000-0</p>
    <p>Interior design &amp; formatting: Giuseppe Molinari<br>Illustrations: vector artwork</p>
    <p>First edition</p>
    <p class="sample">Sample interior · portfolio piece · fictional author</p>
  </div>""", "verso", "copyright"))

# 3  contents (recto)
toc = "".join(f'<li><span>{t}</span><i></i><b>{p}</b></li>' for t, p in TOC)
pages.append(page(f"""
  <h1 class="pg-title">Contents</h1>{il.ornament()}
  <ul class="toc">{toc}</ul>
  <div class="toc-art">{il.candle_small('#F7EBD2', '#E8D3AC', 'toc')}</div>
""", "recto", "contents", 3))

# 4  welcome (verso)
pages.append(page(f"""
  <p class="kicker">Introduction</p>
  <h1 class="pg-title left">Welcome to the<br>Edible Candle Table</h1>
  <div class="two-col dropcap">
    <p>There is a moment at every good dinner when the conversation slows and everyone reaches
    for the bread. This book is about that moment, and about making it glow.</p>
    <p>An edible candle is exactly what it sounds like: a candle shaped from butter, tallow,
    cocoa butter or another food-grade fat, set around a food-safe wick. Lit at the table, it
    melts into a warm, fragrant pool that becomes a dip. What starts as decoration ends as the
    most talked-about course of the evening.</p>
    <p>Edible candles are surprisingly simple. Most need fewer than six ingredients, a paper cup
    for a mold and a few hours in the fridge. Once you know the base method on page 6, you can
    flavor them for any season: herby and garlicky for a spring supper, smoky and spiced for a
    winter roast, sweet and vanilla-scented for dessert.</p>
    <p>Every recipe in these pages has been tested for flavor, for how cleanly it burns and for
    how long it lasts on the table. You will find burn times, make-ahead notes and pairing ideas
    alongside each one.</p>
    <p class="sig">Light one tonight. You’ll see.<br><span>Eleanor</span></p>
  </div>
  <figure class="intro-art">{il.garlic_herb()}<figcaption>The Garlic &amp; Herb Butter Candle, page 12</figcaption></figure>
""", "verso", "intro", 4))

# 5  tools & safety (recto)
pages.append(page(f"""
  <p class="kicker">Before You Light</p>
  <h1 class="pg-title left">Tools &amp; Safety</h1>
  <div class="tools">
    <div><h3>Food-safe wicks</h3><p>Choose 100% unbleached cotton wicks with no wax coating,
      dyes or metal core. Prime with olive oil before use.</p></div>
    <div><h3>Simple molds</h3><p>Paper cups, short glasses, ramekins or silicone molds. Line
      paper and glass with parchment for a clean release.</p></div>
    <div><h3>A steady base</h3><p>Always serve on a rimmed, heat-resistant plate or board
      that can catch the melting pool.</p></div>
    <div><h3>Long matches</h3><p>A long match or lighter keeps hands clear of the soft
      surface and lets you relight easily.</p></div>
  </div>
  <div class="rules">
    <h3>The five golden rules</h3>
    <ol>
      <li><b>Never leave it alone.</b> A lit candle is supervised from first spark to last dip.</li>
      <li><b>Trim to ¼ in.</b> A short wick gives a small, clean flame that melts rather than burns.</li>
      <li><b>Blow out before you dip.</b> Or dip from the outer edge, away from the flame.</li>
      <li><b>Discard the wick.</b> It is never eaten. Pull it out with tongs once cool.</li>
      <li><b>Mind allergies.</b> Label nut and dairy candles when guests are sharing.</li>
    </ol>
  </div>
""", "recto", "safety", 5))

# 6  base method (verso)
steps = [
    ("Soften & flavor", "Beat room-temperature fat until smooth, then fold in herbs, spices or sweeteners."),
    ("Set the wick", "Center a primed wick in the mold and hold it upright with a clothespin."),
    ("Pack & chill", "Fill in layers, tap out air pockets and chill until completely firm."),
    ("Unmold & light", "Release onto a plate, trim the wick and light 10 minutes before serving."),
]
stp = "".join(
    f'<div class="step"><div class="step-art">{il.method_step(i)}</div><span>{i:02d}</span>'
    f'<h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps, 1))
pages.append(page(f"""
  <p class="kicker">Master this once</p>
  <h1 class="pg-title left">The Base Method<br>in Four Steps</h1>
  <p class="lead">Every candle in this book follows the same four steps. Learn them here and
  each recipe becomes a simple change of flavor.</p>
  <div class="steps">{stp}</div>
  <table class="burn">
    <thead><tr><th>Base fat</th><th>Texture when set</th><th>Burn time*</th><th>Best for</th></tr></thead>
    <tbody>
      <tr><td>Butter</td><td>Soft, spreadable</td><td>45–60 min</td><td>Bread, crackers</td></tr>
      <tr><td>Beef tallow</td><td>Firm, waxy</td><td>90+ min</td><td>Sourdough, roasts</td></tr>
      <tr><td>Ghee</td><td>Firm, grainy</td><td>75–90 min</td><td>Flatbreads, naan</td></tr>
      <tr><td>Cocoa butter</td><td>Hard, snappy</td><td>40–50 min</td><td>Fruit, cookies</td></tr>
    </tbody>
  </table>
  <p class="foot">*Based on an 8 oz candle with a ¼ in wick at room temperature.</p>
""", "verso", "method", 6))

# 7  chapter 1 (recto)
pages.append(chapter_page(1, "Savory Butter Candles",
    "Garlic, herbs, cheese and spice, set around a wick and served with the warmest bread "
    "you can find. These are the candles that steal the dinner party.",
    [("Garlic & Herb Butter Candle", 12), ("Hot Honey Beef Tallow Candle", 13),
     ("Parmesan & Sun-Dried Tomato Candle", 15), ("Brown Butter & Sage Candle", 16),
     ("Truffle & Chive Candle", 17), ("Everything Bagel Candle", 18)],
    il.candle_small("#F6D98A", "#E9BE5C", "c1")))

# 8-9  recipes (verso / recto)
pages.append(recipe_page(RECIPES[0], "verso"))
pages.append(recipe_page(RECIPES[1], "recto"))

# 10  full-width art page (verso) - parmesan feature
pages.append(page(f"""
  <figure class="feature-art">{il.parmesan()}</figure>
  <p class="kicker center">From the next pages</p>
  <h2 class="center feature">Parmesan &amp; Sun-Dried Tomato Candle</h2>
  {il.ornament()}
  <p class="center quote">“Two candles, one board, and a crowd around the table who forgot
  there was a main course coming.”</p>
""", "verso", "feature", 14))

# 11  chapter 2 (recto)
pages.append(chapter_page(2, "Sweet Dipping Candles",
    "Cocoa butter, vanilla, caramel and fruit. Light them after dinner and let dessert "
    "melt into a dip right in front of your guests.",
    [("Vanilla Bean Cocoa Butter Candle", 34), ("Banana & Almond Trick Candles", 35),
     ("Salted Caramel Candle", 36), ("Cinnamon Roll Candle", 37),
     ("Orange & Cardamom Candle", 38), ("Peppermint Bark Candle", 39)],
    il.candle_small("#F7EBD2", "#E8D3AC", "c2")))

# 12-13 recipes
pages.append(recipe_page(RECIPES[2], "verso"))
pages.append(recipe_page(RECIPES[3], "recto"))

# 14 conversions (verso)
pages.append(page("""
  <p class="kicker">Kitchen reference</p>
  <h1 class="pg-title left">Measurement Conversions</h1>
  <div class="conv">
    <table><thead><tr><th colspan="3">Volume</th></tr></thead><tbody>
      <tr><td>1 tsp</td><td>5 ml</td><td></td></tr>
      <tr><td>1 tbsp</td><td>15 ml</td><td>3 tsp</td></tr>
      <tr><td>¼ cup</td><td>60 ml</td><td>4 tbsp</td></tr>
      <tr><td>⅓ cup</td><td>80 ml</td><td>5⅓ tbsp</td></tr>
      <tr><td>½ cup</td><td>120 ml</td><td>8 tbsp</td></tr>
      <tr><td>1 cup</td><td>240 ml</td><td>16 tbsp</td></tr></tbody></table>
    <table><thead><tr><th colspan="3">Fats by weight</th></tr></thead><tbody>
      <tr><td>Butter, 1 stick</td><td>½ cup</td><td>113 g</td></tr>
      <tr><td>Butter, 1 cup</td><td>2 sticks</td><td>225 g</td></tr>
      <tr><td>Tallow, 1 cup</td><td></td><td>200 g</td></tr>
      <tr><td>Ghee, 1 cup</td><td></td><td>205 g</td></tr>
      <tr><td>Cocoa butter, 1 cup</td><td></td><td>200 g</td></tr>
      <tr><td>Coconut oil, 1 cup</td><td></td><td>215 g</td></tr></tbody></table>
    <table><thead><tr><th colspan="3">Temperatures</th></tr></thead><tbody>
      <tr><td>Butter melts</td><td>90–95 °F</td><td>32–35 °C</td></tr>
      <tr><td>Cocoa butter melts</td><td>93–100 °F</td><td>34–38 °C</td></tr>
      <tr><td>Tallow melts</td><td>104–122 °F</td><td>40–50 °C</td></tr>
      <tr><td>Fridge</td><td>37–40 °F</td><td>3–4 °C</td></tr></tbody></table>
    <table><thead><tr><th colspan="3">Mold sizes</th></tr></thead><tbody>
      <tr><td>Paper cup, 8 oz</td><td>1 cup fat</td><td>6–8 servings</td></tr>
      <tr><td>Ramekin, 8 oz</td><td>1 cup fat</td><td>6 servings</td></tr>
      <tr><td>Short glass, 6 oz</td><td>¾ cup fat</td><td>4–6 servings</td></tr>
      <tr><td>Mini mold, 2 oz</td><td>¼ cup fat</td><td>1–2 servings</td></tr></tbody></table>
  </div>
""", "verso", "conversions", 96))

# ---------------------------------------------------------------- css
CSS = f"""
@font-face {{ font-family: 'Cormorant'; src: url('{FONTS}/CormorantGaramond.ttf'); font-weight: 300 700; }}
@font-face {{ font-family: 'Cormorant'; src: url('{FONTS}/CormorantGaramond-Italic.ttf'); font-style: italic; font-weight: 300 700; }}
@font-face {{ font-family: 'Jost'; src: url('{FONTS}/Jost.ttf'); font-weight: 100 900; }}
@font-face {{ font-family: 'Vibes'; src: url('{FONTS}/GreatVibes-Regular.ttf'); }}

@page {{ size: 8.125in 10.25in; margin: 0; }}
:root {{ --ink:#3B2418; --soft:#6B5446; --gold:#B8893B; --ember:#A8432A; --paper:#FFFCF6; --cream:#F6EEDF; --night:#2A1A12; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: #888; }}
body {{ font-family: 'Jost', sans-serif; color: var(--ink); -webkit-print-color-adjust: exact; print-color-adjust: exact; }}

.page {{ width: 8.125in; height: 10.25in; position: relative; overflow: hidden; background: var(--paper);
        page-break-after: always; break-after: page; }}
/* live area: bleed .125 on outer/top/bottom, gutter .875in, outer .75in */
.page .live {{ position: absolute; top: .875in; bottom: 1in; }}
.page.recto .live {{ left: .875in; right: .875in; }}
.page.verso .live {{ left: .875in; right: .875in; }}
.recto .live {{ left: .875in !important; right: .875in !important; }}

.folio {{ position: absolute; bottom: .55in; font-size: 8.5pt; letter-spacing: .14em; color: var(--soft);
          display: flex; gap: 10px; align-items: baseline; text-transform: uppercase; }}
.folio span {{ font-family: 'Cormorant'; font-weight: 600; font-size: 12pt; color: var(--ember); letter-spacing: 0; }}
.folio em {{ font-style: normal; }}
.folio.recto {{ right: .875in; flex-direction: row-reverse; }}
.folio.verso {{ left: .875in; }}

.orn {{ width: 1.9in; height: auto; display: block; margin: 8px auto 0; }}
.kicker {{ font-size: 8.5pt; letter-spacing: .28em; text-transform: uppercase; color: var(--ember); font-weight: 500; }}
.center {{ text-align: center; }}
h1, h2, h3 {{ font-family: 'Cormorant'; font-weight: 600; line-height: 1.02; }}
.pg-title {{ font-size: 40pt; text-align: center; margin-top: .3in; }}
.pg-title.left {{ text-align: left; margin: 6px 0 18px; font-size: 34pt; }}

/* title page */
.title .live {{ display: flex; align-items: center; justify-content: center; text-align: center; }}
.tp-pre {{ font-family: 'Cormorant'; font-style: italic; font-size: 15pt; color: var(--soft); }}
.tp-art svg {{ width: 1.6in; height: 1.6in; margin: .2in auto .1in; display: block; }}
.tp h1 {{ font-size: 64pt; line-height: .92; letter-spacing: -.01em; }}
.tp h1 span {{ font-family: 'Vibes'; font-weight: 400; font-size: 66pt; color: var(--ember); display: block; margin-top: 6px; }}
.tp-sub {{ font-family: 'Cormorant'; font-size: 17pt; margin-top: 16px; line-height: 1.25; }}
.tp-author {{ margin-top: 1.1in; font-size: 11pt; letter-spacing: .4em; text-transform: uppercase; }}

/* copyright */
.copyright .live {{ display: flex; flex-direction: column; justify-content: flex-end; }}
.copy p {{ font-size: 8.5pt; line-height: 1.55; color: var(--soft); margin-top: 10px; max-width: 4.6in; }}
.copy b {{ color: var(--ink); font-weight: 500; }}
.copy .sample {{ margin-top: 18px; font-style: italic; font-family: 'Cormorant'; font-size: 10pt; }}

/* toc */
.toc, .ch-list {{ list-style: none; margin-top: .45in; }}
.toc li, .ch-list li {{ display: flex; align-items: baseline; gap: 10px; padding: 9px 0; }}
.toc li span {{ font-family: 'Cormorant'; font-size: 17pt; font-weight: 500; }}
.toc li i, .ch-list li i {{ flex: 1; border-bottom: 1px dotted #C9B9A3; transform: translateY(-4px); }}
.toc li b {{ font-family: 'Cormorant'; font-size: 16pt; color: var(--ember); font-weight: 600; }}
.toc-art svg {{ width: 1.2in; height: 1.2in; display: block; margin: .35in auto 0; }}

/* intro */
.two-col {{ columns: 2; column-gap: .35in; margin-top: 10px; }}
.two-col p {{ font-family: 'Cormorant'; font-size: 13.2pt; line-height: 1.42; margin-bottom: 10px; text-align: justify; hyphens: auto; }}
.dropcap p:first-child::first-letter {{ float: left; font-size: 58pt; line-height: .8; padding: 4px 8px 0 0; color: var(--ember); font-weight: 600; }}
.sig {{ font-style: italic; text-align: left !important; }}
.sig span {{ font-family: 'Vibes'; font-size: 28pt; color: var(--ember); font-style: normal; display: inline-block; margin-top: 6px; }}

.intro-art {{ margin-top: 14px; background: var(--cream); border-radius: 8px; padding: 10px 0 8px; text-align: center; }}
.intro-art svg {{ height: 1.85in; width: auto; }}
.intro-art figcaption {{ font-family: 'Cormorant'; font-style: italic; font-size: 11pt; color: var(--soft); }}
/* tools */
.tools {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 6px; }}
.tools div {{ background: var(--cream); border-radius: 6px; padding: 20px 20px; }}
.tools h3, .rules h3 {{ font-size: 17pt; margin-bottom: 4px; }}
.tools p {{ font-size: 10.5pt; line-height: 1.5; color: var(--soft); }}
.rules {{ margin-top: .3in; border-top: 1px solid var(--gold); padding-top: 16px; }}
.rules ol {{ list-style: none; counter-reset: r; margin-top: 8px; }}
.rules li {{ counter-increment: r; position: relative; padding: 15px 0 15px 44px; font-size: 11pt; line-height: 1.5;
             border-bottom: 1px solid #EDE3D3; }}
.rules li::before {{ content: counter(r); position: absolute; left: 0; top: 8px; font-family: 'Cormorant'; font-size: 24pt;
                     font-weight: 600; color: var(--ember); }}
.rules b {{ font-weight: 600; }}

/* method */
.lead {{ font-family: 'Cormorant'; font-size: 14pt; line-height: 1.4; font-style: italic; color: var(--soft); }}
.steps {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: .25in 0 .3in; }}
.step {{ text-align: center; }}
.step-art svg {{ width: 1.15in; height: 1.15in; background: var(--cream); border-radius: 50%; padding: 8px; }}
.step span {{ display: block; font-family: 'Cormorant'; font-size: 13pt; color: var(--ember); font-weight: 600; margin-top: 6px; }}
.step h3 {{ font-size: 15pt; margin: 2px 0 4px; }}
.step p {{ font-size: 9.4pt; line-height: 1.45; color: var(--soft); }}
table {{ border-collapse: collapse; width: 100%; }}
.burn th {{ font-size: 8pt; letter-spacing: .14em; text-transform: uppercase; text-align: left; padding: 8px 10px;
            background: var(--night); color: #F3E3C3; font-weight: 500; }}
.burn td {{ font-size: 10pt; padding: 11px 10px; border-bottom: 1px solid #E8DCCA; }}
.burn tr:nth-child(even) td {{ background: var(--cream); }}
.foot {{ font-size: 8pt; color: var(--soft); margin-top: 6px; font-style: italic; }}

/* chapter openers: full bleed dark */
.chapter {{ background: var(--night); color: #F6EAD3; }}
.chapter .live {{ text-align: center; }}
.chapter::before {{ content: ''; position: absolute; inset: 0;
   background: radial-gradient(circle at 50% 52%, rgba(244,162,59,.28), rgba(42,26,18,0) 45%); }}
.ch-num {{ margin-top: .2in; font-size: 9pt; letter-spacing: .4em; text-transform: uppercase; color: #E7C47A; }}
.ch-title {{ font-size: 50pt; margin-top: 14px; }}
.ch-blurb {{ font-family: 'Cormorant'; font-style: italic; font-size: 14pt; line-height: 1.4; max-width: 4.6in; margin: 16px auto 0; color: #E9D9BC; }}
.ch-art svg {{ width: 1.9in; height: 1.9in; margin: .25in auto 0; display: block; }}
.ch-list {{ margin: .2in auto 0; max-width: 4.6in; text-align: left; }}
.ch-list li {{ padding: 6px 0; }}
.ch-list li span {{ font-family: 'Cormorant'; font-size: 13.2pt; }}
.ch-list li i {{ border-color: rgba(231,196,122,.45); }}
.ch-list li b {{ font-family: 'Cormorant'; color: #E7C47A; font-size: 13pt; }}

/* recipe */
.recipe .live {{ top: .75in; }}
.r-head {{ text-align: center; }}
.r-head h2 {{ font-size: 31pt; margin-top: 6px; }}
.r-head .orn {{ margin-top: 6px; }}
.r-art {{ margin: 8px -0.1in 0; height: 2.25in; background: var(--cream); border-radius: 8px; display: flex; align-items: center; justify-content: center; }}
.r-art svg {{ height: 2.15in; width: auto; }}
.r-intro {{ font-family: 'Cormorant'; font-style: italic; font-size: 12.5pt; line-height: 1.38; text-align: center;
            margin: 12px .15in 10px; color: var(--soft); }}
.meta {{ display: grid; grid-template-columns: repeat(4, 1fr); border-top: 1px solid var(--gold); border-bottom: 1px solid var(--gold); }}
.meta div {{ text-align: center; padding: 7px 0; }}
.meta div + div {{ border-left: 1px solid #E5D6BC; }}
.meta b {{ display: block; font-size: 7pt; letter-spacing: .24em; text-transform: uppercase; color: var(--ember); font-weight: 500; }}
.meta i {{ font-style: normal; font-family: 'Cormorant'; font-size: 14pt; font-weight: 600; }}
.r-body {{ display: grid; grid-template-columns: 2.05in 1fr; gap: .28in; margin-top: 14px; }}
.r-body h3 {{ font-size: 17pt; margin-bottom: 6px; }}
.ing ul {{ list-style: none; }}
.ing li {{ font-size: 9.2pt; line-height: 1.38; padding: 3.5px 0 3.5px 12px; position: relative; border-bottom: 1px dotted #DCCDB5; }}
.ing li::before {{ content: ''; position: absolute; left: 0; top: 9.5px; width: 4px; height: 4px; border-radius: 50%; background: var(--gold); }}
.ing li.sub {{ font-family: 'Cormorant'; font-style: italic; font-size: 12pt; font-weight: 600; color: var(--ember); border: 0; padding: 8px 0 1px; }}
.ing li.sub::before {{ display: none; }}
.met ol {{ list-style: none; }}
.met li {{ display: grid; grid-template-columns: 22px 1fr; gap: 6px; margin-bottom: 6px; }}
.met li span {{ font-family: 'Cormorant'; font-weight: 700; font-size: 15pt; color: var(--ember); line-height: 1; }}
.met li p {{ font-size: 9.2pt; line-height: 1.45; }}
.tip {{ margin-top: 10px; font-size: 8.9pt !important; background: var(--cream); border-left: 3px solid var(--gold); padding: 8px 12px; font-size: 8.6pt; line-height: 1.45; }}
.tip b {{ font-family: 'Cormorant'; font-style: italic; font-size: 12pt; color: var(--ember); }}

/* feature */
.feature .live {{ display: flex; flex-direction: column; justify-content: center; }}
.feature-art {{ background: var(--cream); border-radius: 10px; padding: .25in; margin-bottom: .35in; }}
.feature-art svg {{ width: 100%; height: auto; }}
h2.feature {{ font-size: 32pt; margin-top: 8px; }}
.quote {{ font-family: 'Cormorant'; font-style: italic; font-size: 15pt; line-height: 1.4; color: var(--soft); max-width: 4.8in; margin: 16px auto 0; }}

/* conversions */
.conv {{ display: grid; grid-template-columns: 1fr 1fr; gap: .45in .3in; margin-top: 6px; }}
.conv th {{ font-family: 'Cormorant'; font-size: 16pt; text-align: left; padding-bottom: 6px; border-bottom: 2px solid var(--gold); font-weight: 600; }}
.conv td {{ font-size: 10pt; padding: 10px 4px; border-bottom: 1px solid #EADFCD; }}
.conv td:last-child {{ text-align: right; color: var(--soft); }}

@media screen {{ .page {{ margin: 20px auto; box-shadow: 0 4px 30px rgba(0,0,0,.25); }} }}
"""

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>The Edible Candle Cookbook — Sample Interior</title><style>{CSS}</style></head>
<body>{''.join(pages)}</body></html>"""

out = ROOT / "build"
out.mkdir(exist_ok=True)
(out / "edible-candle-cookbook.html").write_text(html, encoding="utf-8")
print("pages:", len(pages))
