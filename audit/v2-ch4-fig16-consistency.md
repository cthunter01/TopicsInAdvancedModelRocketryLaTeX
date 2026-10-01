# v2 audit: ch4/fig16 (chapter consistency fix, verification)

Issues to resolve:
1. The solution method. Fehskens-Malewicki (eqs. (20), (21), (67)) is used here, while Figs 6 and 11 use the
   interval method (83)-(87). Does the relayed "use exact curves for 46" cover this figure?
2. The k labels are `\small`; every other Chapter 4 curve label is `\footnotesize`.

The fixer declined 1 (FM kept; data unchanged) and applied 2.

Sources checked:
- Scan `figures/ch4/fig16.png` and `build/v2/png/ch4-fig16-compare.png`.
- `fig16.tex`. I diffed it against the fixer's pre-fix copy (`.../polish/fig16-before.tex`): the only changes
  are `font=\footnotesize` in the label scope and four header comment lines.
- `fig16.py`, `fig16.csv`, `fig16-bengen.csv`, `fig16.calib.json`.
- Inventory row `ch4-fig16`.
- `chapters/ch4-sec5.tex`:60-86, 158-170.
- `corrections/v2-figures.md`, all of it, including the uncommitted diff, and the HEAD version.
- `audit/v2-ch4-fig16-round1.md` and `-round2.md`.
- STYLE.md s16. The k labels and legends in `ch4/fig06a.tex`, `fig10.tex`-`fig14.tex` and `ch2/fig25.tex`.

## Issue 1: properly declined

- **What the relayed line refers to.** "Keep 1-3 as they are, use exact curves for 46" is the Chapter 3 gate
  answer. The Chapter 3 section of `corrections/v2-figures.md` lists, in order, gate items for Fig 9, Fig 12 and
  Fig 28, then Fig 46: "exact eqs. (171a), (171d)" against `\exactfalse`.
- **Where it is recorded.** The decision is already in HEAD (365605b, 2026-10-01 07:38), at line 156: "Chapter 3
  gate (user, 2026-10-01): Figs 9, 12 and 28 kept as redrawn ...; Fig 46 keeps the EXACT curves of (171a) and
  (171d)". That matches the relayed line item for item.
- **Why it cannot mean Ch4.** Chapter 4 has no Figure 46.
- **Conclusion.** The line does not decide Ch4 Fig 16. Keeping FM until the Chapter 4 gate is the right call.
  The book backs it: ch4-sec5.tex:80-82 says such charts are made "using the methods of Section 2", and :64 says
  those methods are the "closed-form, algebraic solutions". The print backs it too (overlay below).
- **Data.** I reran `fig16.py` in scratch (FM). `fig16.csv` and `fig16-bengen.csv` are byte-identical (md5
  2efeef6c..., e1486c06...).
- **Overlay**, rerun with `fig16.calib.json` (residual 0.00 px):
  - FM, the six curves: 95% within 1.00, 1.41, 1.00, 1.00, 1.00 and 1.00 px.
  - FM, Bengen line: 95% within 3.63 px (0.61 mm), max 5.0 px. This is over the 3 px tolerance and unchanged
    from rounds 1 and 2.
  - Interval method (METHOD = "interval" in a scratch copy), the six curves: 95% within 3.16, 2.83, 3.16, 3.00,
    2.00 and 2.00 px.
  - Interval method, Bengen line: 95% within 5.41 px.
  - All of the fixer's numbers reproduce exactly.
- **The interval variant, prepared for the gate.** I built it in scratch with interval CSVs and the label and
  callout positions listed in the new header comment, with the knock-out boxes outlined, at 600 dpi.
  - Every box clears the curves by 0.36-0.76 mm and the Bengen line by 0.44-0.72 mm.
  - The callout point (.0240, 640) lies on the interval Bengen line, which is at m_o .02401 at 640 m.
  - The header's recipe is correct. Switching takes `fig16.py` about 5 s.
