# v2 audit: ch1/fig05 (round 2)

Sources checked: figures/ch1/fig05.png (scan); figures/v2/ch1/fig05.pdf (rendered 300 and 600 dpi, stroke widths
measured in pixels); figures/v2/ch1/fig05.tex:1-27; figures/v2/common/b4.csv, b14.csv, e62.csv, engines.py;
figures/v2/inventory.csv row ch1-fig05; caption chapters/ch1-sec2a.tex:403-412; corrections/v2-figures.md (rule 5);
STYLE.md section 16.

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | should-fix | resolved | All three letters are now at the upper right inside their axes (`rel axis cs:1,1`, `anchor=north east`; fig05.tex:12, 18, 24), the STYLE.md section 16 rule for plots and one of the two fixes round 1 offered. Each panel is its own row, so no common baseline applies. Nothing collides: the B14 and E62 curves are at zero under the (b) and (c) corners. |
| 2 | should-fix | resolved | `clip=false` on axis (a) (fig05.tex:9). At 600 dpi the burnout drop at t = 1.2 sec is 7 px wide, the same as the plateau stroke (7 px). (b) and (c) end inside their x ranges (0.35 and 0.537 sec), so they need no change. |
| 3 | note | accepted: layout change, no content change | One time scale for the three panels (fig05.tex:7, 15, 21), unchanged. |

Rule 5: panel (a) keeps the shared 1994 tracing figures/v2/common/b4.csv (fig05.tex:10), as intended; only Ch1 Fig
4 takes the exception.

## New findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The first x tick label reads "0.0" in all three panels (`fixed zerofill`), where the scan prints "0" and the redraws of Figs 3 and 4 print "0". | fig05.tex:8 | Optional: explicit `xticklabels` (as fig03.tex:11 does) so the origin reads "0" while 1.0 keeps its zero. |
| 2 | note | The B14 and E62 tracings keep a small pixel-staircase wobble: the E62 linear rise departs from its best straight line by up to 0.77 N (0.2 mm, less than the 1pt stroke), and the B14 ends with a 0.7 N vertical hook at 0.35 sec. Visible only when zoomed. | common/b14.csv, e62.csv (engines.py, `--smooth 3`) | None required. |

## Verdict

pass (0 must-fix, 0 should-fix)
