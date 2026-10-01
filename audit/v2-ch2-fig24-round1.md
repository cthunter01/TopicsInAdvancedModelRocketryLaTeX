# v2 audit: ch2/fig24 (round 1)

Sources checked: scan `figures/ch2/fig24.png` (3x upscale of the right half); redraw `figures/v2/ch2/fig24.pdf`
(300 dpi render) and `build/v2/png/ch2-fig24-compare.png`; `figures/v2/ch2/fig24.tex` lines 1-43, `fig24.py`,
`fig24.csv`, `fig24-z0.csv`, `fig24.calib.json`; inventory row `ch2-fig24` (`figures/v2/inventory.csv`:37);
`chapters/ch2-sec3b.tex`:446-462 (eq. (48a), the extended arctangent, the pass through $-\pi/2$ at $\beta = 1$),
:465-470 (caption), :483-485 (abrupt transition, discontinuous at zero damping); `chapters/ch2-sec3d.tex`:419-422
(Figs 30, 31 identical); approved template `figures/v2/ch2/fig25.tex`; `STYLE.md` sections 13, 16;
`corrections/v2-figures.md`.

Checks made:
- **Formula.** `fig24.py` writes $\varphi = -\mathrm{atan2}(2\zeta\beta,\,1-\beta^2)$, which is eq. (48a) on the branch
  running from 0 to $-\pi$. I checked all 1121 rows of `fig24.csv` independently against
  $\arctan[2\zeta\beta/(\beta^2-1)]$, taking $-\pi$ for $\beta > 1$: the largest difference is $5\times10^{-6}$ rad,
  which is rounding. The $\zeta = 0$ step (`fig24-z0.csv`) runs (0,0), (1,0), (1,$-\pi$), (2,$-\pi$).
- **Points evaluated** (rad, for $\zeta$ = .2, .5, $\sqrt2/2$, 1, 2); the render agrees with each:
  - $\beta = 0.5$: $-0.261$, $-0.588$, $-0.756$, $-0.927$, $-1.212$
  - $\beta = 1.5$: $-2.694$, $-2.266$, $-2.103$, $-1.966$, $-1.776$
  - $\beta = 2$: $-2.881$, $-2.554$, $-2.386$, $-2.214$, $-1.930$
- **Label placement.** The right-end labels sit at $-1.930$, $-2.185$, $-2.390$, $-2.595$ and $-2.880$. Each is
  within 0.04 rad (about 1 mm) of its curve's end and in the printed order.
- **Text.** Every curve passes through $(1, -\pi/2)$, on the dashed guide. For every $\beta > 0$, $\varphi$ is
  negative. Lighter damping gives a more abrupt transition, and $\zeta = 0$ is the discontinuous step. The
  $\zeta = .2$ curve stays nearest 0 for $\beta < 1$ and $\zeta = 2$ falls fastest, as in the scan.
- **Lettering.**
  - y title $\varphi$ (rad). y ticks 0, $-\frac\pi4$, $-\frac\pi2$, $-\frac{3\pi}4$, $-\pi$, with unlabelled minor
    ticks at the odd multiples of $-\pi/8$.
  - x title $\beta$; x ticks 0 to 2.00 in steps of 0.25. They use the house-style leading zero, as in the
    approved Fig 25.
  - Curve labels $\zeta = 0$ (beside the drop) and $\zeta = 2, 1, \sqrt2/2, .5, .2$ at the right ends. These are
    all as printed.
- **Overlay** (`digitize.py overlay` with the drafter's calibration, computed curves):

  | $\zeta$ | 95th percentile |
  |---|---|
  | .2 | 3.61 px |
  | .5 | 3.61 px |
  | $\sqrt2/2$ | 3.16 px |
  | 1 | 2.00 px |
  | 2 | 2.00 px |
  | 0 (step) | 0 px |

  The worst gap is about 0.6 mm, just above the 3 px mark, near $\beta$ = 1.1 to 1.3. It is within the drawing
  accuracy of the 1973 art.
- **Size and fonts.** 5.38 in wide; all fonts embedded.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The overlay's 95th percentile for $\zeta$ = .2, .5 and $\sqrt2/2$ is 3.2 to 3.6 px (0.54 to 0.61 mm), just over the 3 px mark. The curves are computed, and the difference is within the 1973 drawing's accuracy. The inventory note already says "agrees within drawing accuracy". | fig24.py | none |
| 2 | note | The printed dashed $-\pi/2$ line runs a little past $\beta = 2.00$ (to about 2.1). The redraw's guide stops at 2.00, as the approved Fig 25's guides do. | fig24.tex:23 | none |
| 3 | note | The $\zeta = 0$ step lies on the bottom axis from $\beta = 1$ to 2 and along $\varphi = 0$ from 0 to 1, as printed. The blue 1 pt line covers the grey axis there, and the outward ticks stay visible. | fig24.tex:25 | none |
| 4 | note | The curve labels keep the printed ".2" and ".5" while the tick labels use leading zeros. This is the same mix the approved Fig 25 has. | fig24.tex:33-37 | Owner's call, for the whole family |

## Verdict

pass (0 must-fix, 0 should-fix)
