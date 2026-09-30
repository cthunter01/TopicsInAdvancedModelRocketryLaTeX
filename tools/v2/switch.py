#!/usr/bin/env python3
"""Switch figures from their version 1 crops to the version 2 redraws.

Usage: tools/v2/switch.py [--dry-run] <dir>/<name> ...        (e.g. ch1/fig01 supplement/ch1-fig02-1994)

For each key: every \\includegraphics[...]{figures/<dir>/<name>.png} in chapters/ and backmatter/ becomes
\\includegraphics{figures/v2/<dir>/<name>.pdf} (natural size: the redraws are drawn at their final size). In the
Errata and Supplement Part (backmatter/supplement/) the second form figures/v2/<dir>/<name>-document.pdf is used
when it exists (the lettering of the reproduced document). The figure's row in figures/v2/inventory.csv must
have status "audited"; it becomes "switched". Refuses a key whose PDF is not built or whose row is not audited.
"""
import argparse, csv, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
INV = ROOT / "figures" / "v2" / "inventory.csv"


def manifest_id(key):
    d, name = key.split("/", 1)
    return f"sup-{name}" if d == "supplement" else f"{d}-{name}"


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("keys", nargs="+")
    a = ap.parse_args(argv)
    with open(INV, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys())
    by_id = {r["id"]: r for r in rows}
    files = sorted((ROOT / "chapters").glob("*.tex")) + sorted((ROOT / "backmatter").rglob("*.tex"))
    bad = False
    for key in a.keys:
        key = key.removeprefix("figures/").removeprefix("v2/").removesuffix(".pdf").removesuffix(".png")
        fid, pdf = manifest_id(key), ROOT / "figures" / "v2" / f"{key}.pdf"
        row = by_id.get(fid)
        if not pdf.exists():
            print(f"{key}: {pdf.relative_to(ROOT)} not built (make figs)"); bad = True; continue
        if row is None or row["status"] not in ("audited", "switched"):
            print(f"{key}: inventory status is {row['status'] if row else 'missing'}, not audited"); bad = True; continue
        pat = re.compile(r"\\includegraphics(\[[^\]]*\])?\{figures/" + re.escape(key) + r"(\.png)?\}")
        doc = ROOT / "figures" / "v2" / f"{key}-document.pdf"
        n = 0
        for p in files:
            text = p.read_text(encoding="utf-8")
            target = f"figures/v2/{key}-document.pdf" if doc.exists() and "backmatter/supplement" in str(p) \
                else f"figures/v2/{key}.pdf"
            new, k = pat.subn(lambda m: "\\includegraphics{" + target + "}", text)
            if k:
                n += k
                print(f"{key}: {p.relative_to(ROOT)}: {k} include(s) -> {target}")
                if not a.dry_run:
                    p.write_text(new, encoding="utf-8")
        if n == 0 and row["status"] != "switched":
            print(f"{key}: no \\includegraphics of figures/{key}.png found"); bad = True; continue
        row["status"] = "switched"
    if not a.dry_run:
        with open(INV, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
