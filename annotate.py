# -*- coding: utf-8 -*-
import pymupdf, sys
sys.path.insert(0, '/workspace')
from answers import ANSWERS

SRC = "/workspace/booklet french M3-pages-1.pdf"
OUT = "/workspace/booklet_french_M3_ANSWERS.pdf"

doc = pymupdf.open(SRC)
print("pages:", doc.page_count)

RED = (0.85, 0.0, 0.0)
for pno, items in ANSWERS.items():
    page = doc[pno - 1]
    W, H = page.rect.width, page.rect.height
    fs = max(9, int(H * 0.020))  # font size scaled to page
    for (fx, fy, text) in items:
        x = fx * W
        y = fy * H + fs  # insert_text uses baseline
        page.insert_text((x, y), text, fontsize=fs, fontname="helv",
                         color=RED, render_mode=0)
        # underline the answer word lightly? skip; red bold-ish via stroke
doc.save(OUT, garbage=4, deflate=True)
import os
print("saved", OUT, os.path.getsize(OUT)//1024, "KB")
