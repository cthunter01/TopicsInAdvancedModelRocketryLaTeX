# v2 audit: ch3/fig13 (consistency fix verification)

Issues checked:
- Velocity profiles are drawn three ways in Chapter 3 (keys ch3/fig10, fig13, fig23, fig33). For Fig 13 the
  suggestion was to copy the family styles from fig16.tex:13-16 and use `profile` and `profile arrow`, keeping the
  base lines and the wall in ink.
- Fig 13's hatched wall band is about 4.3 mm deep, against about 2 mm in Figs 6, 18 and 25. The suggestion was
  `\fill[hatch] (0,-8.6) rectangle (466,0);`.

Sources checked: redraw `figures/v2/ch3/fig13.tex`, `fig13.py`, the `fig13-*.csv` files and `fig13.calib.json`. I
rebuilt it with `make fig F=ch3/fig13` (5.45 x 1.97 in, fonts embedded) and rendered it at 300 and 600 dpi (the
first profile and the leading edge zoomed). Also checked: `build/v2/png/ch3-fig13-compare.png` beside the scan
`figures/ch3/fig13.png`, whose rows I read around the leading edge; inventory row `ch3-fig13`; audits
`audit/v2-ch3-fig13-round1.md` and `-round2.md`; peers fig16.tex:12-16, fig18.tex (its `\wall`), fig06.tex and
fig25.tex. Peer renders at 600 dpi were used for the band depth. I ran the profile overlay again myself.

## Issue 1 (velocity profiles): resolved

- fig13.tex:15-19 defines `profile`, `profile arrow` and `profile stroke`. They match fig16.tex:13-15 character for
  character. The old ink `profile arrow` and `profile line` are gone.
- The arrows of all four stations (fig13.tex:47) are `profile arrow`. The three Blasius curves (fig13.tex:50) and
  the tip line of the uniform upstream profile (fig13.tex:49) are `profile`.
- The four base lines (fig13.tex:48) and the plate surface (fig13.tex:45) stay `outline` (ink), as the issue asked.
  The dashed edge (`guide`), the $\delta(x)$ dimension and the axis arrows are unchanged.
- At 600 dpi the arrow tips land on the curves and the rows are evenly weighted. The heavier-looking row in the
  300 dpi render is pixel alignment only. The figure now reads the same as Figs 16, 17, 18 and 25.

## Issue 2 (wall band depth): resolved

- fig13.tex:44: the band runs from y = -8.6 to 0, which is 8.6 x 0.237 mm = 2.04 mm. Measured at 600 dpi, it is
  46 px, the same as Fig 18's band (46 px). Fig 6's band is 50 px. The pattern is the kit's `hatch`, unchanged.
- The x-axis bracket moved up from y = -36 to -26 (fig13.tex:56), so it does not hang below the thinner band. I
  read the scan: the plate is at row 182, the hatching ends near row 199 and the x arrow is at row 218.5, about
  19 px below the band. The redraw's gap is 17.4 units, which is close to the 1973 spacing. The vertical leg still
  starts just under the open circle, as printed.
- Note: the 1973 band is about 17-18 px deep, so the old 18-unit band matched the scan. The 2 mm band is a
  deliberate family-uniformity choice, as the issue intends. It changes no meaning.

## Regression check: none found

- The data is unchanged (the CSVs date from before round 2). My overlay gives the round-2 numbers exactly: p1 95%
  2.24 px (max 3.00), p2 2.83 px (max 2.83), p3 2.24 px (max 2.83). Each profile's knee is still on the dashed edge.
- The lettering is complete, as in the inventory: $U_\infty$ twice, $y$, $x$ on the L-shaped arrow, $u(x,y)$, and
  $\delta(x)$ upright in its dimension gap. The open circle is at the leading edge. Each station has 16 arrow rows
  (fewer drawn where u is under 4 units, as before). The plate is hatched below.
- The height went from 2.06 to 1.97 in, from the thinner band and the raised bracket. The width is unchanged.
- The round-2 gate items (the computed edge against the 1973 dash-dot, 95% 8.95 px; the edge drawn dashed) are
  unaffected.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | The fixer suggests that Fig 18's `\wall{<x left>}{<x right>}` (a hatched band 2 mm deep under an outline) join `profile`, `profile arrow` and `profile stroke` in the kit, so the wall depth stays uniform across Figs 6, 13, 18 and 25. Fig 13 would need a depth argument, because its unit is 0.237 mm and Fig 18's is 0.203 mm. | fig13.tex:44-45 | Kit decision. No figure change. |

## Verdict: pass (no must-fix)
