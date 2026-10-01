# v2 audit: ch4/fig05b (round 1)

Sources checked:
- Scan `figures/ch4/fig05b.png`: 2x upscale, a 4x crop of the upper left (callouts, FM line, CB $k_{\min}$) and
  pixel columns at rows 70-110.
- Redraw `figures/v2/ch4/fig05b.pdf`: 300 and 400 dpi renders, with a crop of the callouts; `pdffonts`.
- Source files `fig05b.tex`, `fig05b.py` (and the `fig05a.py` helpers it imports), `fig05b.csv` and
  `fig05b.calib.json`.
- Template `fig06a.tex`, compared by diff.
- Inventory row `ch4-fig05b`.
- Chapter text: `chapters/ch4-sec2b.tex`:343-372 and :383-389 (caption).
- `corrections/v2-figures.md`.
- `STYLE.md` sections 15 and 16.

Checks made:
- **Method and reproducibility.** The curves are digitized, which the rule requires (the B14 inputs are not in the
  book). Rerunning `fig05b.py` on a scratch copy writes a CSV byte-identical to the repository's.
- **Calibration.**
  - `digitize.py ticks` finds the bottom-axis ticks at columns 69.5, 107.0 ... 522.0, exactly the `xgrid`.
  - The y axis leans 6 px (column 75.5 at the top, 69.5 at the bottom). The script takes x from the bottom ticks
    and masks the axis row by row, which is the right treatment.
- **Overlay** (`digitize.py overlay`, the drafter's calibration):

  | curve | mean | 95% | max |
  |---|---|---|---|
  | FM $k_{\max}$ | 0.05 px | 0.00 px | 4.00 px |
  | CB $k_{\max}$ | 0.47 px | 2.00 px (0.34 mm) | 2.83 px |
  | FM $k_{\min}$ | 0.05 px | 0.00 px | 4.00 px |
  | CB $k_{\min}$ | 0.19 px | 1.41 px | 3.00 px |

  All four pass, and each trace sits on its own printed line.
- **The FM pair.**
  - Pixel columns show one solid about 3 px thick. A single line elsewhere on these scans is about 2 px. There is
    no separation anywhere, and both k labels lead to it near 0.022-0.025.
  - Writing one trace for both FM curves is therefore faithful: 8.49 at 0.02, 6.14 at 0.05, 5.48 at 0.14,
    against the inventory's 8.5, 6.3 and 5.5.
  - CB $k_{\min}$ runs flat at 6.15 (row 96.5) and joins the line at about 0.048, as printed.
  - CB $k_{\max}$ is 1.96 at 0.02, has its minimum, -0.29, at 0.0355, and rises to 4.15 at 0.14. The inventory
    gives about 2, -0.3 and 4.
- **Lettering.**
  - y title "Percent error in $y_b$"; y ticks -15 to 15 in steps of 5.
  - x title $m_o$ (kg); x ticks 0.02-0.14 with minor ticks at 0.01.
  - $k_{\max}$ and $k_{\min}$, each with two leaders.
  - Legend at lower right, as printed.
  - The thin zero line.
  - No panel letter in the art (`\figurepanel{b}`).
- **Leaders.** All four end on their curves, exactly:
  - (0.022, 8.247) and (0.0235, 8.064) on the FM line;
  - (0.035, -0.287) on CB $k_{\max}$;
  - (0.031, 6.167) on CB $k_{\min}$.
  
  The arrangement matches the scan. The $k_{\max}$ leader runs left to the FM line, and its other leader runs down
  across the FM line and CB $k_{\min}$ to the dip of CB $k_{\max}$. The $k_{\min}$ leaders go up to the FM line
  (crossing CB $k_{\min}$) and to CB $k_{\min}$.
- **Template.** The diff against fig06a.tex changes only the x range, the y title, the CSV name and the label
  positions. Size 4.73 x 3.06 in, as fig06a. Fonts embedded.
- **Caption.** The panel shows the burnout-altitude error for the B14, as the caption says.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The inventory asks either to keep the two FM curves distinguishable or to note the overlap. The redraw draws them as one line, as printed, which is the faithful choice. It does the same for CB $k_{\min}$ from 0.048. The overlap is explained only in the .tex and .py comments. | fig05b.tex:3-4; corrections/v2-figures.md (Minor) | Orchestrator: log one line under "Minor": "Ch4 Fig 5(b): the two Fehskens-Malewicki curves are printed as one line and CB $k_{\min}$ runs into it from about 0.048; drawn so." No change to the figure. |
| 2 | note | Over its first 3 mm the steep start of CB $k_{\max}$ runs 0.3-0.4 point below the traced ink: 1.66 against 2.02 at 0.0212, where the leaning axis meets it. The cause is the end of the smoothing spline. The value at the redraw's axis (1.96 at 0.02) matches the printed start at the drawn axis (about 2.0), so the difference is not visible, and the overlay passes. | fig05b.csv rows 1-8 | None needed. |
| 3 | note | Under the relayed request "use exact curves for 46", Fig 5 cannot be computed: the book does not give the B14's $t_m$ or propellant mass (see the fig05a report). | - | As in fig05a's report, note 3. |

## Verdict

pass (0 must-fix, 0 should-fix)
