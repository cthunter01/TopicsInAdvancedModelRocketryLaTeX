# v2 audit: ch2/fig11 (round 1)

Sources checked: figures/ch2/fig11.png (scan, upscaled 2x); figures/v2/ch2/fig11.pdf (4.62 x 2.86 in, all fonts
embedded; rendered at 300 and 600 dpi) and build/v2/png/ch2-fig11-compare.png; figures/v2/ch2/fig11.tex, fig11.py,
fig11.csv, fig11-marks.csv, fig11.calib.json; inventory row ch2-fig11; caption chapters/ch2-sec3a.tex:233-241;
citing text ch2-sec3a.tex:200-210; eqs. (15)-(20) (ch2-sec3a.tex:60-215); STYLE.md sections 13 and 16;
corrections/v2-figures.md (standing rule 1 names this envelope); approved examples ch1/fig03.tex, ch2/fig25.tex;
the family's other redraws (Figs 10, 12-14).

Checked and correct:
- Lettering, all present: Slope $=\Omega_{X0}$; $\alpha_{X0}$ (y tick); 0; $\alpha_X$ (rad); $t$ (sec);
  $Ae^{-Dt}$ with a bent `leader` ending on the envelope (at t = 4.9, $Ae^{-4.9D} = 0.905$, on the dotted line);
  dimensions $\frac{\pi-\varphi}{\omega}$ (0 to the first zero) and $\frac{\pi}{\omega}$ (first to second zero)
  with extension lines. No A tick, as printed.
- Caption: the envelope is DOTTED (round 1.1 pt dots every 2.6 pt, ink2), as the caption says (standing rule 1);
  the time to the first zero and one-half period are dimensioned.
- Data: fig11.py rerun in scratch gives byte-identical fig11.csv and fig11-marks.csv. With $\zeta = 0.227$
  (D = 0.227, $\omega = \sqrt{1-D^2} = 0.9739$, eqs. (16), (17), (20)), $\alpha_{X0} = 1$, $\Omega_{X0} = 2.27$:
  $\varphi = 0.3719$ by eq. (18), A = 2.752 by eq. (19); the CSV equals eq. (15) and $Ae^{-Dt}$ to 5e-6. The
  envelope touches the curve exactly where $\sin(\omega t+\varphi) = 1$ (t = 1.231: 2.081 = 2.081; t = 7.683:
  0.481 = 0.481), just after each peak, as it should. Zeros at 2.844 and 6.070; difference 3.2258 = $\pi/\omega$.
  The curve's slope at t = 0, $-D\alpha_{X0} + A\omega\cos\varphi$, equals $\Omega_{X0}$, the slope of the drawn
  line (0, 1)-(0.66, 2.498).
- Shape vs scan: first peak 2.14, trough -1.01, second peak 0.50 (units of $\alpha_{X0}$) against printed about
  2.1, -1.0, 0.52. Overlay of the computed response: mean 0.50 px, 95% 1.41 px (0.24 mm): within the 3 px target.
- Style: the family's `tamr sketch` frame (0.4 in per $1/\omega_n$, 0.576 in per unit; ymin -1.8, shortened from the
  printed -2.25 with nothing lost); `series1` curve; orange tangent with an ink label; width 4.62 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Overlay of the computed envelope $Ae^{-Dt}$ on the printed (dashed) envelope, t = 1 to 8.8: mean 2.80 px, 95% 5.83 px (0.99 mm), max 16.3 px: the 1973 envelope sags below the true exponential between the peaks. The computed envelope is the one the caption and text describe (it touches the curve at its points of contact); accepted under the pilot decision on computed curves. | fig11.csv column env | Orchestrator: log as minor in corrections/v2-figures.md if every overlay mismatch is to be listed. |
| 2 | note | Style suggestion (as Fig 10): the local `every axis y label` override (upright label above the arrow) works around `rotate=-90` in `tamr sketch`. | fig11.tex:15; tamrfig.sty:135 | Fix in tamrfig.sty. |

## Verdict

pass (0 must-fix, 0 should-fix)
