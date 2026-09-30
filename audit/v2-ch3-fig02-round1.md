# v2 audit: ch3/fig02 (round 1)

Sources checked: scan `figures/ch3/fig02.png` (2x upscale); redraw `figures/v2/ch3/fig02.pdf` (350 dpi render) and
`build/v2/png/ch3-fig02-compare.png`; `figures/v2/ch3/fig02.tex` lines 1-18, `fig02.py`, `fig02.csv` (51 rows),
`fig02.calib.json`; inventory row `ch3-fig02` (`figures/v2/inventory.csv`:68); `chapters/ch3-intro-sec2a.tex`:
252-269 (citing text, caption), :270-276 (lapse rate of about 1 degree C per 154 m, the basis in Fig 3), :318
(ednote using 1.225); `corrections/v2-figures.md` ("Formulas from outside the book", gate); `STYLE.md` section 14
(the subscript of $\rho_o$ is the letter o) and section 16.

Checks made:
- **Formula.** The troposphere relation of USSA-1962 is used:
  - T = 288.15 - 0.0065 h.
  - $\rho/\rho_o = (T/T_o)^{4.25588}$, where the exponent is $g_oM/(R^*L) - 1$; $g_oM/(R^*L)$ = 9.80665 x 0.0289644 / (8.31432 x 0.0065) = 5.2559.
  - The lapse rate matches the text's "1 degree C per 154 m" (1/0.0065 = 153.8 m).
- **Values** (the CSV reproduces each):
  - 250 m: 0.97622
  - 300 m: 0.97151, a decrease of 2.85%; the text says "just under 3%"
  - 1000 m: 0.90746, 9.25%; the text says "just over 9%"
  - 1750 m: 0.84248
  - 2500 m: 0.78111
  - 3000 m (beyond the axis): 0.7421, 25.8% against the text's 25.6%. This is not a figure matter.
- **Overlay.** `digitize.py overlay` gives a mean of 0.41 px and a 95th percentile of 1.21 px (0.20 mm), so it
  passes. An independent column-by-column centroid of the scan's curve, with the gridline rows masked, sits on
  average 1.0 px (0.17 mm) above the formula and at most about 3.6 px, near 2300 m.
- **Lettering.**
  - y title $\dfrac{\rho}{\rho_o}$ (upright, subscript letter o).
  - y ticks 0.70-1.00, labelled every 0.10 and ruled every 0.05.
  - x ticks 0-2500, step 500, without a thousands separator.
  - x title "Altitude (meters)".
  - In-plot note $\rho_o = 1.225014$ kg/m$^3$ on the 0.80 line. Its knock-out breaks the 0.80 line and the 500
    and 1000 m verticals, as in 1973.
  - The printed closed frame is kept by the 1.00 and 2500 gridlines.
- **Caption and text.** All citing statements that fall inside the plotted range hold, and the note gives the
  ednote's sea-level density of 1.225.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Known gate item: the curve comes from the external USSA-1962 formula, which the book does not print. It passes the overlay criterion (95% within 0.20 mm). The script's geopotential/geometric simplification (under 1 m below 2500 m, a $\rho/\rho_o$ change of about 1e-4) is invisible. | fig02.py | none (gate) |
| 2 | note | The inventory asks for one shared axis style for Figs 2, 3, 4, 7 and 8. This figure defines its axis inline (fig02.tex:7-13). | fig02.tex:7-13 | Factor the axis into a shared style when Figs 3, 4, 7 and 8 are drawn. |

## Verdict

pass (0 must-fix, 0 should-fix)
