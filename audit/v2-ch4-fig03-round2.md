# v2 audit: ch4/fig03 (round 2)

Sources checked:
- Scan `figures/ch4/fig03.png`, with 3x zooms of the "Flight apex" and "3rd stage burnout" label blocks.
- Redraw `figures/v2/ch4/fig03.pdf` (rebuilt with `make fig F=ch4/fig03`; clean log, 3.75 x 4.36 in). I looked at
  300 and 600 dpi renders, 600 dpi crops of the apex and of the spent stages, and
  `build/v2/png/ch4-fig03-compare.png`. All fonts are embedded, with no opacity operators or soft masks.
- Source `fig03.tex`, unchanged since round 1.
- Inventory row `ch4-fig03`, and the caption and citing text in `chapters/ch4-sec2b.tex`:56-75.
- Round-1 audit `audit/v2-ch4-fig03-round1.md` and the fixer's report.

## Independent checks

- **Lettering, against the zoomed scan.** Every block is typeset as lettered, commas included:
  - "Flight apex: $t = t_1 + t_2 + t_3 + t_c$, $v = 0$, / $y = y_b + y_c = y_{\max}$";
  - "3rd stage burnout: $t = t_1 + t_2 + t_3$, $v = v_3 = v_b$, / $y = y_1 + y_2 + y_3 = y_b$";
  - "2nd stage burnout: $t = t_1 + t_2$, $v = v_2$, $y = y_1 + y_2$";
  - "1st stage burnout: $t = t_1$, $v = v_1$, $y = y_1$";
  - "Launch: $t = 0$, $v = 0$, $y = 0$";
  - the dimensions $y_1$, $y_2$, $y_3$, $y_c$ and $y_{\max}$.
  - The forms follow STYLE s15: digit 0, italic b and c, upright max.
- **Drawing.**
  - The event levels are 71, 180, 325 and 635 px above launch, as on the scan (within 2 px).
  - There are dots at launch and at the three burnouts, and none at the apex.
  - The path bends over into the horizontal rocket at the apex. The apex leader ends in a head at the nose, as
    printed.
  - The spent-stage fin cans peel off on arcs tangent to the path.
  - The dimension chain shows the sum the caption and the text (:60-67) describe: $y_{\max}$ = the stage
    increments plus $y_c$.
- **House and family consistency.**
  - `\dimline` with `extension` lines, and `leader` / `leader arrow`.
  - The path is s1 at 1pt (`curve`), as in Figs 2 and 15. The icons are `thin line`, as in Fig 2.
  - Text is in ink, and no kit name is redefined.

## Round-1 findings

- **1 (note, the fin cans 3 px above their leaders): declined by the fixer, which is fair.** It was optional,
  1973 draws the same clearance, and the gap reads as intended at 600 dpi.
- **2 (note, $y_{\max}$ in the outer dimension's gap): no change needed.** The label is still clear of the
  3rd-stage extension line.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| - | - | No findings. | - | - |

## Verdict: pass

The figure is unchanged since round 1 and builds clean against the current kit. All five label blocks and five
dimension labels match the scan, the event levels follow the 1973 proportions, and the house dimension and leader
kit is used throughout.
