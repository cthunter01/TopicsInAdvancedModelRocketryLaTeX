# v2 consistency check: ch3/fig30

Issue 2 (velocity-arrow weight): the two insets' labelled $U$ arrows were `thin vec`. Every other labelled
free-stream arrow, including the Fig 51 inset's $U_\infty$, is `vec` (STYLE s.16: force and velocity vectors are
`vec`).

Issue 1 (break symbol) does not apply, because Fig 30 has no broken-off tube.

Sources checked:
- figures/v2/ch3/fig30.tex:1-61 and figures/v2/ch3/fig30.pdf. The PDF is newer than the .tex (23:14:00 against
  23:13:59). It measures 420.457 x 267.087 pt = 5.84 x 3.71 in, the same as round 1, and all fonts are embedded.
  I rendered it at 300 dpi, and both insets' $U$ arrows at 1200 dpi.
- The scan figures/ch3/fig30.png.
- The round-1 audit, and inventory row ch3-fig30 (figures/v2/inventory.csv:96).
- The `vec` and `thin vec` definitions (tamrfig.sty:62-63).
- The insets of Fig 51 (fig51.tex:62) and Fig 34 (fig34.tex:40), both rendered at 300 dpi.
- The fixer's 300 dpi before and after renders, compared pixel by pixel with my render.

## Checks

- **The issue is resolved.**
  - fig30.tex:37 (inset 1) and :56 (inset 2) are `\draw[vec]`. Their geometry is unchanged: (160 to 192, 121.5)
    and (329 to 380, 203.3) in scan px.
  - The header (lines 10-11) records the change.
  - All three plot insets now draw their labelled free-stream arrow as `vec`: this figure's two, Fig 34's $U$ and
    Fig 51's $U_\infty$. So the fallback (thinning Fig 51) is not needed.
  - At 300 dpi the arrows read clearly in the small insets and do not overpower the 0.6 pt outlines.
- **Clearance at 1200 dpi.**
  - Both $U$ labels (inner sep 2.5 pt, raised from 1.5 pt) clear the 1.3 pt shaft by about 0.7 mm.
  - Inset 1's arrowhead stops about 1.1 mm short of the flat front.
  - Inset 2's tip stops about 0.9 mm short of the front. The dash-dot axis begins just past the tip (x = 381),
    as before.
  - Nothing collides.
- **Nothing else changed.**
  - The fixer's after-render matches my render exactly.
  - Against the before-render, the only differing pixels are two small boxes around the arrows and labels:
    - inset 1: columns 434-531, rows 342-391 at 300 dpi;
    - inset 2: columns 1004-1167, rows 618-666.
  - The CSVs are dated 22:00, before the fix, and are untouched.
  - I re-ran `digitize.py overlay` myself and got round 1's numbers exactly:
    - 2-D: mean 0.01 px, 95% 0.00 px, max 1.0 px;
    - 3-D: mean 0.50 px, 95% 2.00 px, max 3.0 px.
- **Against the scan and the inventory, the lettering is all present and unchanged.**
  - The titles are $\CDo$ and $\dfrac{r}{h}$.
  - The ticks run 0-1.2 and 0-0.5.
  - Both inset labels with their $R$ values are there.
  - Inset 1 has $U$, $r$ (leader to the corner) and $h$ (`\dimout` on extension lines). Inset 2 has $U$.
  - Both curve leaders end at r/h 0.167 and 0.436, as before.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | The label placement differs slightly across the three insets. Fig 30's $U$ sits over the tail of its arrow, as the scan places it. Figs 34 and 51 centre theirs (`midway`, above). This follows each scan, and the arrow weight, which was the issue, is now uniform. | fig30.tex:38, 57 | None. |
| 2 | note | Round 1's note 2 (thin vec on the insets) is superseded by this fix. | - | None. |

## Verdict: pass (issue 2 resolved; issue 1 not applicable; no regression)
