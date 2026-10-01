# v2 audit: ch3/fig48 (round 2)

Sources checked: scan `figures/ch3/fig48.png` (tail zoomed 4x: fins, chamfer, the 0.68, 1.91, 2.07 and 3.30
dimensions); redraw `figures/v2/ch3/fig48.tex`, `figures/v2/ch3/fig48.pdf` rendered at 400 dpi, and
`build/v2/png/ch3-fig48{,-compare}.png`; inventory row ch3-fig48; caption and citing text `chapters/ch3-sec6b.tex`
(lines 11-20, the tangent-ogive nose, l_b = 31.75, d = 1.93); the round-1 audit (`audit/v2-ch3-fig48-round1.md`)
and the round-1 fix report; STYLE.md sections 14 and 16; `pdffonts` (all fonts embedded); page 360.1 x 192.2 pt =
5.00 in wide.

Round-1 follow-up: round 1 passed with three notes and nothing to fix. The fixer made no edits. `fig48.tex` and
`fig48.pdf` are both dated 21:54, before the round-1 audit (22:11), so this is the figure round 1 audited and
there is no regression.

Re-checked independently:
- Lettering: all eight printed values are present and correct: 31.75, 9.14, 3.30, 1.93, 4.19, 0.68, 1.91, 2.07.
  Each sits on the same side as the scan. 4.19 and 0.68 are rotated (numeric, so allowed).
- Geometry: the tex computes the stations from the labels: root LE 28.45, tip LE 30.36, TE 32.43, tip 5.155,
  chamfer top 1.645 above the axis. 28.45 + 1.91 + 2.07 = 32.43 = 31.75 + 0.68, so the chamfer is at 45 degrees.
- The 0.68: the 4x zoom of the scan shows the 0.68 dimension between an extension line at the chamfer top and one
  at the body line, with the lettering above the upper stub. The redraw is the same: extensions at y = 1.645 and
  0.965, and the label above. The scan's chamfer is about 45 degrees too.
- 1.93 is at x = 12.65 (the scan's x = 235 px works out to 12.6 cm on the 31.75 scale). The tangent-ogive nose is
  9.14 long with the nose joint drawn.
- Legibility at 400 dpi: nothing is clipped, no labels overlap, and every arrowhead is visible.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-1 notes 1-3 still apply and need no action: the base extension runs through the upper fin, the xle and 4.19 extensions cross, the 0.68 lower stub crosses the centre line, and 1.93 is drawn as a `\dimout`. Each is as printed or follows the house idiom. | fig48.tex | none |
| 2 | note | Family consistency: the dimension, extension, `\dimout` and `edge fin` usage is the same as Fig 50, and the outline and centre-line styles match. | | none |

## Verdict: pass (no must-fix)
