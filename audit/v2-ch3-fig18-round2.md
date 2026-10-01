# v2 audit: ch3/fig18 (round 2)

Sources checked: the scan `figures/ch3/fig18.png`; the redraw `figures/v2/ch3/fig18.pdf` (current by `make -q`;
304.2 x 168.8 pt = 4.22 x 2.34 in; fonts all embedded), rendered at 400 dpi; `build/v2/png/ch3-fig18-compare.png`;
`figures/v2/ch3/fig18.tex`, `fig18.py`, `fig18-*.csv` and `fig18.calib.json`; the inventory row `ch3-fig18`; the
caption and citing text in `chapters/ch3-sec3b.tex`:382-420; the round-1 report and the fix notes. Round 1 passed
with no must-fix or should-fix items. The fix round changed nothing.

Checks made:
- **Falkner-Skan, re-solved independently** with solve_bvp, f''' + f f'' + beta (1 - f'^2) = 0. (a), beta =
  -0.1983: f''(0) = 0.020, eta99 = 4.693, one inflection at y/delta = 0.479 and u/U = 0.502. Mapped with
  delta = 142.5 px, U = 166 px and the base at x = 32, that is (115.3, 68.3), against fig18-marks.csv
  (115.39, 68.21). (b), beta = +0.07: f''(0) = 0.554 and no inflection inside the layer, so (b) is "fully
  convex", as the caption says.
- **Overlay**, run myself: (a) 95% within 3.16 px (max 4.00), (b) 2.24 px. These are the same as round 1.
- **Lettering and house rules.** y, $U_\infty$, u(y) and the edge circles are in both panels. The delta
  dimension is upright in its gap. "Point of inflection" has a straight leader. The panel letters (a) and (b)
  are in `panel` style at the lower right on one baseline (y = -14). Both panels share one frame, and the wall
  bands (10 px, 45 deg) match Fig 25.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note (gate) | Carried from round 1: the inflection circle, placed by the equation, is about 21 px (4.3 mm) from the 1973 circle. There is still no entry in `corrections/v2-figures.md`. | fig18.tex:5-7; fig18-marks.csv | orchestrator: log it with the Ch3 items |
| 2 | note | No regressions: the file is unchanged since round 1, and the overlay and inflection numbers are the same. | -- | none |

## Verdict: pass (no must-fix)
