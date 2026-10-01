# v2 audit: ch4/fig05c (round 1)

Sources checked:
- Scan `figures/ch4/fig05c.png`: 2x upscale, a 4x crop of the callouts, and a character map of rows 40-111 at
  columns 64-83 (where the curves meet the axis).
- Redraw `figures/v2/ch4/fig05c.pdf`: 300 and 400 dpi renders, with a crop of the callouts; `pdffonts`.
- Source files `fig05c.tex`, `fig05c.py` (and the `fig05a.py` helpers it imports), `fig05c.csv` and
  `fig05c.calib.json`.
- Template `fig06a.tex`, compared by diff.
- Inventory row `ch4-fig05c`.
- Chapter text: `chapters/ch4-sec2b.tex`:343-372 and :392-398 (caption).
- `corrections/v2-figures.md`.
- `STYLE.md` sections 15 and 16.

Checks made:
- **Method and reproducibility.** The curves are digitized, as the rule requires. Rerunning `fig05c.py` on a
  scratch copy writes a byte-identical CSV.
- **Calibration.** `digitize.py ticks` finds the bottom ticks at 75.0, 114.0 ... 511.5, exactly the piecewise
  `xgrid` (the spacing closes up from 39 to 34 px per 0.01). The y ticks are at rows 61.5, 106.5, 151.5, 197.5,
  242 and 288, matching the `ygrid`.
- **Overlay** (`digitize.py overlay`):

  | curve | mean | 95% | max |
  |---|---|---|---|
  | FM $k_{\max}$ | 0.04 px | 0.00 px | 5.00 px |
  | CB $k_{\max}$ | 0.54 px | 2.00 px (0.34 mm) | 4.00 px |
  | FM $k_{\min}$ | 0.05 px | 0.00 px | 5.00 px |
  | CB $k_{\min}$ | 0.49 px | 2.00 px | 5.00 px |

  All four pass, and each trace sits on its own printed line.
- **Values.**

  | curve | redraw | inventory |
  |---|---|---|
  | FM $k_{\max}$ | 10.67 at 0.02, 0.84 at 0.14 | ~11, ~0.8 |
  | CB $k_{\max}$ | crosses 0 at 0.0405; minimum -2.18 near 0.083; -1.97 at 0.14 | ~0 at 0.045, ~-2 |
  | FM $k_{\min}$ | 0.79 at 0.02, -0.39 at 0.14 | ~1, slightly below 0 |
  | CB $k_{\min}$ | -1.23 at 0.02, -0.45 at 0.14 | ~-1.2, ~-0.5 |
- **Lettering.**
  - y title "Percent error in $y_{\max}$" with an upright "max"; y ticks -15 to 15 in steps of 5.
  - x title $m_o$ (kg); x ticks 0.02-0.14 with minor ticks at 0.01.
  - $k_{\max}$ and $k_{\min}$ with a lowercase k: the lettering is capital-like, and STYLE s15 sets it lowercase.
    Each has two leaders.
  - Legend at lower right, as printed.
  - The thin zero line.
  - No panel letter in the art (`\figurepanel{c}`).
- **Leaders.** All four end exactly on their curves: (0.0405, 5.309) FM $k_{\max}$, (0.0345, 1.104) CB $k_{\max}$,
  (0.0235, 0.552) FM $k_{\min}$ and (0.030, -1.170) CB $k_{\min}$.
- **Template.** The diff against fig06a.tex changes only the x range, the y title, the CSV name and the label
  positions. Size 4.73 x 3.06 in. Fonts embedded.
- **Caption.** The panel shows the maximum-altitude error for the B14, as the caption says.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The two steep $k_{\max}$ curves start low at the y axis. **What the print shows:** the drawn axis leans to column 71-72 at these rows, and the printed curves meet it at about 6.2 (CB $k_{\max}$, dash centre row 95.5) and 10.94 (FM $k_{\max}$, row 53). **What the redraw has:** 5.73 and 10.67 at 0.02 (fig05c.csv row 1). That is 0.47 and 0.27 point low, about 1.0 and 0.6 mm at final size (2.1 mm per point). **Cause:** `Scan.to_data` (fig05a.py:59-60) uses `np.interp`, which clamps every column left of the 0.02 tick (col 75) to x = 0.02. The samples at cols 73-75 (10.94, 10.83, 10.78 for FM; 6.11, 6.11 for CB) therefore collapse onto one x, and the smoothing spline sags at the end. **Docstring:** fig05c.py:13 says the CB $k_{\max}$ curve is at "6.1% at the axis", but the CSV has 5.73. The overlay misses this because the curves are steep: the perpendicular distance stays within 4 px. | fig05c.csv rows 1-4; fig05a.py:59-60; fig05c.py:13 | Let the x mapping extrapolate linearly beyond the end ticks (or map the drawn axis at each row to 0.02), so that the traced start reaches 0.02 with its ink value. Then rerun fig05c.py. Fig 5(a) and 5(b) have no samples left of their 0.02 tick, so their CSVs would not change: rerun them to confirm. Check that CB $k_{\max}$ starts at about 6.1-6.2 and FM $k_{\max}$ at about 10.9. |
| 2 | note | The $k_{\min}$ leaders converge upward. The north-west one runs up and to the right to FM $k_{\min}$. The north-east one runs up and to the left to CB $k_{\min}$ at 0.030. In the scan both lean up and to the right, and fig06a's fork diverges. The callout is still legible: each leader ends on a curve, and the left one crosses CB $k_{\min}$ at a steep angle, as printed. | fig05c.tex:28-30 | Optional: `(kmin.north east) -- (axis cs:0.033,-1.13)`, a point on CB $k_{\min}$, so that both leaders lean up and to the right as in the scan. |
| 3 | note | Under the relayed request "use exact curves for 46", Fig 5 cannot be computed: the book does not give the B14's $t_m$ or propellant mass (see the fig05a report). | - | As in fig05a's report, note 3. |

## Verdict

pass after one should-fix (0 must-fix, 1 should-fix)
