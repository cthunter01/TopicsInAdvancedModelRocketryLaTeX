# v2 audit: ch2/fig16 (round 1)

Sources checked: scan `figures/ch2/fig16.png`; inventory row `ch2-fig16`; caption `chapters/ch2-sec3a.tex:623-625`;
citing text `chapters/ch2-sec3a.tex:606-612`; eqs. (16), (17), (30), (31a), (31b), (32a), (32b)
(`chapters/ch2-sec3a.tex:563-697`); credit `backmatter/figure-credits.tex:29`; errata/supplement/`corrections/ch2.md`
(nothing on this figure); redraw `figures/v2/ch2/fig16.{tex,py,csv,calib.json,pdf}`;
`build/v2/png/ch2-fig16{,-compare}.png`; own 400 dpi render; `digitize.py overlay`; STYLE.md sections 13 and 16;
`corrections/v2-figures.md`.

Checks made:
- Lettering: $\frac{2M_s}{C_1}$, $\frac{M_s}{C_1}$ (y ticks, stacked fractions as printed), 0, $\frac{\pi}{\omega_n}$
  (t tick), $\alpha_X$ (rad), $t$ (sec): all present, section 13 forms. Nothing added.
- Curve: independently evaluated $(M_s/C_1)(1-\cos\omega_n t)$ (eq. (30) with $D = 0$, $\varphi = \pi/2$,
  $A = -M_s/C_1$): the CSV agrees to 1e-5 over all 401 points; starts at 0 with zero slope (text 610-612);
  peak $2M_s/C_1$ at $\pi/\omega_n$ = tick 3.14159 (eqs. (32a), (32b)); back to 0 at $2\pi/\omega_n$; ends at
  $t = 2.75\pi/\omega_n$ at 1.707 $M_s/C_1$ (scan about 1.7).
- Marks: solid lines from the axis to the peak and from the peak down to $\pi/\omega_n$ (as printed; `peak
  line`, ink2 0.4 pt); dashed `guide` at $M_s/C_1$ to the curve's end (caption: oscillates about $M_s/C_1$;
  maximum and the time first attained are shown).
- Axes vs scan: $\pi/\omega_n$ at 0.336 of the t axis (scan 0.347); ymax 2.62 (scan about 2.69), ymin -0.36
  (scan about -0.34), in units of $M_s/C_1$.
- Overlay (calibration residual 1.11 px): mean 0.65 px, 95% 2.24 px (0.38 mm), max 3.16 px: within the 3 px
  target although computed.
- Size 333.7 x 200.7 pt (4.63 in wide); fonts Type 1, embedded. Layout (3.8 x 2.5 in, x 0-9.35, y -0.36-2.62)
  shared with Figs 17-19.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The printed vertical axis title becomes upright above the arrow (the `tamr sketch` placement), via a local `every axis y label` override that works around `tamr sketch`'s `rotate=-90` (see the Fig 15 report, finding 3). | `fig16.tex:17-18` | style suggestion only (tamrfig.sty) |
| 2 | note | `peak line` (solid ink2 0.4 pt) is defined locally, identically in Figs 16 and 17; a house `reference line` style would serve these and the similar marks in Figs 10-14. | `fig16.tex:8` | style suggestion only |

## Verdict: pass (no must-fix)
