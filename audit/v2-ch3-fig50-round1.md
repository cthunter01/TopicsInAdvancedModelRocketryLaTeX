# v2 audit: ch3/fig50 (round 1)

Sources checked: scan `figures/ch3/fig50.png` (zoomed 2-4x: the tail of the main drawing and the three variations);
redraw `figures/v2/ch3/fig50.tex`, `fig50.calib.json`, `figures/v2/ch3/fig50.pdf` rendered at 400 and 1000 dpi
(tail detail), and `build/v2/png/ch3-fig50{,-compare}.png`; inventory row ch3-fig50; caption and citing text
`chapters/ch3-sec6c.tex` lines 38-58 and eqs. (181)-(190) (S_F = 2cb, so b runs tip to tip); STYLE.md sections 14
and 16; `pdffonts` (fonts embedded); page 356 x 211 pt = 4.95 in wide.

Checked:
- Lettering: every printed label is present. The lengths are $\ell_n$, $\ell_s$, $\ell_t$, $\ell_b$, kept lowercase as
  printed (D36). Also present: $d_m$, $d_b$, $t$, $b$, $c$, "Ogive" and "Conical boattail" (two lines). Subscripts are
  italic per section 14.
- Main drawing against the scan, in the scan's pixels at 1.25x: nose 83.5, cylinder to 373.5, boattail to 409.5,
  d_b/d_m 0.72; fin LE 10 ahead of the boattail; TE at the base; b = 126 tip to tip, which agrees with eq. (189). The
  fin root follows the boattail correctly (r at the LE = r, then the cone). The tangent-ogive check: at x = 63 the ogive
  radius is 12.47 and the "Ogive" leader ends at 12.9, which is on the outline.
- Variations against the scan: (1) fin 172-189.5, no boattail; (2) boattail 527-584, fin LE 546 on the boattail;
  (3) boattail 487.5-507, fin LE 469. All are within about 1 px of the scan, and the fin half-spans are 36.5, 45.5 and
  36.5 as scanned. The vertical clearances between the rows and the l_b line are fine.
- Dimension idiom is as in Fig 48 and Ch2 Fig 48: chained l_n, l_s, l_t, the l_b line below, and `\dimout` for d_m,
  d_b, t and c. b is a `\dimline` with an upright single letter.
- The edge-on fin pair is drawn on the axis, its thickness exaggerated so that t can be shown (as printed).

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The "Conical boattail" leader crosses the lower stub of the $t$ dimension and ends just past it, so it reads as if it ended on the $t$ arrow. The leader runs from (432,-147) to (491,-113.4). The lower t stub is the vertical at x = 487.5, from y = -132.6 to -104.25. The two cross at (487.5,-115.4), about 1 mm below the boattail outline, and the leader runs on 0.7 mm beyond (seen at 1000 dpi). The scan's leader stops near the boattail joint, ahead of the t line. | fig50.tex line 58 `\draw[leader] (bt.north east) -- (491,\ax-11.4);` | End the leader on the lower boattail outline ahead of the t stub, e.g. `(480,\ax-12.6)` (the cone radius at x = 480 is 12.57). A straight leader from the label to any point aft of x = 487.5 must cross the stub. |
| 2 | note | "boattail" sits about 0.8 mm above the $\ell_b$ dimension line. This is tight but clear, and the scan has the same arrangement. | label at (432,-147), l_b at y = -184 | optional: raise the label 3-4 units |
| 3 | note | The l_s/l_t extension at x = 473.5 runs inside the upper fin, and the body outline continues through the fin roots. Both are as printed and geometrically right. | | none |

## Verdict: pass (no must-fix)
