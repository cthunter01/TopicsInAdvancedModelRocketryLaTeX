# v2 audit: ch2/fig10 (round 1)

Sources checked: figures/ch2/fig10.png (scan, upscaled 2x); figures/v2/ch2/fig10.pdf (4.62 x 5.86 in, all fonts
embedded; rendered at 300 and 600 dpi) and build/v2/png/ch2-fig10-compare.png; figures/v2/ch2/fig10.tex, fig10.py,
fig10.csv, fig10-marks.csv, fig10.calib.json; inventory row ch2-fig10; caption chapters/ch2-sec3a.tex:179-187;
citing text ch2-sec3a.tex:157-165; eqs. (15)-(19) (ch2-sec3a.tex:60-150); axis definitions
ch2-intro-sec1.tex:104-115, 376-399 and the right-handed senses of figures/v2/ch2/fig03.tex; STYLE.md sections 13
and 16; corrections/v2-figures.md (standing rules, pilot decisions); approved examples ch1/fig03.tex (tangent
line), ch2/fig39.tex; the family's other redraws (Figs 11-14) and the sibling ch2/fig27.tex.

Checked and correct:
- Lettering, all present and in the section 13 forms: Slope $=\Omega_{X0}$; y ticks $A$ (with the dashed `guide`
  level from t = 0 to past e) and $\alpha_{X0}$; 0; $\alpha_X$ (rad); $t$ (sec); circled a-f on the curve and under
  the rockets; dimensions $\frac{\pi-\varphi}{\omega_n}$ (0 to b) and $\frac{2\pi}{\omega_n}$ (b to f) with
  extension lines at b and f (the y axis serves at t = 0); angle labels $A$ over a and e, $-A$ over c.
- Data: fig10.py rerun in scratch gives byte-identical fig10.csv and fig10-marks.csv. The curve equals
  $A\sin(\omega_n t+\varphi)$ to 1.5e-5 with $\varphi = \arctan(\alpha_{X0}\omega_n/\Omega_{X0}) = 0.3608$ (eq. (18),
  D = 0) and $A = \alpha_{X0}/\sin\varphi = 2.266 = 2.83\,\alpha_{X0}$ (eq. (19)), the drawn tick ratio. The
  instants are exact: b at $(\pi-\varphi)/\omega_n = 2.781$, f - b = 6.2832 = $2\pi/\omega_n$; a, e at the maxima,
  c at the minimum, b, d, f at the zeros. One consistent $\varphi$ is used, as the inventory asked.
- Tangent: the curve's slope at t = 0 is $A\omega_n\cos\varphi = 2.12 = \Omega_{X0}$, the slope of the drawn line
  (0, 0.8)-(0.85, 2.602); it overshoots the A level as printed.
- Rockets: one silhouette rotated about its C.G. (`cg mark`); +A tilts the nose right at a and e, -A left at c,
  b, d, f upright, as printed; the `angle arc` runs from the vertical reference line to the rocket axis; each
  rocket stands under its instant (evenly spaced at $\pi/2\omega_n$, as the printed row). Proportions (nose 0.20 L,
  fin root 0.20 L, C.G. 0.685 L) match the scan.
- Style: `tamr sketch` with the family's frame (0.4 in per $1/\omega_n$, 0.576 in per unit, xmax 9.6, ymax 2.8;
  ymin -3.1 here for the dimensions under the trough); curve `series1`; tangent orange 1pt with an ink label (as
  the approved Ch1 Fig 3 tangent and sibling Fig 27); width 4.62 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The tag (f) sits directly over the t-axis arrowhead: f is at t = 9.064 and the arrow tip at 9.6 (15.4 pt to the right); `above right=4pt` puts the 11 pt circle 4-15 pt right of f with its lower edge about 2.5 pt above the arrowhead, so (f), the arrowhead and "$t$ (sec)" read as one cluster. The scan puts (f) to the left of f, inside the last lobe. | fig10.tex:62 (`\instant{f}{0}{above right}`) | Put (f) left of f above the axis, as printed: e.g. the tag centre about 12 pt left and 8 pt above f (the curve is nearly straight there, slope -3.26 on the page; this clears it by about 3.5 pt and the axis by about 2.5 pt). |
| 2 | note | Filled points mark the six instants on the curve (not in the scan). They tie the curve to the rocket row and change no meaning; keep. | fig10.tex:45-48 (`\instant`), 61-62 | none |
| 3 | note | Overlay of the computed curve on the scan: mean 2.66 px, 95% 6.32 px (1.07 mm), max 9.85 px. The 1973 sinusoid rises from $\alpha_{X0}$ to a and falls to b more slowly than one with its own A/$\alpha_{X0}$ tick ratio (fitted alone it has A about 1.73 $\alpha_{X0}$, as fig10.py's docstring records). Computed curve accepted; the doubt is recorded only in fig10.py. | fig10.py docstring | Orchestrator: log as a minor item in corrections/v2-figures.md (STYLE.md section 16, curve data). |
| 4 | note | v1 caption question, not a redraw defect. The caption says the rockets are "viewed from the negative y axis", but $\alpha_X = \alpha_D$ is a rotation about X (ch2-intro-sec1.tex:112, 382), which moves the nose in the Y direction: seen from -Y the nose moves toward the viewer, not sideways. With the right-handed axes (Fig 3: $\omega_D$ turns E toward F), +$\alpha_X$ moves the nose toward -Y, which is the viewer's right when viewed from the negative x axis, the sense the art and the redraw show. | ch2-sec3a.tex:184 | Orchestrator: consider a v1 query (corrections/ch2.md); no change to the figure. |
| 5 | note | Style suggestion: `tamr sketch` sets `rotate=-90` on the y label (tamrfig.sty:135), which turns it sideways under `axis lines=middle`; every file of this family (and fig27) overrides `every axis y label` to keep it upright above the arrow. | tamrfig.sty:135; fig10.tex:15 | Fix once in tamrfig.sty (drop the rotate) and remove the local overrides later. |

## Verdict

pass (0 must-fix, 1 should-fix)
