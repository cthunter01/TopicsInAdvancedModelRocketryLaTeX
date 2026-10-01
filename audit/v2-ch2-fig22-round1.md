# v2 audit: ch2/fig22 (round 1)

Sources checked: figures/ch2/fig22.png (scan); figures/v2/ch2/fig22.pdf (current build: 4.76 x 2.71 in, all
fonts embedded; rendered at 400 dpi) and build/v2/png/ch2-fig22-compare.png; figures/v2/ch2/fig22.tex, fig22.py,
fig22.csv, fig22.calib.json; figures/v2/inventory.csv row ch2-fig22; caption chapters/ch2-sec3b.tex:163-165;
citing text ch2-sec3b.tex:145-158 (eq. (39)) and 224-238 (eqs. (42a), (42b)); eqs. (16), (22), (23) at
ch2-sec3a.tex; STYLE.md sections 13 and 16; corrections/v2-figures.md; approved examples ch1/fig03.tex,
ch2/fig25.tex; siblings Figs 21, 23.

Checked and correct:
- Lettering: $\alpha_X$ (rad) and $t$ (sec) titles; y ticks $0$ and $\alpha_{Xm}$; t tick $t_m$; "Slope $=
  \dfrac{H}{I_L}$". Below the plot, $\alpha_{Xm} = \frac{H}{I_L D e}$ and $t_m = \frac{1}{D}$ in the printed
  order. These are eqs. (42b), (42a) exactly. Nothing added.
- Curve: eq. (39), $\alpha_X = (H/I_L)\,t\,e^{-Dt}$, with $D = 1$ in units of $\omega_n$ (critical damping, the
  same rocket as Figs 21 and 23). This is fully determined. fig22.csv agrees with $te^{-t}$ to $5\times10^{-6}$,
  and fig22.py reruns to a byte-identical CSV.
- Marks: $t_m = 1$, $\alpha_{Xm} = 1/e = 0.3679$, at the numerical maximum. The dashed guides meet at the drawn
  peak.
- Tangent: the line $\alpha = t$ (slope $H/I_L = 1$) is the true tangent at the origin. It crosses the
  $\alpha_{Xm}$ level at $t_m/e$, as the equations require (inventory note).
- Range: $t$ to 8.3 on an axis to 8.6 (the scan's about $8.6/D$). The curve has decayed onto the axis by the
  right edge (0.002), as printed. The y axis does not run below 0 (nothing is there).
- Overlay on the scan. `main` calibration: mean 3.16 px, 95% 12.21 px (2.07 mm). `fit` calibration: mean
  0.89 px, 95% 3.15 px (0.53 mm). The difference is the 1973 art's near-cusp peak and its faster fall just after
  it (inventory note). The computed curve is the approved choice.
- Caption: the initial yaw rate, the maximum yaw angle and its time are shown.
- Style and legibility: the conventions are identical to Figs 21 and 23 (tangent `series2, solid`, curve
  `series1`, `guide` marks, the same axis scale, formulas 0.35 in right of the axis). The width is 4.76 in.
  Nothing overlaps or is clipped.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The computed peak is round where the 1973 peak is a near-cusp, and the computed curve sits above the printed one just after $t_m$ (overlay, `main`: 95% 12.2 px). This is approved: the curve is computed from eq. (39). Per STYLE.md section 16 the mismatch should be logged in corrections/v2-figures.md, which the drafter cannot write. | fig22.py; corrections/v2-figures.md | For the orchestrator: one minor line, shared with Figs 21 and 23. |

## Verdict

pass (0 must-fix, 0 should-fix)
