# v2 audit: ch2/fig29 (round 1)

Sources checked: scan `figures/ch2/fig29.png` (zoomed: the Slope${}= H/I_L$ label and line, origins);
inventory row `ch2-fig29`; caption and citing text `chapters/ch2-sec3d.tex:156-238` (initial conditions,
eqs. (65)-(67)); credit `backmatter/figure-credits.tex:68`; `corrections/ch2.md`, `corrections/v2-figures.md`
(nothing on this figure); redraw `figures/v2/ch2/fig29.{tex,py,csv,calib.json,pdf}` and `fig29-marks.csv`;
`build/v2/png/ch2-fig29{,-compare}.png`; my own 400 dpi render; `digitize.py overlay`; STYLE.md sections 13 and
16; sibling Figs 26-28.

Checks made:
- Lettering: upper Slope${}=\dfrac{H}{I_L}$, 0, $\alpha_X$ (rad), $t$ (sec); lower 0, $\alpha_Y$ (rad), $t$
  (sec). All present, with $I_L$ as printed. Nothing added (no tick label at the origin slope, as printed).
- Curves: $A_1\sin\varphi_1$, (65a), (66a), (67) in the script match the book. My independent integration from
  $(\alpha_{X0}, \alpha_{Y0}, \Omega_{X0}, \Omega_{Y0}) = (0, 0, 3.1, 0)$, $C_2 = 0.47$, agrees with the CSV to
  $1.3\times10^{-4}$ (the t-column rounding times the slope 3.1). One motion for both plots.
- Shapes against the inventory: upper tall first peak 2.05 (t 1.26), a shallow double-dipped negative
  stretch ($-0.28$, $-0.25$, $-0.39$), a small hump 0.32, back to 0.03 at the right end; lower starting
  level (initial pitch rate zero, the caption), positive lobe 0.83, deeper trough $-1.07$, hump 0.45, ending
  at $-0.16$ slightly below the axis.
- Tangent: through the origin with slope $H/I_L = 3.1$ (CSV initial slope 3.08 by first difference), on the
  1973 line (overlay 95% 1.02 px). The fraction label clears the curve's peak by about 0.13 in and the
  $\alpha_X$ (rad) title by about 5 pt.
- Overlay (fitted calibration): upper curve 95% 2.24 px, lower 1.41 px: within target.
- Size 316.9 x 346.0 pt (4.40 x 4.81 in); fonts embedded; layout identical to Figs 26-28.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The printed vertical titles become upright titles above the arrows (the `tamr sketch` placement, with the same `every axis y label` override as the other sketch figures). | `fig29.tex:11-15`; `tamrfig.sty` | style suggestion: drop `rotate=-90` from `tamr sketch`'s `ylabel style` |

## Verdict: pass (no must-fix)
