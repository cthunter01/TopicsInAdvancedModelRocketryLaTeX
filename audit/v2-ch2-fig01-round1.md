# v2 audit: ch2/fig01 (round 1)

Sources checked: figures/ch2/fig01.png (scan, zoomed 3-10x, contrast-stretched, and resampled into a strip
straightened along the rocket's axis); figures/v2/ch2/fig01.pdf (current: newer than the .tex; 355.6 x 245.7 pt =
4.94 x 3.41 in, three Type 1 fonts all embedded; rendered at 150, 300 and 600 dpi) and
build/v2/png/ch2-fig01-compare.png; figures/v2/ch2/fig01.tex; figures/v2/inventory.csv row ch2-fig01; caption
chapters/ch2-intro-sec1.tex:120-123; citing text ch2-intro-sec1.tex:104-115 and 127-137 (the dashed line Of,
Oe, Od, the planes of the three rotations); Fig 3 (approved, same view) figures/v2/ch2/fig03.tex and its caption
ch2-intro-sec1.tex:227-229; STYLE.md sections 13 and 16; corrections/v2-figures.md (standing rules, pilot
decisions); tamrfig.sty.

Checked and correct:
- Lettering: A, B, C, D, E, F, d, e, f, O, and the six angle labels are all present and in the right sectors:
  A-d $\alpha_E$, d-D $\alpha_F$, B-e $\alpha_D$, e-E $\alpha_F$, C-f $\alpha_D$, f-F $\alpha_E$ (as the scan and
  the inventory). Uppercase angle subscripts (STYLE 13). Nothing added. Labels \small.
- Rotations: the code's yaw about A, pitch about Oe, roll about F are a consistent rigid rotation (I checked
  each formula against the right-hand rotation matrices about the 1st, 2nd and 3rd body axes). Every sentence of
  the text holds for the drawing: B, e, C, f lie in the B-C plane (yaw); F and d lie in the plane of A and Of, so
  the A-d and f-F angles ($\alpha_E$) share one plane (pitch); D and E lie in the plane of Od and Oe (roll). Od,
  Oe and Of are dashed (the text's "dashed line Of"); the A-F axes have arrowheads, d, e, f do not (as printed).
- View: x = (1.58053, 0.83755), y = (-1.58053, 0.83755), z = (0, 1.89556) cm is Fig 3's orthographic view
  (vertical/horizontal 0.530 = sin 32 deg; z/horizontal 1.199 = cos 32/cos 45) with x = B, y = C, z = A, so
  A x B = C (right-handed), placed as Fig 3's E, F, D. Projected axis directions (deg from the page's +x):
  A 90.0, B 27.9, C 152.1, D 66.6, E 8.4, F 130.7, d 79.3, e 19.7, f 141.8; my readings of the scan are A 89.6,
  B 29.4, C 149.8, D 69.5, E 10.5, F 131.6, d 81.3, e 21.4, f 139 (within 3 deg, as the header says).
- Angle marks: each arc is a true circle in its own plane (w built from u, v and the angle between them; the
  angles passed equal the true angles between the lines), radius 0.91 L, label in a gap at the middle, both
  arrowheads visible at 600 dpi. The pairs meet on the fold lines, as the printed dimension lines do. The f-F
  arc is trimmed to end on the nose's silhouette (F is inside the body there); the scan's line ends there too.
- Sectors: each is two plane faces folded on Od, Oe, Of, hatched with lines parallel to the face's outer edge
  (so in the face's plane), chevrons on the fold, clear near the outer edge for the angle marks, as printed.
  Projected hatch spacing 0.64-0.76 mm in all six faces (even tone), 0.3 pt ink2 (the house hatch weight).
- Rocket: along F with the C.G. (house `cg mark`) at O, nose tip at the end of the C-f-F sector, F arrow out of
  the tip; seen from astern (F . c = -0.55, F points away from the viewer), so the tail is a full ellipse and the
  nose-base ring shows its near half; fins +D and -E in front of the body, +E and -D behind (depths checked:
  D . c = +0.55, E . c = -0.63). Four clipped-delta fins, trailing edges square to the body (crd = swp + ctp).
  Dash-dot centre line aft of O and beyond the tail, as printed.
- Size and legibility: 4.94 in wide (under 6.5 in); nothing clipped or overlapping; O sits clear of the body.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The F axis is not visible between O and the nose. In the scan the edge OF of the f-F sector is drawn as a solid line along the forward body's axis, from O to the nose tip (straightened strip: a continuous line on the O-tip line, t = 30-270 px). In the redraw the white body hides it and the centre line stops at O, so the line that $\alpha_E$ is measured to, and about which $\alpha_F$ is taken, is shown only by the short arrow beyond the nose. | fig01.tex:127 (`\draw[centerline] (O) -- ($ {\stail}*(F) $);`) | Continue the centre line forward through the body, e.g. `\draw[centerline] (O) -- ($ {\snb}*(F) $);` (or to the tip) after `\draw[outline] \bodypath;`, so F runs visibly from O to its arrow, as A-E do. |
| 2 | should-fix | The 1973 occlusion is reversed without a record. The scan draws the hatched f-F face over the lower half of the forward body: the face's edge F runs solid along the body's axis and the hatching covers the strip between it and the body's lower wall, with the upper half white (scan, about (141, 88) to (282, 246) at 150 dpi). The redraw draws the whole body in front of the face. The redraw is right for its own right-handed view: at the body's lower silhouette the face lies 1.74 body radii behind it ((n . e)/(c . e) = 0.823/(-0.474)). But it is a visible departure from the art, and neither the header nor the inventory mentions it. | fig01.tex:1-19 (header) | No change to the drawing. Add a sentence to the header (1973: the face drawn over the lower half of the forward body; redrawn with the body in front, as the view requires, under standing rule 4) so the gate sees it. |
| 3 | should-fix | The body is about 30% too slim for the scan. The scan's body measures 17.5 px across at 150 dpi (aft walls at k = -9.5 and +8, the forward walls the same, the tail ring 17.5 px), that is, 0.175 units at the drawing's 1 unit = 100 scan px. The redraw has `\rad` = 0.062, a diameter of 0.124 units (2.8 mm against the scan's 4.0 mm at the redraw's scale). The header says "body, fins and tail ring in the scan's proportions". | fig01.tex:62 (`\def\rad{0.062}`) | Set `\rad` to about 0.088. The f-F arc trim is computed from `\rad`, so it follows. Or, if the slimmer body is wanted, correct the header's claim. Keep Fig 6 identical. |
| 4 | note | The hatching is per-face parallel strokes, not the house `hatch`/`hatch back` (45/135 deg only, STYLE 16). This is justified: the strokes lie in the planes of the angles, which is what the 1973 hatching shows and what the family brief asks for (a true 3D reading). | fig01.tex:24, 67-72 | None. Style suggestion: record in STYLE 16 that 3D plane faces may be hatched parallel to an edge in their own plane. |
| 5 | note | The yaw is drawn negative in Fig 3's sense (e is B turned away from C; -11 deg), while pitch and roll are positive, as in the 1973 art (the scan's e lies clockwise of B and f clockwise of C on the page). The text and caption give no signs; the header documents it. | fig01.tex:10-12, 34 | None. |
| 6 | note | The faces are left clear over the outer 19% of the radius uniformly. The scan leaves a clear band only around the angle marks (the C-f-F faces are hatched nearly to their outer edges elsewhere). This does not change the meaning. | fig01.tex:50 (`\hout`) | None (optional: `\hout` about 0.85 where no label sits). |

## Verdict

pass (0 must-fix, 3 should-fix)
