# v2 audit: ch3/fig18 (round 1)

Sources checked: scan `figures/ch3/fig18.png` (panel (a) zoomed 4x); redraw `figures/v2/ch3/fig18.pdf` (current;
304.2 x 168.8 pt = 4.22 x 2.34 in; fonts all embedded), rendered at 400 dpi, and
`build/v2/png/ch3-fig18-compare.png`; `figures/v2/ch3/fig18.tex`, `fig18.py`, `fig18-a.csv`, `fig18-b.csv`,
`fig18-arrows.csv`, `fig18-marks.csv`, `fig18.calib.json`; inventory row `ch3-fig18`
(`figures/v2/inventory.csv`:84); caption `chapters/ch3-sec3b.tex`:411-420; citing text :382-386 (Rayleigh, a
profile with a point of inflection is unstable), :396-403 (favorable gradient: full, "as in Figure 18b"; adverse:
inflection points, "as in Figure 18a"); `STYLE.md` sections 14 and 16; `corrections/v2-figures.md`.

Checks made:
- **Profiles.** Both are Falkner-Skan solutions of eqs. (38)-(39). I re-solved them independently by shooting.
  (a): beta = -0.1983 gives f''(0) = 0.0200, eta99 = 4.693, and an inflection (f''' = 0) at y/delta = 0.479,
  u/U = 0.502, that is (115.4, 68.3) px; this agrees with fig18-marks.csv (115.39, 68.21). (b): beta = +0.07
  gives f''(0) = 0.554 and no inflection, so (b) is "fully convex in the direction of flow", as the caption says.
  delta is at u = 0.99 U in both.
- **Overlay.** I ran it myself: 95% within 3.16 px for (a) (max 4.0) and 2.24 px for (b). Both are computed
  curves, and both sit on the 1973 curves. The near-wall part of (a) follows the scan; I checked this at 4x.
- **Lettering.** Both panels carry y, $U_\infty$, u(y) and the small circle at the boundary-layer edge. (a) also
  has the delta dimension, from the wall to the edge, with an extension line from the circle and the label
  upright in a gap, and "Point of inflection" with a straight leader to a circle on the curve. The panel letters
  are the house `panel` style "(a)", "(b)" at the lower right of each panel on one baseline; the 1973 art circles
  them, and the text cites "Figure 18a/b" and the caption "Profile (a)".
- **Frame and style.** Both panels share one frame: U = 166 px, delta = 142.5 px, top 215 px, 22 arrows per
  panel at even 10 px spacing (the scan has about 24), and hatched walls (a 10 px band, 45 deg, as in Fig 25). The
  profile styles are identical to Figs 16, 17 and 25.
- **Layout.** No overlaps: u(y) in (a) clears the delta line by about 1 mm, and the inflection label clears the
  curve and the delta line. Nothing is clipped.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note (gate) | The inflection point is placed where the equation puts it, (115, 68) px, about 21 px (4.3 mm at final size) below and to the left of the 1973 circle at about (132, 80). This follows the "marks placed by the equations" decision, but it is not yet in `corrections/v2-figures.md`. | fig18.tex:5-7; fig18-marks.csv | orchestrator: log it with the Ch3 items |
| 2 | note | (a) is set just short of separation (f''(0) = 0.02, not the 0 the least-squares fit tends to), so it keeps a slight wall slope and is not the same profile as Fig 25's separation profile c. This is a sensible, documented choice. | fig18.py:31 | none |

## Verdict: pass (no must-fix)
