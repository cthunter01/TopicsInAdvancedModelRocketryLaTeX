# v2 audit: ch3/fig29 (round 1)

Sources checked: scan `figures/ch3/fig29.png` (566 x 276 px; zoomed 3x, the cavity of shape 7 dumped pixel by
pixel); redraw `figures/v2/ch3/fig29.pdf` (current: same time as the .tex; 356.9 x 156.2 pt = 4.96 x 2.17 in; all
fonts embedded Type 1), rendered at 400 dpi, and `build/v2/png/ch3-fig29-compare.png`; `figures/v2/ch3/fig29.tex`;
inventory row `ch3-fig29` (`figures/v2/inventory.csv`:95); caption `chapters/ch3-sec4b.tex`:146-148; citing text
:131-141 (first two shapes near zero; bluntness rises "from left to right", errata note), :152-156 ("the first
shape", negative value), :165 ("shapes #3 and #6"), :188-189, :196-197; `corrections/v2-figures.md`; `STYLE.md`
sections 14 and 16; `tamrfig.sty` (outline, hatch, centerline, hidden, vec); `macros.tex` (`\CDo` = $C_{D_0}$).

Checks made:
- **Lettering.** The row label is $\CDo =$, and the seven values, left to right, are $-.05$, $+.01$ (with the
  explicit plus), .20, .20, .34, .90 and 1.0, with leading-dot decimals as printed, all on one baseline under the
  body centres. $U$ is at the lower end of the flow line. Nothing is missing and nothing is added. The family
  brief says "$C_{Db}$ values", but the scan and the inventory letter $C_{D_0}$, and the redraw follows the scan
  (STYLE section 14: `\CDo`).
- **Order and shapes.** The order is the text's #1-#7. On the scan I measured the body centres (87.5, 164.5,
  240.5, 315, 388.5, 461.5, 534.5 px) and the radius (19-19.5 px). The redraw spaces the bodies evenly at
  R = 19, within 3.8 px of the scan's centres.
  - Shape 1 is a half ellipsoid 30 px long. At 13.5 and 23.5 px below its base it gives half-widths of 17.0 and
    11.8 px; the scan measures 16.75 and 11.5.
  - Shape 2 is a hemisphere.
  - Shape 3 has a corner radius of 0.1 d.
  - Shape 4 is a cone of 22 deg half-angle. The scan gives 21.7 deg (half-width 14.5 px at 36.5 px from the
    tip).
  - Shape 5 is a cone of 39 deg half-angle. The scan gives 39.3 deg.
  - Shapes 4 and 5 have their joint lines.
  - Shape 6 has a flat face.
  - Shape 7 has a flat face with a hidden-line cavity, depth 1.0 d (the scan's 36 px on 35.5).
  - #3 against #6 (a small rounding against sharp corners) reads as the text needs.
- **Break and line work.** Every body is broken off at the top with the conventional round-bar break: a hatched
  lobe at 45 deg on the left and the surface arc on the right, as printed. The dash-dot centre lines run beyond
  both ends. The outlines are 0.6 pt and there is no fill.
- **Flow.** The 1973 flow line has no arrowhead. The redraw draws $U$ as a house `vec` pointing up, towards the
  noses, which is the right sense for bodies drawn nose down (flow from below).
- **Legibility.** Labels are `\small` and nothing overlaps. The width is 4.96 in, under 6.5 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | Shape 7's cavity is 0.70 d wide (inner wall 5.7 px inside the outer wall). On the scan it is about 0.76 d (walls at x = 521 and 548 on a body 516.5-552). The difference is 0.3 mm at final size, and the cavity still reads as a cup. | fig29.tex:52 (`\xg-13.3`, `\xg+13.3`) | Optional: ±14.5 instead of ±13.3. |
| 2 | note | The arrowhead on $U$ is added (the 1973 line is plain), as a house velocity vector. The sense is right for flow from below. | fig29.tex:54-55 | None. |
| 3 | note | The family brief's "$C_{Db}$" does not match the artwork. The redraw correctly keeps the printed $C_{D_0}$. | fig29.tex:57 | None. |

## Verdict: pass (no must-fix)
