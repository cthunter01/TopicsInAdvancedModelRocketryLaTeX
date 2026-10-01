# v2 audit: ch3/fig07 (round 1)

Sources checked: scan `figures/ch3/fig07.png` (in-plot note zoomed 3x); redraw `figures/v2/ch3/fig07.pdf`
(current: newer than the .tex and .csv; 366.70 x 212.27 pt = 5.09 x 2.95 in; fonts all embedded Type 1),
rendered at 400 dpi, and `build/v2/png/ch3-fig07-compare.png`; `figures/v2/ch3/fig07.tex`, `fig07.py`,
`fig07.csv` (51 rows), `fig07.calib.json`; inventory row `ch3-fig07` (`figures/v2/inventory.csv`:73); caption
`chapters/ch3-intro-sec2a.tex`:528-532; citing text :522-525 ("mu is seen to decrease steadily with increasing
altitude"); `backmatter/figure-credits.tex`:154; the approved `figures/v2/ch3/fig02.tex`;
`corrections/v2-figures.md` (pilot gate: USSA-1962 for Ch3 Figs 2, 7, 8); `STYLE.md` sections 14 (the subscript
of $\mu_o$ is the letter o) and 16.

Checks made:
- **Formula.** USSA-1962 Sutherland law, mu = 1.458e-6 T^1.5/(T + 110.4), with T = 288.15 - 0.0065 h, normalized
  at 288.15 K. I recomputed the 51 CSV rows (maximum difference 5e-7). Values: 300 m 0.99473, 1000 m 0.98238,
  2500 m 0.95557. The curve decreases steadily, as the text says.
- **Overlay.** The calibration's xgrid/ygrid entries are the gridline centres from `digitize.py lines` (x 97.0,
  188.5, 280.5, 372.5, 463.5, 557.0 px; y 15.5, 86.5, 158.0, 227.5, 301.0 px). `digitize.py overlay` gives a mean
  of 0.36 px, a 95th percentile of 1.00 px (0.17 mm) and a maximum of 2.00 px. It passes.
- **Lettered mu_o** (the brief asks for this check). The figure letters
  $\mu_o = 1.78943 \times 10^{-5}$ kg/(m-sec).
  - Sutherland's formula at 288.15 K gives 1.789380e-5. The USSA-1962 table value is 1.7894e-5.
  - The lettered 1.78943e-5 equals the formula at 288.16 K (1.789429e-5). It also equals the 1962 English-unit
    table value 3.7373e-7 lb-sec/ft^2 x 47.880259 (1.789429e-5), so 1973 most likely converted the English table.
  - The difference is 3 parts in 10^6 and does not affect the plotted ratio. The lettering is kept as printed,
    correctly; the drafter documents this in the fig07.py docstring.
- **Lettering.**
  - y title $\dfrac{\mu}{\mu_o}$, upright, with the subscript the letter o.
  - y ticks 0.950, 0.975, 1.000 (house leading zero for the printed .950, .975); ruled every 0.0125, with minor
    lines at 0.9625 and 0.9875, as printed.
  - x ticks 0-2500 in steps of 500; x title "Altitude (meters)".
  - The note reads "$\mu_o = 1.78943 \times 10^{-5}$ kg/(m-sec)", hyphen as printed. Its knock-out breaks the
    0.9625 line and the 500 and 1000 m verticals; 1973 broke the 500, 1000 and 1500 m verticals just under that
    line. It is placed as Fig 2's note: anchor west at 250 m, centred on the line.
  - The note clears the curve: its right end is near 1370 m at 0.9625, where the curve is at about 0.976.
- **Frame.** The axes are 4.2 x 2.4 in, the grid is on both axes, and the curve is s1, identical to Fig 2. The
  width, 5.09 in, is under 6.5 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The lettered mu_o = 1.78943e-5 differs from the USSA-1962 Sutherland value at 288.15 K, 1.78938e-5 (table: 1.7894e-5), in the sixth significant figure. It is the English-unit table value converted. It is kept as printed, which is correct. Only the fig07.py docstring records it. | fig07.tex:17; fig07.py docstring | Orchestrator: log in corrections/v2-figures.md "Minor" (no note in the book, per the no-notes-on-minor-arithmetic rule). |
| 2 | note | The inventory row still lists method "digitize" (with "Recommended: regenerate"). Under the pilot gate the curve is computed, and that is what the drafter did. | figures/v2/inventory.csv:73 | Orchestrator: set method to compute at the status update. |

## Verdict

pass (0 must-fix, 0 should-fix)
