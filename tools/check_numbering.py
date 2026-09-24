#!/usr/bin/env python3
"""Verify the structure of every transcribed chapter against inventory/chN.csv.

Run after a FULL build (`make all`, i.e. latexmk -> build/main.pdf).  Standard library only.
The project root is the parent of this tools/ directory, so the script can be run from anywhere.

Inputs (relative to the project root):
  build/main.aux and the chapter .aux files it \\@input's   -- hyperref \\newlabel lines
                             \\newlabel{LABEL}{{NUMBER}{PAGE}{TITLE}{ANCHOR}{}}; a \\tag number
                             arrives as {{102b}} and is unwrapped
  inventory/chN.csv          columns kind,number,pdf_page,unit; kind in eq, fig, tab, plate;
                             the label is chN:<kind>:<number> (27a, 102b included)
  inventory/chN-renumber.json  optional {"21": "23"} (label 21 is displayed as 23 after the
                             corrections); keys may be kind-qualified ("fig:3": "4") or nested
                             ({"eq": {"21": "23"}}); a bare key means an equation; a lettered
                             label (21a) follows the renumbering of its number (23a)
  figures/manifest.csv       columns id,pdf_page,x0,y0,x1,y1,kind,owner,output,notes; the owner
                             unit (ch1-sec2a) gives the chapter; when it is blank the chapter is
                             taken from the id or the output path and this is noted
  chapters/*.tex             chN.tex and the unit files chN-<unit>.tex (comments are ignored)
  build/main.log

Checks (numbered as in the report; chapters without an inventory file are named as skipped for
checks 1-2 but still get the source checks 4-7):
  1  every inventory row has a \\newlabel (missing ones listed with unit and pdf_page); eq/fig/
     tab/plate labels in the .aux that the inventory does not list fail, except chN:eq:nK labels
     (equations that exist only in the corrected edition) and the parent label of a subequations
     group whose lettered members are inventoried, which are informational
  2  the displayed NUMBER equals the label number, or the renumber map's value; n-labels exempt
  3  hyperref ANCHORs are unique within a document (a root .aux plus its \\@input files);
     labels/anchors starting with "page." are ignored; a label written twice is also listed
  4  every manifest output owned by a unit of the chapter is included by \\includegraphics
     exactly once across chapters/*.tex (matched by path, extension optional), and every
     \\includegraphics path in the chapter's own files exists on disk; paths that are not in
     the manifest are noted
  5  every figure/plate/table environment has exactly one \\caption and exactly one \\label,
     and the label is of the matching kind (fig/plate/tab)
  6  no \\newcommand, \\renewcommand, \\def, \\let, \\usepackage, \\DeclareRobustCommand
     (or close relatives such as \\gdef, \\providecommand, \\newenvironment) in chapters/*.tex
  7  \\draftnote occurrences per unit file (report only)
  8  the log: undefined references/citations, multiply defined labels, duplicate PDF
     destinations (pdfTeX "destination with the same identifier", e.g. a \\tag inside a numbered
     equation, which sends links to the wrong equation) and TeX errors fail;
     "Overfull \\hbox" wider than --overfull pt (default 20) are reported with the file TeX was
     reading (best effort: TeX reports an overfull box at the end of the paragraph)

A warning is printed when build/main.aux is older than a source file (stale build).  Labels
whose prefix is not a chapter (e.g. smoke:eq:1) are counted in the header and otherwise ignored.

Usage:
  python3 tools/check_numbering.py [--chapter ch1 ...] [--aux PATH ...] [--log PATH]
                                   [--overfull PT] [--tolerate-undefined] [--verbose]

  --chapter  restrict the chapter checks to these chapters (ch1 or 1; repeatable)
  --aux      use these .aux files instead of build/main.aux (e.g. build/unit/smoke-unit.aux or
             several unit builds at once); \\@input lines are followed relative to each file and
             the .log next to each file is read for check 8 when it exists
  --log      log file for check 8 (default: build/main.log, or the .log next to each --aux file)
  --tolerate-undefined  list undefined references without failing (standalone unit builds
             legitimately reference labels of chapters not yet transcribed, STYLE.md section 6)

Exit status: 1 if any check fails (or build/main.aux is missing), else 0.  Input problems
(unreadable rows, missing \\@input files) are listed at the end and do not fail by themselves.
"""
import argparse
import csv
import json
import re
import sys
import time
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KINDS = ("eq", "fig", "tab", "plate")
KIND_WORD = {"eq": "equation", "fig": "figure", "tab": "table", "plate": "plate"}
FLOAT_ENVS = {"figure": "fig", "figure*": "fig", "plate": "plate", "table": "tab", "table*": "tab"}
FORBIDDEN = ("newcommand", "renewcommand", "providecommand", "def", "gdef", "edef", "xdef", "let",
             "usepackage", "RequirePackage", "DeclareRobustCommand", "NewDocumentCommand",
             "RenewDocumentCommand", "DeclareMathOperator", "newenvironment", "renewenvironment")
