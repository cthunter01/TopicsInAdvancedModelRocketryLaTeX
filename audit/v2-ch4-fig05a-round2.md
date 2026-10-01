# v2 audit: ch4/fig05a (round 2)

Sources checked:
- Scan `figures/ch4/fig05a.png`, with a 5x zoom of the callouts.
- Redraw `figures/v2/ch4/fig05a.pdf`, rendered at 300 and 600 dpi, with a crop of the callouts.
- Source files `fig05a.tex`, `fig05a.py` (now also holding the shared helpers `extrap`, `Scan`, `smooth`,
  `curve` and `write`), `fig05a.csv` and `fig05a.calib.json`.
- Template `fig06a.tex`, compared by diff.
- Inventory row `ch4-fig05a`.
- Captions and key table: `chapters/ch4-sec2b.tex`:343-380.
- `corrections/v2-figures.md`, including the rule entry at :82 and the Chapter 3 gate decision at :157.
- Round-1 audit and fix reports.

Checks made:
- **Reproducibility after the helper change.** I copied the scripts, calibrations and scans into a scratch tree
  and reran `fig05a.py`. It wrote a `fig05a.csv` byte-identical to the repository's, which is also identical to
  the round-1 file.
  - The new `extrap()` is correct: it is np.interp inside the grid and a linear continuation of the end
    intervals outside it.
  - 5(a) has no samples beyond its end ticks, so the change has no effect here.
- **Overlay** (`digitize.py overlay`, piecewise calibration, residual 0.24 px). All four curves pass:

  | curve | 95% | max |
  |---|---|---|
  | FM $k_{\max}$ | 0.00 px | 0.00 px |
  | CB $k_{\max}$ | 2.00 px (0.34 mm) | 2.24 px |
  | FM $k_{\min}$ | 0.00 px | 1.00 px |
  | CB $k_{\min}$ | 2.00 px (0.34 mm) | 2.24 px |

- **Round-1 note 1 (the $k_{\max}$ leaders): applied.**
  - The leaders now run from `kmax.north` to (0.047, 6.132) on FM $k_{\max}$ and from `kmax.west` to
    (0.037, 1.971) on CB $k_{\max}$.
  - Both endpoints lie on the CSV curves (difference 0.000).
  - At 600 dpi the upper leader rises to the right and the lower one drops almost vertically, so the pair now
    forks as in fig06a and as in the scan.
- **Other leaders.**
  - The $k_{\min}$ leaders are unchanged: (0.028, -0.106) on FM $k_{\min}$ and (0.032, -1.771) on CB $k_{\min}$.
  - Both end on their curves.
  - The left one crosses the CB $k_{\min}$ dashes steeply, as printed.
- **Content.** All present: the y title "Percent error in $v_b$", y ticks -15 to 15, x ticks 0.02-0.14 with the
  odd 0.01 minors, $m_o$ (kg), $k_{\max}$ and $k_{\min}$ with two leaders each, the legend at lower right, and the
  thin zero line. The two off-scale curves are clipped at 15, as printed.
- **Template.**
  - The diff against fig06a.tex changes only the header, the x range and ticks, the zero line's end, the CSV name
    and the label positions.
  - Page 4.73 x 3.05 in, as fig06a. Fonts embedded.
- **Caption.** "Burnout velocity error ... Type B14 engine" holds.
- **The relayed request "Keep 1-3 as they are, use exact curves for 46".** It is the owner's Chapter 3 gate
  answer, not a Chapter 4 instruction.
  - Its items 1-3 are the Ch3 gate items Figs 9, 12 and 28 (corrections:120, :125, :130), and "46" is Ch3
    Fig 46's exact curves (:149).
  - It is recorded as applied in the "Chapter 3 gate (user, 2026-10-01)" paragraph (:157).
  - It therefore does not concern Fig 5. Round 1's note 3 ("confirm the reading") is closed, and digitizing
    stays required by the rule at :82.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The inventory `method` still reads "compute-partial+digitize", and `status` reads "todo". The figure is digitized throughout, and the round-1 note asked for "digitize". This is outside the figure files. | figures/v2/inventory.csv row ch4-fig05a | Orchestrator: set method to "digitize" and status to "audited" when the family closes. |

## Verdict

pass (0 must-fix, 0 should-fix). Round 1's note 1 has been applied and verified; there are no regressions.
