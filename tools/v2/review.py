#!/usr/bin/env python3
"""Build a review PDF of version 2 figures: each redraw beside the scan crop it replaces, both at printed size.

Usage: tools/v2/review.py [--out build/v2/review.pdf] [--title TEXT] <dir>/<name> ...
       (e.g. ch3/fig02 ch2/fig25; a key may also be a manifest id such as ch3-fig02)

One landscape page per figure: its manifest id, LaTeX label and caption (from the chapter source), the scan
crop at 150 dpi (its printed size) on the left and the vector redraw at its own size on the right, each
scaled down only if it would not fit. Needs the redraws built (make figs).
"""
import argparse, csv, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
BUILD = ROOT / "build" / "v2"


def drop_command(text, cmd):
    """Remove every cmd{...} (balanced braces) from text."""
    while (i := text.find(cmd + "{")) >= 0:
        k, depth = i + len(cmd) + 1, 1
        while k < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[k], 0)
            k += 1
        text = text[:i] + text[k:]
    return text


def caption_for(label):
    """The \\caption{...} text of the figure environment carrying \\label{label}, from chapters/ and backmatter/."""
    for p in sorted((ROOT / "chapters").glob("*.tex")) + sorted((ROOT / "backmatter").rglob("*.tex")):
        t = p.read_text(encoding="utf-8")
        i = t.find("\\label{" + label + "}")
        if i < 0:
            continue
        j = t.rfind("\\caption{", 0, i)
        if j < 0:
            return ""
        k, depth = j + len("\\caption{"), 1
        start = k
        while k < len(t) and depth:
            depth += {"{": 1, "}": -1}.get(t[k], 0)
            k += 1
        cap = drop_command(t[start:k - 1], "\\ednote")
        return re.sub(r"\\label\{[^}]*\}", "", cap)
    return ""


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="build/v2/review.pdf")
    ap.add_argument("--title", default="Version 2 figures: review")
    ap.add_argument("keys", nargs="+")
    a = ap.parse_args(argv)
    inv = {r["id"]: r for r in csv.DictReader(open(ROOT / "figures" / "v2" / "inventory.csv", encoding="utf-8"))}
    pages = []
    for key in a.keys:
        if "/" not in key:  # manifest id -> dir/name
            m = re.match(r"(sup)-(.*)$", key)
            key = f"supplement/{m.group(2)}" if m else key.replace("-", "/", 1)
        d, name = key.split("/", 1)
        fid = f"sup-{name}" if d == "supplement" else f"{d}-{name}"
        pdf, crop = f"figures/v2/{key}.pdf", f"figures/{key}.png"
        if not (ROOT / crop).exists() and key.endswith("-document"):   # a second form of a redraw: same crop
            crop = f"figures/{key.removesuffix('-document')}.png"
            fid = fid.removesuffix("-document")
        if not (ROOT / pdf).exists():
            sys.exit(f"{pdf} not built (make figs)")
        row = inv.get(fid, {})
        label = row.get("label", "").split(";")[0].split(",")[0].strip()
        cap = caption_for(label) if re.match(r"ch\d:fig:", label) else ""
        pages.append((fid, label, cap, crop, pdf))
    body = []
    for fid, label, cap, crop, pdf in pages:
        head = f"\\textbf{{{fid}}}" + (f"\\quad (\\texttt{{{label}}})" if label else "")
        cap_tex = f"\\par\\smallskip\\begin{{minipage}}{{\\linewidth}}\\small {cap}\\end{{minipage}}" if cap else ""
        body.append(f"""\\noindent {head}{cap_tex}\\par\\medskip
\\noindent\\begin{{minipage}}[t]{{0.42\\linewidth}}\\centering\\textsf{{\\footnotesize scan (v1)}}\\par\\smallskip
\\includegraphics[width=\\linewidth,height=0.7\\textheight,keepaspectratio]{{{crop}}}\\end{{minipage}}\\hfill
\\begin{{minipage}}[t]{{0.56\\linewidth}}\\centering\\textsf{{\\footnotesize redraw (v2)}}\\par\\smallskip
\\includegraphics[width=\\linewidth,height=0.7\\textheight,keepaspectratio]{{{pdf}}}\\end{{minipage}}
\\clearpage""")
    tex = r"""\documentclass[11pt]{article}
\usepackage[letterpaper,landscape,margin=0.5in]{geometry}
\usepackage[T1]{fontenc}\usepackage{mathtools}\usepackage{newtxtext}\usepackage{newtxmath}\usepackage{graphicx}
\usepackage{xcolor}\usepackage{hyperref}
\input{macros}
\pagestyle{plain}
\begin{document}
""" + "\n".join(body) + "\n\\end{document}\n"
    BUILD.mkdir(parents=True, exist_ok=True)
    src = BUILD / "review.tex"
    src.write_text(tex, encoding="utf-8")
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", f"-output-directory={BUILD}", str(src)],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        return 1
    out = ROOT / a.out
    if out != BUILD / "review.pdf":
        out.parent.mkdir(parents=True, exist_ok=True)
        (BUILD / "review.pdf").replace(out)
    print(f"{len(pages)} figures -> {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
