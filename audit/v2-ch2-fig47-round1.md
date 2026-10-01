# v2 audit: ch2/fig47 (round 1)

Sources checked: scan crop `figures/ch2/fig47.png` (zoomed x3-x10 at the noses, the crossing and the tail);
inventory row `ch2-fig47`; caption and citing text `chapters/ch2-sec5.tex:326-368` (released at $\alpha_0$, the
rocket overshoots to $\alpha_1$ on the opposite side of zero, both taken as positive; same gimbal with the shaft
through the C.G.); redraw `figures/v2/ch2/fig47.tex` and its PDF (rebuilt with `make fig F=ch2/fig47`: 5.22 x 2.00 in,
all fonts embedded), the compare render and a 400 dpi render; for family consistency, `figures/v2/ch2/fig45.tex`
(the same rocket) and approved Ch1 Fig 6; STYLE.md sections 13 and 16.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | All lettering is present: "Position at / greatest / overshoot" and "Original / deflected / position" (three lines each, as printed), $\alpha_1$, $\alpha_0$ (digit subscripts, STYLE section 13), and "Wind axis". The scan prints "Wind axis" on two lines around the axis end; the redraw sets it on one line above the end. The wording is unchanged. | fig47.tex:31, 41-42 | none |
| 2 | note | The geometry matches the caption and text. Both rocket axes pass through one pivot on the wind axis. The original position (nose down) is solid, at $\alpha_0$ = 17.55 deg below the axis. The overshoot position (nose up) is a phantom line, at $\alpha_1$ = 12.74 deg above it, on the opposite side of zero and smaller, as damping requires. Both arcs are centred at the pivot, run from the wind axis and end on the extended axes. My scan measurements agree: about 18 and 13 deg. | fig47.tex:13-40 | none |
| 3 | note | The scan uses dash-dot for the overshoot outline and short dashes on parts of its fins (the inventory's "hidden parts of the fins dashed"). The redraw draws the whole overshoot outline, fins included, in one local `phantom` style (dash-dot-dot, 0.6pt ink), distinct from the grey `centerline`. The overshoot rocket is a position at another time, not a hidden part, so a uniform phantom line loses nothing and is easier to read. | fig47.tex:11-12, 20-23 | Style suggestion: a shared `phantom` style in tamrfig.sty for alternative positions. |
| 4 | note | The angle letters are knocked out of their arcs, as in Fig 45. The scan and the approved Ch1 Fig 6 set them beside the arc. Both read clearly. | fig47.tex:36-39 | Optional: set them beside the arcs, as in Ch1 Fig 6, and keep Figs 45 and 47 the same. |
| 5 | note | The pivot is 221 px behind the nose here and 216.5 px in Fig 45. It is the same rocket, balanced the same way (shaft through the C.G.). The difference is 1.2% of the length and invisible. | fig47.tex:13 vs fig45.tex:12 | Optional: share one value between Figs 45 and 47. |

## Verdict: pass
