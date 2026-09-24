#!/usr/bin/env python3
"""Crop the artwork listed in figures/manifest.csv from on-demand pdftoppm renders of the source PDF.

Usage: tools/crop_figures.py [--chapter chN] [--force] [--manifest figures/manifest.csv]

Coordinate convention (shared by seed_manifest.py, crop_figures.py and contact_sheet.py)
---------------------------------------------------------------------------------------
x0,y0,x1,y1 in figures/manifest.csv are PDF points in the page's *MediaBox* space, origin at the
top-left corner, y growing downwards: exactly the numbers that `pdftotext -bbox-layout` prints
(its <page width= height=> is the MediaBox). Most scanned pages are ~499 x 709 pt, but a few
(e.g. PDF 32, 79, 82) have a larger MediaBox with a CropBox inside it, so never assume 612 x 792
and never pass -cropbox to pdftoppm. A page is rendered once with `pdftoppm -r DPI -png`
(default boxes = MediaBox) into build/render/pNNN-DPI.png and the box is scaled by DPI/72
(150 dpi, the native resolution of the scans, for kind=line and photo; 300 dpi for kind=eq).
Never crop from figures/pages/pNNN.png: those native bitmaps sit on the page with an unknown offset.

For every selected row: crop the box, auto-trim the white border with an ink-density rule (a row
or column counts as ink only if at least MIN_INK of its pixels are darker than DARK; plain
getbbox is defeated by JPEG-2000 noise), keep one pixel of anti-aliased edge, add a MARGIN px
white margin and save: kind=line or eq -> greyscale PNG, kind=photo -> JPEG quality 90 (RGB when
the scan has colour, else greyscale). Outputs newer than the manifest are skipped unless --force.
Prints one line per figure with the final pixel size; exits 1 if any row failed.
"""
import argparse, csv, pathlib, subprocess, sys
import numpy as np
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = ROOT / "Topics_in_Advanced_Model_Rocketry.pdf"
RENDER = ROOT / "build" / "render"
DARK, MIN_INK, MARGIN = 200, 3, 10


def render(page, dpi):
    out = RENDER / f"p{page:03d}-{dpi}.png"
    if not out.exists():
        RENDER.mkdir(parents=True, exist_ok=True)
        subprocess.run(["pdftoppm", "-r", str(dpi), "-png", "-f", str(page), "-l", str(page),
                        "-singlefile", str(PDF), str(out.with_suffix(""))], check=True)
    return out


def trim(img):
    """Auto-trim white borders and add the white margin; None when the box holds no ink."""
    a = np.asarray(img.convert("L"))
    ink = a < DARK
    rows = np.flatnonzero(ink.sum(axis=1) >= MIN_INK)
    cols = np.flatnonzero(ink.sum(axis=0) >= MIN_INK)
    if rows.size == 0 or cols.size == 0:
        return None
    box = (max(cols[0] - 1, 0), max(rows[0] - 1, 0),
           min(cols[-1] + 2, a.shape[1]), min(rows[-1] + 2, a.shape[0]))
    core = img.crop(box)
    canvas = Image.new(img.mode, (core.width + 2 * MARGIN, core.height + 2 * MARGIN), "white")
    canvas.paste(core, (MARGIN, MARGIN))
    return canvas


def is_grey(img):
    a = np.asarray(img.convert("RGB"))
    return bool((a[..., 0] == a[..., 1]).all() and (a[..., 1] == a[..., 2]).all())


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--chapter", help="only ids equal to or starting with this prefix (e.g. ch1)")
    ap.add_argument("--force", action="store_true", help="rewrite outputs even if newer than the manifest")
    ap.add_argument("--manifest", default=str(ROOT / "figures" / "manifest.csv"))
    args = ap.parse_args()
    manifest = pathlib.Path(args.manifest)
    with manifest.open(newline="") as f:
        rows = list(csv.DictReader(f))
    if args.chapter:
        rows = [r for r in rows if r["id"] == args.chapter or r["id"].startswith(args.chapter + "-")]
    stamp = manifest.stat().st_mtime
    done = failed = skipped = 0
    for r in rows:
        rid, kind = r["id"], (r["kind"] or "line").strip()
        try:
            page = int(r["pdf_page"])
            x0, y0, x1, y1 = (float(r[k]) for k in ("x0", "y0", "x1", "y1"))
        except (KeyError, ValueError):
            print(f"{rid:<14} ERROR: unreadable row {r}"); failed += 1; continue
        out = ROOT / r["output"]
        if out.exists() and out.stat().st_mtime > stamp and not args.force:
            print(f"{rid:<14} p{page:03d} skip: {r['output']} is newer than the manifest"); skipped += 1; continue
        dpi = 300 if kind == "eq" else 150
        src = Image.open(render(page, dpi))
        s = dpi / 72.0
        px = [round(x0 * s), round(y0 * s), round(x1 * s), round(y1 * s)]
        px = [min(max(px[0], 0), src.width), min(max(px[1], 0), src.height),
              min(max(px[2], 0), src.width), min(max(px[3], 0), src.height)]
        if px[2] <= px[0] or px[3] <= px[1]:
            print(f"{rid:<14} ERROR: empty box {px} on p{page:03d} ({src.width}x{src.height} px)"); failed += 1; continue
        crop = src.crop(px)
        crop = crop.convert("RGB") if kind == "photo" and not is_grey(crop) else crop.convert("L")
        res = trim(crop)
        if res is None:
            print(f"{rid:<14} ERROR: no ink inside box {px} on p{page:03d}; nothing written"); failed += 1; continue
        out.parent.mkdir(parents=True, exist_ok=True)
        if kind == "photo":
            if out.suffix.lower() not in (".jpg", ".jpeg"):
                print(f"{rid:<14} WARNING: kind=photo but output is {out.suffix}; saving PNG")
                res.save(out, "PNG", optimize=True)
            else:
                res.save(out, "JPEG", quality=90)
        else:
            res.save(out, "PNG", optimize=True)
        print(f"{rid:<14} p{page:03d} {kind:<5} {res.width}x{res.height} px -> {r['output']}")
        done += 1
    print(f"{done} written, {skipped} skipped, {failed} failed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
