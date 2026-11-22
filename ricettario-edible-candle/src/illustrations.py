"""Hand-built SVG illustrations for the Edible Candle Cookbook sample.

Every drawing is vector, so it prints sharp at any size (KDP needs 300 DPI
for raster art; vectors sidestep that entirely).
"""

INK = "#3B2418"


def flame(cx, top, h=46, uid="f"):
    w = h * 0.42
    return f"""
  <defs>
    <radialGradient id="glow-{uid}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFD27A" stop-opacity=".55"/>
      <stop offset="100%" stop-color="#FFD27A" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="fl-{uid}" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="#E8572A"/>
      <stop offset="45%" stop-color="#F4A23B"/>
      <stop offset="100%" stop-color="#FFE7A3"/>
    </linearGradient>
  </defs>
  <circle cx="{cx}" cy="{top + h*0.55}" r="{h*1.5}" fill="url(#glow-{uid})"/>
  <path d="M{cx},{top} C{cx + w*0.9},{top + h*0.45} {cx + w},{top + h*0.8} {cx},{top + h}
           C{cx - w},{top + h*0.8} {cx - w*0.9},{top + h*0.45} {cx},{top} Z"
        fill="url(#fl-{uid})" stroke="{INK}" stroke-width="1.6"/>
  <path d="M{cx},{top + h*0.45} C{cx + w*0.35},{top + h*0.65} {cx + w*0.35},{top + h*0.85} {cx},{top + h*0.92}
           C{cx - w*0.35},{top + h*0.85} {cx - w*0.35},{top + h*0.65} {cx},{top + h*0.45} Z"
        fill="#FFF6D6" opacity=".9"/>
  <line x1="{cx}" y1="{top + h*0.92}" x2="{cx}" y2="{top + h + 10}" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>
"""


def leaf(x, y, rot, s=1.0, fill="#7C9A5B"):
    return f"""<g transform="translate({x},{y}) rotate({rot}) scale({s})">
    <path d="M0,0 C8,-10 26,-10 34,0 C26,10 8,10 0,0 Z" fill="{fill}" stroke="{INK}" stroke-width="1.3"/>
    <line x1="2" y1="0" x2="30" y2="0" stroke="{INK}" stroke-width=".9"/></g>"""


def sprig(x, y, rot, n=5, fill="#7C9A5B"):
    parts = [f'<g transform="translate({x},{y}) rotate({rot})">',
             f'<path d="M0,0 L0,-{n*14+6}" stroke="{INK}" stroke-width="1.4" fill="none"/>']
    for i in range(n):
        yy = -(i * 14 + 8)
        parts.append(leaf(0, yy, -40, .55, fill))
        parts.append(leaf(0, yy - 5, -140, .55, fill))
    parts.append("</g>")
    return "".join(parts)


def plate(cx, cy, rx=150, ry=22, fill="#F4EDE1"):
    return f"""<ellipse cx="{cx}" cy="{cy+6}" rx="{rx}" ry="{ry}" fill="#000" opacity=".06"/>
  <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{INK}" stroke-width="1.8"/>
  <ellipse cx="{cx}" cy="{cy-3}" rx="{rx*0.72}" ry="{ry*0.6}" fill="none" stroke="{INK}" stroke-width="1" opacity=".45"/>"""


def pillar(cx, base, w, h, body, shade, uid, drips=True, specks=None):
    top = base - h
    x0, x1 = cx - w / 2, cx + w / 2
    drip = ""
    if drips:
        drip = f"""<path d="M{x0},{top+8} Q{x0+w*0.12},{top+30} {x0+w*0.18},{top+8}
          Q{x0+w*0.30},{top+46} {x0+w*0.40},{top+8}
          Q{x0+w*0.62},{top+24} {x0+w*0.72},{top+8}
          Q{x0+w*0.84},{top+38} {x1},{top+8}" fill="{body}" stroke="{INK}" stroke-width="1.4"/>"""
    sp = ""
    if specks:
        import random
        r = random.Random(uid)
        for _ in range(specks[1]):
            sx = r.uniform(x0 + 6, x1 - 6)
            sy = r.uniform(top + 18, base - 8)
            sp += f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{r.uniform(1.1,2.4):.1f}" fill="{specks[0]}"/>'
    return f"""
  <rect x="{x0}" y="{top}" width="{w}" height="{h}" rx="7" fill="{body}" stroke="{INK}" stroke-width="1.8"/>
  <rect x="{x1 - w*0.22}" y="{top+6}" width="{w*0.16}" height="{h-12}" rx="4" fill="{shade}" opacity=".55"/>
  <rect x="{x0 + w*0.1}" y="{top+10}" width="{w*0.06}" height="{h*0.6}" rx="3" fill="#fff" opacity=".45"/>
  {sp}
  <ellipse cx="{cx}" cy="{top+4}" rx="{w/2-2}" ry="7" fill="{shade}" stroke="{INK}" stroke-width="1.4"/>
  {drip}
"""


