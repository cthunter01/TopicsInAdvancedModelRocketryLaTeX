# v2 audit: ch1/fig04b (round 2)

Sources checked: figures/ch1/fig04b.png (scan); figures/v2/ch1/fig04b.pdf (rendered 300 and 600 dpi, extents,
stroke widths and letter positions measured in pixels); figures/v2/ch1/fig04b.tex:1-29;
figures/v2/common/b4-1973.csv (area integrated); figures/v2/inventory.csv row ch1-fig04b; caption
chapters/ch1-sec2a.tex:345-355 and citing text ch1-sec2a.tex:367-381; corrections/v2-figures.md (rule 5 and its
exception; minor item on Fig 4(c)); STYLE.md section 16; the fig04a redraw and its round-2 report.

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | should-fix | resolved | `clip=false` on the (c) axis (fig04b.tex:11). At 600 dpi the burnout drop at t = 1.2 sec is 10 px wide (1pt stroke plus antialiasing), the same as the rise's stroke. |
| 2 | note | accepted: logged minor | The curve is now the 1973 tracing (area 5.189 N-sec, about 52 squares against the lettered 49.7): corrections/v2-figures.md, Minor, "Ch1 Fig 4(c)", keeps the book's count. |
| 3 | note | not resolved (note, no action required) | The white knock-out behind "(c)" (fig04b.tex:15, `fill=white`) still breaks the t = 1.1 sec and F = 15 N lines in the upper right corner. No enclosed square is affected. |

Rule-5 exception: (c) (fig04b.tex:14) and (d) (fig04b.tex:22) both draw b4-1973.csv, the tracing of fig04a. They
are at one scale: at 600 dpi the (c) curve spans 1357 x 771 px and the (d) cutout 1353 x 768 px (the difference
is the 1pt against 0.6pt stroke); the reference strip is 1124 px long, 1.0 sec at that scale. (c)'s grid is 0.1
sec x 1 N, one weight, closed at 1.2 sec and 16 N; the lettering of (c) and (d) is as printed.

## New findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The panel letters of the row are not on one baseline (STYLE.md section 16). (c) sits at the upper right inside its axes (ink rows 328-397 at 600 dpi); (d) sits at the top of the figure, above the reference strip (rows 30-100), 0.50 in (12.6 mm) higher. | fig04b.tex:15, 26 | Name the (c) node and set (d) at the right edge of panel (d) on its baseline, e.g. `\node[panel, anchor=base east] at (<x of the present (d)> |- pc.base) {(d)};`. At that height the right end of (d) is empty (the strip is above it, the cutout's plateau is 3.6 N high). |
| 2 | note | The spike's shoulders at about 11 N (fig04a round 2, new finding 1: the same b4-1973.csv) show in (c) and in the outline of (d). | common/b4-1973.csv | Fixed with fig04a. |
| 3 | note | The two images of the float are 437.2 pt (fig04a) and 430.3 pt (fig04b) wide with their y axes at the same offset from the left edge, so when they are stacked and centred, as in the float (ch1-sec2a.tex:342-344), (c)'s axis sits 3.4 pt (1.2 mm) right of (a)'s. | fig04a.tex, fig04b.tex (bounding boxes) | Optional: give both the same width (e.g. `\useasboundingbox` or a phantom at the right), or make Figure 4 one 2 x 2 figure, as the inventory row suggests. |

## Verdict

pass (0 must-fix, 1 should-fix)
