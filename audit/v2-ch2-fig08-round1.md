# v2 audit: ch2/fig08 (round 1)

Sources checked: figures/ch2/fig08.png (scan, upscaled 3x); figures/v2/ch2/fig08.pdf (rebuilt with `make fig
F=ch2/fig08`, 4.69 x 2.87 in, fonts embedded; rendered at 150 and 300 dpi) and build/v2/png/ch2-fig08-compare.png;
figures/v2/ch2/fig08.tex, fig08.py (and the functions it imports from fig07.py), fig08.calib.json, fig08.csv;
figures/v2/inventory.csv row ch2-fig08; caption chapters/ch2-sec2.tex:45-46; citing text ch2-sec2.tex:26-32; Fig 9
caption ch2-sec2.tex:114-119 and eq. (9) (ch2-sec2.tex:100-104); STYLE.md sections 13 and 16;
corrections/v2-figures.md; approved examples ch2/fig25.tex, ch1/fig03.tex, ch4/fig06a.tex.

Checked and correct:
- Lettering: y title "Damping moment $M_d$ (dyn-cm)", x title "Angular velocity $\Omega_X$ (rad/sec)" (section 13
  form); y ticks 0, $1\times10^6$, $2\times10^6$ labelled with unlabelled minor ticks at $0.5\times10^6$ and
  $1.5\times10^6$; x ticks 0, 50, 100, 150 labelled with minor ticks at 25, 75, 125, all as in the scan; open left and
  bottom axes, no grid, as printed. Nothing added.
- Data: fig08.py reruns to a byte-identical fig08.csv; trace fit residual rms 0.40 px, 95% 0.86 px. `digitize.py
  overlay` on the scan: mean 0.03 px, 95% 0.00 px, max 1.00 px (within the 3 px target). The curve is exactly
  $C_2\Omega_X$ with $C_2 = 1.25\times10^4$ dyn-cm-sec up to 60 rad/sec (tangent at zero = the Fig 9 lettering,
  eq. (9)), then concave with a C2 join; values 3.125e5 at 25, 6.25e5 at 50, 9.34e5 at 75, 1.189e6 at 100, maximum
  1.373e6 at 139, 1.359e6 at 150, matching the inventory's reading (flat maximum about 1.38e6 near 137, 1.36e6 at
  150). At 87 rad/sec it is 1.9% below the tangent, consistent with the Fig 9 caption. The data are the same as Fig
  9's true $M_d$ (fig09-md.csv column `true` equals fig08.csv exactly).
- The calibration reads the unevenly drawn x ticks piecewise (69-73 px per 25 rad/sec), which accounts for the
  inventory's "drawn initial slope about 3% steeper than $C_2$": against the drawn ticks the traced slope is $C_2$.
- Legibility and style: width 4.69 in; single `series1` curve; same axes size and layout as Figs 7 and 9.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| - | - | No findings. | - | - |

## Verdict

pass (0 must-fix, 0 should-fix)
