# v2 audit: ch1/fig03 (round 1)

Sources checked: figures/ch1/fig03.png (scan, upscaled 4x); figures/v2/ch1/fig03.pdf (rendered 300 and 600 dpi);
figures/v2/ch1/fig03.tex:1-47; figures/v2/ch1/fig03.py and fig03.csv; figures/v2/inventory.csv row ch1-fig03;
caption chapters/ch1-sec2a.tex:92-101 and citing text ch1-sec2a.tex:87-90; corrections/v2-figures.md;
figures/v2/tamrfig.sty. Overlay: a calibration of panel (a) written for this audit (every labelled tick, max
residual 1.0 px) and `digitize.py overlay` of the mass curve, the tangent line m = 12.8 - 9(t - 0.4) and the
dashed legs.

Checked and correct:
- **Axes and labels.** y 0-21 step 3, x 0-1.2 step 0.2 (printed with leading zeros, house style), $m$ (g) set
  horizontal left of the axis, $t$ (sec).
- **Tangent construction.** The tangent line runs from t = 0.03 to 1.2 with slope -9 g/sec through (0.4, 12.8),
  where the dot sits. The dashed legs run from (0.2, 14.6) down to (0.2, 9.2) and across to (0.8, 9.2), so
  $\Delta m$ = -5.4 g and $\Delta t$ = 0.6 sec. $\Delta m$ is set beside the vertical leg and $\Delta t$ below
  the horizontal leg. The "Tangent line" leader has its arrowhead.
- **Lettering of (a).** $\Delta m = -5.4$ g; $\Delta t = 0.6$ sec; $dm/dt]_{t=0.4} \cong -9$ g/sec.
- **Table of (b).** Header $t$ (sec) | $m$ (g), with the vertical rule and the rule under the header. All seven
  rows are exact (0.0/21.0 ... 1.2/9.0). The $\Delta t$ bracket spans the rows 0.2-0.6 and the $\Delta m$
  bracket spans 15.1-11.3.
- **Lettering of (b).** $\Delta m = 11.3 - 15.1 = -3.8$ g; $\Delta t = 0.6 - 0.2 = 0.4$ sec;
  $dm/dt]_{t=0.4} \cong -9.5$ g/sec. The arithmetic checks.
- **Mass curve.** It passes exactly through every table value for t = 0.2-1.2. Its slope at t = 0.4 is -9.1
  g/sec, so the drawn line is tangent to it. It stays above the tangent line on both sides (by less than 0.001 g
  within 0.01 sec of the point).
- **Overlay against the scan.** Tangent line: 95% within 1.0 px. Legs: 95% within 1.7 px.
- **Caption.** Everything it relies on is present: the "tangent" line in (a), the table in (b), and negative
  $\Delta m$.
- **Panel letters.** Both are present, in the house `panel` style.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The steep start of the mass curve is read early, and its knee is sharper than printed. fig03.py places the knee at (0.05, 18.8) and (0.10, 16.5). The printed line, sampled column by column at its centre, reads 19.2 g at 0.05 sec, 18.3 at 0.075, 17.3 at 0.10, 16.35 at 0.125 and 15.85 at 0.15. The redraw therefore runs up to 0.8 g below the printed curve at t = 0.075-0.10. It also turns its corner at t = 0.10 (slope -44 to -21 g/sec between 0.08 and 0.11 sec), where the print rounds the knee over 0.10-0.16 sec. This is visible at final size as an angular knee. The overlay passes the tolerance (95% 2.24 px, max 4.0 px), with every outlying point in this stretch. | fig03.py:10-11 (`T`, `M`) | Use T = [0, 0.05, 0.10, 0.125, 0.15, 0.2, ...] and M = [21.0, 19.2, 17.3, 16.35, 15.85, 15.1, ...]. Checked: this passes through the same table values, overlays at 95% 1.0 px (max 1.0 px), and keeps the slope at t = 0.4 at -9.08 g/sec. |
| 2 | should-fix | The "Tangent line" arrow overshoots the line. It ends at (1.02, 7.0), but the line crosses m = 7.0 at t = 1.044. The tip therefore lies 0.024 sec (1.5 mm) past the line, and the whole 4pt head sits on top of the 1pt orange line instead of touching it. In the scan the tip touches the line. | fig03.tex:19 | End the leader at the line, e.g. `-- (axis cs:1.05,7.0)` (or keep 1.02 with `shorten >=` about 1.2 mm). |

## Verdict

pass (0 must-fix, 2 should-fix)
