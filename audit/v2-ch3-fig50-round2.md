# v2 audit: ch3/fig50 (round 2)

Sources checked: scan `figures/ch3/fig50.png` (tail of the main drawing zoomed 4x); redraw `figures/v2/ch3/fig50.tex`
(dated 22:14, after the round-1 fix), `figures/v2/ch3/fig50.pdf` rendered at 400 dpi (whole figure) and at 1200 dpi
(the tail: boattail, the t and d_b stubs, c, b and the leader); `build/v2/png/ch3-fig50{,-compare}.png`; inventory
row ch3-fig50; caption and citing text `chapters/ch3-sec6c.tex` lines 36-60 (ogive nosecone, cylinder, rectangular
fins, conical boattail; the variations); the round-1 audit and the fix report; STYLE.md sections 14 and 16;
`pdffonts` (all fonts embedded); page 356.1 x 211.1 pt = 4.95 in wide.

Round-1 follow-up:
- Should-fix 1 (the "Conical boattail" leader crossed the lower stub of t) is **resolved**. Line 58 now ends the
  leader at (480,\ax-12.6). The cone radius at x = 480 is 13.25 - 3.75 x 6.5/36 = 12.573, so the end lies 0.03 units
  (0.006 mm) outside the lower boattail outline: on the line. That is 6.5 units aft of the boattail joint at 473.5
  and 7.5 units ahead of the t stub at 487.5. At 1200 dpi the leader ends on the outline and does not touch the t
  stub or its arrowhead. Like the scan's leader, it crosses the lower fin's leading edge on the way in.
- Note 2 ("boattail" close to the l_b line) is optional and was left as printed. Note 3 needed no action.
- No regression. The rest of the file is as round 1 described it: the main GCR stations, b tip to tip (eq. (189)),
  the fin roots following the boattail, and the three variations.

Re-checked independently:
- Lettering: $\ell_n$, $\ell_s$, $\ell_t$, $\ell_b$ (lowercase as printed, D36), $d_m$, $d_b$, $t$, $b$, $c$,
  "Ogive" and "Conical / boattail" are all present. Every single-letter dimension label is upright. Both
  callouts are straight leaders.
- Legibility: nothing is clipped or overlapping, and the arrowheads are visible at final size.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-1 should-fix 1 is verified fixed at 1200 dpi: the leader ends on the boattail outline between the joint and the t line. | fig50.tex line 58 | none |
| 2 | note | "boattail" still sits about 0.8 mm above the $\ell_b$ line, as in the scan (round-1 note 2, optional). | label at (432,-147) | optional: raise it 3-4 units |

## Verdict: pass (no must-fix)
