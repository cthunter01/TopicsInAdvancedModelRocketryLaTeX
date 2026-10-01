# v2 audit: ch2/fig27 (round 1)

Sources checked: scan `figures/ch2/fig27.png` (zoomed: lettering, slope lines, origins); inventory row
`ch2-fig27`; caption and citing text `chapters/ch2-sec3c.tex:720-755` (positively-stable condition, slow/fast
mode decay); eqs. (51), (55)-(59) (`ch2-sec3c.tex:21-28, 467-660`); credit `backmatter/figure-credits.tex:62`;
`corrections/ch2.md`, `corrections/v2-figures.md` (nothing on this figure); redraw
`figures/v2/ch2/fig27.{tex,py,csv,calib.json,pdf}` and `fig27-marks.csv` (with the shared functions of
`fig26.py`); `build/v2/png/ch2-fig27{,-compare}.png`; my own 400 dpi render; `digitize.py overlay`; STYLE.md
sections 13 and 16; sibling Figs 26, 28, 29.

Checks made:
- Lettering: upper Slope${}=\Omega_{X0}$, $\alpha_{X0}$ (tick label with tick), 0, $\alpha_X$ (rad), $t$ (sec);
  lower Slope${}=\Omega_{Y0}$, $\alpha_{Y0}$, 0, $\alpha_Y$ (rad), $t$ (sec). All present, in the section 13
  forms. Nothing added.
- Curves: my independent integration of the coupled equations with $C_2 = 0.47$ (the rocket and initial
  conditions of Fig 26) agrees with the CSV to $7\times10^{-5}$ (its t-column rounding). One motion for both
  plots. $\omega_1 = 0.7209$ (slow, same sign as $\omega_Z$), $\omega_2 = -1.3172$ (fast, opposite sign),
  $D_1 = 0.1662 < C_2/2I_L = 0.235 < D_2 = 0.3038$: the slow mode decays more slowly and the fast mode
  faster than the decoupled case, as the text says (lines 728-741). The stability inequality holds
  (left side 1.038 > 0.089).
- Shapes against the inventory: upper peak 1.21 (t 0.78), a flat shoulder near 0.45 (t 2.8-3.6), zero at
  5.2, trough $-0.60$, hump 0.27, ending at 0.06; lower peak 1.83, trough $-1.05$, broad hump 0.28, crossing
  zero at 11.4 and ending at $-0.19$. Caption: "Both ... eventually decay to zero" holds.
- Tangents: slopes 1.55 from $(0, \alpha_{X0})$ and $(0, \alpha_{Y0})$, equal to the curves' initial slopes.
  Against the 1973 lines: upper 95% 3.15 px, lower 0.07 px (they lie on them).
- Overlay (fitted calibration): upper curve 95% 2.24 px (max 3.16), lower 1.41 px (max 2.00): within target.
- Size 320.2 x 346.0 pt (4.45 x 4.81 in); fonts embedded; layout identical to Figs 26, 28, 29.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The printed vertical titles beside the axes become upright titles above the arrows (the `tamr sketch` placement). Wording and units are unchanged. | `fig27.tex:13-16` | none |
| 2 | note | Same `every axis y label` override as the other sketch figures (the `tamr sketch` `rotate=-90` issue). | `tamrfig.sty` `tamr sketch` | style suggestion: drop `rotate=-90` from `tamr sketch`'s `ylabel style` |

## Verdict: pass (no must-fix)
