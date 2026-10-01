# v2 audit: ch4/fig05b (round 2)

Sources checked:
- Scan `figures/ch4/fig05b.png`: a 5x zoom of the callouts and a character map of rows 70-111, columns 66-130.
- Redraw `figures/v2/ch4/fig05b.pdf`, rendered at 300 and 600 dpi.
- Source files `fig05b.tex` (unchanged since round 1), `fig05b.py`, `fig05b.csv` and `fig05b.calib.json`.
- The shared helpers in `fig05a.py`.
- Template `fig06a.tex`.
- Inventory row `ch4-fig05b`.
- Caption: `chapters/ch4-sec2b.tex`:383-389.
- `corrections/v2-figures.md`.
- Round-1 audit and fix reports.

Checks made:
- **Reproducibility with the new helpers.** I reran `fig05b.py` in a scratch tree. The CSV is byte-identical to
  the repository's, and so to round 1's. The new linear extrapolation in `Scan.to_data` has no effect here.
  - The y axis leans right of the .02 tick (col 69.5) at the top, so every sample lies right of it.
  - The start is still run back to 0.02 along the end slope, as in round 1.
- **Overlay** (`digitize.py overlay`). All four curves pass:

  | curve | 95% | max |
  |---|---|---|
  | FM $k_{\max}$ | 0.00 px | 4.00 px |
  | CB $k_{\max}$ | 2.00 px (0.34 mm) | 2.83 px |
  | FM $k_{\min}$ | 0.00 px | 4.00 px |
  | CB $k_{\min}$ | 1.41 px | 3.00 px |

- **CB $k_{\min}$ at the axis.** The character map shows a short dash stub at cols 76-79, row 96.5, right at the
  leaning axis. So the curve does start at the axis, as the redraw draws it (6.15 at 0.02).
- **Leaders.** All four end on their CSV curves (difference 0.000):
  - (0.022, 8.247) and (0.0235, 8.064) on the FM line;
  - (0.035, -0.287) on CB $k_{\max}$;
  - (0.031, 6.167) on CB $k_{\min}$.

  The arrangement matches the scan zoom. Both labels lead to the FM line near the axis. The $k_{\max}$ leader
  runs down across the FM line and CB $k_{\min}$ to the dip of CB $k_{\max}$, and the $k_{\min}$ leaders rise to
  the FM line and to CB $k_{\min}$.
- **Content.** All present: the y title "Percent error in $y_b$", the ticks, $m_o$ (kg), both k labels, the
  legend at lower right and the zero line.
- **Template.** Page 4.74 x 3.05 in; fonts embedded. The diff against fig06a.tex is as in round 1.
- **Caption.** "Burnout altitude error ... Type B14 engine" holds.
- **The relayed request "Keep 1-3 as they are, use exact curves for 46".** It is the owner's Chapter 3 gate
  answer (Ch3 Figs 9, 12 and 28; Ch3 Fig 46's exact curves), recorded at corrections/v2-figures.md:157. It does
  not bear on Fig 5. Round 1's note 3 is closed.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Still open from round 1, outside the figure: the Minor line on the merged curves has not been written. Its content: as printed, the two Fehskens-Malewicki curves are one line, and CB $k_{\min}$ runs into it from about 0.048. The fixer correctly declined, since corrections/ is outside its files. | corrections/v2-figures.md, "Minor (logged only)" | Orchestrator: add "Ch4 Fig 5(b): the two Fehskens-Malewicki curves are printed as one line and the Caporaso-Bengen $k_{\min}$ curve runs into it from about 0.048 kg; drawn so." |
| 2 | note | The inventory `method` still reads "compute-partial+digitize" (see fig05a's report). | figures/v2/inventory.csv row ch4-fig05b | Orchestrator: change it to "digitize". |

## Verdict

pass (0 must-fix, 0 should-fix). The figure is unchanged since round 1, and the helper change in fig05a.py
leaves its data byte-identical.