- **Still open, for the orchestrator** (not a figure change). Audit round 2 finding 1 asked for a Chapter 4 entry
  in `corrections/v2-figures.md`, and it is still absent: the file has no "Ch4 Fig 16" or "Bengen" line. The
  entry should record:
  - FM per Section 5.1;
  - the overlay figures;
  - the Bengen line at 3.6 px, with its lower end at .0378 kg against about .040 drawn;
  - the FM-versus-interval question, as a **gate** item.

  The fixer's proposed text is accurate, with one correction: cite ch4-sec5.tex:64 and :80-82, not :70-82.

## Issue 2: resolved

- **The fix.** The label scope now reads
  `every node/.style={fill=white, inner sep=1.2pt, font=\footnotesize}`.
  - This matches the k_max/k_min labels of fig06a (`\footnotesize`), the time labels of Figs 10-14 (`font=\footnotesize`)
    and the Ch2 Fig 25 curve labels.
  - The digits measure 2.12-2.16 mm at 600 dpi, i.e. 9 pt.
  - The callout "Line of Bengen's maxima" and "$m_o$ of engine alone" stay `\small`, like the axis titles and other
    text labels.
- **Clearance.** I measured it on a scratch copy with the knock-outs outlined in colour, at 600 dpi.
  - Each white box clears the curves by 0.51-0.65 mm and the Bengen line by 0.38-0.72 mm. The closest is
    ".0016" to the lower end of the line, at 0.38 mm.
  - With the 1.2 pt inner sep, the ink clears by about 0.8-1.1 mm, the "about 1 mm" of rounds 1 and 2.
  - No knock-out covers a curve or the line.
  - The anchors are unchanged (south west, and west for .00005), so each box is a subset of its earlier `\small`
    box.
- **Build.** A scratch recompile of the current `.tex` renders pixel-identical to `figures/v2/ch4/fig16.pdf` at
  400 dpi (empty difference bounding box).
  - Page 325.28 x 414.11 pt (4.52 x 5.75 in, unchanged).
  - No LaTeX warnings.
  - All fonts embedded.
  - No `/ca`, `/CA`, `/SMask` or shading.

## No regressions

- **Against the scan and the inventory row**, everything is as audited in rounds 1 and 2:
  - the six curves and their values (maxima (.0250, 536.8) ... (.0378, 68.6); engine-alone .021 kg);
  - the grid every .01 kg and 100 m;
  - all lettering, with the leading-dot k values;
  - the callout on the computed line (m_o .02375 at 640 m);
  - the engine line as `guide`, the locus as `series2`;
  - the caption's claims (the Bengen line lies right of the engine-mass line).
- **Kit.** No kit names are redefined.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix (orchestrator; no figure change) | Carried from audit round 2, finding 1. `corrections/v2-figures.md` still has no Chapter 4 entry for Fig 16. It should record the FM method per Section 5.1, the overlay evidence (FM curves 1.0-1.4 px against interval 2.0-3.2 px), the Bengen line at 3.6 px over tolerance with its lower end at .0378 kg against about .040 drawn, and the FM-versus-interval question for the Chapter 4 gate. | `corrections/v2-figures.md`, Chapter 4 | Orchestrator: add the fixer's proposed entry, with the citation changed to ch4-sec5.tex:64, 80-82. Mark it **gate**. |
| 2 | note | The `fig16.py` docstring (line 6) cites "ch4-sec5.tex:70-77" for "the methods of Section 2 ... closed-form, algebraic solutions". Those phrases are at :81 and :64. The comment is wrong; the data are not affected. | `fig16.py`:6 | Optional: cite :64, 80-82. |

## Verdict: pass

Issue 2 is fixed with no side effects. Issue 1 is properly declined, because the relayed line is the recorded
Chapter 3 gate answer about Ch3 Fig 46. Its follow-up entry in `corrections/v2-figures.md` and the gate question
are left to the orchestrator.
