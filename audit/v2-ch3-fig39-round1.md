# v2 audit: ch3/fig39 (round 1)

Sources checked: figures/v2/ch3/fig39.tex, .py, .calib.json, fig39-tip2..6.csv, fig39-core1..6.csv and .pdf
(built 22:17, after the .tex; log clean; 371.9 x 448.7 pt = 5.17 x 6.23 in, fonts embedded). Renders at 400 and
500 dpi; the 500 dpi render (4 px per unit, columns shifted by the .tex's \col offsets) was overlaid on the 4x scan
column by column for panel (b), sections, planforms, cores, tip lines and labels. `tools/v2/digitize.py overlay`
was run on all 11 CSVs. Also checked: figures/ch3/fig39.png (zoomed: (a), (b), the six relation signs); inventory
row ch3-fig39; caption chapters/ch3-sec5a.tex:372-383; citing text ch3-sec5a.tex:343-354; corrections/v2-figures.md
standing rule 1 (Fig 39 "dotted", printed dashed); STYLE.md sections 14 and 16 (\AR, \Delta\AR, \cong; 3D kit).

Lettering: $\bar{U}$; tip numbers 1-6; $y$ (upright, between the tip line of 3 and the core's extension line, as
printed); $\Delta\AR = {+0.04}$, $-0.18$, $-0.20$, $-0.19$ with "=" and $\Delta\AR \cong 0.0$, $0.0$ for 5 and 6.
Zoomed, the scan shows "=" for 1-4 and tilde-over-two-bars for 5 and 6. The labels are two lines each, as printed,
and panel letters (a), (b) sit on one right edge. All present and correct.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Digitized data sit on the scan (overlay run by the auditor). Tip outlines 2-6: 95% within 0-1 px, max 1 px. Cores 1-6: 95% within 2 px, max 2.2-3.0 px. All are "ok" against the 3 px target. In the column-by-column overlay of the render, sections, planforms, hatched teardrops, tip lines, cores, the y construction and the labels coincide with the 1973 ink. | fig39.py; fig39-*.csv | none |
| 2 | note | The rotation sense matches the caption. The house view looks from behind (-y), left (-x) and above, so the sense on paper equals the sense "viewed from behind". Left (-x) vortex: helix angle 180 - theta(s) decreasing downstream and its ring arrows (113 to -16, 293 to 164) clockwise. Right (+x) vortex: theta increasing and its ring arrows counterclockwise. Both match the 1973 arrows, and both match a wing lifting upward (outboard flow below the tip, up round it, inboard on top). The cores descend (-0.065 chord per chord) and tuck in (0.1 chord), as the caption says. | fig39.tex:30-50 | none |
| 3 | note | Panel (b) draws the planforms' inboard cut as a straight line through a symmetric hatched teardrop (a revolved section). The 1973 cut is an S-shaped freehand break, while the top-row end views keep a break (\breakline). The hatched section still marks the wing as cut, so the meaning holds, but the two rows now use different cut conventions. | fig39.tex:80-91 (\cutsection, \planform) | optional: draw the edge below the teardrop as a gentle S-break as printed (bulging about 5 units inboard at mid-chord) |
| 4 | note | The (a) wing is a square-tipped slab (\blk, AR 3); the 1973 slab has rounded tip outlines. Panel (a) does not depend on the tip shape, and the family brief asked for a slab. | fig39.tex:37 | none |
| 5 | note | Vortex cores use `dotted guide` (caption "dotted line"; the print is dashed), as standing rule 1 already lists. The tip lines use a figure-local `tip line` style (ink2, 0.45 pt) under a new name, which the kit rules allow; the 1973 tip lines are full weight. Solid tip line and dotted core remain easy to tell apart. | fig39.tex:31, 93-99 | none |
| 6 | note | The panel separator is one ink2 0.5 pt rule; the 1973 rule is double. This is a style change only. | fig39.tex:53 | none |

Legibility at final size: the ring arrows of (a) cross the helix loops, which is busy but readable and as printed.
In (b) nothing overlaps: each Delta-AR label clears its core and the next column's tip line by at least 1.5 mm. The
y gap (3.2 mm) holds the letter, and the dotted cores read as dotted. The figure is 6.23 in tall, which with its
eight-line caption still fits a float page.

## Verdict: pass (no must-fix)
