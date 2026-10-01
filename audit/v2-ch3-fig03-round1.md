# v2 audit: ch3/fig03 (round 1)

Sources checked: scan `figures/ch3/fig03.png` (y-title region zoomed 4x); redraw `figures/v2/ch3/fig03.pdf`
(current: newer than the .tex and .csv; 372.96 x 212.31 pt = 5.18 x 2.95 in; fonts all embedded Type 1),
rendered at 400 dpi, and `build/v2/png/ch3-fig03-compare.png`; `figures/v2/ch3/fig03.tex`, `fig03.py`,
`fig03.csv` (51 rows), `fig03.calib.json`; inventory row `ch3-fig03` (`figures/v2/inventory.csv`:69); caption
`chapters/ch3-intro-sec2a.tex`:292-296; citing text :237-238 (sea-level 288 K), :271-276 (Fig 2 is based on this
relation; "linear lapse rate" of about 1 degree C per 154 m, "as can be seen from the graph"); the approved frame
`figures/v2/ch3/fig02.tex`/`fig02.py`; `corrections/v2-figures.md` (rule 2; pilot decision on USSA-1962);
`STYLE.md` sections 14 and 16; `tamrfig.sty` (tamr grid).

Checks made:
- **Formula.** T = 288.15 - 0.0065 h (USSA-1962 troposphere), the same law as fig02.py. The text's lapse rate
  1/154 = 0.006494 K/m agrees with 0.0065 to 0.1%; over 2500 m the two differ by 0.02 K. I recomputed all 51
  CSV rows: maximum difference 6e-14. Values: 0 m 288.15 K (just under the 290 line, as printed), 1000 m 281.65,
  2000 m 275.15, 2500 m 271.90. The geopotential/geometric difference at 2500 m is 1.0 m (0.006 K): invisible.
- **Overlay.** I checked the calibration against `digitize.py lines`: the gridline centres (x 115.0, 206.5,
  299.5, 393.0, 487.0, 581.0 px; y 17.5, 90.0, 163.5, 236.5, 311.0 px) are the calib's xgrid/ygrid entries.
  `digitize.py overlay` gives a mean of 0.53 px, a 95th percentile of 1.41 px (0.24 mm) and a maximum of 2.00 px.
  It passes.
- **Lettering.**
  - y title "T (°K)", upright at mid-height left of the tick labels, as printed (rule 2; the family note keeps
    the 1973 °K). $T$ is italic and the unit is roman.
  - y ticks 270, 280, 290; the grid is ruled every 5 (minor lines at 275 and 285), as printed.
  - x ticks 0-2500 in steps of 500, with no thousands separator; x title "Altitude (meters)".
  - Nothing is added.
- **Frame.** The axes are 4.2 x 2.4 in, the grid is on both axes, and the curve is s1 at 1 pt, identical to the
  approved Fig 2 and to Figs 4, 7 and 8. The 290 and 2500 gridlines close the frame as in Fig 2. The width,
  5.18 in, is under 6.5 in.
- **Caption and text.** The line is straight (the "linear lapse rate" the text reads off it) and starts at
  288.15 K, the text's 288 K. Fig 2 (fig02.py) uses the same T(h).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | "(°K)" is kept as printed, per rule 2 and the family brief. The inventory row's open question ("keep or modernize to K") is therefore settled as keep. | fig03.tex:13 | none; record the keep with the Chapter 3 gate items |
| 2 | note | Fig 2's round-1 audit proposed a shared axis style for Figs 2, 3, 4, 7 and 8. The drafter copied Fig 2's axis options inline instead, identically in all four files, so the figures are consistent; a shared style can only go into tamrfig.sty, which the drafter may not edit. | fig03.tex:8-13 | optional: a `tamr altitude chart` style in tamrfig.sty at a kit update |

## Verdict

pass (0 must-fix, 0 should-fix)
