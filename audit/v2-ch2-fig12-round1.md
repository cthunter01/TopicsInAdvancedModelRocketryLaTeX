# v2 audit: ch2/fig12 (round 1)

Sources checked: figures/ch2/fig12.png (scan, upscaled 2x); figures/v2/ch2/fig12.pdf (4.62 x 2.86 in, all fonts
embedded; rendered at 300 and 600 dpi) and build/v2/png/ch2-fig12-compare.png; figures/v2/ch2/fig12.tex, fig12.py,
fig12.csv, fig12.calib.json; inventory row ch2-fig12; caption chapters/ch2-sec3a.tex:350-357; citing text
ch2-sec3a.tex:330-348; eqs. (16), (22), (23) (ch2-sec3a.tex:250-330); STYLE.md sections 13 and 16;
corrections/v2-figures.md (standing rule 4 names this figure); the family's other redraws (Figs 10, 11, 13, 14).

Checked and correct:
- Lettering, all present: Slope $=\Omega_{X0}$; $\alpha_{X0}$ (y tick); 0; $\alpha_X$ (rad); $t$ (sec).
- Data: fig12.py rerun in scratch gives a byte-identical fig12.csv, equal to eq. (22)
  $(A_1 + A_2 t)e^{-Dt}$ with eq. (23) $A_1 = \alpha_{X0} = 1$, $A_2 = \Omega_{X0} + D\alpha_{X0} = 1.6$ and
  $D = \omega_n = 1$ ($\zeta = 1$) to 5e-6.
- Rule 4: the line (0, 1)-(2.3, 2.38) has slope 0.6 = $\Omega_{X0} = A_2 - DA_1$, the curve's slope at t = 0: truly
  tangent (checked at 600 dpi; the line and curve leave $\alpha_{X0}$ together).
- Caption and text: no oscillation and no crossing of the t axis (minimum 0.0016 at t = 9.2); a single low peak
  (1.10 $\alpha_{X0}$ at t = 0.375) because $\alpha_{X0}$ and $\Omega_{X0}$ are both positive "as shown"; approach to
  zero from above.
- Shape vs scan: overlay mean 1.36 px, 95% 2.00 px (0.34 mm), max 3.0 px: within the 3 px target even though
  computed (at t = 4: 0.136 against about 0.14 printed).
- Family: same $\alpha_{X0}$, $\Omega_{X0}$, $C_1/I_L$ and tangent as Fig 13, so Fig 13's comparison shows; the
  family's frame and styles; width 4.62 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | With the true tangent ($\Omega_{X0} = 0.6$, fitted to the drawn curve) the "Slope" line is far less steep than the printed one (about 41 degrees on the page against about 75). This is standing rule 4, approved; no action. | fig12.tex:20-21 | none |
| 2 | note | From about t = 6.3 ($\alpha_X < 0.02$, less than 1.2 pt above the axis) the 1 pt curve lies on the t axis to the end, as the printed curve merges with the axis at about t = 6.5. The caption's "asymptotically from above" stays true of the curve; no change needed. | fig12.csv tail | Optional: none. |
| 3 | note | Style suggestion (as Fig 10): local `every axis y label` override works around `rotate=-90` in `tamr sketch`. | fig12.tex:13; tamrfig.sty:135 | Fix in tamrfig.sty. |

## Verdict

pass (0 must-fix, 0 should-fix)
