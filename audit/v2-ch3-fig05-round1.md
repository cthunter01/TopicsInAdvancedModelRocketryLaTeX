# v2 audit: ch3/fig05 (round 1)

Sources checked: figures/ch3/fig05.png (scan, zoomed 3x, the corner arcs 6x); figures/v2/ch3/fig05.pdf (rebuilt
with `make fig F=ch3/fig05`, 4.45 x 2.33 in, fonts embedded; rendered at 300 dpi) and
build/v2/png/ch3-fig05-compare.png; figures/v2/ch3/fig05.tex; figures/v2/inventory.csv row ch3-fig05; caption
chapters/ch3-intro-sec2a.tex:448-452; citing text ch3-intro-sec2a.tex:414-434 (forces "in the manner shown in
Figure 5a", tau = F/A_c, the rhomboid "as shown in Figure 5b" with theta less than 90 deg, gamma = pi/2 - theta);
STYLE.md sections 14 and 16; corrections/v2-figures.md; figures/v2/tamrfig.sty (vec, angle arc, panel).

Checked and correct:
- Lettering complete against the inventory: (a) $\tau = \dfrac{F}{A_c}$ above; four $F$; "Face area $= A_c$";
  $\dfrac{\pi}{2}$ at the lower-left corner; (b) $\gamma = \dfrac{\pi}{2} - \theta$ above; four $F$; $\theta$. $A_c$
  with an italic c subscript (STYLE s.14 letter subscripts italic); $\gamma$ is the shear strain (the looped hand
  glyph). Nothing added.
- Force senses as printed and as the text needs (a balanced system): top to the right, right side up, bottom to
  the left, left side down; in (b) the forces lie along the turned sides with the same senses.
- Geometry of (b): pure shear, the horizontal sides turned 6.5 deg counterclockwise and the vertical sides 6.5 deg
  clockwise about the centre, so the top moves right relative to the bottom, as the forces require, and
  theta = 90 - 13 = 77 deg (< 90 deg, as the text says). The scan's sides are turned 6.5 deg (top) and 7.1 deg
  (left): the redraw's symmetric form matches the "neither move away nor turn" reading.
- Angle arcs: `angle arc` with a head at both ends; the zoomed scan shows small heads at both ends of both arcs.
  The arc of (b) runs from the bottom side (g/2) to the left side (90 - g/2), so it measures theta exactly.
- Panel letters (a), (b) in the `panel` style at the lower right of each drawing, on one baseline (y = -2.6 cm),
  same offset from each drawing.
- Legibility: the formulas clear the top force labels by about 4 mm; $\pi/2$ and $\theta$ clear their arcs;
  nothing clipped; width within 6.5 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The scan sets $\pi/2$ and $\theta$ in a gap in their arcs; the redraw sets them just outside the arcs (radius + 0.42 cm and + 0.3 cm at 45 deg). Both read clearly; the kit's `angle label` (white knock-out) would reproduce the scan's form if wanted. | fig05.tex:46-47, 60-61 | None needed. |
| 2 | note | The 1973 (b) is very slightly rotated as well as sheared (sides turned 6.5 and 7.1 deg); the redraw draws pure shear with equal 6.5 deg turns, which is what the text describes. | fig05.tex:2-9, 52-58 | None. |

## Verdict: pass (0 must-fix, 0 should-fix)
