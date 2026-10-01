# v2 audit: ch3/fig30 (round 1)

Sources checked: scan `figures/ch3/fig30.png` (581 x 359 px; both insets zoomed 4x; the rear of the 2-D section
dumped pixel by pixel); redraw `figures/v2/ch3/fig30.pdf` (current: same time as the .tex; 420.5 x 267.1 pt =
5.84 x 3.71 in; fonts embedded), rendered at 400 dpi and at 1200 dpi (inset 1), and
`build/v2/png/ch3-fig30-compare.png`; `figures/v2/ch3/fig30.tex`, `fig30.py`, `fig30-2d.csv`, `fig30-3d.csv`,
`fig30.calib.json`; inventory row `ch3-fig30` (`figures/v2/inventory.csv`:96); caption
`chapters/ch3-sec4b.tex`:181-184; citing text :165-176 (sharp decline at r/h ≅ 0.1 for 3-D shapes; critical
r/h = 0.1); `STYLE.md` sections 14 and 16; `tamrfig.sty` (tamr, series1/2, thin vec, leader, extension, \dimout).

Checks made:
- **Calibration.** `digitize.py ticks` puts the x ticks at columns 86.5, 162.5, 239.0, 313.5, 387.5 and 460.5 and
  the y ticks at rows 286, 241, 196.5, 151.5, 106.5, 61.5 and 16.5. These are exactly the calib's xgrid and
  ygrid, so the piecewise calibration is right for the hand-ruled ticks.
- **Data.**
  - I re-ran `fig30.py` with its writes intercepted. Both CSVs come out byte-identical, so they are current and
    reproducible.
  - `digitize.py overlay`, run myself: 2-D mean 0.01 px, 95% 0.00 px, max 1.0 px; 3-D (dashed) mean 0.50 px,
    95% 2.00 px (0.34 mm), max 3.0 px. Both pass.
  - Sampled values (2-D / 3-D): r/h 0: 1.148 / 1.027; 0.05: 0.961 / 0.766; 0.07: 0.766 / 0.338; 0.08:
    0.666 / 0.214; 0.1: 0.566 / 0.144; 0.2: 0.357 / 0.067; 0.5: 0.171 / 0.053. These match the inventory's
    reading.
  - The 3-D curve falls almost vertically between r/h 0.04 and 0.08, which is the sharp decline near 0.1 that
    the text relies on.
  - The 3-D tail rises by 0.0008 between r/h 0.436 and 0.47. That is sub-pixel, follows the ink and is invisible.
- **Lettering.**
  - The y title is $C_{D_0}$, horizontal, as printed. The x title is $\dfrac{r}{h}$, stacked.
  - The ticks run 0-1.2 by 0.2 (labelled 1.0 and 1.2) and 0-0.5 by 0.1, as printed.
  - Inset labels: "2-D half-streamlined section, $R = 10^{5}$" and "3-D streamlined body, $R = 10^{6}$" (R italic,
    STYLE section 14). Inset 1 also has $U$, $r$ (leader to the front corner) and $h$ (upright, between two
    `\dimout` arrows from outside on extension lines). Inset 2 has $U$. Everything is present and nothing is
    added.
- **Curve identity.** The solid curve is series1 and the dashed curve series2, matching the printed solid and
  dashed. Each is tied to its inset by a leader, as printed: from (246, 134.5) to the 2-D curve at r/h 0.167,
  and from (444, 216.5) to the 3-D curve at r/h 0.436. These are the scan's leader ends (214 and 414 px →
  r/h 0.167 and 0.436).
- **Insets.**
  - Inset 1: I fitted the 2-D section's rear on the scan. It is a half-ellipse of about 45 x 13 px from
    x ≈ 276, tip at 321.5. The redraw's is 55 x 13 px from 270, tip at 325, within about 3 px across its height.
    The flat front has corner radius r, as printed.
  - Inset 2 has a flat front with rounded corners, a cylinder and an ogive tail to a point, with a dash-dot
    axis. It sits where the scan has it.
  - The insets are placed in scan pixels on the 4.2-in axes (`scale only axis` is set, so they stay registered).
- **Legibility.** Nothing overlaps. The `r` leader stops at the corner arc, and both `U` arrows end at the
  bodies' front faces. The width is 5.84 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | The 3-D leader crosses the solid 2-D curve near r/h 0.46, as printed. It is a thin ink2 line between two coloured curves, so it is not mistaken for either. | fig30.tex:48 | None. |
| 2 | note | Arrowheads are added on the insets' $U$ lines (thin vec), where the 1973 lines are plain. Fig 29's free-stream $U$ uses the heavier `vec`, which suits its larger scale. | fig30.tex:36, 55 | None. |
| 3 | note | The y title is $C_{D_0}$ while the caption says "drag coefficient". It is kept as printed (rule 2). | fig30.tex:21 | None. |

## Verdict: pass (no must-fix)
