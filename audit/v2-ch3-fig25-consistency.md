# v2 consistency verification: ch3/fig25

Issue verified: labelled free-stream velocity arrows were drawn at two weights across Chapter 3. They were `vec` in
Figs 06, 11, 27, 28, 29, 39 and 51, and `thin vec` in Figs 16, 25, 30 and 34. The fix for this figure was the
U_inf and u arrows at fig25.tex:73-74. The suggestion was to keep `thin vec` for the unlabelled outer-flow arrows.

Sources checked:
- the scan `figures/ch3/fig25.png`: the U_inf/u area and the outer-flow area zoomed 3-4x
- the redraw `figures/v2/ch3/fig25.pdf`, current by `make -q` (built 23:12:31, after the 23:12:28 .tex): 333.60 x 172.83 pt = 4.63 x 2.40 in, the same as before, with all fonts embedded. I rendered it at 400 dpi and the left third at 1000 dpi.
- `build/v2/png/ch3-fig25-compare.png`
- `figures/v2/ch3/fig25.tex`, `fig25.py`, `fig25-*.csv` and `fig25.calib.json`
- the inventory row `ch3-fig25`
- STYLE.md section 16 and the kit `vec` and `thin vec` styles (`tamrfig.sty`:62-63)
- the round-1 and round-2 reports
- every labelled `vec` and `thin vec` arrow in `figures/v2/ch3/*.tex`

Checks made:
- **The issue is resolved.** fig25.tex:73 (U_inf) and :74 (u) are now kit `vec`. As the suggestion asked, the following stay as they were:
  - the three unlabelled outer-flow arrows under "Undisturbed outer flow" (:76-78, `thin vec`)
  - the pressure-gradient arrow (:79)
  - the reversed-flow arrows (:60)
  - the streamline heads (`stream head`)

  Elsewhere in the chapter, labelled velocity arrows are now `vec` everywhere: Figs 06, 11, 16, 27, 28, 29, 30, 34, 39 and 51.
- **Only the intended change.** I compiled a scratch copy with lines 73-74 set back to `thin vec`. It is 333.60 x 172.83 pt, the size in the round-2 report. A pixel comparison at 300 dpi against the current PDF (same page size) found exactly three changed regions: the U_inf arrow, the u arrow, and their two labels. Each label sits 0.35 pt higher because the node's default outer sep grows with the line width. Nothing else moved.
- **No regression against the scan or the data.** The CSVs and fig25.py (22:36) predate the round-2 audit (22:44). I re-ran the overlay myself, and the 95% values are unchanged from round 2:

  | curve | 95% within |
  |---|---|
  | wall | 2.83 px |
  | edge | 2.24 px |
  | a | 2.83 px |
  | b | 2.00 px |
  | c | 2.24 px |
  | d | 8.06 px |
  | e | 2.83 px |
  | u = 0 line | 11.00 px |
  | streamlines | 7.21 px |
- **Lettering and layout at 1000 dpi.** The inventory has $U_\infty$ and u "over a short horizontal arrow stroke", and the redraw matches. The 0.55 cm u arrow keeps a visible shaft behind its 7 pt head. Both labels sit clear above their shafts. The U_inf arrow (y = 73) is about 3.7 mm above the dashed edge, and the u arrow sits inside the layer, clear of the delta dimension and of profile a. The scan draws U_inf and u as bold short strokes, so the heavier marks are closer to the 1973 art than the thin ones were.
- **Within the figure.** U_inf (heavy) and the outer-flow arrows (thin) now differ in weight, although the 1973 art draws all five strokes at about one weight. This follows the issue's stated split: arrows labelled with a symbol are `vec`, and unlabelled flow-direction marks are `thin vec`, like the "Flow direction" lines of Figs 37 and 38. The result reads as intended: one labelled free-stream vector and lighter flow indications downstream.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Resolved: U_inf and u are now kit `vec`, matching the chapter's labelled velocity arrows (STYLE s.16). The unlabelled outer-flow, pressure-gradient and reversed-flow arrows stay light, as the suggestion said. Nothing else changed apart from a 0.35 pt lift of the two labels (outer sep). | fig25.tex:73-74 | none |
| 2 | note | U_inf (heavy) and the three outer-flow arrows (thin) show the same free stream at different weights, where the scan's weights are similar. This is the issue's chosen split (symbol-labelled arrows `vec`, unlabelled flow marks `thin vec`), and it is consistent with Figs 37 and 38. | fig25.tex:73, 76-78 | none |
| 3 | note (gate) | Carried from rounds 1 and 2: d's shallower reversed layer (8.1 px), the u = 0 line (11 px) and the streamlines (7.2 px) differ from the 1973 freehand art. They are still missing from `corrections/v2-figures.md`. | fig25.tex:7-9 | orchestrator: log them with the Ch3 items |

## Verdict: pass (no must-fix)