def bread(x, y, rot=0):
    return f"""<g transform="translate({x},{y}) rotate({rot})">
  <path d="M0,0 C4,-26 70,-30 78,-4 C80,6 74,12 64,12 L10,12 C2,12 -2,6 0,0 Z" fill="#D9A15B" stroke="{INK}" stroke-width="1.6"/>
  <path d="M6,6 C14,-8 62,-10 72,2" fill="none" stroke="#F6E2BC" stroke-width="5" stroke-linecap="round" opacity=".8"/>
  <path d="M20,-10 l8,6 M36,-14 l8,6 M52,-12 l8,6" stroke="{INK}" stroke-width="1.3" stroke-linecap="round"/></g>"""


def svg(inner, w=520, h=300):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
            f'role="img" preserveAspectRatio="xMidYMid meet">{inner}</svg>')


def garlic_herb():
    cx, base = 260, 250
    g = plate(cx, base + 4, 190, 26)
    g += bread(70, base - 14, -8) + bread(385, base - 12, 6)
    g += pillar(cx, base, 120, 150, "#F6D98A", "#E9BE5C", "gh", specks=("#5E7B3E", 38))
    g += flame(cx, base - 150 - 58, 46, "gh")
    g += sprig(150, base - 20, -18, 5) + sprig(372, base - 18, 22, 4)
    g += f'<circle cx="205" cy="{base+2}" r="9" fill="#F7F1E3" stroke="{INK}" stroke-width="1.4"/>'
    g += f'<circle cx="320" cy="{base+4}" r="7" fill="#F7F1E3" stroke="{INK}" stroke-width="1.4"/>'
    return svg(g)


def tallow():
    cx, base = 260, 250
    g = plate(cx, base + 4, 180, 24, "#EFE4D4")
    # ramekin
    g += f"""<path d="M{cx-95},{base-110} L{cx-85},{base} L{cx+85},{base} L{cx+95},{base-110} Z" fill="#B84A3A" stroke="{INK}" stroke-width="1.8"/>
    <path d="M{cx-88},{base-90} L{cx+88},{base-90} M{cx-86},{base-70} L{cx+86},{base-70} M{cx-84},{base-50} L{cx+84},{base-50} M{cx-82},{base-30} L{cx+82},{base-30}" stroke="#8E3328" stroke-width="2.2" opacity=".6"/>
    <ellipse cx="{cx}" cy="{base-110}" rx="95" ry="14" fill="#F2EAD9" stroke="{INK}" stroke-width="1.8"/>
    <ellipse cx="{cx}" cy="{base-110}" rx="70" ry="8" fill="#F8C24E" opacity=".8"/>
    <path d="M{cx-40},{base-112} q14,-6 28,0 q14,6 28,0" stroke="#D9861E" stroke-width="2.2" fill="none"/>"""
    g += flame(cx, base - 110 - 62, 50, "tl")
    # honey dipper
    g += f"""<g transform="translate(400,{base-70}) rotate(28)">
      <rect x="-4" y="-80" width="8" height="90" rx="4" fill="#C98F4E" stroke="{INK}" stroke-width="1.4"/>
      <ellipse cx="0" cy="22" rx="16" ry="22" fill="#E9A93B" stroke="{INK}" stroke-width="1.5"/>
      <path d="M-15,14 h30 M-16,24 h32 M-14,34 h28" stroke="{INK}" stroke-width="1.1"/></g>"""
    for x, y in [(110, base - 6), (128, base + 8), (420, base + 6)]:
        g += f'<path d="M{x},{y} l8,-14 l8,14 Z" fill="#C8372D" stroke="{INK}" stroke-width="1.1"/>'
    g += bread(40, base - 16, -6)
    return svg(g)


def parmesan():
    cx, base = 260, 250
    g = plate(cx, base + 4, 190, 26)
    g += pillar(cx - 60, base, 92, 120, "#F3CF7E", "#E0AF4E", "pm1", specks=("#B43A26", 26))
    g += pillar(cx + 62, base, 80, 92, "#F3CF7E", "#E0AF4E", "pm2", specks=("#B43A26", 18))
    g += flame(cx - 60, base - 120 - 56, 44, "pm1") + flame(cx + 62, base - 92 - 52, 40, "pm2")
    g += f"""<path d="M80,{base-4} l52,-40 l26,46 Z" fill="#F4E2A6" stroke="{INK}" stroke-width="1.6"/>
    <circle cx="112" cy="{base-14}" r="3" fill="#E0C680"/><circle cx="130" cy="{base-26}" r="2.4" fill="#E0C680"/>"""
    g += leaf(380, base - 4, -20, 1.1) + leaf(400, base + 2, 30, 1.0)
    return svg(g)


