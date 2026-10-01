# v2 audit: ch4/fig07c (round 1)

Sources checked: scan `figures/ch4/fig07c.png` (3x-5x zooms of both label areas). I measured the tick-label baselines
and the legend rules to test whether the crop is turned. Redraw `figures/v2/ch4/fig07c.pdf` (rendered at 300 and 600
dpi, with a crop of the leaders). Source `figures/v2/ch4/fig07c.tex` lines 1-32; `fig07c.py` lines 1-50 (with the
helpers it imports from `fig07a.py`); `fig07c.csv` (378 rows); `fig07c.calib.json`. Other sources: inventory row
`ch4-fig07c` (`figures/v2/inventory.csv`:134); float and caption `chapters/ch4-sec2b.tex`:441-447; the collective
text and key table :306-372; `corrections/v2-figures.md`:82-84; the template `fig06a.tex`.

Reruns:
- I ran `fig07c.py` on a copy in the scratch directory. The CSV it writes is byte-identical to the repository's.
- I ran the overlay of the four curves. 95% of the points are within 0.00 px for FM k_min and FM k_max and 2.00 px
  for CB k_min and CB k_max. The maxima are 2.0, 0.0, 2.24 and 2.24 px. All pass.
- Calibration: the y residual is 0.78 px at most.
- I checked CB k_min from 0.095 to the end against the dash centres of the scan, column by column. It is within
  0.1 point everywhere, so its slight rise to -5.75 near 0.11 and its return to -6.0 are printed.

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The $k_{\max}$ leader ends on the upper FM solid, but first it crosses the lower FM solid (FM k_min). At its end ($m_o$ = 0.061) the two solids are only 0.47 point apart: 1.0 mm centre to centre at final size, or 0.65 mm of clear space between the two 1 pt blue lines. So the only stretch of leader that shows which solid it marks is 0.65 mm long, between two lines of the same colour and style. This leader is the figure's only direct cue to which solid is k_max. (The $k_{\min}$ leader ends on the lower solid at 0.091, and the reader has to infer the rest.) The inventory already flags the pair as ambiguous. The 1973 art avoids this by breaking the lower solid where the leader passes (scan cols 212-221, row ~159). | fig07c.tex:24-25 | Do what the print does: leave a short white gap in the FM k_min line where the leader crosses it. Before the leader at line 25, add a flat white casing that stops short of the upper solid: `\draw[white, line width=2.4pt, shorten >=1.9pt] (kmax.north) -- (axis cs:0.0611,-0.421);`. I tested this on a scratch copy at 600 dpi: the lower solid gets a clean gap about 2 pt wide, and the upper solid and the zero line are untouched. With `shorten >=1.2-1.3pt`, or as a `preaction` with that shorten, the upper solid gets a visible notch. Alternatively, move the fork a little to the right, where the solids are further apart (0.6 point at 0.075), keeping the label between the solids and the dashed curve. |
| 2 | note | The values differ from the inventory's eyeball reading, but the calibration is right. The inventory reads the solids' ends as about -2 and -3.2 and calls the rising zero line (about +0.5 at the right end) a drafting slip. The crop is in fact turned by about 0.55 degrees: the x axis rises 4.5 px across the axis, the zero line rises the same, and the tick-label baselines rise 5 px (rows 313 at .03 to 308 at .13). The affine fit uses the x axis and the zero line at every tick column, so it takes the turn out. The redraw's level zero line and its end values (FM k_max -2.31, FM k_min -3.69) are read relative to the drawn zero line, which is right. The inventory's "draw it level" is met. | fig07c.calib.json; inventory.csv:134 | None for the figure. The inventory's curve values could be updated when its status changes. |
| 3 | note | The other three leaders cross no curve. The $k_{\max}$ leader to CB k_max is a short stub (about 1.7 mm at final size, from the label's south-west corner), as in the print. | fig07c.tex:26-29 | None needed. |

Also checked, with no issue:
- **Frame and axes.** The frame is identical to fig06a (axis box 2403 x 1501 px at 600 dpi). x runs 0.03-0.13,
  labelled at the odd hundredths with minor ticks at the even ones. y runs -15 to 15 in steps of 5. The titles are
  "Percent error in $y_{\max}$" and "$m_o$ (kg)".
- **Legend.** The legend is at the upper right, as printed.
- **Curve identities.** The solids are assigned by the leaders, as the drafter says. The $k_{\max}$ leader passes a
  break in the lower solid to the upper one, and the $k_{\min}$ leader ends on the lower one. So upper = k_max, which
  agrees with the inventory.
- **Leader ends.** The leader ends lie on the CSV curves within 0.002 point: FM k_max -0.422, CB k_max -4.050,
  FM k_min -2.096, CB k_min -6.005.
- **Curve shapes.**
  - The two solids start together at +0.8 and run as one line to about 0.036.
  - The FM k_max solid crosses the zero line near 0.05.
  - The dashed curves cross near 0.079 (print about 0.08).
  - CB k_max runs from -1.4 to -9.3.
  - CB k_min runs from -5.3, down to -6.4 near 0.06, and to -6.0 at the end.
- **Labels.** $k_{\max}$ is at (0.0604, -2.64) and $k_{\min}$ at (0.0897, -4.21), matching the print's (0.061, -2.75)
  and (0.0895, -4.2).
- **Style.** The house style is followed, and there is no panel letter in the art (`\figurepanel{c}`).
- **Caption.** The caption holds for the redraw.

## Verdict

fix (0 must-fix, 1 should-fix: the k_max leader crossing the k_min solid)