GRAPHIC_EXTS = (".png", ".pdf", ".jpg", ".jpeg", ".eps")
LOG_WIDTH = 79          # TeX's max_print_line: lines of exactly this length continue on the next
DETAIL_CAP = 60         # detail lines shown per check unless --verbose

OK, FAIL, INFO = "OK", "FAIL", "INFO"


# --------------------------------------------------------------------------- small helpers
def read_group(s, i):
    """s[i] is '{'; return (content between the balanced braces, index after the closing brace)."""
    if i >= len(s) or s[i] != "{":
        raise ValueError("expected '{'")
    depth, j, n = 0, i, len(s)
    while j < n:
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced braces")


def split_groups(body):
    """'{a}{b}{c}' -> ['a', 'b', 'c'] (whitespace between groups tolerated)."""
    out, j, n = [], 0, len(body)
    while j < n:
        if body[j].isspace():
            j += 1
            continue
        if body[j] != "{":
            break
        g, j = read_group(body, j)
        out.append(g)
    return out


def strip_outer_braces(s):
    """'{102b}' -> '102b' (a \\tag number is written with an extra brace level)."""
    s = s.strip()
    while s.startswith("{"):
        try:
            inner, end = read_group(s, 0)
        except ValueError:
            break
        if end != len(s):
            break
        s = inner.strip()
    return s


def strip_comments(text):
    """Remove TeX comments (an unescaped % to end of line) but keep the line structure."""
    out = []
    for line in text.split("\n"):
        i, n = 0, len(line)
        while i < n:
            c = line[i]
            if c == "\\":
                i += 2
                continue
            if c == "%":
                line = line[:i]
                break
            i += 1
        out.append(line)
    return "\n".join(out)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def chapter_key(ch):
    m = re.fullmatch(r"ch(\d+)", ch)
    return (0, int(m.group(1)), "") if m else (1, 0, ch)


def norm_chapter(s):
    s = s.strip()
    return "ch" + s if s.isdigit() else s


def rel(path):
    try:
        return str(Path(path).resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def plural(n, word, words=None):
    return f"{n} {word if n == 1 else (words or word + 's')}"


# --------------------------------------------------------------------------- aux files
class Label:
    __slots__ = ("name", "number", "page", "title", "anchor", "source", "line", "doc")

    def __init__(self, name, number, page, title, anchor, source, line, doc):
        self.name, self.number, self.page, self.title = name, number, page, title
        self.anchor, self.source, self.line, self.doc = anchor, source, line, doc

    @property
    def chapter(self):
        return self.name.split(":", 1)[0] if ":" in self.name else None

    @property
    def kind(self):
        parts = self.name.split(":")
        return parts[1] if len(parts) >= 3 and parts[1] in KINDS else None

    @property
    def key(self):
        """('eq', '27a') for chN:eq:27a, else None."""
        parts = self.name.split(":", 2)
        if len(parts) == 3 and parts[1] in KINDS:
            return (parts[1], parts[2])
        return None


def parse_aux(path, doc, seen, problems):
    """Parse one .aux file and, recursively, the files it \\@input's. Returns a list of Label."""
    path = Path(path)
    key = str(path.resolve())
    if key in seen:
        return []
    seen.add(key)
    if not path.exists():
        problems.append(f"{rel(path)}: not found")
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    labels = []
    for m in re.finditer(r"\\newlabel\s*\{", text):
        start = m.end() - 1
        try:
            name, j = read_group(text, start)
            while j < len(text) and text[j] in " \t":
                j += 1
            body, _ = read_group(text, j)
            fields = split_groups(body)
        except ValueError:
            problems.append(f"{rel(path)}:{line_of(text, m.start())}: malformed \\newlabel line")
            continue
        if name.endswith("@cref"):
            continue
        fields += [""] * (5 - len(fields))
        labels.append(Label(name, strip_outer_braces(fields[0]), fields[1].strip(), fields[2],
                            fields[3].strip(), rel(path), line_of(text, m.start()), doc))
    for m in re.finditer(r"\\@input\s*\{([^}]*)\}", text):
        labels += parse_aux(path.parent / m.group(1).strip(), doc, seen, problems)
    return labels


# --------------------------------------------------------------------------- inventories
def load_inventory(path, problems):
    """inventory/chN.csv -> list of dict(kind, number, pdf_page, unit, line)."""
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        missing_cols = [c for c in ("kind", "number", "unit") if c not in (reader.fieldnames or [])]
        if missing_cols:
            problems.append(f"{rel(path)}: missing column(s) {', '.join(missing_cols)}")
            return rows
        for i, row in enumerate(reader, start=2):
            kind = (row.get("kind") or "").strip()
            number = (row.get("number") or "").strip()
            if not kind and not number:
                continue
            if kind not in KINDS:
                problems.append(f"{rel(path)}:{i}: unknown kind {kind!r} (expected one of {', '.join(KINDS)})")
                continue
            if not number:
                problems.append(f"{rel(path)}:{i}: empty number")
                continue
            rows.append({"kind": kind, "number": number, "pdf_page": (row.get("pdf_page") or "").strip(),
                         "unit": (row.get("unit") or "").strip(), "line": i})
    return rows


def load_renumber(path, problems):
    """inventory/chN-renumber.json -> {(kind, number): displayed}."""
    mapping = {}
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError) as exc:
        problems.append(f"{rel(path)}: cannot read renumber map ({exc})")
        return mapping
    if not isinstance(data, dict):
        problems.append(f"{rel(path)}: renumber map must be a JSON object")
        return mapping
    for k, v in data.items():
        if isinstance(v, dict):
            if k not in KINDS:
                problems.append(f"{rel(path)}: unknown kind {k!r} in renumber map")
                continue
            for k2, v2 in v.items():
                mapping[(k, str(k2).strip())] = str(v2).strip()
            continue
        kind, num = ("eq", k) if ":" not in k else k.split(":", 1)
        kind = kind.strip()
        if kind not in KINDS:
            problems.append(f"{rel(path)}: unknown kind {kind!r} in renumber key {k!r}")
            continue
        mapping[(kind, str(num).strip())] = str(v).strip()
    return mapping


