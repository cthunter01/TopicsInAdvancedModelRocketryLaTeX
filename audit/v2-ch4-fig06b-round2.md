# v2 audit: ch4/fig06b (round 2)

Sources checked:
- Scan `figures/ch4/fig06b.png`, with a 5x zoom of the callouts.
- Redraw `figures/v2/ch4/fig06b.pdf`, rendered at 300, 600 and 1200 dpi (the 1200 dpi render crops the curve
  starts).
- Source files `fig06b.tex` (unchanged since round 1), `fig06b.csv` (committed with the pilot; `git status` shows
  it unmodified) and `fig06b.calib.json`.
- `fig06.py` and `trajectory.py`, which I read and ran but did not edit.
- Template `fig06a.tex`.
- Inventory row `ch4-fig06b`.
- The book's equations: `chapters/ch4-sec2a.tex`:55-64 and :118-130, and `ch4-sec2b.tex`:56-66 and :281-300.
- Caption: `ch4-sec2b.tex`:408-414.
- `corrections/v2-figures.md`:41, :74-81 and :157.
- Round-1 audit and fix reports.

Checks made:
- **Data, recomputed independently.**
  - I wrote my own implementation in a scratch session, without importing `trajectory.py`:
    - the exact solution: eqs. (83)-(87), dt = 0.001 s, with the mass by the impulse delivered (eq. (74)), the
      B4 of Fig 4 by (73a)-(73c), $m_p$ = 8.33 g and g = 9.8;
    - Fehskens-Malewicki: eqs. (20), (21);
    - Caporaso-Bengen: eqs. (27), (28);
    - both approximations with $m = m_o - m_p/2$ and $F = I_t/t_b$.
  - All 164 values of fig06b.csv agree within 0.0005 point, which is its rounding.
  - `trajectory.py`'s Table 2 regression also passes: 111.407 / 78.058 / 6.461 / 265.561 / 343.618.
- **Overlay** (computed curves, numbers for the record; `digitize.py overlay`, residual 1.01 px):

  | curve | 95% | max |
  |---|---|---|
  | FM $k_{\max}$ | 5.00 px (0.85 mm) | 6.00 px |
  | CB $k_{\max}$ | 5.10 px (0.86 mm) | 5.39 px |
  | FM $k_{\min}$ | 4.00 px (0.68 mm) | 4.00 px |
  | CB $k_{\min}$ | 5.39 px (0.91 mm) | 6.00 px |

  These are the same as round 1. Using the computed curves is the owner's pilot-gate decision for Ch4 Fig 6
  (corrections:41).
- **Leaders.** All four end on the CSV curves (difference 0.000):
  - (0.038, -1.809) on FM $k_{\max}$;
  - (0.026, -4.364) on CB $k_{\max}$;
  - (0.026, -5.337) on FM $k_{\min}$;
  - (0.032, -8.943) on CB $k_{\min}$.

  The arrangement matches the scan zoom. The $k_{\max}$ label sits between FM $k_{\max}$ and CB $k_{\max}$, and
  the $k_{\min}$ label sits below, forking up to FM $k_{\min}$ and CB $k_{\min}$. Both forks diverge.
- **Content.** All present: the y title "Percent error in $y_b$", y ticks -15 to 15, x ticks 0.02-0.10 with the
  minors, $m_o$ (kg), both k labels, the legend at upper right (as printed, clear of the curves) and the zero
  line.
- **Template.** The diff against fig06a.tex is as in round 1. Page 4.74 x 3.05 in; fonts embedded.
- **Sampling.** The curves are polylines at 2 g spacing, as in the approved fig06a (the shared fig06.py). The
  facets on the curved FM $k_{\min}$ start show only at 1200 dpi, so they are not an issue at final size.
- **Caption.** "Burnout altitude error ... Type B4 engine" holds.
- **The relayed request "Keep 1-3 as they are, use exact curves for 46".** It is the owner's Chapter 3 gate
  answer: Ch3 Figs 9, 12 and 28 kept as redrawn, and Ch3 Fig 46's exact curves (corrections:120-157). It is not
  a reading of Ch4 Figs 4-6, so round 1's note 2 ("confirm the reading") is closed. The computed curves stand
  under the pilot-gate decision.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix (orchestrator; no change to the figure) | Still open from round 1. The Ch4 Fig 6 entry quotes only 6(a)'s overlay ("4-6 px (0.7-1.0 mm) ... k_min pair about 0.6 point low"). STYLE s16 asks for each failed overlay to be logged. 6(b) misses on all four curves: 95% at 4.0-5.4 px (0.68-0.91 mm), every curve 0.5-0.7 point below the print. The fixer declined properly, since corrections/ is not among its files, and passed the numbers on. | corrections/v2-figures.md:74-81 | Orchestrator: extend the entry with "6(b): 95% at 4.0-5.4 px (0.7-0.9 mm), all four curves 0.5-0.7 point below the print (FM $k_{\max}$ 1.46 against about 2 at 0.022; CB $k_{\max}$ -13.80 against about -13.3 at 0.10)". |

## Verdict

pass (0 must-fix; 1 should-fix, which is record-keeping for the orchestrator outside the figure files). The
figure and its data are unchanged since round 1 and have been re-verified.
