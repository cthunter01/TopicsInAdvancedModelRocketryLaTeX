# v2 audit: ch3/fig27 (round 2)

Sources checked:
- Scan: `figures/ch3/fig27.png`, including a 6x crop of the slot and the $A_2$ leader.
- Redraw: `figures/v2/ch3/fig27.pdf`, which is current (22:15:05, after the tex). Rendered at 300 dpi whole, and at 800 dpi for the upstream face and the slot. Checked with `pdfinfo` and `pdffonts`.
- Source: `figures/v2/ch3/fig27.tex`.
- Earlier rounds: the round-1 audit and the round-1 fix report.
- Inventory row `ch3-fig27`.
- Caption and citing text: `chapters/ch3-sec4b.tex`:33-57.
- Standing rule 1.

## Round-1 findings

Round 1 raised no must-fix or should-fix items, and the fix round changed nothing.
- Note 1 (hatched wall sections against the 1973 heavy lines) is carried as a gate doubt in the fix report.
- Note 2 (the heavy `vec` arrows) is consistent with Fig 28.

## Re-check

- **Control surface.** It is drawn in the kit `dotted guide`, as the text's "dotted line" requires (standing rule 1).
  - Upstream face: 4.36 R ahead of the nose. The scan has about 4.4 R.
  - Downstream face: through the middle of the slot, which runs from 16.56 to 17.06 R. The scan's slot is about 0.55 R wide.
- **Half-body.** Both parts are drawn as printed.
  - The front part is the Rankine contour, the same body as Fig 28.
  - The after-body runs from the slot to the kit `\breakline`.
- **Lettering.** Every inventory item is present: $p_1$, $u_1$, $A_1$, $p_2$, $A_2$, $u_2$.
  - At 800 dpi the subscript of $u_1$ clears the dotted face by about 3 mm.
  - The $A_2$ leader lands on the after-body's face at the slot. On the way it crosses the body's top edge, as the 1973 dog-leg leader does. The redraw's leader is straight, per the house rule.
- **Caption and text.** The two areas and the wide hollow cylinder are as the caption and text describe:
  - $A_1$ is the frontal area of the control surface.
  - $A_2$ is the frontal area of the half-body.
- **Size and fonts.** The page is 5.12 x 1.67 in, and the fonts are embedded.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The figure is unchanged since round 1, and nothing has regressed. The control surface, the slot, the body and all six labels are as printed and as the text describes. | fig27.tex | None. |
| 2 | note | The tube walls are still hatched section bands where the 1973 art has heavy lines. This is already a gate doubt in the round-1 fix report. | fig27.tex:20-21 | The gate decides. If it prefers the 1973 look, use plain `outline` lines. |

## Verdict: pass

No must-fix and no should-fix.