def cocoa():
    cx, base = 260, 250
    g = plate(cx, base + 4, 190, 26, "#F6EFE7")
    g += pillar(cx, base, 112, 140, "#F7EBD2", "#E8D3AC", "cb", specks=("#3B2418", 44))
    g += flame(cx, base - 140 - 58, 46, "cb")
    # strawberries
    for x, y, r in [(110, base - 8, -20), (148, base + 4, 10), (380, base - 2, 15)]:
        g += f"""<g transform="translate({x},{y}) rotate({r})">
          <path d="M0,-18 C18,-20 22,-2 0,22 C-22,-2 -18,-20 0,-18 Z" fill="#D9363E" stroke="{INK}" stroke-width="1.5"/>
          <path d="M-10,-18 l5,-8 l5,6 l5,-6 l5,8 Z" fill="#6E8F45" stroke="{INK}" stroke-width="1.1"/>
          <circle cx="-5" cy="-6" r="1.3" fill="#FCE3A0"/><circle cx="5" cy="-2" r="1.3" fill="#FCE3A0"/><circle cx="-1" cy="6" r="1.3" fill="#FCE3A0"/></g>"""
    # vanilla pod
    g += f'<path d="M330,{base+14} C370,{base+6} 420,{base+10} 455,{base-6}" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>'
    g += f'<path d="M330,{base+14} C370,{base+6} 420,{base+10} 455,{base-6}" stroke="#4A2C1C" stroke-width="3" stroke-linecap="round" fill="none"/>'
    return svg(g)


def banana():
    cx, base = 260, 250
    g = plate(cx, base + 4, 200, 26, "#F2ECE2")
    for i, x in enumerate([170, 260, 350]):
        h = [96, 120, 86][i]
        g += f"""<path d="M{x-24},{base} L{x-22},{base-h+10} Q{x},{base-h-6} {x+22},{base-h+10} L{x+24},{base} Z"
          fill="#FBF1C7" stroke="{INK}" stroke-width="1.7"/>
          <path d="M{x+12},{base-h+14} L{x+14},{base-4}" stroke="#EADB98" stroke-width="6" stroke-linecap="round"/>"""
        g += flame(x, base - h - 46, 36, f"bn{i}")
    g += f"""<path d="M60,{base-2} q40,20 80,4" stroke="#5A321F" stroke-width="7" stroke-linecap="round" fill="none" opacity=".85"/>
    <path d="M380,{base+8} q40,14 82,-6" stroke="#5A321F" stroke-width="7" stroke-linecap="round" fill="none" opacity=".85"/>"""
    for x, y in [(96, base + 12), (430, base - 8), (450, base + 6)]:
        g += f'<ellipse cx="{x}" cy="{y}" rx="9" ry="4.5" fill="#E9C99A" stroke="{INK}" stroke-width="1.1"/>'
    return svg(g)


def candle_small(color="#F6D98A", shade="#E9BE5C", uid="s"):
    cx, base = 100, 190
    g = pillar(cx, base, 70, 100, color, shade, uid, specks=None)
    g += flame(cx, base - 100 - 46, 38, uid)
    return svg(g, 200, 200)


def method_step(n):
    """Tiny line drawings for the 4-step base method."""
    s = 'fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"' % INK
    if n == 1:  # soften + mix in bowl
        g = f'<path d="M20,60 Q60,120 100,60 Z" {s} fill="#F6D98A"/><path d="M14,60 h92" {s}/>' \
            f'<path d="M80,20 L60,70" {s}/><circle cx="48" cy="74" r="3" fill="#5E7B3E"/><circle cx="66" cy="82" r="3" fill="#5E7B3E"/>'
    elif n == 2:  # wick in mold
        g = f'<rect x="34" y="30" width="52" height="80" rx="4" {s}/><path d="M60,10 V104" {s}/>' \
            f'<path d="M44,10 h32" {s}/><circle cx="60" cy="104" r="4" fill="{INK}"/>'
    elif n == 3:  # chill (snowflake)
        g = f'<rect x="34" y="30" width="52" height="80" rx="4" {s} fill="#F6D98A"/>' \
            f'<g transform="translate(96,26)"><path d="M0,-14 V14 M-12,-7 L12,7 M-12,7 L12,-7" {s}/></g>'
    else:  # unmold + light
        g = f'<rect x="38" y="52" width="44" height="58" rx="4" {s} fill="#F6D98A"/>' \
            f'<path d="M60,52 V44" {s}/><path d="M60,20 C70,32 70,40 60,44 C50,40 50,32 60,20 Z" fill="#F4A23B" stroke="{INK}" stroke-width="2"/>'
    return f'<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">{g}</svg>'


def ornament(color="#B8893B"):
    return (f'<svg viewBox="0 0 220 20" xmlns="http://www.w3.org/2000/svg" class="orn">'
            f'<path d="M0,10 H88 M132,10 H220" stroke="{color}" stroke-width="1"/>'
            f'<path d="M110,1 C116,7 116,13 110,19 C104,13 104,7 110,1 Z" fill="{color}"/>'
            f'<circle cx="96" cy="10" r="2" fill="{color}"/><circle cx="124" cy="10" r="2" fill="{color}"/></svg>')
