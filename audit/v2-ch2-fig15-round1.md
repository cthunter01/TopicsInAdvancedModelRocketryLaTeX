# v2 audit: ch2/fig15 (round 1)

Sources checked: scan `figures/ch2/fig15.png` (zoomed: title, M_s tick, origin); inventory row `ch2-fig15`;
caption and citing text `chapters/ch2-sec3a.tex:493-513` (step definition, unnumbered display 510-513);
credit `backmatter/figure-credits.tex:26`; errata/supplement/`corrections/ch2.md` (nothing on this figure);
redraw `figures/v2/ch2/fig15.{tex,py,csv,calib.json,pdf}`; `build/v2/png/ch2-fig15{,-compare}.png`; own
400 dpi render; `digitize.py overlay`; STYLE.md sections 13 and 16; `corrections/v2-figures.md`.

Checks made:
- Lettering: "Yawing moment $M_X$ (dyn-cm)", $M_s$ (y tick), 0 (below right of the origin, as printed),
  $t$ (sec): all present; $M_X$ in the section 13 form. Nothing added.
- Curve: `fig15.py` is the text's step, $f_x = 0$ for $t < 0$, $M_s$ for $t \ge 0$, riser on the vertical
  axis at $t = 0$ (CSV: (-1,0) ... (0,0), (0,0.02) ... (0,1), ... (1,1)). Caption ("zero before $t = 0$; $M_s$
  after") holds.
- Axes: four-quadrant as printed. Scan extents in units of $M_s$ and of the right half-axis: left 1.01, top
  1.29, bottom 1.20; redraw xmin -1, xmax 1.08, ymax 1.3, ymin -1.24. $M_s$ line ends at $t = 1$, short of the
  arrow, as in the scan.
- Overlay (calibration residual 0.68 px): mean 0.01 px, 95% 0.00 px, max 1.00 px (the step coincides with
  the scan's axes and $M_s$ line).
- Size 306.6 x 196.7 pt (4.26 in wide); fonts Type 1, embedded. Same axis box (3.8 x 2.5 in) as Figs 16-19.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The printed two-line vertical title left of the axis becomes a one-line upright title above the arrow (the `tamr sketch` placement); wording and units unchanged. | `fig15.tex:13-16` | none |
| 2 | note | $f_x = 0$ for $t < 0$ is drawn in the curve colour over the negative $t$ axis, and the riser over the vertical axis, as the scan does (its step also coincides with the axes). This reads correctly and matches the caption. | `fig15.tex:17`, `fig15.py` | none |
| 3 | note | The per-file override `every axis y label/.style={at={(ticklabel* cs:1.0)}, anchor=south}` is needed: with `axis lines=middle` and compat 1.18 pgfplots does not rotate the y label (`pgfplots.code.tex:2929-2937`), so `tamr sketch`'s `rotate=-90` would turn it to read downward. This is a house-style issue, not a defect of this figure (Figs 16-19 and 21-23 carry the same override). | `tamrfig.sty` `tamr sketch` | style suggestion: drop `rotate=-90` from `tamr sketch`'s `ylabel style` (then the overrides can go) |

## Verdict: pass (no must-fix)
