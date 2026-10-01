# v2 audit: ch2/fig19 (round 1)

Sources checked: scan `figures/ch2/fig19.png`; inventory row `ch2-fig19`; caption `chapters/ch2-sec3a.tex:767-769`;
citing text `chapters/ch2-sec3a.tex:729-762` and `772-777`; eqs. (25), (35), (36a), (36b); credit
`backmatter/figure-credits.tex:38`; errata/supplement/`corrections/ch2.md` (nothing on this figure); redraw
`figures/v2/ch2/fig19.{tex,py,csv,calib.json,pdf}`; `build/v2/png/ch2-fig19{,-compare}.png`; own 400 dpi render;
`digitize.py overlay`; Fig 18's CSV (for the caption's comparison); STYLE.md sections 13 and 16.

Checks made:
- Lettering: $\frac{M_s}{C_1}$ (y tick), 0, $\alpha_X$ (rad), $t$ (sec): all present, as printed. Nothing added.
- Curve: independently evaluated eq. (35) with (25), (36a), (36b), $\zeta = 2.1$: $\tau_1 = 3.9466/\omega_n$,
  $\tau_2 = 0.2534/\omega_n$; the CSV agrees to 6e-6; zero value and slope at 0; monotone; ends at 0.8803
  $M_s/C_1$ (the scan's end measures about 0.87-0.88).
- Caption ("approached asymptotically from below, but more slowly than ... the critically damped response"):
  on the shared axes, Fig 19's curve lies below Fig 18's at every one of the 401 sample times, and both start
  with the same curvature $M_s/I_L$ (same $C_1/I_L$), so the comparison reads directly from Fig 18 to Fig 19.
- Overlay (calibration exact, 3 points): mean 2.17 px, 95% 7.21 px (1.22 mm), max 7.81 px (computed curve;
  the scan's early rise is slower and its middle faster; ends agree).
- Size 329.2 x 196.3 pt (4.57 in wide); fonts Type 1, embedded; identical layout to Fig 18.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Overlay 95% 7.2 px is the computed shape against the sketch (least-squares $\zeta \approx 2.12$ per the .py; 2.1 used); within the approved computed-curve decision. | `fig19.py` | none |
| 2 | note | Same local `every axis y label` override as the family (style suggestion in the Fig 15 report). | `fig19.tex:15-16` | style suggestion only |

## Verdict: pass (no must-fix)
