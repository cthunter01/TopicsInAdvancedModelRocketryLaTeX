# v2 audit: ch2/fig31 (round 1)

Sources checked: scan `figures/ch2/fig31.png` (pixel measurements of the peak and the tails); redraw
`figures/v2/ch2/fig31.pdf` (300 and 400 dpi renders) and `build/v2/png/ch2-fig31-compare.png`;
`figures/v2/ch2/fig31.tex` lines 1-40, `fig31.py`, `fig31.csv`, `fig31-z0.csv`, `fig31.calib.json`; inventory row
`ch2-fig31` (`figures/v2/inventory.csv`:44); `chapters/ch2-sec3d.tex`:406 (eq. (73b)), :410-418 (eqs. (74a), (75)),
:419-422 ("identical to" Figs 24, 25), :433-439 (caption); approved `figures/v2/ch2/fig25.tex` and
`audit/v2-ch2-fig25-round1.md`; `corrections/v2-figures.md` (Ch2 Fig 25 gate item, "Ch2 Fig 31 is the same plot");
`STYLE.md` sections 13, 16.

Checks made:
- **Formula.** `fig31.py` computes eq. (73b) in units of $1/C_1$. I checked all 1121 rows independently: the
  largest difference is $5\times10^{-6}$. The $\zeta_c = 0$ branches, $1/|\beta_c^2-1|$, end exactly on the
  frame at $\beta_c = \sqrt{2/3} = 0.8165$ and $\sqrt{4/3} = 1.1547$. A `nan` row separates the two branches, and
  `unbounded coords=jump` keeps them apart.
- **Points evaluated** (units of $1/C_1$, for $\zeta_c$ = .2, .5, $\sqrt2/2$, 1, 2); the render agrees with each:
  - $\beta_c = 0.5$: 1.288, 1.109, 0.970, 0.800, 0.468 ($\zeta_c = 0$: 1.333)
  - $\beta_c = 2$: 0.322, 0.277, 0.243, 0.200, 0.117 ($\zeta_c = 0$: 0.333)
- **Peaks.** Eqs. (74a) and (75) give 2.552 at $\beta_c = 0.959$ for $\zeta_c = .2$, and 1.155 at 0.707 for
  $\zeta_c = .5$. The drawn peaks (`fig31.csv` maxima 2.5516 and 1.1547) match.
- **Labels.**
  - The three on-curve labels lie on their curves: $\zeta_c = \sqrt2/2$ at (1.06, 0.667), $\zeta_c = 1$ at
    (0.62, 0.722) and $\zeta_c = 2$ at (0.30, 0.664).
  - At 400 dpi the knock-outs cut only their own curve and the $\beta_c = 1$ guide.
  - $\zeta_c = 0$ at (1.21, 2.75) clears the right branch by about 2 mm. It is moved 0.02 right of Fig 25's
    position to allow for the subscript.
- **Lettering.** Everything matches the scan and the inventory:
  - y title $\mathit{AR}_c$ [rad/(dyn-cm)]; y ticks 0, $\frac1{C_1}$, $\frac2{C_1}$, $\frac3{C_1}$, with minor ticks
    at half steps.
  - x title $\beta_c$; x ticks 0 to 2.00.
  - Six $\zeta_c$ labels, and dashed guides at $1/C_1$ and at $\beta_c = 1$.
- **Consistency.** The layout, size (4.2 in by 3.0 in axes; 4.90 in wide overall), label positions and styles are
  the approved Fig 25's. All fonts are embedded.
- **Overlay** (computed curves against the 1973 art):

  | curve | 95th percentile |
  |---|---|
  | $\zeta_c$ = 0 | 6.08 px |
  | $\zeta_c$ = .2 | 10.30 px (1.74 mm) |
  | $\zeta_c$ = .5 | 3.16 px |
  | $\zeta_c$ = $\sqrt2/2$ | 3.16 px |
  | $\zeta_c$ = 1 | 3.00 px |
  | $\zeta_c$ = 2 | 7.07 px |

  Measured on the scan:
  - The 1973 $\zeta_c = .2$ peak is drawn at about $2.42/C_1$ (row 78; eq. (75) gives 2.55).
  - At $\beta_c = 1.95$ the $\zeta_c$ = 0 and .2 tails are drawn at 0.41 and 0.37, against the computed 0.357
    and 0.344.
  - $\zeta_c = 2$ is drawn slightly high between $\beta_c$ 0.3 and 0.7 (0.50 against 0.468 at 0.5).

  These are the 1973 art's errors, not the redraw's. The owner decided at the pilot gate to use the computed
  curves.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The computed curves differ from the 1973 Fig 31 art in its own ways. The drawn peak is 2.42 against 2.55; the tails are drawn high; the overlay's 95th percentile is up to 10.3 px. The inventory row claims the "scan agrees with eq (73b) (e.g. $\zeta_c=.2$ peak about $2.5/C_1$)", which is not accurate. `corrections/v2-figures.md` covers Fig 31 only as "the same plot" as Fig 25, whose art differs differently. This is not a defect in the redraw: the computed curves are the approved decision. | inventory.csv:44; corrections/v2-figures.md (Ch2 Fig 25 item) | Orchestrator: add the Fig 31 numbers to the Fig 25 gate item (STYLE section 16: mismatches go to corrections) |
| 2 | note | As in Fig 25, the $\zeta_c$ = 0 and .2 tails nearly merge past $\beta_c \approx 1.75$ (0.333 against 0.322 at 2.00). This is correct by eq. (73b), and the labels at the peak keep the two curves identifiable. | fig31.tex:22-25 | none |

## Verdict

pass (0 must-fix, 0 should-fix)
