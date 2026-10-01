# v2 consistency check: ch3/fig21

The issue resolved here is the panel-letter placement inside the plot axes (Figs 21 and 26). The approved figures
place the letter with `\node[panel, anchor=north east] at (rel axis cs:1,1)`. Fig 21 had added `inner sep=1.5pt,
xshift=-1pt, yshift=-1pt`. I am the verifier only and made no edits.

Sources checked:
- `figures/v2/ch3/fig21.tex` (current) and `fig21.pdf`; `fig21-a.csv`, `fig21-b.csv`, `fig21.calib.json`.
- The round-2 audit's 300 dpi render (taken before this fix) and the fixer's before and after crops.
- `build/v2/png/ch3-fig21-compare.png` (rebuilt by the fixer).
- `figures/v2/tamrfig.sty` (`panel`, `tamr grid`); STYLE.md section 16.
- The approved placements in Ch3 Fig 53, Ch1 Figs 3 and 5, and Ch2 Figs 20 and 46.
- The scan `figures/ch3/fig21.png`; inventory row `ch3-fig21`; `audit/v2-ch3-fig21-round1.md` and `-round2.md`.
- My own builds in the scratch dir: the current source, plus a variant without `fill=white`. I rendered them at
  300 and 600 dpi.

Checks made:
- **Source.** Both letters now read `\node[panel, anchor=north east, fill=white] at (rel axis cs:1,1)`.
  `inner sep=1.5pt, xshift=-1pt, yshift=-1pt` are gone, so the kit's `panel` inner sep (1pt) applies. The header
  comment records the placement and why the fill is kept. There is no local `\tikzset`, and no kit style is
  redefined.
- **Tree PDF is current.** My scratch build of the current source renders pixel-identical to the PDF in the tree
  at 300 dpi.
- **Placement against the approved figures.** These were measured with `pdftotext -bbox` against the tick-label
  centres of the right and top rulings.
  - The right side of (a) and of (b) sits 1.196 pt inside the right ruling. This equals Fig 53's (a) to the
    0.001 pt.
  - The tops sit 0.03 pt below the top ruling for (a) and 0.27 pt for (b). Fig 53 gives 0.04 and 0.28.
  - At 600 dpi the ink of "(a)" spans x -104 to -16 px and y 10 to 79 px from the corner. Fig 53's "(a)" spans
    x -104 to -16 and y 11 to 80. They match to 1 px, which is ruling rounding.
  - So the letters have moved up and right by about 1.5 pt to the approved corner. The fixer's "about 8 px at
    400 dpi" agrees.
  - Fig 26 has since been changed to the same spec (fig26.tex:24, 30). Figs 21, 26 and 53 now match.
- **The white fill is justified.** This was the issue's condition: keep `fill=white` only where a gridline would
  cross the letter.
  - Without the fill, the u/U = 0.9 minor ruling (600 dpi columns -107 to -105 from the corner) merges with the
    outer bulge of "(". The ink overlaps by 1 px over about 15 rows, so the line visibly touches the letter.
  - With the fill, the ruling is blanked only over the letter box and resumes just below it. This echoes the
    scan, whose rulings break around the circled letters.
  - Fig 53's rulings are 0.42 in apart, and none of them reaches its letters, so leaving its letters unfilled is
    consistent with the same rule.
- **Border rulings are intact.** The node's outer sep keeps the fill 0.2 pt inside the corner.
  - At 600 dpi the right ruling (u/U = 1.0) is 4 px wide (grey 205) beside the letters, the same as far below.
  - The top ruling (eta = 4) is 3 px wide above the letters, the same as further left.
  - This holds for both panels.
- **No regression.**
  - The current 300 dpi render (1532 x 1014 px) differs from the round-2 audit's render only in two 52 x 52 px
    boxes at the two letters: x 627-678 and 1434-1485, y 29-81.
  - Page 367.551 x 243.238 pt (5.10 x 3.38 in), unchanged; all fonts are embedded.
  - The curves, ticks, titles and frame are unchanged.
  - I re-ran the overlays (`digitize.py overlay`, residual 0.00 px). (a): mean 0.32 px, 95% 1.00 px, max
    1.41 px. (b): mean 0.68 px, 95% 2.24 px, max 2.83 px. Both are ok and identical to rounds 1 and 2.
  - The letters stay well clear of the curves, which end at eta 2.69 and 1.55.
- **Against the inventory and the scan.** Every lettered item is still present: the eta_2-D and eta_3-D titles,
  u/U without the infinity subscript, y ticks 0-4 with a grid every 0.5, and x ticks 0, 0.5, 1.0 with a grid
  every 0.1. The circled letters at eta = 3 are now in the house panel style, as accepted in rounds 1 and 2.
- **Baselines.** The baselines of (a) and (b) differ by 0.24 pt. This comes from the north anchor and the taller
  "b", the same as in Fig 53 and Ch2 Fig 20. It is house behaviour, and the round-2 audit already noted it.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The header says the 0.9 ruling "runs through" the letters. Strictly, the ruling touches the outer edge of "(" (a 1 px overlap at 600 dpi) rather than crossing the glyph. The fill is still justified. | fig21.tex:6-7 | None needed. |
| 2 | note | Figs 21 and 26 now both use `panel` with `fill=white` on gridded axes. The round-2 kit suggestion (a `panel on grid` style) remains open for the orchestrator. It is not a defect in this figure. | fig21.tex:21, 26 | Orchestrator's call. |

## Verdict: pass

The issue is resolved, there is no regression, and nothing is must-fix or should-fix.
