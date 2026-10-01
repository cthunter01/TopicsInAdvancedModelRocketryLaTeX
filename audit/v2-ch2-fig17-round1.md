# v2 audit: ch2/fig17 (round 1)

Sources checked: scan `figures/ch2/fig17.png` (zoomed: the peak tick label and its exponent); inventory row
`ch2-fig17`; caption `chapters/ch2-sec3a.tex:632-635`; citing text `chapters/ch2-sec3a.tex:612-616` and
`698-700`; eqs. (16), (17), (30), (31a), (31b), (32a), (32b); credit `backmatter/figure-credits.tex:32`;
errata/supplement/`corrections/ch2.md` (nothing on this figure); redraw
`figures/v2/ch2/fig17.{tex,py,csv,calib.json,pdf}`; `build/v2/png/ch2-fig17{,-compare}.png`; own 400 dpi
render; `digitize.py overlay`; STYLE.md sections 13 and 16; `corrections/v2-figures.md` (standing rule 2).

Checks made:
- Lettering: $\frac{M_s}{C_1}\bigl(1 + e^{-\frac{\pi D}{\omega}}\bigr)$ and $\frac{M_s}{C_1}$ (y ticks), 0,
  $\frac{\pi}{\omega}$ (t tick), $\alpha_X$ (rad), $t$ (sec): all present. The art's parentheses are kept
  (eq. (32b) prints square brackets; standing rule 2). Nothing added.
- Curve: independently evaluated the underdamped step response
  $1 - e^{-\zeta t}(\cos\omega t + \frac{\zeta}{\sqrt{1-\zeta^2}}\sin\omega t)$, $\zeta = 0.233$ (equal to eq. (30)
  with (16), (17), (31a), (31b)): the CSV agrees to 8e-6. Zero value and slope at $t = 0$ (text 614-616).
  First peak 1.47109 $M_s/C_1$ at $\pi/\omega = 3.23051/\omega_n$, exactly the tick positions in the .tex, and
  equal to $1 + e^{-\pi D/\omega}$ (eq. (32b)); the scan's overshoot measures 1.472 from the calibration.
  The first peak is the global maximum of the plotted curve (text 698-700 relies on it). Undershoot 0.778 at
  $2\pi/\omega$; ends at 1.042 at $2.67\pi/\omega$ just above the dashed line, having crossed it upward at
  $2.58\pi/\omega$ (the scan also ends just above it).
- Marks: solid lines from the axis to the peak and down to $\pi/\omega$; dashed `guide` at $M_s/C_1$ (caption:
  comes to rest at $M_s/C_1$; maximum and its time shown).
- Overlay (calibration residual 0.72 px): mean 3.07 px, 95% 8.49 px (1.44 mm), max 9.22 px (MISMATCH by the
  3 px target). A computed curve: the difference is the scan's hand drawing, whose minimum sits at about
  $2.2\pi/\omega$ rather than $2\pi/\omega$ and whose curve runs to about $2.89\pi/\omega$; the redraw keeps the
  family time axis ($2.75\pi/\omega_n$). This follows the approved computed-curve decision; the numbers are
  for the record.
- Size 372.4 x 199.4 pt (5.17 in wide); fonts Type 1, embedded. Same axis box and ranges as Figs 16, 18, 19.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | At 150 dpi the scan's exponent shows no minus sign (it reads $e^{\pi D/\omega}$). The redraw's $e^{-\pi D/\omega}$ follows eq. (32b) and the inventory reading, and is the only form consistent with a peak below $2M_s/C_1$. Correct as drawn. | `fig17.tex:18` | none |
| 2 | note | The exponent's stacked fraction is at scriptscript size (5 pt under the 9 pt `\footnotesize` tick labels). It is legible at 400 dpi and keeps the printed stacked form; a slash form ($e^{-\pi D/\omega}$, 6 pt) would read more easily but depart from the lettering. | `fig17.tex:18` | none (optional; keep as printed) |
| 3 | note | The overlay's 95% of 8.5 px is the computed-versus-hand-drawn difference described above, not a drafting error. | `fig17.py` | none |
| 4 | note | The same local `every axis y label` override and local `peak line` style as Fig 16 (style suggestions in the Fig 15 and Fig 16 reports). | `fig17.tex:10, 20-21` | style suggestion only |

## Verdict: pass (no must-fix)
