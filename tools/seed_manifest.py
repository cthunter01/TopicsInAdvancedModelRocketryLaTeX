#!/usr/bin/env python3
"""Propose figures/manifest.csv rows for the "Figure N:" / "Plate N:" captions of a page range.

Usage: tools/seed_manifest.py CHAPTER FIRST LAST [--manifest CSV]     e.g.  tools/seed_manifest.py ch1 31 82

Coordinate convention (shared by seed_manifest.py, crop_figures.py and contact_sheet.py)
---------------------------------------------------------------------------------------
x0,y0,x1,y1 in figures/manifest.csv are PDF points in the page's *MediaBox* space, origin at the
top-left corner, y growing downwards: exactly the numbers that `pdftotext -bbox-layout` prints
(its <page width= height=> is the MediaBox). Most scanned pages are ~499 x 709 pt, but a few
(e.g. PDF 32, 79, 82) have a larger MediaBox with a CropBox inside it, so never assume 612 x 792
and never pass -cropbox to pdftoppm. crop_figures.py renders a page with `pdftoppm -r DPI -png`
(default boxes = MediaBox) into build/render/pNNN-DPI.png and scales the box by DPI/72
(150 dpi, the native resolution of the scans, for kind=line and photo; 300 dpi for kind=eq).
Never crop from figures/pages/pNNN.png: those native bitmaps sit on the page with an unknown offset.

Seeding rules (a proposal only; fix the box by hand where it is wrong, then run crop_figures.py)
- A caption is a text line (words chained by vertical centre) whose text starts with
  "Figure N" or "Plate N" followed by ":" or "." (case-insensitive; up to two OCR errors in the
  word are tolerated, e.g. "Pigure", "11gure"; l/I/O in the number are read as 1/1/0; a lone
  l/I/1/i before a capitalised word is taken for a misread colon, e.g. "Figure 101 Examples").
- The artwork region runs from the top of the page content (TOP_MARGIN, or the first text line
  when it starts above that) down to GAP above the caption line, over the full width between
  SIDE_MARGIN and W - SIDE_MARGIN; crop_figures.py trims the white away.
- When a page holds two captions, the second figure's region starts GAP below the first caption
  block (the caption line plus the following lines at normal line pitch). A prose line above the
  caption (wider than PROSE_WIDTH of the page) also pushes the region top below itself.
- id = chN-figNN (chN-plateNN), kind = line (photo), output = figures/chN/figNN.png (plateNN.jpg),
  owner blank, notes = "auto". Ids already in the manifest are never duplicated (a hand-split
  chN-fig04a/chN-fig04b also counts as chN-fig04, so re-seeding a finished chapter adds nothing).
- A caption with no room above it (artwork on another page, e.g. Chapter 1 Figure 10 whose
  caption is on PDF 78 and artwork on PDF 79) is still emitted, with a note saying so.
"""
import csv, pathlib, re, subprocess, sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = ROOT / "Topics_in_Advanced_Model_Rocketry.pdf"
MANIFEST = ROOT / "figures" / "manifest.csv"
FIELDS = ["id", "pdf_page", "x0", "y0", "x1", "y1", "kind", "owner", "output", "notes"]

TOP_MARGIN = 18.0    # pt: default top of the artwork region
SIDE_MARGIN = 12.0   # pt: left and right edge of the region
GAP = 3.0            # pt: clearance above a caption line / below a caption block
PROSE_WIDTH = 0.6    # a text line wider than this fraction of the page width is prose, not a label
MIN_HEIGHT = 40.0    # pt: a region shorter than this holds no artwork

# word (OCR noise allowed, e.g. "11gure"), number (l/I/O noise allowed), then ":" or "." -- or a lone
# l/I/1/i standing for a misread colon when a capitalised word follows ("Figure 101 Examples").
CAPTION = re.compile(r'^[\W_]{0,3}(\S{4,7})\s*([0-9lIO]{1,3})\s*(?:[:.;!]|[lI1i](?=\s+[A-Z"(]))')


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def caption_of(text):
    """('fig'|'plate', number) when the line text is a caption, else None."""
    m = CAPTION.match(text)
    if not m:
        return None
    word = m.group(1).lower()
    num = m.group(2).translate(str.maketrans("lIO", "110"))
    if not num.isdigit():
        return None
    if lev(word, "figure") <= 2:
        return "fig", int(num)
    if lev(word, "plate") <= 1:
        return "plate", int(num)
    return None


