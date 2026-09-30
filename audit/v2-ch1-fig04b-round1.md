# v2 audit: ch1/fig04b (round 1)

Sources checked: figures/ch1/fig04b.png (scan); figures/v2/ch1/fig04b.pdf (rendered 300 and 400 dpi, with the
axis and strip positions measured in pixels); figures/v2/ch1/fig04b.tex:1-29; figures/v2/common/b4.csv (area
integrated); figures/v2/inventory.csv row ch1-fig04b; caption chapters/ch1-sec2a.tex:343-355 and citing text
ch1-sec2a.tex:367-381; corrections/v2-figures.md (standing rule 5); figures/v2/tamrfig.sty; the fig04a redraw
(same curve, same panel size).

Checked and correct:
- **(c) axes.** y 0-16 step 4 and x 0-1.2 step 0.4 (printed 0, 0.4, 0.8, 1.2). $F$ (N) is rotated; $t$ (sec)
  is present.
- **(c) grid.**
  - The squares are 0.1 sec x 1 N, as the caption requires: minor grid at every 0.1 sec and every 1 N, 12 x 16
    squares.
  - The grid is closed at t = 1.2 and F = 16.
  - All lines have one weight, and the curve is drawn over them.
- **(c) lettering.** $I_t \cong 49.7 \times 0.1$ / $= 4.97$ N-sec is set above the plot; 49.7 x 0.1 = 4.97.
- **(d) scale.** The cutout is the same b4.csv, closed along the baseline (`-- cycle`). It is drawn at (c)'s
  scale: 2.25 in per 1.2 sec (measured 900 px at 400 dpi in both panels) and 1.55 in per 16 N (peak measured
  12.98 N).
- **(d) reference strip.** It is exactly 1 sec x 1 N at that scale (750 x 39 px at 400 dpi) and is centred
  above the cutout.
- **(d) lettering.** "0.38 g = 1.0 N-sec" above the strip and "1.90 g = 5.0 N-sec" below the cutout;
  1.90 / 0.38 = 5.0.
- **Panel letters.** (c) and (d) are present.
- **Caption and text.** Everything they rely on for (c) and (d) is true of the redraw.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | In (c) the burnout drop at t = 1.2 sec lies on the plot's clip edge (xmax = 1.2). Half of the stroke is clipped, so the drop renders at about half the curve's width, while the same drop in (d) (clip=false) is full width. | fig04b.tex:9, 14 | `clip=false` on the (c) axis (as in fig04a finding 2 and fig05 finding 2). |
| 2 | note | The drawn curve encloses 5.09 N-sec, i.e. 50.9 squares of (c) and 5.09 strips of (d), while the lettering says 49.7 squares (4.97 N-sec) and 1.90 g = 5.0 N-sec. A reader counting the redraw's squares gets about 51. The difference (2.4%) is within the "approximate number of squares" the caption speaks of, and it is the consequence of the shared 1994 tracing (rule 5). If the gate adopts the 1973 tracing for Fig 4 (fig04a finding 1, option (i)), recheck the count. | fig04b.tex:14, 18, 22-25 | None required; mention it at the gate with fig04a finding 1. |
| 3 | note | The white knock-out behind "(c)" blanks the grid in the upper right corner (about t 1.09-1.2, F 14.4-16): the t = 1.1 sec and F = 15 N lines break there. No square the curve encloses is affected. | fig04b.tex:15 | Optional: set (c) above the plot's upper right corner, beside the formula, and leave the grid whole. |

## Verdict

pass (0 must-fix, 1 should-fix)
