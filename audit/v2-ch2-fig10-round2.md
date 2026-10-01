# v2 audit: ch2/fig10 (round 2)

Sources checked: figures/ch2/fig10.png (scan); figures/v2/ch2/fig10.pdf (rebuilt 19:12 after the round-1 fix,
newer than fig10.tex, the CSVs and tamrfig.sty; 332.3 x 421.8 pt = 4.61 x 5.86 in, 6 fonts all embedded; rendered
at 300 and 600 dpi) and build/v2/png/ch2-fig10-compare.png; figures/v2/ch2/fig10.tex, fig10.py, fig10.csv,
fig10-marks.csv, fig10.calib.json; inventory row ch2-fig10; caption chapters/ch2-sec3a.tex:175-189; citing text
ch2-sec3a.tex:157-173; eqs. (15)-(19) (ch2-sec3a.tex:55-155); axis definitions ch2-intro-sec1.tex:104-115,
376-391; STYLE.md sections 13 and 16; corrections/v2-figures.md; round-1 audit and fix record; the family's other
redraws (Figs 11-14).

Round-1 items:
- Should-fix 1 (tag (f) over the t-axis arrowhead): **resolved**. `\instant` now takes the tag's placement
  options (fig10.tex:45-48); (f) is `xshift=-12pt, yshift=8pt` (fig10.tex:63), left of f inside the last lobe, as
  printed. Measured at 600 dpi (ink edge to ink edge): 3.0 pt clear of the curve, 1.9 pt above the t axis, 3.6 pt
  left of the point at f, and well apart from the arrowhead and "$t$ (sec)". The other tags keep their round-1
  placements (a, e `below=4pt`; b `above right=4pt`; c `above=4pt`; d `above left=4pt`): no regression.
- Notes 2-5: the filled points are kept (note 2). Notes 3-5 were for the orchestrator. They are still open, see
  findings 1-3.

Rechecked (no regression):
- Data: fig10.csv and fig10-marks.csv are unchanged since round 1 (17:54). Evaluated again in memory, the curve
  equals $A\sin(\omega_n t+\varphi)$ to 1.5e-5. With $\alpha_{X0} = 0.8$ and $\Omega_{X0} = 2.12$, eq. (18) gives
  $\varphi = 0.3608$ and eq. (19) gives $A = 2.266 = 2.83\,\alpha_{X0}$. The instants are a = 1.210, b = 2.781,
  c = 4.352, d = 5.922, e = 7.493 and f = 9.064, and f - b = $2\pi/\omega_n$. The tangent (0, 0.8)-(0.85, 2.602) has
  slope 2.12 = $A\omega_n\cos\varphi$, so it is truly tangent.
- Lettering complete: Slope $=\Omega_{X0}$, $A$ (y tick and dashed guide), $\alpha_{X0}$, 0, $\alpha_X$ (rad),
  $t$ (sec), circled a-f on the curve and under the rockets, dimensions $\frac{\pi-\varphi}{\omega_n}$ and
  $\frac{2\pi}{\omega_n}$ with extension lines at b and f, and angle labels $A$, $-A$, $A$. The rockets tilt nose
  right at a and e, nose left at c, and stand upright at b, d and f, each under its instant.
- Overlay rerun: mean 2.66 px, 95% 6.32 px (1.07 mm), max 9.85 px, the same as round 1. This is a computed curve
  and is accepted.
- Legibility and style: nothing overlaps or is clipped, and the arrowheads are visible. The family frame is
  unchanged (0.4 in per $1/\omega_n$, 0.576 in per unit, xmax 9.6, ymax 2.8, ymin -3.1). Width 4.61 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Still open from round 1, not a redraw defect: the mismatch between the 1973 sinusoid and its own A/$\alpha_{X0}$ tick ratio (overlay 95% 6.32 px) is recorded only in the fig10.py docstring. It is not yet in corrections/v2-figures.md. | corrections/v2-figures.md, Minor | Orchestrator: log it as minor. |
| 2 | note | Still open from round 1: the v1 caption question. "Viewed from the negative y axis" (ch2-sec3a.tex:183-184) cannot show $\alpha_X$, a rotation about X (ch2-intro-sec1.tex:112, 382-383). It is not yet in corrections/ch2.md. The figure is unaffected. | ch2-sec3a.tex:183-184 | Orchestrator: consider a corrections/ch2.md query. |
| 3 | note | Still open: the style suggestion to drop `rotate=-90` from the `tamr sketch` y label (tamrfig.sty:135). The sty has not changed (16:55), so the local override at fig10.tex:14-15 is still needed and correct. | tamrfig.sty:135; fig10.tex:15 | Orchestrator/sty owner. No change to the figure. |

## Verdict

pass (0 must-fix, 0 should-fix)
