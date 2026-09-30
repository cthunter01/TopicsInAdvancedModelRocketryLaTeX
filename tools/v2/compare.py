#!/usr/bin/env python3
"""Render a version 2 figure and set it beside the version 1 crop it replaces.

Usage: tools/v2/compare.py <dir>/<name> [...]      e.g. ch1/fig01, supplement/ch1-fig02-1994

For figures/v2/<dir>/<name>.pdf: prints its size (inches) and fails if it is wider than the text block
(6.5 in) or has a font that is not embedded; renders it at 150 dpi (the scan's resolution, so both
images are at printed scale) to build/v2/png/<dir>-<name>.png and writes the side-by-side
build/v2/png/<dir>-<name>-compare.png (scan crop left, redraw right). Exits 1 on any failure.
"""
import pathlib, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "build" / "v2" / "png"
TEXTWIDTH_IN = 6.5
DPI = 150


def font(size):
    for f in ("/usr/share/fonts/TTF/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            pass
    return ImageFont.load_default()


def page_size_in(pdf):
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=True).stdout
    m = re.search(r"Page size:\s+([\d.]+) x ([\d.]+) pts", info)
    return float(m.group(1)) / 72, float(m.group(2)) / 72


def unembedded_fonts(pdf):
    out = subprocess.run(["pdffonts", str(pdf)], capture_output=True, text=True, check=True).stdout
    bad = []
    for line in out.splitlines()[2:]:
        cols = line.split()
        # name type [encoding...] emb sub uni object ID: emb is the 5th field from the right
        if len(cols) >= 7 and cols[-5] != "yes":
            bad.append(cols[0])
    return bad


def compare(key):
    pdf = ROOT / "figures" / "v2" / f"{key}.pdf"
    crop = ROOT / "figures" / f"{key}.png"
    name = key.replace("/", "-")
    ok = True
    if not pdf.exists():
        print(f"{key}: {pdf.relative_to(ROOT)} not found (make figs)")
        return False
    w, h = page_size_in(pdf)
    msg = f"{key}: {w:.2f} x {h:.2f} in"
    if w > TEXTWIDTH_IN + 0.01:
        ok = False
        msg += f"  FAIL: wider than the text block ({TEXTWIDTH_IN} in)"
    bad = unembedded_fonts(pdf)
    if bad:
        ok = False
        msg += f"  FAIL: fonts not embedded: {', '.join(bad)}"
    print(msg)
    OUT.mkdir(parents=True, exist_ok=True)
    png = OUT / f"{name}.png"
    subprocess.run(["pdftoppm", "-r", str(DPI), "-png", "-singlefile", str(pdf), str(png.with_suffix(""))], check=True)
    new = Image.open(png).convert("RGB")
    if crop.exists():
        old = Image.open(crop).convert("RGB")
        pad, head = 24, 30
        sheet = Image.new("RGB", (old.width + new.width + 3 * pad, max(old.height, new.height) + head + pad), "white")
        sheet.paste(old, (pad, head))
        sheet.paste(new, (old.width + 2 * pad, head))
        d = ImageDraw.Draw(sheet)
        d.text((pad, 6), "scan (v1)", fill=(90, 90, 90), font=font(16))
        d.text((old.width + 2 * pad, 6), "redraw (v2)", fill=(90, 90, 90), font=font(16))
        d.line([(old.width + 1.5 * pad, head), (old.width + 1.5 * pad, sheet.height - pad)], fill=(200, 200, 200))
        cmp = OUT / f"{name}-compare.png"
        sheet.save(cmp)
        print(f"  render {png.relative_to(ROOT)}  compare {cmp.relative_to(ROOT)}")
    else:
        print(f"  render {png.relative_to(ROOT)}  (no v1 crop figures/{key}.png to compare)")
    return ok


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    results = [compare(k.removesuffix(".pdf").removesuffix(".tex").removeprefix("figures/v2/")) for k in argv]
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
