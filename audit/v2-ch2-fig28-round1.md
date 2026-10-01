# v2 audit: ch2/fig28 (round 1)

Sources checked: scan `figures/ch2/fig28.png` (zoomed: the $M_s/C_1$ label and dashed line, origins);
inventory row `ch2-fig28`; caption and citing text `chapters/ch2-sec3d.tex:1-154` (eqs. (61)-(64), the
$A_1\sin\varphi_1$, $A_1\cos\varphi_1$, $A_2\sin\varphi_2$, $A_2\cos\varphi_2$ displays); credit
`backmatter/figure-credits.tex:65`; `corrections/ch2.md`, `corrections/v2-figures.md` (nothing on this
figure); redraw `figures/v2/ch2/fig28.{tex,py,csv,calib.json,pdf}` and `fig28-marks.csv`;
`build/v2/png/ch2-fig28{,-compare}.png`; my own 400 dpi render; `digitize.py overlay`; STYLE.md sections 13 and
16; sibling Figs 26, 27, 29.

Checks made:
- Lettering: upper $\dfrac{M_s}{C_1}$ (stacked tick label with tick, its bar on the dashed line as printed),
  0, $\alpha_X$ (rad), $t$ (sec); lower 0, $\alpha_Y$ (rad), $t$ (sec). All present. Nothing added.
- Curves: the script's $A_1\sin\varphi_1$, $A_2\sin\varphi_2$, (63a), (63b), (64a), (64b) match the book's
  displays term by term (checked against the general formulas with $\alpha_{X0} = -M_s/C_1$). My independent
  integration of the stepped coupled equations from rest ($C_2 = 0.47$, $M_s/C_1 = 1.33$) agrees with the
  CSV to $5\times10^{-6}$. One motion for both plots.
- Shapes: upper from 0 with zero slope, overshoot 1.75 (t 3.4), dip to 1.12 below the asymptote (t 8.9),
  back to 1.44 at the end, approaching $M_s/C_1$ (caption); lower from 0 with zero slope, first lobe
  positive (0.58) as $I_R\omega_Z\,\dot\alpha_X > 0$ requires, trough $-0.36$, decaying to 0.04 (caption:
  pitching decays to zero).
- Asymptote: `guide` (dashed, the house style for asymptotes) at $\alpha_X = 1.33$ from the axis to the
  curve's end, as printed; overlay on the 1973 dashed line 95% 2.0 px.
- Overlay (fitted calibration): upper curve 95% 1.00 px, lower 3.00 px (max 4.0): within target.
- Size 320.0 x 346.0 pt (4.44 x 4.81 in); fonts embedded; layout identical to Figs 26, 27, 29.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The 1973 dashed line is heavy; the redraw's `guide` (0.4 pt, ink2) is lighter but clearly dashed at final size. The house style sets it so, and neither the caption nor the text names the line style. | `fig28.tex:26` | none |
| 2 | note | The printed vertical titles become upright titles above the arrows (the `tamr sketch` placement, with the same `every axis y label` override as the other sketch figures). | `fig28.tex:10-14`; `tamrfig.sty` | style suggestion: drop `rotate=-90` from `tamr sketch`'s `ylabel style` |

## Verdict: pass (no must-fix)
