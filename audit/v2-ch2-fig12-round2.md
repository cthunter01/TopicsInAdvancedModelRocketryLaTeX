# v2 audit: ch2/fig12 (round 2)

Sources checked: figures/ch2/fig12.png (scan); figures/v2/ch2/fig12.pdf (17:55, newer than fig12.tex, fig12.csv
and tamrfig.sty; 4.61 x 2.86 in, 5 fonts all embedded; rendered at 300 and 600 dpi) and
build/v2/png/ch2-fig12-compare.png; figures/v2/ch2/fig12.tex, fig12.py, fig12.csv, fig12.calib.json; inventory
row ch2-fig12; caption chapters/ch2-sec3a.tex:350-358; citing text ch2-sec3a.tex:325-348; eqs. (16), (22), (23);
STYLE.md sections 13 and 16; corrections/v2-figures.md (standing rule 4); round-1 audit and fix record; Fig 13's
redraw.

Round-1 items: none were must-fix or should-fix, and the figure is unchanged. Notes 1 and 2 needed no action.
Note 3 (the sty suggestion) is still open, see the findings.

Rechecked (no regression):
- Lettering: Slope $=\Omega_{X0}$, $\alpha_{X0}$, 0, $\alpha_X$ (rad), $t$ (sec).
- Data, evaluated in memory: the CSV equals $(A_1 + A_2t)e^{-Dt}$ to 5e-6, with $D = \omega_n = 1$, $A_1 = 1$ and
  $A_2 = \Omega_{X0} + D\alpha_{X0} = 1.6$ (eq. (23)). There is one peak, 1.100 at t = 0.375. At t = 2, 4, 6, 8
  the curve is 0.568, 0.136, 0.026, 0.005, and it is 0.0016 at t = 9.2: it never crosses the axis.
- Rule 4: the line (0, 1)-(2.3, 2.38) has slope 0.600 = $A_2 - DA_1$. At 600 dpi the line and the curve leave
  $\alpha_{X0}$ together, so the line is truly tangent.
- Overlay rerun: 95% 2.00 px (0.34 mm), max 3.00 px, within the target, as in round 1.
- Caption: no oscillation, and the curve approaches zero asymptotically from above.
- Style and family: the same frame, tangent and initial conditions as Fig 13. Width 4.61 in. Nothing clipped or
  overlapping.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Still open: the `tamr sketch` y-label suggestion (tamrfig.sty:135). The local override (fig12.tex:12-13) is still needed and correct. | fig12.tex:13 | Orchestrator/sty owner. |

## Verdict

pass (0 must-fix, 0 should-fix)
