# v2 audit: ch3/fig55 (round 1)

Sources checked: scan `figures/ch3/fig55.png` (zoomed x4 at the top of the chart and at the y title); redraw
`figures/v2/ch3/fig55.tex`, `fig55.py`, `fig55-10.csv`, `fig55-25.csv`, `fig55-50.csv`, `fig55-100.csv`,
`fig55.calib.json`; `figures/v2/ch3/fig55.pdf` (5.09 x 3.31 in, fonts embedded) rendered at 400 dpi;
`build/v2/png/ch3-fig55-compare.png`; inventory row `ch3-fig55`; eqs. (223)-(230) and the citing text and
caption `chapters/ch3-sec8.tex:150-222` (g = 9.8 m/s^2 at line 113); standing rule 3 and the pilot gate
decisions in `corrections/v2-figures.md`; STYLE.md section 16; approved log chart `figures/v2/ch3/fig22.tex`.

Checks run:
- Eq. (230): x = -(m/2k) ln[1 - tanh^2(t sqrt(gk/m))] = (m/k) ln cosh(t sqrt(gk/m)), so
  t = arccosh(exp(x k/m)) / sqrt(g k/m), as fig55.py. Evaluated by hand: at k/m = 1e-3, t = 1.431, 2.269,
  3.221, 4.593 s (CSVs 1.431, 2.269, 3.221, 4.593); at k/m = 0.1, 10 m 1.675 s, 25 m 3.224 s, 50 m 5.751 s;
  the 100 m curve leaves t = 10 s at k/m = 0.0836 (CSV ends there). True log axes, 1 decade in t, 2 in k/m.
- Caption: the curves flatten at the top; for x k/m >> 1, t ~ (x k/m + ln 2)/sqrt(g k/m), roughly
  proportional to sqrt(k/m): true of the computed curves.
- `digitize.py overlay` (xgrid/ygrid read against the drawn rulings): 10 m 95% 2.83 px, 25 m 95% 4.00 px
  (max 5.00, reported MISMATCH), 50 m 2.83 px, 100 m 2.24 px. The nearest-ink measure understates the misfit
  here (the rulings are 4-8 px apart at the top). Read directly (curve centre per scan row, mapped through the
  calibration's drawn gridlines, lean included): from k/m = 1e-3 to about 0.02 the 1973 curves and eq. (230)
  agree to 0.03 s (e.g. 0.0174: drawn 1.48, 2.42, 3.69, 5.93 s, computed 1.47, 2.43, 3.67, 5.87 s); above
  about 0.04 the drawn curves bend further right: at k/m = 0.094 drawn 1.75, 3.74, 6.31 s, computed 1.66,
  3.17, 5.62 s; at 0.064 drawn 1.64, 3.24, 5.35, 9.38 s, computed 1.59, 2.88, 4.92, 8.97 s; the drawn 100 m
  curve meets t = 10 at k/m about 0.068 (computed 0.084). On the scan this is up to 12-15 px (2-2.5 mm) at the
  top of the 10, 25 and 50 m curves.
- Labels 10, 25, 50, 100 at k/m = 0.012 on white, beside the curves (computed t there 1.46, 2.37, 3.52,
  5.46 s; the knock-outs start at 1.49, 2.43, 3.61, 5.60): no knock-out touches a curve (the 100's clears it
  by about 0.1 mm at its upper corner; checked at 400 dpi).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The computed curves (eq. (230), g = 9.8) differ visibly from the 1973 art in the upper part of the chart (k/m above about 0.04): at k/m = 0.094 the drawn 10, 25, 50 m curves are at 1.75, 3.74, 6.31 s against 1.66, 3.17, 5.62 s computed (up to 18%, 2-2.5 mm on the scan); the 100 m curve meets t = 10 at 0.068 drawn, 0.084 computed. The bottom of the chart agrees. Using the computed curves follows the pilot gate decision, but the mismatch is not recorded: STYLE.md section 16 requires an overlay failure to go to corrections/v2-figures.md, and neither fig55.tex nor fig55.py mentions it. | fig55.py docstring; fig55.tex:1-5; corrections/v2-figures.md (no Fig 55 item) | Report it for the Chapter 3 gate (like Ch2 Fig 25 / Ch3 Fig 22: "computed from eq. (230); the 1973 curves bend further right above k/m about 0.04, by up to 0.57 s at 0.094"), and add a line to the fig55.tex header comment. No change to the curves. |
| 2 | note | Lettering complete and as printed: y title $\dfrac{k}{m}$ ($\mathrm{m}^{-1}$) rotated, as the scan; y ticks $10^{-3}$, 2, 3, 4, 6, 8, $10^{-2}$, 2, 3, 4, 6, 8, $10^{-1}$; x title $t$ (sec); x ticks 1, 2, 3, 4, 5, 6, 8, 10; rulings 1, 1.5, 2, 2.5, 3, 3.5, 4, 5 ... 9 per decade on both axes (as Fig 22). The family's other fraction title (Fig 53) and the approved Fig 2 set their fractions upright; here the title carries a unit and stays rotated, as printed. | fig55.tex:12-19 | Optional: for a stacked fraction read upright, `ylabel style={rotate=-90, anchor=east, align=center}`, `ylabel={$\dfrac{k}{m}$\\($\mathrm{m}^{-1}$)}`. |
| 3 | note | An ordered family of four in r2-r5 (light to dark with increasing drop distance), each labelled directly on the curve; r1 skipped (the lightest). Axes 4.2 x 2.75 in, `tamr grid`, `grid=both`. | fig55.tex:20-29 | none |
| 4 | note | fig55.calib.json's affine `points` fit has a 46.7 px residual (the log fit cannot match the non-log paper); harmless, since its `xgrid`/`ygrid` replace the fit, but a reader of the file may be misled. | fig55.calib.json "axes.main.points" | Optional: note in the file that the points serve only as a fallback. |

## Verdict: pass (no must-fix)
