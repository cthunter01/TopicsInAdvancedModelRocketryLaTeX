# v2 audit: ch3/fig09 (round 2)

Sources checked: figures/ch3/fig09.png (the scan); figures/v2/ch3/fig09.pdf (rebuilt with `make fig F=ch3/fig09`:
4.08 x 2.52 in, fonts embedded, clean log; rendered at 300 dpi, with the profile's top and bottom and the element's
lower corner zoomed 3x) and build/v2/png/ch3-fig09-compare.png; figures/v2/ch3/fig09.tex, fig09.py, fig09.csv,
fig09-arrows.csv, fig09.calib.json; figures/v2/inventory.csv row ch3-fig09; the caption
(chapters/ch3-sec2b.tex:36-38) and the citing text (ch3-sec2b.tex:22-24; eq. (13) at 83-88); STYLE.md sections 14 and
16 (3D drawings); corrections/v2-figures.md; the round 1 audit and the fix record; the profile styles of Figs 6,
10, 13, 16, 17, 18 and 25.

Overlay, run myself (`digitize.py overlay fig09.calib.json --axes profile` on fig09.csv and fig09-arrows.csv with
their columns swapped to u, y): profile 101 points, mean 0.04 px, 95% 0.00 px, max 1.41 px (ok); arrow tips 18
points, 0.00 px (ok). I also ran fig09.py to see its fit report: 324 traced points, residual rms 0.58 px, max 2.45 px.
That run rewrote fig09.csv and fig09-arrows.csv. Both are byte-identical to the copies taken before it (same
contents and size). I then rebuilt the figure with `make fig` so that the PDF is newer than its data.

Geometry recomputed from fig09.tex. The hidden axis's unit vectors are x = vs Hy (1.15, 0.61) cm and
y = vs Hy (0, 1.38) cm, with vs = 1.75 and Hy = 2.3. These are the `tamr view` TikZ x and z vectors scaled by Hy.
So the u arrows lie along TikZ x at 27.94 deg on the page, the same angle as the tau arrows, the dx edges and the
book's x axis. The arrow tips lie on the curve within 6e-6 H. The arrows run from 0.80 cm (the shortest) to
1.81 cm. The base line rises 5.55 cm and the curve's top 6.38 cm, which is the oblique view's rise of u along x.

Round 1 findings:
- R1 #1 (should-fix: the tau arrows lie at 28 deg to the flat profile's u arrows): **resolved by option (i).** The
  u(y) profile is drawn in the same house view, in a plane parallel to the element's x-y plane: the base line runs
  along y (TikZ z) and the arrows along x (TikZ x). The u arrows are now parallel to both shear stresses and to the
  dx edges, as the 1973 art draws them. The header (l.2-12) records the reason. The fixer has flagged this for the
  gate: the profile is now seen obliquely instead of flat (note 1).
- R1 #2 (should-fix: profile styling): **resolved.** `profile` / `profile arrow` (l.22-25) match fig06.tex and
  fig16-18/25.tex exactly. The curve uses `profile` (l.36), the 18 arrows use `profile arrow` (l.34-35) and the base
  line is an `outline` (l.37).
- R1 #3 (note: the lower tau is hidden inside the element): unchanged and still right. The segment from the
  lower-face centre to the midpoint of the -x face's bottom edge lies in the unseen bottom face, so it is dashed,
  and the arrow is solid beyond that edge.
- R1 #4 (note: check that the shortest arrow still reads with 3.4pt heads): checked. At 300 dpi the lowest
  arrow (0.80 cm) has a clear head, and the top arrows' heads sit on the curve where it turns back.

Re-checked for regressions:
- Lettering is complete and unchanged: $u(y)$; $\tau + \dfrac{\partial\tau}{\partial y}\,dy$ (partial signs, as
  drawn); $\tau$; $dx$, $dy$, $dz$. Nothing is added, and there are no panel letters (the 1973 parts are unlettered).
- The element is unchanged apart from the shift to (3.95, 1.4). It is right-handed (book x = TikZ x, y = TikZ z,
  z = -TikZ y). Its seen faces are -x, +z and the top. The three hidden edges meet at the far bottom corner. The
  diagonals of the top face are solid and those of the bottom face dashed, and the face centres are marked with
  `point`. The upper arrow points +x and the lower one -x, as eq. (13) needs. The dx, dy and dz labels sit on
  edges of the right directions. $dz$ clears the tau arrow by about 5 mm at 300 dpi.
- Layout: the profile and the element do not touch. $u(y)$ clears the curve, and the tau label clears the
  profile's foot. The curve's top end reaches the page edge at the bounding box (a butt cap on a near-vertical
  line, so it is not visibly cut). Width 4.08 in.
- House rules: the data curve is in s1, the text in ink, the vectors use `vec`, and the hidden edges use `hidden`.
  The local `profile` styles are the chapter's profile-family definitions, not redefinitions of kit names.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | For gate visibility (the fixer also flagged it): the u(y) profile is now drawn obliquely in the house view. Its arrows rise at 28 deg from a vertical base line, parallel to the tau arrows and dx edges, where the 1973 art keeps the profile flat with horizontal arrows. The shape (bulge near 0.8 H, slight turn back at the top) is still visible, sheared, and the profile reads as a profile seen in the element's x-y plane. This is a correct and consistent geometry. The alternative is the round 1 flat layout with the 28 deg difference recorded for the gate. | fig09.tex:30-39 | None for the redraw; the owner decides at the Ch3 gate. |
| 2 | note | Outside this family, Ch3 Figs 10 and 13 still use the ink profile form. Figs 6, 9, 16, 17, 18 and 25 now share the s1 profile-family styles (see the Fig 6 round 2 note 2). | fig10.tex:12-13, fig13.tex:13-14 | For the chapter consistency pass. |

## Verdict: pass (0 must-fix, 0 should-fix)
