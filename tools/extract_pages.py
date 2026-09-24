#!/usr/bin/env python3
"""Extract every page of the source PDF as figures/pages/pNNN.png.

Pages that are a single scanned image (the 1973 book and most of the supplement) are extracted
losslessly with `pdfimages -png` (native 150 ppi, 1040x1476 px), ignoring the 1x1 stencil masks
Acrobat added on many pages. Pages with no image stream (the typeset 2025 front matter, PDF 1-6,
and the 2022 correction pages 683, 685, 686) are rendered with `pdftoppm -r 150`.

Usage: tools/extract_pages.py [first] [last]
"""
import hashlib, pathlib, re, shutil, subprocess, sys, tempfile

root = pathlib.Path(__file__).resolve().parent.parent
pdf = root / "Topics_in_Advanced_Model_Rocketry.pdf"
want = re.search(r"sha256: `([0-9a-f]{64})`", (root / "README.md").read_text()).group(1)
have = hashlib.sha256(pdf.read_bytes()).hexdigest()
if want != have:
    sys.exit(f"sha256 mismatch for {pdf.name}: have {have}, README says {want}")
first = int(sys.argv[1]) if len(sys.argv) > 1 else 1
last = int(sys.argv[2]) if len(sys.argv) > 2 else 712
out = root / "figures" / "pages"; out.mkdir(parents=True, exist_ok=True)

# choose, per page, the largest stream of type "image" (stencils are 1x1 masks)
best = {}
listing = subprocess.run(["pdfimages", "-list", "-f", str(first), "-l", str(last), str(pdf)],
                         capture_output=True, text=True, check=True).stdout.splitlines()[2:]
for line in listing:
    f = line.split()
    page, num, kind, w, h = int(f[0]), int(f[1]), f[2], int(f[3]), int(f[4])
    if kind == "image" and w * h > best.get(page, (0, -1))[0]:
        best[page] = (w * h, num)

with tempfile.TemporaryDirectory() as tmp:
    subprocess.run(["pdfimages", "-png", "-p", "-f", str(first), "-l", str(last), str(pdf), f"{tmp}/p"], check=True)
    rendered = []
    for page in range(first, last + 1):
        target = out / f"p{page:03d}.png"
        if page in best:
            src = pathlib.Path(tmp) / f"p-{page:03d}-{best[page][1]:03d}.png"
            shutil.move(src, target)
        else:
            subprocess.run(["pdftoppm", "-r", "150", "-png", "-f", str(page), "-l", str(page),
                            "-singlefile", str(pdf), str(target.with_suffix(""))], check=True)
            rendered.append(page)
print(f"pages {first}-{last}: {len(best)} extracted natively, rendered {rendered}")
