# v2 audit: ch3/fig38 (round 1)

Sources checked: figures/v2/ch3/fig38.tex and .pdf (built 22:12, after the .tex; log clean; 357.7 x 155.6 pt =
4.97 in wide, fonts embedded), render at 400 dpi and at 4 px per drawing unit, overlaid on the 4x scan aligned on
the trailing edge; figures/ch3/fig38.png (zoomed, including the C.P. mark); inventory row ch3-fig38; caption
chapters/ch3-sec5a.tex:270-273; citing text ch3-sec5a.tex:256-265 and ch3-sec4b.tex:257-267 ("rounded leading
edge ... gently-sloping aftersurface culminating in a sharp trailing edge"); Ch2 eq. (89)
(chapters/ch2-sec4.tex:428-430); corrections/v2-figures.md (Ch2 gate: C.P. marks by the equations); STYLE.md
sections 14 and 16.

Lettering: $\vec{D}_i$, $\vec{L}$, $\vec{F}$ (arrows as drawn and as in the caption), $\alpha_i$, $\alpha$,
"Flow direction" (above the right end of the flow arrow, as printed). All present and correct.

Geometry: F = L + D_i with L normal to the flow, D_i along it (downstream) and F tilted back by alpha_i =
atan(29/135) = 12.1 deg. The section has its leading edge up and forward at alpha = 12 deg (the scan's chord
extension measures 11.8 deg), so lift is upward, and the signs agree with the caption and sec5a:258-265. The flow
line passes through the C.P., and the chord-line extension meets it there, so the alpha arc is centred on the true
vertex. The 1973 drawing has the same construction: its chord extension, produced, passes through its C.P. on the
flow line.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The C.P. is placed by Ch2 eq. (89) for a rectangular fin (x_t = 0, c_r = c_t = c gives (1/6)(2c - c/2) = c/4), which agrees with thin-airfoil theory. The 1973 art draws it at 0.36 c. Measured on the overlay, the C.P., forces and flow line move 50 units forward (0.11 c, about 1.2 cm at final size). This follows the approved "C.P. by the equations" decision (Ch2 gate), but unlike Ch2 Figs 34-36 it is not yet recorded in corrections/v2-figures.md. | fig38.tex:5-7, 30-35 | orchestrator: add a Ch3-gate line to corrections/v2-figures.md (one-line revert: shift the section by -0.36c instead of -0.25c) |
| 2 | note | The section sits on the 1973 one along its whole length in the overlay: rounded LE, constant thickness, straight taper over the last 17% to a sharp TE. It is hatched at 45 deg with the house `hatch`, consistent with the cut sections of Fig 39(b). | fig38.tex:28-34 | none |
| 3 | note | alpha_i (about 3 mm of arc at r = 62) is marked by two `angle arc single` arrows from outside, the angular analogue of \dimout. The 1973 art draws one arc crossing L and F. Both read the same. | fig38.tex:46-50 | none |
| 4 | note | The text (sec5a:261) calls the total force the "normal force N"; the figure and caption letter it F. Kept as printed (standing rule 2). | — | none |

No overlaps or clipping at final size. The arrowheads of D_i and F meet at one point, as printed, and both stay
visible. The alpha label is clear of the arc, and the cp mark is white-filled over the hatching.

## Verdict: pass (no must-fix)
