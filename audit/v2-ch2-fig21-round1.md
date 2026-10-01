# v2 audit: ch2/fig21 (round 1)

Sources checked: figures/ch2/fig21.png (scan); figures/v2/ch2/fig21.pdf (current build: 4.76 x 3.65 in, all
fonts embedded; rendered at 400 dpi) and build/v2/png/ch2-fig21-compare.png; figures/v2/ch2/fig21.tex, fig21.py,
fig21.csv, fig21.calib.json; figures/v2/inventory.csv row ch2-fig21; caption chapters/ch2-sec3b.tex:141-143;
citing text ch2-sec3b.tex:117-136 (eqs. (37a), (37b), (38)) and 196-222 (eqs. (41a), (41b)); eqs. (15)-(17) at
ch2-sec3a.tex:53-120; STYLE.md sections 13 and 16; corrections/v2-figures.md; approved examples ch1/fig03.tex
(tangent line in `series2, solid`, `guide` construction lines), ch2/fig25.tex; sibling Figs 22, 23 and Ch2 Figs
10-14 (the `tangent` = `s2`, 1 pt convention).

Checked and correct:
- Lettering: $\alpha_X$ (rad) and $t$ (sec) titles; y ticks $0$ and $\alpha_{Xm}$; t tick $t_m$; "Slope $=
  \dfrac{H}{I_L}$" at the top of the tangent. The two formulas are typeset below the plot in the printed order
  ($\alpha_{Xm}$ first). Character for character they are eq. (41b) and eq. (41a) as set in
  ch2-sec3b.tex:213-222 and as the inventory gives them. Subscripts are in the section 13 forms. Nothing added.
- Curve: eq. (38) with $D$, $\omega$ by eqs. (16), (17) at $\zeta = 0.25$, in units of $1/\omega_n$ and
  $H/(I_L\omega_n)$. I checked fig21.csv independently against $(1/\omega)e^{-\zeta t}\sin\omega t$: maximum
  difference $5\times10^{-6}$ (rounding). fig21.py reruns to a byte-identical CSV.
- Marks: $t_m = 1.3613$, $\alpha_{Xm} = 0.7115$ by eqs. (41a), (41b), which equal the curve's numerical maximum.
  The dashed guides meet exactly at the drawn peak.
- Tangent: the line $\alpha = t$ from the origin is the true tangent: slope 1 $= H/I_L$ (eq. (37b)) in these
  units, and the curve's slope at $t = 0$ is $(1/\omega)\cdot\omega = 1$. Its top is at $1.21\,\alpha_{Xm}$,
  as on the scan.
- Shape: trough $-0.316$ at $t = 4.60$, ratio of successive extremes $0.444$ (inventory reading about 0.44). The
  curve ends at $t = 8.3$, just past the second peak ($t = 7.84$), as printed. The y axis stops at $-0.42$ (the
  scan runs it down past the formulas, with nothing there).
- Overlay on the scan (`digitize.py overlay`). With the `main` calibration (origin, $t_m$, $\alpha_{Xm}$ marks):
  mean 2.79 px, 95% 9.22 px (1.56 mm). With the `fit` calibration: mean 1.76 px, 95% 4.47 px (0.76 mm). The
  computed curve follows the 1973 shape closely (accepted for computed curves).
- Caption and text: the initial angular velocity (the slope), the maximum yaw angle and its time are all shown.
- Style and legibility: the tangent is `series2, solid` (orange) as in approved ch1/fig03.tex, and the curve is
  `series1`. The guides use `guide`. Label text is ink. The width is 4.76 in, within 6.5 in. Nothing overlaps or
  is clipped. The axes have the same scale as Figs 22 and 23 (0.46 in per $1/\omega_n$, 1.8 in per
  $H/(I_L\omega_n)$), so the three dampings compare directly.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The exponent fractions ($D/\omega$, $\omega/D$ in $e^{-\frac{D}{\omega}\arctan(\frac{\omega}{D})}$) are at scriptscript size of `\small`, about 5 pt. That is legible at 400 dpi and no smaller than the 1973 lettering. The chapter's own eq. (41b) sets them at 6 pt. | fig21.tex:26-31 | Optional: set the formula node at `\normalsize` (the chapter's display size) for 6 pt exponents. Do it in Figs 21-23 alike or not at all. |
| 2 | note | STYLE.md section 16 says an overlay mismatch goes to corrections/v2-figures.md. The 95% figures above (9.22 px main, 4.47 px fit) exceed 3 px. The drafter cannot write that file. | corrections/v2-figures.md | For the orchestrator: log one minor line for Figs 21-23 (computed sketches; overlay numbers as in these reports). |

## Verdict

pass (0 must-fix, 0 should-fix)
