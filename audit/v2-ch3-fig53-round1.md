# v2 audit: ch3/fig53 (round 1)

Sources checked: scan `figures/ch3/fig53.png` (zoomed x4 at the rise, the peaks, the inset and panel (b));
redraw `figures/v2/ch3/fig53.tex`, `fig53.py`, `fig53-a-ogive.csv`, `fig53-a-half.csv`, `fig53-b-ogive.csv`,
`fig53-b-half.csv`, `fig53.calib.json`; `figures/v2/ch3/fig53.pdf` (5.00 x 5.64 in, fonts embedded) rendered at
400 dpi; `build/v2/png/ch3-fig53-compare.png`; inventory row `ch3-fig53`; caption and citing text
`chapters/ch3-sec7.tex:160-195, 208-252`, eqs. (214a)-(215b), Table 8 (`ch3-sec7.tex:256-310`); STYLE.md
sections 14, 16; `corrections/v2-figures.md`.

Checks run:
- (b) computed curves against eqs. (214), (215) and Table 8's [C_D/C_Ds]_a column at all ten Mach numbers:
  ogive 1.000, 1.089, 1.355, 1.800, 1.679, 1.513, 1.356, 1.300, 1.281, 1.274; half-round 1.000, 1.181, 1.388,
  1.606, 1.831, 2.300, 2.095, 2.030, 2.010, 2.003: all equal to the table (to its rounding). Peaks 1.800 at
  M = 1.05 and 2.300 at 1.2 (value of the second formula; the first gives 1.799 and 2.298, continuous to the
  eye). 1.0 below M = 0.9.
- (a) digitized curves against Table 8's [C_D/C_Ds]_e column: ogive 1.009, 1.139, 1.448, 1.700, 1.679, 1.573,
  1.405, 1.301, 1.254, 1.249 (table 1.00, 1.17, 1.43, 1.70, 1.67, 1.57, 1.40, 1.30, 1.27, 1.27); half-round
  1.788, 2.008, 2.170, 2.099, 2.031, 2.000, 2.000 from M 1.05 (table 1.76, 2.00, 2.17, 2.10, 2.03, 2.00, 2.00).
  Peaks: ogive 1.703 at M 1.061, half-round 2.171 at M 1.215; split at M 1.038, 1.69. The text's 1.7 at 1.05,
  2.17 at 1.2 and 2.0 toward M 2.0 are true of the redraw.
- `digitize.py overlay` (points M >= 0.85): (a) ogive 95% 0.00 px, max 1.00 px; half-round 95% 2.00 px, max
  2.24 px; (b) ogive 95% 1.00 px, max 1.41 px; half-round 95% 2.00 px, max 3.00 px: all "ok". A 1 px polyline
  of the (a) curves drawn over the x8 scan (through the script's own gridline interpolation) sits on the ink
  centre through the rise, the split and both peaks; the slight steepening of the rise where it crosses
  M = 1.0 is in the 1973 ink.
- Scan pixels at column 540 (M ~ 1.95): the drawn ogive line is at y = 1.248, so the art ends at 1.25, not
  Table 8's 1.27.
- Inset rocket measured on the scan (from the nose tip): tip at M 1.076, y 0.632 (redraw 1.09, 0.632); nose
  about 47 px, hatched band about 25-47 px, base about 155 px, fin tips 27.5 px off the axis, thick axis line to
  about 189 px; redraw 44, 21-44, 150, 27.2, 185. Consistent.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The white patch that blanks the grid behind the inset stops at M = 1.985 to keep the M = 2.0 ruling, which leaves 0.015-wide stubs (about 0.8 mm) of the 0.4 and 0.8 rulings against the right edge, reading as stray ticks. In the scan these rulings stop at M ~ 0.82 and do not reach the right edge. | fig53.tex:23 | End the patch at the 2.0 ruling and inset it by half a ruling, as Fig 51 does: `\fill[white] ([shift={(0.2pt,0.2pt)}]axis cs:0.85,0.29) rectangle ([shift={(-0.2pt,-0.2pt)}]axis cs:2.0,0.95);` (the 2.0 ruling keeps its full weight, the stubs go). |
| 2 | note | (a) ogive toward M = 2.0: the redraw (digitized, faithful to the art, which reads 1.248 at M 1.95) ends at 1.25, against Table 8's [C_D/C_Ds]_e 1.27 at M 1.8 and 2.0 and the text's "about 1.27 C_Ds" (0.02, about 0.5 mm at final size). Within "about" and as printed. | fig53-a-ogive.csv (end); ch3-sec7.tex:165-166 | No change; log as **minor** in corrections/v2-figures.md (art 1.25 vs table 1.27). |
| 3 | note | Lettering complete: y title $\dfrac{\CD}{C_{Ds}}$ upright (as printed, as Figs 2, 7, 8), y ticks 0-2.4 every 0.4, x title $M$, x ticks 0-2.0 every 0.2 (leading zeros), "Half-round", "Ogive" in each panel; panel letters (a), (b) upper right inside the axes (house rule). Ogive solid s1, half-round dashed s2 in both panels, as printed; the common flat part drawn once (solid). Both panels one 4.2 x 2.25 in frame. | fig53.tex:14-49 | none |
| 4 | note | Inset drawn with kit macros (`\rocketoutline`, `\rocketfins`, `hatch`, `centerline`); the 1973 shading strokes inside the tube are dropped (flat line art). The thick axis line aft of the fins is kept as printed (comment queries "a support sting?", unexplained in the text; harmless). | fig53.tex:31-42 | none |
| 5 | note | Text and caption: (a) "experimentally determined", (b) "analytical functions ... (214) and (215)": true; Table 8's [..]_a column is reproduced exactly by (b). | ch3-sec7.tex:190-195, 252-254 | none |

## Verdict: pass (no must-fix)
