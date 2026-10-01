# v2 audit: ch4/fig05c (round 2)

Sources checked:
- Scan `figures/ch4/fig05c.png`: a 5x zoom of the callouts, a character map of rows 44-104, columns 64-96, and
  the ink rows at each CSV point from 0.020 to 0.034.
- Redraw `figures/v2/ch4/fig05c.pdf`, rendered at 300 and 600 dpi.
- Source files `fig05c.tex`, `fig05c.py`, `fig05c.csv` and `fig05c.calib.json`.
- The shared helpers in `fig05a.py` (`extrap`, `Scan.to_data`, `smooth`, `curve(w0=...)`).
- Template `fig06a.tex`, compared by diff.
- Inventory row `ch4-fig05c`.
- Caption: `chapters/ch4-sec2b.tex`:392-398.
- `corrections/v2-figures.md`.
- Round-1 audit and fix reports.

Checks made:
- **Reproducibility.** Rerunning `fig05c.py` in a scratch tree writes a CSV byte-identical to the repository's.
- **Round-1 should-fix 1 (the $k_{\max}$ curves start low): resolved.**
  - `Scan.to_data` now continues the end tick intervals linearly instead of clamping. Ink left of col 75 (the .02
    tick), where the drawn axis leans to cols 71-72, keeps its own m_o of about 0.0195.
  - The first two samples are weighted 30 in the smoothing spline.
  - Starts at 0.02, CSV against the scan's ink centre in col 75:

    | curve | CSV | ink at col 75 | round 1 |
    |---|---|---|---|
    | CB $k_{\max}$ | 6.01 | 6.11 (rows 96-97) | 5.73 |
    | FM $k_{\max}$ | 10.73 | 10.78 (rows 53-56) | 10.67 |

    The remaining 0.05-0.10 point is 0.1-0.2 mm at final size.
  - Further along CB $k_{\max}$, CSV against ink at each 0.001:
    - 0.021: 5.53 against 5.33;
    - 0.022: 5.05 against 4.94;
    - 0.023: 4.61 against 4.39;
    - 0.024: 4.18 against 4.06;
    - 0.026: 3.42 against 3.39;
    - 0.028: 2.76 against 2.67.

    So the spline runs at most 0.2 point (about 2 scan px) above the dashes just after the start. The CSV has no
    kink: the slope falls steadily from 478 to 292 %/kg over 0.020-0.030.
  - The leaning-axis treatment (the value at the .02 tick, not at the drawn axis) matches 5(b)'s, as the fixer
    argued. The docstring now gives the true values (6.1 at the tick, 6.0 in the CSV, 6.2 at the leaning axis;
    10.8, 10.7 and 10.9).
- **Overlay** (`digitize.py overlay`). All four curves pass:

  | curve | 95% | max |
  |---|---|---|
  | FM $k_{\max}$ | 0.00 px | 5.00 px |
  | CB $k_{\max}$ | 2.00 px (0.34 mm) | 4.00 px |
  | FM $k_{\min}$ | 0.00 px | 5.00 px |
  | CB $k_{\min}$ | 2.00 px (0.34 mm) | 5.00 px |

  The zoomed overlay shows each trace on its own printed line, the starts included.
- **Other values.** Unchanged within 0.05 beyond 0.034:
  - FM $k_{\min}$: 0.84 at 0.02 (ink 0.83).
  - CB $k_{\min}$: -1.21 at 0.02 (ink -1.20).
  - CB $k_{\max}$: crosses 0 near 0.0405 and levels out at -2.0.
  - FM $k_{\max}$: 0.84 at 0.14.
- **Round-1 note 2 (the $k_{\min}$ leaders): applied.**
  - `(kmin.north east)` now runs to (0.033, -1.130) on CB $k_{\min}$, and `(kmin.north west)` runs to
    (0.0235, 0.574) on FM $k_{\min}$.
  - Both lean up and to the right, as in the scan.
  - Both endpoints lie on the new CSV curves, as does the moved CB $k_{\max}$ endpoint (0.0345, 1.085)
    (difference 0.000).
  - The $k_{\max}$ fork (north west up to FM $k_{\max}$, south west left to CB $k_{\max}$) matches the scan.
- **Content.** All present: the y title "Percent error in $y_{\max}$" (upright max), the ticks, $m_o$ (kg), both
  k labels with two leaders each, the legend at lower right and the zero line.
- **Template.** The diff against fig06a.tex changes only the header, the x range and ticks, the y title, the zero
  line's end, the CSV name and the label positions. Page 4.74 x 3.05 in; fonts embedded.
- **Caption.** "Maximum altitude error ... Type B14 engine" holds.
- **The relayed request "Keep 1-3 as they are, use exact curves for 46".** It is the owner's Chapter 3 gate
  answer (Ch3 Figs 9, 12 and 28; Ch3 Fig 46's exact curves), recorded at corrections/v2-figures.md:157. It does
  not bear on Fig 5. Round 1's note 3 is closed.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The inventory `method` still reads "compute-partial+digitize" (see fig05a's report). | figures/v2/inventory.csv row ch4-fig05c | Orchestrator: change it to "digitize". |

## Verdict

pass (0 must-fix, 0 should-fix). Round 1's should-fix is resolved: the $k_{\max}$ curves now start on the ink
at the .02 tick, and the overlay passes. Optional note 2 has been applied, with no regressions.
