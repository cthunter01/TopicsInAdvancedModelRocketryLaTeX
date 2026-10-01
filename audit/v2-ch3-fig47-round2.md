# v2 audit: ch3/fig47 (round 2)

Sources checked: scan `figures/ch3/fig47.png` (cells (a)-(c) zoomed x3); redraw `figures/v2/ch3/fig47.tex`,
`fig47.py`, `fig47.csv`; `make fig F=ch3/fig47` (5.89 x 3.57 in; one font, TeXGyreTermesX-Italic, embedded),
rendered at 400 and 600 dpi, with 1200 dpi crops of the (b) and (c) cones and the (e) nose; compare image;
inventory row `ch3-fig47`; caption and citing text `chapters/ch3-sec6a.tex:289-329`; `figures/v2/tamrfig.sty`
(phantom, hidden, hatch, panel); approved Ch2 Fig 41 (`phantom, draw=ink2`, fig41.tex:22); round-1 audit and fix
report.

Checks run (fig47.py imported and `run()` evaluated in memory; no project file written):
- Regeneration: `run()` gives the same 11874 rows and style codes as `fig47.csv`. Coordinates agree to 5e-5 cm,
  which is the CSV's 4-decimal rounding.
- Geometry: alpha = 21.80 deg. The planes lie at 42.00 / 21.80 / 14.00 deg to the axis. Eccentricities are
  0.800 / 1.000 / 1.045. Every section point lies on the cone to 3.3e-16. The (a) ellipse closes at z 0.70-1.81.
  The (b) and (c) sections end on the base chord (z = 0), with vertices at z = 2.10 and 2.31. For (b),
  K^2 sin^2(beta) = cos^2(beta), so Q(b) is linear and the section is a true parabola. m.C is 0.76 / 0.28 / 0.33.
- Nose ratios l/d: (a) 0.834, (b) 1.542, (c) 1.372, (d) 1.422, (e) 0.973. These agree with the fix report.
- Page directions. The right silhouette runs at 25.9 deg from the vertical. The steepest line of each plane (s)
  runs at 30.8 / 24.6 / 15.4 deg from the vertical in (a) / (b) / (c). In (b), the plane's long edges are within
  1.3 deg of parallel to the right silhouette, which shows "parallel to a generator". In (c) they are steeper than
  the silhouette. So the different plane azimuths (gamma 40 / 6 / 14) still let the reader see the order
  greater / equal / less that the caption gives.
- Proximity on the page between section outline and right silhouette, below 0.9 H: (b) 0.82 mm, (c) 0.81 mm. In
  round 1 it was 0 over 1.0-1.8 cm. The cut-away lines (code 7) still run within 0.6 mm of solid lines for at most
  0.38 cm. All of these are at junctions or crossings: the chord ends, the base arc where it crosses the
  rectangle's edge, the apex, and the tangent meeting points.
- Rectangle corners against the cone outlines, as page distances (corner order (a-,b-), (a+,b-), (a+,b+), (a-,b+)):
  all are 1.5 mm or more except (b) corner (a+, b+) at (4.32, -1.78) cm, which is 0.46 mm from the left silhouette,
  and (c) corner (a+, b+) at (7.41, -1.80) cm, 0.88 mm from it. The apex is 1.87 mm (b) and 0.99 mm (c) from the
  nearest rectangle edge. The rectangle tops are at y = -0.35 and -0.28 cm, below the rule tops at -0.25.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-1 should-fix 1 (ragged double edge in (c) and (b)) is **resolved**. The (b) and (c) sections now keep 0.82 / 0.81 mm from the cut-away right silhouette everywhere. At 1200 dpi the hatched sliver's right edge and the grey phantom are clearly separate lines, about 1.0-1.3 mm apart over most of their length. What remains near other lines are only meeting points: tangency at the section vertex, the chord ends and the base silhouette points. Moving the planes kept the conic types and the angles to the axis. | fig47.py PLANES (b), (c) | none |
| 2 | note | Round-1 should-fix 2 is **resolved**. Code 7 is drawn `phantom, draw=ink2`, as in Ch2 Fig 41, and the kept piece's hidden edges stay `hidden` in ink. The cut-away pieces now read as context and the hidden edges as hidden. | fig47.tex:29 | none |
| 3 | should-fix | **New in the fix.** In (b), the plane rectangle's left corner (a = +1.60, b = bv + 0.40; page (4.32, -1.78) cm) is only 0.46 mm from the cone's left silhouette generator. The silhouette crosses the rectangle's lower-left edge right beside the corner. With 0.6 pt lines this leaves a gap of about 0.25 mm between the line edges, so at final size the corner, the solid silhouette and the first hidden dash meet in one knot, and the plane's corner appears to sit on the cone's side. The fix report says the corners are at least 1.5 mm from "the generator", but that is true only of the right one. The (c) corner is 0.88 mm away, which is acceptable. Changing aw alone does not help, because t projects within 15 deg of the left silhouette's page direction, so the corner moves along the generator. | fig47.py:82 (PLANES "b" rect = (1.60, 0.25, 0.40)) | Move the corner off the generator by changing the upper margin. For example, rect = (1.50, 0.25, 0.55) puts the left corner 1.45 mm from the left silhouette, the right corner 1.24 mm from the right one (now 1.52) and the top corner at y = -0.29 cm (still below the rules). The apex is then 1.60 mm from the nearest edge. (1.45, 0.25, 0.60) gives 1.80 mm with top y = -0.28. Check at 600 dpi. |
| 4 | note | Consequence of the new plane azimuths, legible as it stands. In (b) and (c) the base chord is parallel to the rectangle's lower t-edge, about 1.1 / 1.2 mm away. In (c) the hidden left generator (black dashes) runs about 0.9 mm from, and parallel to, the rectangle's upper-left t-edge for about 0.7 cm (page angles 64.1 and 64.8 deg). Dashed against solid at 0.9 mm reads correctly at 600 dpi. | cells (b), (c) | none required |
| 5 | note | The fixer's doubts are reasonable as stated. The (b) and (c) planes face differently from (a) (gamma 6 / 14 against 40). The 1973 art is not consistent either, and the page-angle check above shows the order the caption gives is still visible. The (b) nose is blunter than the 1973 art (l/d 1.54 against about 2.3 by eye) because it is the exact segment of the re-placed plane. It is still more slender than (c) (1.37). Phantom pieces shorter than the 14 pt dash (apex to section in (a)-(c)) render as solid grey, as in approved Ch2 Fig 41. | fig47.py docstring, PLANES | Gate or doubt items only; no change needed. |
| 6 | note | Round-1 note 4 (optional) is declined, and that is acceptable. In (e) the phantom left generator crosses the phantom base ellipse's back arc and runs within 0.6 mm of it for about 0.48 cm, down to the leftmost point. That is a small tangle of two dash patterns at the lower left of the (e) nose. It follows from the 1973 meridian-section convention. | cell (e), nose base left | Optional, as in round 1. |
| 7 | note | No other regressions. Cells (a), (d) and (e) are unchanged. Panel letters (a)-(e) use the house panel style at the lower right of each cell, on one baseline. The cells are separated by ink2 rules and have no outer frame. The hatch is at 45 deg. Width 5.89 in, under the 6.5 in limit. | fig47.tex | none |

## Verdict: pass (no must-fix)
