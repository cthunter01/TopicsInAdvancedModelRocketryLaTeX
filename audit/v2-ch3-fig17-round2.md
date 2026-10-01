# v2 audit: ch3/fig17 (round 2)

Sources checked: the scan `figures/ch3/fig17.png`, with the plate and edges zoomed 4x; the redraw
`figures/v2/ch3/fig17.pdf` (321.6 x 187.7 pt = 4.47 x 2.61 in; fonts all embedded), rendered at 400 dpi, with the
O-B region at 900 dpi; `build/v2/png/ch3-fig17-compare.png`; `figures/v2/ch3/fig17.tex`, `fig17.py`,
`fig17-*.csv` and `fig17.calib.json`; the inventory row `ch3-fig17`; the caption, citing text and Table 2 in
`chapters/ch3-sec3b.tex`:121-168; eqs. (73)-(76) and (80); the round-1 report and the fix notes. Round 1 passed
with no must-fix or should-fix items. The fix round changed nothing.

Checks made:
- **Overlay**, run myself; 95% within: upper edge 12.17 px, profile at O 6.01 px, wake at B 11.52 px. These are
  the same as round 1. All are computed curves under the pilot decision.
- **Equations**, spot-checked from the CSVs. Edge at x = 332.331: 58 (224.331/232)^0.8 = 56.46, and the CSV has
  56.461 (eq. (80)). Profile at O, y = 28.90: 340 + 56 (28.90/58)^(1/7) = 390.70, and the CSV has 390.696
  (eq. (74)). In fig17.py:wake() the one-sided Gaussian momentum integral equals theta = 7 delta/72 (eqs. (73),
  (76)).
- **Build state.** `make -q figures/v2/ch3/fig17.pdf` reports the PDF out of date, because round 1 re-ran
  fig17.py at 22:22 after the 22:17 build and so rewrote its CSVs. I recompiled fig17.tex into a temporary
  directory and deleted it afterwards. The 300 dpi render is pixel-identical to the existing PDF (difference
  bbox None), so only the timestamp is stale.
- **Lettering, line styles, layout.** Everything listed in round 1 is still true: all the inventory lettering is
  present, the edges are dashed to O and solid beyond B, the U_inf references are dashed, the plate is drawn
  heavy to O, and nothing is clipped. The h and delta dimensions meet tip to tip on the plate's plane. The lower
  arrowhead of h, like the y = +5 profile arrows, lies inside the 8 px hatched AB band. It stays legible at
  900 dpi, and the scan has the same overlap.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note (gate) | Carried from round 1: the edges from eq. (80) (near-straight wedges, up to 16 px off the 1973 parabola-like edges) and the wake dip from the momentum balance (u(0) = 0.77 U, against about 0.35 U printed) have no entry in `corrections/v2-figures.md`, although the .tex header cites one. | fig17.tex:5-8 | orchestrator: add the Ch3 gate item |
| 2 | note | Carried from round 1: the corner letters $A$, $A_1$, $B$, $B_1$ and $O$ stay math italic rather than `curve tag`, because Table 2 uses them as segment names ($AA_1$, $A_1B_1$). This exception still needs confirming at the consistency pass. | fig17.tex:64-68 | confirm at the consistency pass |
| 3 | note | fig17.pdf is older than its CSVs, which round 1 rewrote with identical data, so the next `make fig F=ch3/fig17` will rebuild it. A scratch recompile is pixel-identical, so the content does not change. | figures/v2/ch3/fig17.pdf | none (a rebuild only refreshes the timestamp) |

## Verdict: pass (no must-fix)