def expected_number(kind, number, renumber):
    """Displayed number expected for a label: the renumber map's value or the label number."""
    if (kind, number) in renumber:
        return renumber[(kind, number)], True
    m = re.fullmatch(r"(\d+)([A-Za-z]+)", number)   # 27a follows a renumbering of 27
    if m and (kind, m.group(1)) in renumber:
        return renumber[(kind, m.group(1))] + m.group(2), True
    return number, False


def is_new_equation(number):
    return bool(re.fullmatch(r"n\d+[A-Za-z]*", number))


# --------------------------------------------------------------------------- tex sources
def find_includegraphics(text):
    """[(line, path)] for every \\includegraphics in comment-stripped text."""
    out = []
    for m in re.finditer(r"\\includegraphics\*?", text):
        j = m.end()
        n = len(text)
        while j < n and text[j].isspace():
            j += 1
        if j < n and text[j] == "[":
            depth = 0
            while j < n:
                if text[j] == "{":
                    depth += 1
                elif text[j] == "}":
                    depth -= 1
                elif text[j] == "]" and depth == 0:
                    j += 1
                    break
                j += 1
            while j < n and text[j].isspace():
                j += 1
        if j < n and text[j] == "{":
            try:
                arg, _ = read_group(text, j)
            except ValueError:
                continue
            out.append((line_of(text, m.start()), arg.strip()))
    return out


def graphic_exists(path):
    p = ROOT / path
    if p.exists():
        return True
    if not p.suffix:
        return any(p.with_suffix(ext).exists() for ext in GRAPHIC_EXTS)
    return False


def graphic_stem(path):
    p = path.strip().replace("\\", "/")
    while p.startswith("./"):
        p = p[2:]
    if Path(p).suffix.lower() in GRAPHIC_EXTS:
        p = p[: -len(Path(p).suffix)]
    return p


def load_manifest(path, problems):
    rows = []
    if not path.exists():
        problems.append(f"{rel(path)}: not found (check 4 has no manifest rows)")
        return rows
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for i, row in enumerate(reader, start=2):
            owner = (row.get("owner") or "").strip()
            output = (row.get("output") or "").strip()
            ident = (row.get("id") or "").strip()
            chapter, inferred = None, False
            # a non-blank owner is authoritative: an owner such as "supplement" that names no chapter
            # means the row belongs to no chapter; only a blank owner falls back to the id or output path
            cands = ((owner, False),) if owner else ((ident, True), (re.sub(r"^figures/", "", output), True))
            for cand, via in cands:
                m = re.match(r"(ch\d+)(?:$|[-_/.])", cand)
                if m:
                    chapter, inferred = m.group(1), via
                    break
            rows.append({"id": ident, "owner": owner, "output": output, "chapter": chapter,
                         "owner_inferred": inferred, "kind": (row.get("kind") or "").strip(), "line": i})
    return rows


