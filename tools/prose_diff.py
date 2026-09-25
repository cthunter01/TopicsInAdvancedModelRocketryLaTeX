#!/usr/bin/env python3
"""Detect dropped or duplicated prose in the transcribed chapters.

Compares the book's OCR text layer (drafts/pNNN.txt, one file per PDF page; each chapter's page
range is "pdf_pages" in inventory/chapters.json) against the text of the compiled PDF
(`pdftotext -nopgbrk build/main.pdf -`).

Method: both sides are normalised the same way (NFKC, lowercase, end-of-line hyphenation rejoined,
punctuation and digits stripped, tokens shorter than 4 characters dropped). The OCR's blank lines
fall mid-sentence (the original is double-spaced), so paragraphs are ignored: a 30-token window
slides with stride 15 over each source page (the last window is clamped so the page's tail is
covered), and a window's score is the fraction of its word 3-grams found among the 3-grams of the
whole compiled document.  Window verdicts: >= 0.6 pass, 0.3-0.6 inspect, < 0.3 missing.  A page
passes when every window passes, is "missing" when every window is missing, and is "inspect"
otherwise.  Pages with fewer than 30 tokens (figure pages) are skipped and listed.
Duplicate check: every 8-gram occurring twice or more in the compiled document, with its count,
excluding 8-grams made only of the symbols-table header words (symbol, meaning).

Usage: python3 tools/prose_diff.py [--chapter ch1 ...] [--pdf build/main.pdf]
  default: every chapter whose "units" object in inventory/chapters.json is non-empty.
Writes build/prose-chN.md and prints the per-page table.
Exit status: 1 if some page with at least two windows has all of them below 0.3 (a likely dropped
page); 2 on a setup error (missing PDF, draft or chapter); 0 otherwise.  A chapter's optional
"artwork_pages" object in inventory/chapters.json ({"274": "reason"}) names pages whose OCR cannot
match the compiled text for a checked reason (lettering inside a figure crop; a letter-spaced OCR of
a typed table); such a page is still scored and listed, but with its reason instead of as a likely
dropped page.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys
import unicodedata
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "inventory" / "chapters.json"
DRAFTS = ROOT / "drafts"

WINDOW, STRIDE = 30, 15
NGRAM, DUP_NGRAM = 3, 8
MIN_TOKEN_LEN = 4
PASS, INSPECT = 0.6, 0.3
HEADER_WORDS = {"symbol", "meaning"}

# "-" (also the typographic hyphen and soft hyphen pdftotext may emit) at the end of a line
HYPHEN_EOL = re.compile(r"[-\u2010\u00ad][ \t]*\r?\n[ \t]*")
NON_LETTER = re.compile(r"[\W\d_]+")


def die(msg):
    """Setup error: exit 2 so it is never mistaken for a dropped-page verdict (exit 1)."""
    print(f"prose_diff: {msg}", file=sys.stderr)
    sys.exit(2)


def tokens(text):
    """Normalise text to the token list both sides are compared on."""
    text = unicodedata.normalize("NFKC", text).lower()
    text = HYPHEN_EOL.sub("", text)
    return [t for t in NON_LETTER.split(text) if len(t) >= MIN_TOKEN_LEN]


def ngrams(toks, n):
    return [tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)]


def window_starts(n):
    """Start offsets of the windows over n >= WINDOW tokens; the tail is always covered."""
    starts = list(range(0, n - WINDOW + 1, STRIDE))
    if starts[-1] + WINDOW < n:
        starts.append(n - WINDOW)
    return starts


def window_verdict(score):
    return "pass" if score >= PASS else "inspect" if score >= INSPECT else "missing"


def page_verdict(scores):
    if all(s >= PASS for s in scores):
        return "pass"
    if all(s < INSPECT for s in scores):
        return "missing"
    return "inspect"


def compiled_text(pdf):
    try:
        return subprocess.run(["pdftotext", "-nopgbrk", str(pdf), "-"],
                              capture_output=True, text=True, check=True).stdout
    except FileNotFoundError:
        die("pdftotext not found (install poppler-utils)")
    except subprocess.CalledProcessError as e:
        die(f"pdftotext failed on {pdf}: {e.stderr.strip()}")


def duplicates(doc):
    """(8-gram, count) for every repeated 8-gram, in order of first occurrence, and the maximal
    repeated spans (runs of consecutive repeated 8-grams), each listed once."""
    grams = ngrams(doc, DUP_NGRAM)
    counts = Counter(g for g in grams if not set(g) <= HEADER_WORDS)
    repeated = [(g, c) for g, c in counts.items() if c >= 2]
    spans, seen = [], set()
    i = 0
    while i < len(grams):
        if counts.get(grams[i], 0) < 2:
            i += 1
            continue
        j = i
        while j + 1 < len(grams) and counts.get(grams[j + 1], 0) >= 2:
            j += 1
        text = " ".join(doc[i:j + DUP_NGRAM])
        if text not in seen:
            seen.add(text)
            spans.append((min(counts[g] for g in grams[i:j + 1]), text))
        i = j + 1
    return repeated, spans


def md_table(header, align, rows):
    lines = ["| " + " | ".join(header) + " |", "|" + "|".join(align) + "|"]
    lines += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(lines)


def check_chapter(key, chapter, trigrams, dups, pdf):
    first, last = chapter["pdf_pages"]
    rows, skipped, flagged, dropped, excused = [], [], [], [], []
    artwork = chapter.get("artwork_pages", {})
    for p in range(first, last + 1):
        path = DRAFTS / f"p{p:03d}.txt"
        if not path.exists():
            die(f"{path.relative_to(ROOT)} missing (run tools/extract_text.py)")
        toks = tokens(path.read_text())
        if len(toks) < WINDOW:
            skipped.append((p, len(toks)))
            continue
        scores = []
        for s in window_starts(len(toks)):
            w = toks[s:s + WINDOW]
            grams = ngrams(w, NGRAM)
            score = sum(g in trigrams for g in grams) / len(grams)
            scores.append(score)
            if score < PASS:
                flagged.append((p, s, f"{score:.2f}", window_verdict(score), " ".join(w[:8])))
        rows.append((p, len(scores), f"{min(scores):.2f}", f"{sum(scores) / len(scores):.2f}",
                     page_verdict(scores)))
        if len(scores) >= 2 and max(scores) < INSPECT:
            (excused if str(p) in artwork else dropped).append(p)

    table = md_table(["PDF page", "windows", "min score", "mean score", "verdict"],
                     ["---:", "---:", "---:", "---:", ":---"], rows)
    print(f"== {key}: {chapter['title']} (PDF pages {first}-{last}) vs {pdf.relative_to(ROOT)}")
    print(table)
    tally = Counter(r[4] for r in rows)
    print(f"pages: {len(rows)} checked ({tally['pass']} pass, {tally['inspect']} inspect, "
          f"{tally['missing']} missing), {len(skipped)} skipped; "
          f"{len(flagged)} windows to inspect; {len(dups[0])} repeated 8-grams in the document")
    if dropped:
        print(f"LIKELY DROPPED PAGES: {', '.join(str(p) for p in dropped)}")
    for p in excused:
        print(f"artwork page {p} (below {INSPECT} everywhere, excused): {artwork[str(p)]}")

    out = ROOT / "build" / f"prose-{key}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    md = [f"# Prose check: {key} -- {chapter['title']}", "",
          f"OCR pages {first}-{last} (`drafts/pNNN.txt`) vs `{pdf.relative_to(ROOT)}`. "
          f"Window = {WINDOW} tokens, stride {STRIDE}; score = share of the window's word "
          f"{NGRAM}-grams found in the compiled document. Verdicts: >= {PASS} pass, "
          f">= {INSPECT} inspect, else missing; a page passes when every window passes and is "
          f"missing when every window is missing.", "",
          "## Per-page scores", "", table, ""]
    if dropped:
        md += ["**Likely dropped pages (every window below "
               f"{INSPECT}):** {', '.join(str(p) for p in dropped)}", ""]
    if excused:
        md += [f"Artwork pages (every window below {INSPECT}; excused in inventory/chapters.json): " +
               "; ".join(f"p{p:03d}: {artwork[str(p)]}" for p in excused), ""]
    md += [f"Skipped (fewer than {WINDOW} tokens): " +
           (", ".join(f"p{p:03d} ({n} tokens)" for p, n in skipped) if skipped else "none"), ""]
    md += ["## Windows to inspect", ""]
    if flagged:
        md += [md_table(["PDF page", "start token", "score", "verdict", "first eight tokens"],
                        ["---:", "---:", "---:", ":---", ":---"], flagged), ""]
    else:
        md += ["none", ""]
    repeated, spans = dups
    md += [f"## Repeated {DUP_NGRAM}-grams in the compiled document", ""]
    if repeated:
        md += ["### Repeated spans (consecutive repeated 8-grams merged)", "",
               md_table(["count", "span"], ["---:", ":---"], spans), "",
               "### All repeated 8-grams", "",
               md_table(["count", "8-gram"], ["---:", ":---"],
                        [(c, " ".join(g)) for g, c in repeated]), ""]
    else:
        md += ["none", ""]
    out.write_text("\n".join(md))
    print(f"report: {out.relative_to(ROOT)}")
    return 1 if dropped else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--chapter", action="append", metavar="chN",
                    help="chapter key in inventory/chapters.json (repeatable); "
                         "default: every chapter with transcription units")
    ap.add_argument("--pdf", default="build/main.pdf", metavar="FILE",
                    help="compiled PDF to check against (default: build/main.pdf)")
    args = ap.parse_args()

    chapters = json.loads(CHAPTERS.read_text())
    if args.chapter:
        keys = [c if (c.startswith("ch") or c in chapters) else f"ch{c}" for c in args.chapter]
        unknown = [k for k in keys if k not in chapters]
        if unknown:
            die(f"unknown chapter(s) {', '.join(unknown)}; known: {', '.join(chapters)}")
    else:
        keys = [k for k, c in chapters.items() if c.get("units")]
        if not keys:
            print("prose_diff: no chapter has transcription units yet; nothing to check")
            return 0

    pdf = pathlib.Path(args.pdf)
    if not pdf.is_absolute():
        pdf = ROOT / pdf
    if not pdf.exists():
        die(f"{pdf} not found (build it first)")
    doc = tokens(compiled_text(pdf))
    trigrams = set(ngrams(doc, NGRAM))
    dups = duplicates(doc)

    rc = 0
    for key in keys:
        rc = max(rc, check_chapter(key, chapters[key], trigrams, dups, pdf))
        print()
    return rc


if __name__ == "__main__":
    sys.exit(main())
