# v2 audit: ch2/fig49 (round 1)

Sources checked: scan `figures/ch2/fig49.png` (3x upscale of the left part); redraw `figures/v2/ch2/fig49.pdf`
(300 dpi render) and `build/v2/png/ch2-fig49-compare.png`; `figures/v2/ch2/fig49.tex` lines 1-22, `fig49.py`,
`fig49.csv`, `fig49.calib.json`; inventory row `ch2-fig49` (`figures/v2/inventory.csv`:62);
`chapters/ch2-sec3b.tex`:517-519 (eq. (50)); `chapters/ch2-sec3d.tex`:416-418 (eq. (75)); `chapters/ch2-sec6.tex`:
151-156 (citing text), :159-165 (caption), :547-553 (1.746 at $\zeta = 0.3$, "see Figure 49"; ten times at 0.05);
`corrections/v2-figures.md` (Ch2 Fig 49 gate item and the pilot decision); `STYLE.md` sections 13, 16.

Checks made:
- **Formula.** `fig49.py` computes eq. (50), $\mathit{AR}_{\mathrm{res}} = 1/(2C_1\zeta\sqrt{1-\zeta^2})$, in units of
  $1/C_1$. It uses 301 points spaced evenly in $\log\zeta$, from $\zeta_8 = 0.06262$ (where the curve enters the
  frame at $8/C_1$) to 0.7. The rows agree with an independent evaluation to $4\times10^{-4}$: the only
  difference is the five-decimal rounding of $\zeta$ on the steep first rows. The curve lies within
  $\zeta < \sqrt2/2$, where eq. (50) holds.
- **Points evaluated** (units of $1/C_1$); the render agrees with each:

  | $\zeta$ | 0.0626 | 0.1 | 0.2 | 0.3 | 0.5 | 0.7 |
  |---|---|---|---|---|---|---|
  | $\mathit{AR}_{\mathrm{res}}$ | 8.00 | 5.03 | 2.55 | 1.747 | 1.155 | 1.000 |

  The text's 1.746 at 0.3 ("see Figure 49") reads correctly off the redraw. The caption's coupled form, eq. (75),
  is the same function.
- **Lettering.** Everything matches the scan and the inventory:
  - y title $\mathit{AR}_{\mathrm{res}}$ [rad/(dyn-cm)], with an upright "res" (STYLE section 13).
  - y ticks 0, $\frac2{C_1}$, $\frac4{C_1}$, $\frac6{C_1}$, $\frac8{C_1}$, upright stacked fractions, with minor
    ticks at 1, 3, 5 and 7.
  - x title $\zeta$; x ticks 0, 0.1, ... 0.7, with minor ticks every 0.05.
- **Known gate item.** The 1973 curve reaches $8/C_1$ at $\zeta \approx 0.052$ against the computed 0.0626. The
  pilot gate decided to use the computed curve. The overlay (computed against the scan) gives a mean of 1.65 px,
  a 95th percentile of 5.10 px (0.86 mm) and a maximum of 8.06 px. The departure is confined to
  $\zeta < 0.1$; elsewhere the two agree within the line width. This is consistent with the logged item.
- **Size and legibility.** 4.87 in wide, with 4.2 in by 2.6 in axes; the height follows the scan's flatter aspect.
  All fonts are embedded. There are no overlaps, and the curve ends cleanly at the top of the y axis, as printed.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | `fig49.calib.json` fits with a 5.56 px residual. The calibration's xgrid and ygrid tables (piecewise, which the tool uses in place of the affine fit) put the computed curve on the scan's ink for $\zeta > 0.1$, so the overlay numbers above stand. | fig49.calib.json | none |
| 2 | note | The figure is 2.6 in tall where Figs 24, 25, 30 and 31 are 3.0 in. This is justified by the scan's aspect (plot area about 0.55 high:wide). | fig49.tex:10 | none |

## Verdict

pass (0 must-fix, 0 should-fix)
