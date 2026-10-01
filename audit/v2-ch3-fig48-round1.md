# v2 audit: ch3/fig48 (round 1)

Sources checked: scan `figures/ch3/fig48.png` (zoomed 3-4x: fins, nose, every dimension); redraw
`figures/v2/ch3/fig48.tex`, `fig48.calib.json`, `figures/v2/ch3/fig48.pdf` rendered at 400 dpi, and
`build/v2/png/ch3-fig48{,-compare}.png`; inventory row ch3-fig48; caption and citing text
`chapters/ch3-sec6b.tex` (lines 1-140: tangent-ogive nose, l_b = 31.75, 22.61 + 9.14, root chord 3.97, tip 2.07,
d = 1.93, t = 0.238); STYLE.md sections 14 and 16; `corrections/v2-figures.md` (rule 4, D26 via the inventory);
approved Ch2 Fig 48 for the dimension idiom; `pdffonts` (fonts embedded); page 360 x 192 pt = 5.0 in wide.

Checked:
- Lettering: all eight printed dimensions are present with the printed values: 31.75, 9.14, 3.30, 1.93, 4.19, 0.68, 1.91,
  2.07. 4.19 and 0.68 are rotated like the scan (numeric, so allowed). Each label sits on the same side as in the scan:
  1.91 to the left and 2.07 to the right (both `\dimout`), 0.68 above, 1.93 above.
- Geometry drawn to the labels at 1:3. Root leading edge 28.45, tip leading edge 30.36, trailing edge 32.43, tip
  5.155 above the axis, chamfer top 1.645 above the axis. The labels close exactly (28.45 + 1.91 + 2.07 = 32.43 =
  31.75 + 0.68), so the chamfer is at 45 degrees. That matches the scan (TE about 32.47 cm, chamfer about 0.66 high
  on the scan's body scale). The root chord to the TE line is 3.98, against the text's 3.97. Labels are kept per D26.
- Tangent-ogive nose (the text: "tangent-ogive nose"), 9.14 long, diameter 1.93. The nose-body joint is drawn.
- The edge-on fin pair is a thin rectangle on the axis, running from the root LE to the TE past the base. This is
  geometrically right: the scan's lens shape stops at the base, but the fins stand 0.68 past it.
- Extension lines have gaps at the outline (0.35). The dimension and extension styles match Ch2 Fig 48. The
  `dim stub length` is reset after the 1.93 dimension.
- Nothing is clipped, no labels overlap, and the arrowheads are visible at final size.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The base extension line, shared by 31.75 and 3.30, runs up through the upper fin and across its tip chord. The xle extension crosses the 4.19 extension at (28.45, 5.155). Both are as printed in 1973 and read clearly. | fig48.tex `\draw[extension] (\Lb,\R+0.35) -- (\Lb,10.6);` | none needed (optionally break the base extension inside the fin) |
| 2 | note | The 1.93 is a leader-style vertical line in the scan. The redraw makes it a two-arrow `\dimout` with the label above, in the house idiom. | x = 12.65 | none |
| 3 | note | The 0.68 lower stub crosses the centre line below the body, as in the scan. | `\dimout` at x = 33.6 | none |

## Verdict: pass (no must-fix)
