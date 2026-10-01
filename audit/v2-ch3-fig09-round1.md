# v2 audit: ch3/fig09 (round 1)

Sources checked: figures/ch3/fig09.png (scan, zoomed 3x); figures/v2/ch3/fig09.pdf (rebuilt with `make fig
F=ch3/fig09`, 4.28 x 2.38 in, fonts embedded; rendered at 300 and 600 dpi) and build/v2/png/ch3-fig09-compare.png;
figures/v2/ch3/fig09.tex, fig09.py, fig09.csv, fig09-arrows.csv, fig09.calib.json; figures/v2/inventory.csv row
ch3-fig09; caption chapters/ch3-sec2b.tex:36-38; citing text ch3-sec2b.tex:22-24 (element moving parallel to x at
u(x, y)) and 83-88 (eq. (13): (tau + dtau/dy dy) dx dz - tau dx dz); STYLE.md sections 14 and 16 (3D drawings: the
house view, \blk); corrections/v2-figures.md; the other Ch3 profile figures (fig10, fig13, fig16-18).
Overlay run myself: `digitize.py overlay fig09.calib.json --axes profile` on fig09.csv (columns swapped to u, y):
101 points, mean 0.04 px, 95% 0.00 px, max 1.41 px (ok); arrow tips (fig09-arrows.csv) 18 points, 95% 0.00 px.

Checked and correct:
- Lettering complete against the inventory: $u(y)$; $\tau + \dfrac{\partial\tau}{\partial y}\,dy$ (partial sign
  as drawn); $\tau$; $dx$, $dy$, $dz$. Nothing added; no panel letters (the 1973 parts are unlettered).
- Profile: a qualitative sketch with no governing equation in the book, so matched to the scan (cubic fit to a
  row-by-row trace, residual rms about 0.6 px); it sits on the scan (overlay above), bulges to its maximum near
  0.8 H and turns back a little at the top as printed. 18 arrows at y = (k + 1/2)/18 from the base line to the
  curve, as printed (scan: top arrow at 0.972 H, bottom at 0.025 H).
- Element: \blk x 0..dx, TikZ y -dz..0, z 0..dy in `tamr view`; book x = TikZ x, book y = TikZ z, book z = -TikZ y,
  right-handed (x cross y = z). Seen faces: -x, +z (the book's front face, as printed) and the top +y face. The
  three hidden edges meet at the far bottom corner (dx, 0, 0); the lower face's diagonals hidden, the upper face's
  solid; both face centres (diagonal crossings) marked with `point`.
- Shear stresses as eq. (13) needs: $\tau + (\partial\tau/\partial y)dy$ from the upper-face centre along +x,
  $\tau$ from the lower-face centre along -x; the lower one hidden inside the element up to the -x face's bottom
  edge, then solid (it is in front of that face). The upper arrow beyond the top face's far edge is not occluded.
- Edge labels on edges of the right directions: $dx$ under an x edge of the front (+z) face, $dy$ at its right
  vertical edge, $dz$ under a z edge (the -x face's bottom edge), clear of the $\tau$ arrow (about 1 mm).
- The element is dx : dy : dz = 1.2 : 1 : 0.75, not a cube: justified in the header (a cube at azimuth 45 deg puts
  both face centres on the front vertical edge's line).
- Legibility: everything readable at final size, nothing clipped, width within 6.5 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The shear stresses act along x, the flow direction, but in the house view x projects up-right at 27.9 deg while the profile beside it draws the u arrows (also along x) horizontal; the 1973 art (an oblique projection) draws the tau arrows parallel to the u arrows. A reader comparing the two parts sees the shear at 28 deg to the flow. A true orthographic view cannot keep both x horizontal and y vertical with three faces seen, so "rotate the view" alone does not cure it. | fig09.tex:20-27 (profile), 29-49 (element) | Either (i) draw the profile in the same house view, in the element's x-y plane (base line along TikZ z, arrows along TikZ x), so the u and tau arrows are parallel; or (ii) keep it and record the 28 deg difference in corrections/v2-figures.md for the Chapter 3 gate (the orchestrator asked for `tamr view`). |
| 2 | should-fix | Profile styling differs from the other Ch3 profile figures (same finding as Fig 6): s1 1 pt line with ink `thin vec` arrows here and in Fig 6; ink line and ink 0.4 pt arrows in Figs 10, 13; s1 line and s1 0.5 pt arrows in Figs 16-18. | fig09.tex:22-24 | Apply the chapter's one profile convention (settled in the consistency pass) to Figs 6 and 9 together. |
| 3 | note | The 1973 art draws the lower tau line solid across the front face; the redraw hides it inside the element (dashed) until it leaves through the -x face. Consistent with the hidden-edge treatment; meaning unchanged. | fig09.tex:40, 44-45 | None. |
| 4 | note | `quiver` arrows inside the hidden pgfplots axis take `thin vec`; fine, but if finding 2 moves to the Figs 16-18 styles, the heads shrink to 3.4 pt: check the shortest arrow (0.92 cm) still reads. | fig09.tex:22-23 | None. |

## Verdict: pass (0 must-fix, 2 should-fix)
