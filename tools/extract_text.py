#!/usr/bin/env python3
"""Dump the PDF's OCR text layer page by page to drafts/pNNN.txt (typing aid for prose only).

Usage: tools/extract_text.py [first] [last]   (defaults: whole book)
"""
import subprocess, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
pdf = root / "Topics_in_Advanced_Model_Rocketry.pdf"
first = int(sys.argv[1]) if len(sys.argv) > 1 else 1
last = int(sys.argv[2]) if len(sys.argv) > 2 else 712
out = root / "drafts"; out.mkdir(exist_ok=True)
for p in range(first, last + 1):
    txt = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), str(pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    (out / f"p{p:03d}.txt").write_text(txt.replace("\f", ""))
print(f"wrote drafts for pages {first}-{last}")
