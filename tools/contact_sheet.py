#!/usr/bin/env python3
"""Contact sheet of every crop whose manifest id starts with chN, labelled with its id.

Usage: tools/contact_sheet.py chN [--cols 4] [--cell 360]      -> build/contact-chN.png

Coordinate convention: the manifest boxes are MediaBox points (see tools/seed_manifest.py and
tools/crop_figures.py); this tool only reads the finished crops named in the output column.
Thumbnails are scaled to fit a CELL x CELL square, keeping the aspect ratio; a crop that has not
been produced yet is shown as a red "missing" cell.
"""
import argparse, csv, math, pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "figures" / "manifest.csv"


def font(size):
    for name in ("DejaVuSans.ttf", "LiberationSans-Regular.ttf", "Arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("chapter", help="id prefix, e.g. ch1")
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--cell", type=int, default=360, help="thumbnail box side in px")
    args = ap.parse_args()
    with MANIFEST.open(newline="") as f:
        rows = [r for r in csv.DictReader(f)
                if r["id"] == args.chapter or r["id"].startswith(args.chapter + "-")]
    if not rows:
        raise SystemExit(f"no manifest rows with id prefix {args.chapter}")
    cell, pad, label_h = args.cell, 16, 44
    cols = max(1, min(args.cols, len(rows)))
    nrows = math.ceil(len(rows) / cols)
    sheet = Image.new("RGB", (cols * (cell + pad) + pad, nrows * (cell + label_h + pad) + pad), "white")
    draw = ImageDraw.Draw(sheet)
    f_id, f_sub = font(18), font(14)
    for i, r in enumerate(rows):
        cx = pad + (i % cols) * (cell + pad)
        cy = pad + (i // cols) * (cell + label_h + pad)
        path = ROOT / r["output"]
        draw.rectangle((cx - 1, cy - 1, cx + cell, cy + cell), outline=(200, 200, 200))
        if path.exists():
            im = Image.open(path).convert("RGB")
            w, h = im.size
            im.thumbnail((cell, cell))
            sheet.paste(im, (cx + (cell - im.width) // 2, cy + (cell - im.height) // 2))
            sub = f"p{int(r['pdf_page']):03d}  {w}x{h} px  {r['kind']}"
        else:
            draw.rectangle((cx, cy, cx + cell - 1, cy + cell - 1), outline=(220, 0, 0), width=3)
            draw.text((cx + 12, cy + 12), "missing", fill=(220, 0, 0), font=f_id)
            sub = f"p{r['pdf_page']}  {r['output']} not found"
        draw.text((cx, cy + cell + 4), r["id"], fill="black", font=f_id)
        draw.text((cx, cy + cell + 26), sub, fill=(90, 90, 90), font=f_sub)
    out = ROOT / "build" / f"contact-{args.chapter}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, "PNG", optimize=True)
    print(f"wrote {out.relative_to(ROOT)} ({len(rows)} crops, {sheet.width}x{sheet.height} px)")


if __name__ == "__main__":
    main()
