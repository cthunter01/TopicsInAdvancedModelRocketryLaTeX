# v2 audit: ch3/fig08 (round 1)

Sources checked: scan `figures/ch3/fig08.png` (in-plot note zoomed 3x); redraw `figures/v2/ch3/fig08.pdf`
(current: newer than the .tex and .csv; 356.66 x 212.27 pt = 4.95 x 2.95 in; fonts all embedded Type 1),
rendered at 400 dpi, and `build/v2/png/ch3-fig08-compare.png`; `figures/v2/ch3/fig08.tex`, `fig08.py`,
`fig08.csv` (51 rows), `fig08.calib.json`; inventory row `ch3-fig08` (`figures/v2/inventory.csv`:74); caption
`chapters/ch3-intro-sec2a.tex`:550-554; citing text :534-545 (nu = mu/rho; "nu increases relatively slowly";
"about 2.4% greater" at 300 m; the working value 1.495e-5); `backmatter/figure-credits.tex`:156; Figs 2 and 7
(fig02.py, fig07.py); `corrections/v2-figures.md`; `STYLE.md` sections 14 (the subscript of $\nu_o$ is the letter
o; nu decided by context) and 16.

Checks made:
- **Formula.** nu/nu_o = (mu/mu_o)/(rho/rho_o): Sutherland as in Fig 7, and rho/rho_o = (T/288.15)^4.25588 as in
  Fig 2 (I checked g_oM/(R*L) = 9.80665 x 28.9644/(8314.32 x 0.0065) = 5.25588). I recomputed the 51 CSV rows
  (maximum difference 7e-7). Values:
  - 300 m: 1.02390. The text says "only about 2.4% greater", which holds.
  - 1000 m: 1.08255.
  - 2500 m: 1.22336.

  The curve is slightly concave up, as printed.
- **Overlay.** The calibration's xgrid/ygrid entries are the gridline centres from `digitize.py lines` (x 87.0,
  184.5, 280.5, 374.0, 467.5, 560.5 px; y 16.5-288.0 px every 0.05). `digitize.py overlay` gives a mean of
  0.02 px, a 95th percentile of 0.00 px and a maximum of 1.00 px. It passes.
- **Lettered nu_o** (the brief asks for this check).
  - The figure letters $\nu_o = 1.461 \times 10^{-5}$ m$^2$/sec.
  - mu_o/rho_o from the formulas, 1.78938e-5/1.2250, is 1.46072e-5. From the lettered values,
    1.78943e-5/1.225014, it is 1.46074e-5. The USSA-1962 table gives 1.4607e-5.
  - All of these round to 1.461e-5, so the lettering is consistent. The text's 1.495e-5 is a stated average,
    not a mismatch.
- **Lettering.**
  - y title $\dfrac{\nu}{\nu_o}$, upright, with the subscript the letter o.
  - y ticks 1.0, 1.1, 1.2, 1.3; ruled every 0.05 (minor lines at 1.05, 1.15, 1.25), as printed.
  - x ticks 0-2500 in steps of 500; x title "Altitude (meters)".
  - The note is in the band between 1.20 and 1.25, where 1973 put it, anchor west at 250 m as Figs 2 and 7. Its
    knock-out breaks the 500 and 1000 m verticals as printed, and it is well clear of the curve.
  - The scanner speck near 1100 m, 1.28 is rightly not drawn. Nothing is added.
- **Frame.** The axes are 4.2 x 2.4 in, the grid is on both axes, and the curve is s1, identical to Fig 2. The
  width, 4.95 in, is under 6.5 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The inventory row still lists method "digitize" (with "regenerate" recommended). Under the pilot gate the curve is computed, and that is what the drafter did. | figures/v2/inventory.csv:74 | Orchestrator: set method to compute at the status update. |
| 2 | note | The fig08.py print line uses rho_o = 1.225 (giving 1.46072e-5); the lettering uses 1.225014. The difference does not affect the figure (the plotted ratio is independent of both). | fig08.py:25 | none |

## Verdict

pass (0 must-fix, 0 should-fix)