def check_floats(ch, files):
    """Check 5 on [(relpath, stripped text)]: returns (n_env, details)."""
    details, n_env = [], 0
    for relpath, text in files:
        for m in re.finditer(r"\\begin\{(figure\*?|plate|table\*?)\}", text):
            env = m.group(1)
            n_env += 1
            end = text.find(f"\\end{{{env}}}", m.end())
            body = text[m.end():end if end != -1 else len(text)]
            loc = f"{relpath}:{line_of(text, m.start())}"
            if end == -1:
                details.append(f"{loc}: \\begin{{{env}}} without \\end{{{env}}}")
            captions = len(re.findall(r"\\caption\s*[\[{]", body))
            labs = [l.strip() for l in re.findall(r"\\label\s*\{([^}]*)\}", body)]
            if captions != 1:
                details.append(f"{loc}: {env} environment has {captions} \\caption (expected 1)")
            if len(labs) != 1:
                details.append(f"{loc}: {env} environment has {len(labs)} \\label (expected 1)"
                               + (f": {', '.join(labs)}" if labs else ""))
            for lab in labs:
                mm = re.fullmatch(r"(ch\d+):(eq|fig|tab|plate):.+", lab)
                if not mm or mm.group(2) != FLOAT_ENVS[env]:
                    details.append(f"{loc}: label {lab} in a {env} environment should be {ch}:{FLOAT_ENVS[env]}:<n>")
    return n_env, details


FORBIDDEN_RE = re.compile(r"\\(" + "|".join(FORBIDDEN) + r")\b")


def check_forbidden(files):
    """Check 6 on [(relpath, stripped text)]: returns detail lines, one per hit."""
    details = []
    for relpath, text in files:
        for m in FORBIDDEN_RE.finditer(text):
            details.append(f"{relpath}:{line_of(text, m.start())}: \\{m.group(1)}")
    return details


def count_draftnotes(files):
    """Check 7: [(relpath, count)]."""
    return [(relpath, len(re.findall(r"\\draftnote\b", text))) for relpath, text in files]


# --------------------------------------------------------------------------- log file
def unwrap_log(text):
    lines, out, buf = text.split("\n"), [], ""
    for line in lines:
        buf += line
        if len(line) == LOG_WIDTH:
            continue
        out.append(buf)
        buf = ""
    if buf:
        out.append(buf)
    return out


FILE_TOKEN = re.compile(r"\(((?:\./|\.\./|/)?[^\s()\[\]{}]+\.(?:tex|sty|cls|def|clo|cfg|ldf|fd|aux|toc|out|bbl|lof|lot|lop))(?=[\s()\[]|$)")


def files_at_lines(lines):
    """Best-effort: the .tex file TeX was reading at the start of each log line."""
    stack, current = [], []
    for line in lines:
        top = next((f for f in reversed(stack) if f), None)
        current.append(top)
        i = 0
        while i < len(line):
            c = line[i]
            if c == "(":
                m = FILE_TOKEN.match(line, i)
                stack.append(m.group(1) if m else None)
            elif c == ")":
                if stack:
                    stack.pop()
            i += 1
    return current


RE_UNDEF = re.compile(r"LaTeX Warning: (Reference|Citation) `([^']*)' on page (\S+) undefined on input line (\d+)")
RE_UNDEF_ANY = re.compile(r"LaTeX Warning: There were undefined (references|citations)")
RE_MULTI = re.compile(r"LaTeX Warning: Label `([^']*)' multiply defined")
RE_MULTI_ANY = re.compile(r"LaTeX Warning: There were multiply-defined labels")
RE_OVERFULL = re.compile(r"Overfull \\hbox \(([\d.]+)pt too wide\)(.*)")
RE_DUPDEST = re.compile(r"destination with the same identifier \(name\{([^}]*)\}\)")
RE_ERROR = re.compile(r"^(?:! .+|(?:\./)?[^\s:]+\.tex:\d+: .+)$")


