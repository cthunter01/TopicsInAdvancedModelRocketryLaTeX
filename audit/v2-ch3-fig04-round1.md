# v2 audit: ch3/fig04 (round 1)

Sources checked: scan `figures/ch3/fig04.png` (y-title region zoomed 4x); redraw `figures/v2/ch3/fig04.pdf`
(current: newer than the .tex and .csv; 354.90 x 212.27 pt = 4.93 x 2.95 in; fonts all embedded Type 1),
rendered at 400 dpi, and `build/v2/png/ch3-fig04-compare.png`; `figures/v2/ch3/fig04.tex`, `fig04.py`,
`fig04.csv` (51 rows), `fig04.calib.json`; inventory row `ch3-fig04` (`figures/v2/inventory.csv`:70); caption
`chapters/ch3-intro-sec2a.tex`:407-411; citing text :389-392 (sea-level sound speed "about 340
meters/second", see Fig 4), the ednote at :315-326 (340 m/s "plotted in Figure 4"), `chapters/ch3-sec7.tex`:25-44
(eq. (213), c = c_std sqrt(T/T_std); "varies only slightly---a few percent at most"; sea-level value of about
340 m/s); `backmatter/figure-credits.tex`:150 ("After U.S. Standard Atmosphere, 1962"); the approved
`figures/v2/ch3/fig02.tex`; `corrections/v2-figures.md`; `STYLE.md` sections 14 (lowercase c for the speed of
sound) and 16.

Checks made:
- **Formula.** c = 340 sqrt(T/288.15) with T = 288.15 - 0.0065 h. This is eq. (213), applied with the text's
  sea-level c_std = 340 m/s and T_std = 288.15 K, and Fig 3's temperature. I recomputed the 51 CSV rows (maximum
  difference 5e-5 m/s). Values: 0 m 340.00, 300 m 338.85, 1000 m 336.14, 2000 m 332.24, 2500 m 330.27 m/s.
  The drop over the plotted range is 2.9%, the text's "a few percent at most".
- **Which formula reproduces the print.** I ran `digitize.py overlay` with the same calibration on three curves:
  - the draft, 340 sqrt(T/288.15): mean 0.04 px, 95th percentile 0.00 px, maximum 1.00 px. It passes.
  - USSA-1962's own c = sqrt(1.4 x 287.053 x T), which starts at 340.29 m/s: 95th percentile 7.07 px (1.20 mm).
    The overlay reports MISMATCH.
  - 340 sqrt(T/288), with the text's rounded 288 K: 95th percentile 2.24 px.

  The drafter's choice is the one the print and the text support. The calibration's xgrid/ygrid entries match
  the gridline centres from `digitize.py lines`; the hand-ruled intervals vary from 91 to 96 px, so piecewise
  calibration is appropriate.
- **Lettering.**
  - y title "c (m/sec)", rotated, as printed. The c is lowercase italic (STYLE 14).
  - y ticks 330, 335, 340; the grid is ruled every 2.5 (minor lines at 332.5 and 337.5), as printed.
  - x ticks 0-2500 in steps of 500; x title "Altitude (meters)".
  - Nothing is added.
- **Frame.** The axes are 4.2 x 2.4 in, the grid is on both axes, and the curve is s1, as Figs 2, 3, 7 and 8.
  The width, 4.93 in, is under 6.5 in. The curve starts exactly at the 340 corner, as printed.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The figure credit says "After U.S. Standard Atmosphere, 1962", and the pilot gate's outside-formula decision names Figs 2, 7 and 8, not this one. The curve is instead computed from the book's eq. (213) with the text's 340 m/s. That reproduces the print exactly; the USSA-1962 value sqrt(gamma R T) = 340.29 m/s at sea level would sit 0.29 m/s (about 1.8 mm at final size) above it and fails the overlay. This is the right choice, but it is not recorded in corrections/v2-figures.md. | fig04.py docstring; corrections/v2-figures.md | Orchestrator: log under "Minor" (or the Ch3 gate list): "Ch3 Fig 4: computed from eq. (213) with c_std = 340 m/s (the text's value; reproduces the print), not USSA-1962's 340.29". |
| 2 | note | Within the family, Fig 4's y title is rotated and Figs 2, 3, 7 and 8 have upright titles. Both forms are as printed in 1973. | fig04.tex:13 | none (as printed); optionally make it upright, like the other four, for family uniformity, at the owner's choice |
| 3 | note | eq. (213) is stated for a non-standard temperature at a fixed altitude. Using it with sea-level c_std and T_std to trace the standard-atmosphere curve is a reinterpretation, but it is the one that reproduces the print, and the inventory documents it. | fig04.py | none |

## Verdict

pass (0 must-fix, 0 should-fix)
