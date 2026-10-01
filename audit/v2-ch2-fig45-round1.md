# v2 audit: ch2/fig45 (round 1)

Sources checked: scan crop `figures/ch2/fig45.png` (zoomed x3 by halves); inventory row `ch2-fig45`;
caption and citing text `chapters/ch2-sec5.tex:225-275` (data reduction: degrees / 57.3, grams x 980 x pulley
radius in cm; shaft through the rocket's centre of mass); redraw `figures/v2/ch2/fig45.tex` and its PDF
(rebuilt with `make fig F=ch2/fig45`: 4.95 x 2.82 in, all fonts embedded), the compare render
`build/v2/png/ch2-fig45-compare.png` and a 400 dpi render; STYLE.md sections 13 and 16; standing rules in
`corrections/v2-figures.md`; approved Ch1 Fig 6 (the angle-arc and extended-axis convention).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | All lettering is present and correct: "Deflection angle (rad) $= \alpha^\circ/57.3$", "Moment (dyn-cm) $= M \times 980 \times R$", "$R$ (cm)" with a leader to the pulley rim, "$\alpha^\circ$", "Wind axis", "$M$ (g)" with a leader to the weight in the pan. $M$ and $R$ are italic in the formulas and the callouts alike. | fig45.tex:52-60 | none |
| 2 | note | The geometry is consistent. The rocket axis passes through the wheel centre (the shaft), on the wind axis. The cords leave the rim tangentially at $\pm R$ on the wind axis. The pan hangs on the right, so a weight turns the nose up, which matches the nose-up $\alpha^\circ$. The arc is centred at the pivot (r = 260), and its arrowheads land on the extended axis (drawn to r = 278) and on the wind axis. The tilt of 10.28 deg matches the scan (about 10.5 deg measured). The body lines behind the wheel are dashed, as printed. | fig45.tex:14-40 | none |
| 3 | note | The $\alpha^\circ$ label is knocked out of the arc (`fill=white` at pos 0.5). The scan and the approved Ch1 Fig 6 set the angle letter beside its arc. Both read clearly at final size. | fig45.tex:37-38 | Optional, for consistency with Ch1 Fig 6: set the label beside the arc (e.g. `left`) instead of on it. |
| 4 | note | A local `hidden` style (0.5pt, on 3pt off 2pt) is used for the body lines behind the wheel. Ch2 Figs 41 and 42 each define their own `hidden` style (0.45pt, on 2.6pt off 1.6pt). | fig45.tex:11 | Style suggestion: one shared `hidden` style in tamrfig.sty, used by all three. |
| 5 | note | The formula block aligns the two = signs, which leaves about 0.25 in of space after "Moment (dyn-cm)". This is acceptable typesetting of an aligned pair; the scan does not align them. | fig45.tex:54-58 | none |

## Verdict: pass