def check_log(path, threshold, tolerate_undefined=False):
    """Returns (status, summary, details) for check 8 on one log file."""
    if not path.exists():
        return FAIL, f"{rel(path)} not found", []
    lines = unwrap_log(path.read_text(encoding="utf-8", errors="replace"))
    files = files_at_lines(lines)
    undefined, multi, overfull, errors = [], [], [], []
    dupdest = {}
    undef_any = multi_any = False
    for idx, line in enumerate(lines):
        m = RE_UNDEF.search(line)
        if m:
            undefined.append(f"{m.group(1).lower()} `{m.group(2)}' undefined (page {m.group(3)}, input line {m.group(4)}"
                             + (f" of {files[idx]}" if files[idx] else "") + ")")
            continue
        if RE_UNDEF_ANY.search(line):
            undef_any = True
            continue
        m = RE_MULTI.search(line)
        if m:
            multi.append(f"label `{m.group(1)}' multiply defined")
            continue
        if RE_MULTI_ANY.search(line):
            multi_any = True
            continue
        m = RE_DUPDEST.search(line)
        if m:
            dupdest.setdefault(m.group(1), files[idx])
            continue
        m = RE_OVERFULL.search(line)
        if m:
            pts = float(m.group(1))
            if pts > threshold:
                where = m.group(2).strip()
                overfull.append(f"{pts:.1f}pt {where}" + (f"  [{files[idx]}]" if files[idx] else ""))
            continue
        m = RE_ERROR.match(line)
        if m and not line.startswith("!  ==> Fatal error"):
            errors.append(line.strip())
    details = []
    failed = False
    if errors:
        failed = True
        details.append(f"TeX errors ({len(errors)}):")
        details += ["  " + e for e in errors]
    if undefined or undef_any:
        failed = failed or not tolerate_undefined
        details.append(f"undefined references/citations ({len(undefined)}"
                       + (", plus the summary warning" if undef_any and not undefined else "")
                       + (", tolerated" if tolerate_undefined else "") + "):")
        details += ["  " + u for u in undefined]
    if multi or multi_any:
        failed = True
        details.append(f"multiply defined labels ({len(multi)}"
                       + (", plus the summary warning" if multi_any and not multi else "") + "):")
        details += ["  " + u for u in multi]
    if dupdest:
        failed = True
        details.append(f"duplicate PDF destinations ({len(dupdest)}; links to them land on the first one):")
        details += [f"  {n}" + (f"  [{f}]" if f else "") for n, f in dupdest.items()]
    if overfull:
        details.append(f"Overfull \\hbox over {threshold:g}pt ({len(overfull)}, report only):")
        details += ["  " + o for o in overfull]
    summary = (f"{rel(path)}: {plural(len(errors), 'error')}, {len(undefined)} undefined, "
               f"{len(multi)} multiply defined, {len(dupdest)} duplicate destinations, "
               f"{len(overfull)} overfull > {threshold:g}pt")
    return (FAIL if failed else OK), summary, details


# --------------------------------------------------------------------------- report
class Report:
    def __init__(self, verbose):
        self.sections = OrderedDict()   # section title -> list of (no, title, status, summary, details)
        self.verbose = verbose
        self.failures = []

    def add(self, section, no, title, status, summary, details=()):
        self.sections.setdefault(section, []).append((no, title, status, summary, list(details)))
        if status == FAIL:
            self.failures.append((section, no))

    def print(self):
        for section, checks in self.sections.items():
            print(f"\n=== {section} ===")
            for no, title, status, summary, details in checks:
                head = f"[{no}] {title}"
                print(f"{head:<38}{status:<5} {summary}")
                shown = details if self.verbose or len(details) <= DETAIL_CAP else details[:DETAIL_CAP]
                for d in shown:
                    print("      " + d)
                if len(shown) < len(details):
                    print(f"      ... {len(details) - len(shown)} more (use --verbose)")


