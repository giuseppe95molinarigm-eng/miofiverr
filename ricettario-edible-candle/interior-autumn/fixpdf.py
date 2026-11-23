"""Snaps every page box to the exact KDP size (8.125 x 10.25 in = 585 x 738 pt).
Chromium writes 585.12 pt wide pages; the extra 0.12 pt sits in the bleed."""
import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

src = sys.argv[1]
r = PdfReader(src)
w = PdfWriter()
for p in r.pages:
    box = RectangleObject([0, 0, 585, 738])
    p.mediabox = box
    p.cropbox = box
    w.add_page(p)
w.add_metadata({"/Title": "The Edible Candle Cookbook — Interior Sample"})
with open(src, "wb") as f:
    w.write(f)