def page_lines(page):
    """(W, H, lines); each line is a dict x0,y0,x1,y1,text (y0/y1 = median of its words), top to bottom."""
    xml = subprocess.run(["pdftotext", "-bbox-layout", "-f", str(page), "-l", str(page), str(PDF), "-"],
                         capture_output=True, text=True, check=True).stdout
    root = ET.fromstring(xml)
    tag = lambda el: el.tag.rsplit("}", 1)[-1]
    pg = next(el for el in root.iter() if tag(el) == "page")
    W, H = float(pg.get("width")), float(pg.get("height"))
    words = [(float(el.get("xMin")), float(el.get("yMin")), float(el.get("xMax")), float(el.get("yMax")),
              (el.text or "").strip()) for el in root.iter() if tag(el) == "word"]
    words.sort(key=lambda w: ((w[1] + w[3]) / 2, w[0]))
    heights = sorted(w[3] - w[1] for w in words)
    tol = 0.6 * (heights[len(heights) // 2] if heights else 10.0)
    # chain words into lines by vertical centre; a tall glyph (vector arrow spanning two lines)
    # then lands in a line of its own instead of gluing two text lines together
    lines, prev_yc = [], None
    for x0, y0, x1, y1, text in words:
        yc = (y0 + y1) / 2
        if prev_yc is None or yc - prev_yc > tol:
            lines.append([])
        lines[-1].append((x0, y0, x1, y1, text))
        prev_yc = yc
    out = []
    for ws in lines:
        ws.sort()
        med = lambda k: sorted(w[k] for w in ws)[len(ws) // 2]
        out.append({"x0": min(w[0] for w in ws), "x1": max(w[2] for w in ws), "y0": med(1), "y1": med(3),
                    "text": " ".join(w[4] for w in ws)})
    lines = out
    return W, H, sorted(lines, key=lambda ln: ln["y0"])


def line_pitch(lines):
    gaps = sorted(b["y0"] - a["y0"] for a, b in zip(lines, lines[1:]) if 5 < b["y0"] - a["y0"] < 40)
    return gaps[len(gaps) // 2] if gaps else 20.0


def caption_block_end(lines, i, pitch):
    """y1 of the last line of the caption block starting at lines[i]."""
    end = lines[i]["y1"]
    for a, b in zip(lines[i:], lines[i + 1:]):
        if b["y0"] - a["y0"] > 1.6 * pitch or caption_of(b["text"]):
            break
        end = b["y1"]
    return end


def propose(chapter, page):
    W, H, lines = page_lines(page)
    if not lines:
        return []
    pitch = line_pitch(lines)
    page_top = min(TOP_MARGIN, max(lines[0]["y0"] - 1.0, 0.0))
    rows, prev_end = [], None
    for i, ln in enumerate(lines):
        cap = caption_of(ln["text"])
        if not cap:
            continue
        kind, n = cap
        top = page_top if prev_end is None else max(page_top, prev_end + GAP)
        for other in lines[:i]:
            if other["x1"] - other["x0"] > PROSE_WIDTH * W and other["y1"] <= ln["y0"]:
                top = max(top, other["y1"] + GAP)
        bottom = ln["y0"] - GAP
        note = "auto"
        if bottom - top < MIN_HEIGHT:
            note = "auto; no artwork above this caption - artwork is on another page, fix pdf_page and box"
            top, bottom = page_top, max(bottom, page_top + MIN_HEIGHT)
        stem = f"{kind}{n:02d}"
        rows.append({"id": f"{chapter}-{stem}", "pdf_page": page,
                     "x0": f"{SIDE_MARGIN:.1f}", "y0": f"{top:.1f}", "x1": f"{W - SIDE_MARGIN:.1f}", "y1": f"{bottom:.1f}",
                     "kind": "photo" if kind == "plate" else "line", "owner": "",
                     "output": f"figures/{chapter}/{stem}.{'jpg' if kind == 'plate' else 'png'}",
                     "notes": note})
        prev_end = caption_block_end(lines, i, pitch)
    return rows


def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("chapter", help="id prefix, e.g. ch1")
    ap.add_argument("first", type=int); ap.add_argument("last", type=int)
    ap.add_argument("--manifest", default=str(MANIFEST), help="CSV to append to (default figures/manifest.csv)")
    args = ap.parse_args()
    chapter, first, last, manifest = args.chapter, args.first, args.last, pathlib.Path(args.manifest)
    existing = []
    if manifest.exists() and manifest.stat().st_size:
        with manifest.open(newline="") as f:
            existing = [r["id"] for r in csv.DictReader(f)]
    # a hand-split figure (ch1-fig04a, ch1-fig04b) also covers the plain id ch1-fig04
    seen = set(existing) | {re.sub(r"(\d)[a-z]$", r"\1", i) for i in existing}
    new, skipped = [], 0
    for page in range(first, last + 1):
        for row in propose(chapter, page):
            if row["id"] in seen:
                print(f"  skip p{page:03d} {row['id']}: id already in manifest")
                skipped += 1
                continue
            seen.add(row["id"])
            new.append(row)
            print(f"  {row['id']:<14} p{page:03d} box ({row['x0']},{row['y0']})-({row['x1']},{row['y1']})  {row['notes']}")
    write_header = not existing and (not manifest.exists() or manifest.stat().st_size == 0)
    with manifest.open("a", newline="") as f:
        w = csv.DictWriter(f, FIELDS, lineterminator="\n")
        if write_header:
            w.writeheader()
        w.writerows(new)
    print(f"{chapter} pages {first}-{last}: appended {len(new)} rows to {manifest}"
          f" ({skipped} duplicate ids skipped)")


if __name__ == "__main__":
    main()