# --------------------------------------------------------------------------- main
def main(argv=None):
    ap = argparse.ArgumentParser(description="Structural checks of the LaTeX edition against inventory/chN.csv.")
    ap.add_argument("--chapter", action="append", default=[], metavar="chN",
                    help="restrict chapter checks to this chapter (ch1 or 1); repeatable")
    ap.add_argument("--aux", nargs="+", default=None, metavar="PATH",
                    help="use these .aux files instead of build/main.aux")
    ap.add_argument("--log", default=None, metavar="PATH", help="log file for check 8")
    ap.add_argument("--overfull", type=float, default=20.0, metavar="PT",
                    help="report Overfull \\hbox wider than this many points (default 20)")
    ap.add_argument("--tolerate-undefined", action="store_true",
                    help="report undefined references without failing (for standalone unit builds, "
                         "whose cross-chapter references are expected to be undefined)")
    ap.add_argument("--verbose", action="store_true", help="never truncate detail lists")
    args = ap.parse_args(argv)

    problems = []          # input problems that are not check failures but must be visible
    report = Report(args.verbose)

    # ---- aux files (one "document" per root aux) ----
    if args.aux:
        roots = [Path(p) if Path(p).is_absolute() else ROOT / p for p in args.aux]
    else:
        roots = [ROOT / "build" / "main.aux"]
        if not roots[0].exists():
            print("build/main.aux not found: no full build is available.\n"
                  "Run   make all   from the project root (latexmk main.tex -> build/main.pdf), then rerun\n"
                  "python3 tools/check_numbering.py.  (For a single unit's .aux use --aux PATH.)")
            return 1
    missing_roots = [r for r in roots if not r.exists()]
    if missing_roots:
        print("aux file(s) not found: " + ", ".join(rel(r) for r in missing_roots))
        return 1

    labels, docs = [], []
    for root_aux in roots:
        seen = set()
        doc_labels = parse_aux(root_aux, rel(root_aux), seen, problems)
        labels += doc_labels
        docs.append((root_aux, sorted(rel(Path(s)) for s in seen), doc_labels))

    # ---- chapters ----
    requested = [norm_chapter(c) for c in args.chapter]
    chapters = set(requested)
    for p in (ROOT / "chapters").glob("ch*.tex"):
        m = re.fullmatch(r"(ch\d+)\.tex", p.name)
        if m:
            chapters.add(m.group(1))
    for p in (ROOT / "inventory").glob("ch*.csv"):
        m = re.fullmatch(r"(ch\d+)\.csv", p.name)
        if m:
            chapters.add(m.group(1))
    titles = {}
    chapters_json = ROOT / "inventory" / "chapters.json"
    if chapters_json.exists():
        try:
            meta = json.loads(chapters_json.read_text(encoding="utf-8"))
            for ch, info in meta.items():
                chapters.add(ch)
                if isinstance(info, dict) and info.get("title"):
                    titles[ch] = info["title"]
        except ValueError as exc:
            problems.append(f"inventory/chapters.json: {exc}")
    chapters = sorted(chapters, key=chapter_key)
    if requested:
        chapters = [c for c in chapters if c in requested]

    labels_by_chapter = defaultdict(list)
    for lab in labels:
        labels_by_chapter[lab.chapter].append(lab)

    manifest = load_manifest(ROOT / "figures" / "manifest.csv", problems)

    # every chapters/*.tex, comment-stripped, grouped by chapter
    tex_by_chapter = defaultdict(list)     # chapter -> [(relpath, stripped text)]
    all_includes = []                      # (relpath, line, path)
    for p in sorted((ROOT / "chapters").glob("*.tex")):
        m = re.match(r"(ch\d+)(?:-|\.tex$)", p.name)
        ch = m.group(1) if m else "other"
        text = strip_comments(p.read_text(encoding="utf-8", errors="replace"))
        tex_by_chapter[ch].append((rel(p), text))
        for line, path in find_includegraphics(text):
            all_includes.append((rel(p), line, path))

    # ---- header ----
    print("check_numbering.py -- structural checks of the LaTeX edition")
    for root_aux, files, doc_labels in docs:
        extra = [f for f in files if f != rel(root_aux)]
        print(f"aux: {rel(root_aux)}" + (f" + {len(extra)} \\@input file(s): {', '.join(extra)}" if extra else "")
              + f"  ({plural(len(doc_labels), 'label')})")
    inventoried = [c for c in chapters if (ROOT / "inventory" / f"{c}.csv").exists()]
    skipped = [c for c in chapters if c not in inventoried]
    print("chapters with inventory: " + (", ".join(inventoried) or "none")
          + (f";  skipped for checks 1-2 (no inventory/chN.csv): {', '.join(skipped)}" if skipped else ""))
    unknown = Counter(lab.chapter for lab in labels if lab.chapter not in chapters)
    if unknown:
        print("labels outside the checked chapters (informational): "
              + ", ".join(f"{k or '(no prefix)'} x{v}" for k, v in sorted(unknown.items(), key=lambda kv: str(kv[0]))))
    # stale-build warning
    if not args.aux:
        aux_mtime = roots[0].stat().st_mtime
        newer = sorted(rel(p) for p in list((ROOT / "chapters").glob("*.tex")) + [ROOT / "preamble.tex", ROOT / "main.tex"]
                       if p.exists() and p.stat().st_mtime > aux_mtime)
        if newer:
            stamp = time.strftime("%Y-%m-%d %H:%M", time.localtime(aux_mtime))
            print(f"WARNING: build/main.aux ({stamp}) is older than {plural(len(newer), 'source file')} "
                  f"({', '.join(newer[:4])}{', ...' if len(newer) > 4 else ''}); rerun make all before trusting the results")

    # ---- per-chapter checks ----
    for ch in chapters:
        section = ch + (f" -- {titles[ch]}" if ch in titles else "")
        ch_labels = labels_by_chapter.get(ch, [])
        by_name = {}
        for lab in ch_labels:
            by_name.setdefault(lab.name, lab)
        kinds = Counter(lab.kind for lab in ch_labels if lab.kind)
        inv_path = ROOT / "inventory" / f"{ch}.csv"

        if inv_path.exists():
            inventory = load_inventory(inv_path, problems)
            renum_path = ROOT / "inventory" / f"{ch}-renumber.json"
            renumber = load_renumber(renum_path, problems) if renum_path.exists() else {}
            inv_keys = {}
            for row in inventory:
                k = (row["kind"], row["number"])
                if k in inv_keys:
                    problems.append(f"{rel(inv_path)}:{row['line']}: duplicate row {row['kind']} {row['number']}")
                inv_keys.setdefault(k, row)

            # check 1: inventory rows vs \newlabel
            missing = [row for row in inventory if f"{ch}:{row['kind']}:{row['number']}" not in by_name]
            extra, new_eqs, parents = [], [], []
            for lab in ch_labels:
                k = lab.key
                if not k or k in inv_keys:
                    continue
                kind, num = k
                if kind == "eq" and is_new_equation(num):
                    new_eqs.append(lab)
                elif kind == "eq" and num.isdigit() and any((kind, num + c) in inv_keys for c in "abcdefghij"):
                    parents.append(lab)
                else:
                    extra.append(lab)
            details = []
            if missing:
                by_unit = OrderedDict()
                for row in missing:
                    by_unit.setdefault(row["unit"] or "(no unit)", []).append(row)
                for unit, rows in by_unit.items():
                    items = ", ".join(f"{r['kind']} {r['number']} (p{r['pdf_page'] or '?'})" for r in rows)
                    details.append(f"missing, unit {unit}: {items}")
            for lab in extra:
                details.append(f"not in inventory: {lab.name} (displayed {lab.number}, PDF page {lab.page}, {lab.source}:{lab.line})")
            for lab in new_eqs:
                details.append(f"info: corrected-edition equation {lab.name} (displayed {lab.number})")
            for lab in parents:
                details.append(f"info: subequations group label {lab.name} (lettered members are in the inventory)")
            status = FAIL if (missing or extra) else OK
            counts = ", ".join(f"{k} {kinds.get(k, 0)}" for k in KINDS)
            summary = (f"{len(inventory) - len(missing)}/{len(inventory)} inventory rows labelled, "
                       f"{len(missing)} missing, {len(extra)} extra (aux has {counts}"
                       + (f"; renumber map {rel(renum_path)}" if renumber else "") + ")")
            report.add(section, 1, "inventory rows vs \\newlabel", status, summary, details)

            # check 2: displayed numbers
            compared, mismatches = 0, []
            for lab in ch_labels:
                k = lab.key
                if not k or (k[0] == "eq" and is_new_equation(k[1])):
                    continue
                compared += 1
                expected, renumbered = expected_number(k[0], k[1], renumber)
                shown = lab.number
                if k[0] in ("fig", "plate"):      # a panel figure displays 5(a) for label 5a (\figurepanel)
                    shown = re.sub(r"^(\d+)\(([a-z])\)$", r"\1\2", shown)
                if shown != expected:
                    mismatches.append(f"{lab.name}: displayed {lab.number!r}, expected {expected!r}"
                                      + (" (from renumber map)" if renumbered else "") + f"  [{lab.source}:{lab.line}]")
            report.add(section, 2, "displayed numbers", FAIL if mismatches else OK,
                       f"{compared} labels compared, {len(mismatches)} mismatch(es)", mismatches)
        else:
            report.add(section, 1, "inventory rows vs \\newlabel", INFO, f"skipped: no inventory/{ch}.csv"
                       + (f" (aux has {', '.join(f'{k} {v}' for k, v in sorted(kinds.items()))})" if kinds else ""))
            report.add(section, 2, "displayed numbers", INFO, "skipped: no inventory")

        # check 4: figure files
        ch_tex = tex_by_chapter.get(ch, [])
        details, failed = [], False
        owned = [row for row in manifest if row["chapter"] == ch]
        blank = [row for row in owned if not row["output"]]
        for row in owned:
            if not row["output"]:
                continue
            stems = {graphic_stem(row["output"]), graphic_stem("figures/" + row["output"])}
            hits = [(f, l) for f, l, p in all_includes if graphic_stem(p) in stems]
            if len(hits) != 1:
                failed = True
                where = ", ".join(f"{f}:{l}" for f, l in hits)
                details.append(f"manifest {row['id'] or ('row ' + str(row['line']))} output {row['output']} (owner {row['owner'] or 'blank'}): "
                               + ("not included by any \\includegraphics" if not hits else f"included {len(hits)} times: {where}"))
        for name in blank:
            details.append(f"info: manifest {name['id'] or ('row ' + str(name['line']))} (owner {name['owner']}) has no output yet")
        inferred = [row for row in owned if row["owner_inferred"]]
        if inferred:
            details.append(f"info: {len(inferred)} of {len(owned)} manifest rows have no owner unit; "
                           f"chapter taken from the id/output column")
        n_inc = 0
        manifest_stems = {graphic_stem(r["output"]) for r in manifest if r["output"]} | \
                         {graphic_stem("figures/" + r["output"]) for r in manifest if r["output"]}
        for relpath, text in ch_tex:
            for line, path in find_includegraphics(text):
                n_inc += 1
                if not graphic_exists(path):
                    failed = True
                    details.append(f"{relpath}:{line}: \\includegraphics{{{path}}} does not exist on disk")
                elif manifest and graphic_stem(path) not in manifest_stems:
                    details.append(f"info: {relpath}:{line}: {path} is not listed in figures/manifest.csv")
        report.add(section, 4, "figure files", FAIL if failed else OK,
                   f"{len(owned) - len(blank)} manifest outputs owned by {ch}, {n_inc} \\includegraphics in its files", details)

        # check 5: float environments
        n_env, details = check_floats(ch, ch_tex)
        report.add(section, 5, "float environments", FAIL if details else OK,
                   f"{plural(n_env, 'figure/plate/table environment')}, "
                   f"{'problems found' if details else 'each with one caption and one label'}", details)

        # check 6: forbidden macros
        details = check_forbidden(ch_tex)
        report.add(section, 6, "forbidden macro definitions", FAIL if details else OK,
                   f"{len(details)} found in {plural(len(ch_tex), 'file')}", details)

        # check 7: draftnotes (report only)
        counts, total = [], 0
        for relpath, n in count_draftnotes(ch_tex):
            total += n
            name = Path(relpath).stem
            if name != ch or n:
                counts.append(f"{name} {n}")
        report.add(section, 7, "\\draftnote count (report only)", INFO,
                   f"{total} total: " + (", ".join(counts) or "no unit files"))

    if "other" in tex_by_chapter and not requested:
        details = check_forbidden(tex_by_chapter["other"])
        report.add("other files under chapters/", 6, "forbidden macro definitions", FAIL if details else OK,
                   f"{len(details)} found in {', '.join(r for r, _ in tex_by_chapter['other'])}", details)

    # ---- document-level checks ----
    for root_aux, files, doc_labels in docs:
        section = f"document {rel(root_aux)}"
        details = []
        anchors = defaultdict(list)
        names = Counter(lab.name for lab in doc_labels)
        for lab in doc_labels:
            if lab.name.startswith("page.") or lab.anchor.startswith("page.") or not lab.anchor:
                continue
            anchors[lab.anchor].append(lab)
        dups = {a: labs for a, labs in anchors.items() if len(labs) > 1}
        for a, labs in sorted(dups.items()):
            details.append(f"anchor {a} shared by: " + ", ".join(f"{l.name} ({l.source}:{l.line})" for l in labs))
        for name, n in sorted(names.items()):
            if n > 1:
                details.append(f"label {name} written {n} times in the .aux files")
        n_anch = sum(len(v) for v in anchors.values())
        report.add(section, 3, "anchor uniqueness", FAIL if details else OK,
                   f"{n_anch} anchored labels, {len(dups)} duplicate anchor(s)", details)

        if args.log:
            log_path = Path(args.log) if Path(args.log).is_absolute() else ROOT / args.log
        elif args.aux:
            log_path = root_aux.with_suffix(".log")
            if not log_path.exists():
                log_path = ROOT / "build" / "main.log"
        else:
            log_path = ROOT / "build" / "main.log"
        status, summary, details = check_log(log_path, args.overfull, args.tolerate_undefined)
        report.add(section, 8, "log: references, labels, boxes", status, summary, details)

    if problems:
        report.add("input problems", "-", "inputs", INFO, f"{len(problems)} note(s)", problems)

    report.print()
    print()
    if report.failures:
        where = ", ".join(f"{s.split(' -- ')[0]} [{n}]" for s, n in report.failures)
        print(f"RESULT: FAIL -- {plural(len(report.failures), 'failing check')}: {where}")
        return 1
    print("RESULT: OK -- all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
