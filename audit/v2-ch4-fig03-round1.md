# v2 audit: ch4/fig03 (round 1)

Sources checked:
- Scan `figures/ch4/fig03.png`, with 4x crops of the apex and of the spent stages, and `digitize.py lines` for
  the event levels.
- Redraw `figures/v2/ch4/fig03.pdf` (`make fig F=ch4/fig03`; clean log, 3.75 x 4.36 in): 300 dpi render, 800 dpi
  crops of the apex and the spent stages, and `build/v2/png/ch4-fig03-compare.png`. I also checked `pdffonts` (all
  embedded) and looked for opacity operators (none).
- Source `fig03.tex`.
- Inventory row `ch4-fig03`.
- Text: caption and citing text in `chapters/ch4-sec2b.tex`:56-73.
- STYLE.md sections 15 and 16.

Checks made:
- **Event levels.** `digitize.py lines` finds the scan's event lines at rows 669 (launch), 596, 487, 343.5 and 34
  (apex). That is 73, 182, 325.5 and 635 px above launch. The redraw uses 71, 180, 325 and 635, so it is within
  2 px (0.3 mm), at the printed size. The book gives no values, so the 1973 proportions are the right choice.
- **Lettering.** Every block is typeset as lettered:
  - Flight apex: $t = t_1 + t_2 + t_3 + t_c$, $v = 0$, $y = y_b + y_c = y_{\max}$.
  - 3rd stage burnout: $t = t_1 + t_2 + t_3$, $v = v_3 = v_b$, $y = y_1 + y_2 + y_3 = y_b$.
  - 2nd stage burnout: $t = t_1 + t_2$, $v = v_2$, $y = y_1 + y_2$.
  - 1st stage burnout: $t = t_1$, $v = v_1$, $y = y_1$.
  - Launch: $t = 0$, $v = 0$, $y = 0$.
  - Dimensions: $y_1$, $y_2$, $y_3$, $y_c$ inside and $y_{\max}$ outside.
  - Subscripts follow STYLE s15: digit 0, italic b and c, upright max. The line breaks are as printed.
- **Drawing.**
  - The vertical path has dots at launch and at the three burnouts, and none at the apex, as printed.
  - It bends over into the horizontal rocket at the apex. The rocket's tail is exactly at the end of the bend.
  - The apex leader ends in a head at the nose, as printed. The other leaders are plain.
  - The spent first and second stages leave on short arcs that start tangent to the path, as fin cans with the
    tail on the left, as printed.
  - The inner dimension column is chained: launch to $y_1$, $y_2$, $y_3$, then $y_c$ to the apex. The outer
    $y_{\max}$ runs from launch to the apex.
- **Caption and text.** The total altitude is $y_c$ plus the stage increments, and the total time is $t_c$ plus
  the burn times (:60-62). The dimension chain and the label blocks show both.
- **House style.**
  - `\dimline` dimensions with `extension` lines. The labels are horizontal, in white gaps.
  - `leader` and `leader arrow`. The event marks use the `point` style. The path is s1, like the trajectories of
    Figs 2 and 15.
  - The icons are `thin line` (as in Fig 2). Text is in ink.
  - Nothing is filled or transparent, and no kit name is redefined. Legible at final size (`\small`).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Each spent-stage fin can's lower fin tip sits 3 px (0.5 mm) above its burnout leader line, as in 1973. The gap shows at 800 dpi and at 150 dpi. | `fig03.tex`:39-46 | None. Optionally lift the cans 2 px (shift `\y+17`, and arc radius 17). |
| 2 | note | The $y_{\max}$ label sits in the outer dimension's gap at mid-height (317 px). That is 8 px (1.4 mm) below the 3rd-stage extension line, which starts 31 px to its right, so they do not touch. 1973 sets $y_{\max}$ beside the line at about the same height. | `fig03.tex`:32 | None. |

## Verdict: pass

No must-fix and no should-fix. All five label blocks and five dimension labels are kept as lettered, the event
levels follow the 1973 proportions within 2 px, and the house dimension and leader kit is used throughout.
