# v2 audit: ch3/fig40 (round 2)

Sources checked: scan `figures/ch3/fig40.png`; redraw `figures/v2/ch3/fig40.tex`, `fig40.py`, `fig40.csv`,
`fig40.calib.json`; rebuilt with `make fig F=ch3/fig40` (5.09 x 3.31 in, all fonts embedded) and rendered at
350 dpi, with label zooms; `build/v2/png/ch3-fig40-compare.png`; inventory row `ch3-fig40`; caption and citing
text `chapters/ch3-sec5b.tex:15-40` (eqs. (146), (147)); `corrections/v2-figures.md` (pilot gate lines 38-40,
50-54); STYLE.md sections 14, 16; round-1 audit `audit/v2-ch3-fig40-round1.md` and the round-1 fix report.

Checks run:
- Regression: none of the figure's files has changed since round 1 (fig40.tex 21:50, .py 21:42, .csv 21:51,
  .calib.json 21:52; round-1 audit 21:59). The kit (`tamrfig.sty` 21:33), STYLE.md and the Makefile are also
  older than round 1. The rebuilt render is the same as the one audited in round 1.
- `fig40.py` rerun in memory: its output is byte-identical to `fig40.csv` (201 points). Prints K_F(B) = 1.242
  and K_B(F) = 0.419 at d/b = .289.
- I recoded the NACA TR 1307 K_W(B) formula separately (r/s form). It matches the CSV to five places at d/b =
  0.05, 0.1, 0.25, 0.3, 0.5, 0.75, 0.9 and 0.995: K_F(B) = 1.03744, 1.07697, 1.20646, 1.25276, 1.45028,
  1.71769, 1.88568, 1.99425; K_B(F) = 0.06506 ... 1.98578. I also checked the sum rule from slender-body
  apparent mass. The cross-flow apparent mass at the fin trailing edge is pi rho [(s - a^2/s)^2 + a^2]. Remove
  the nose's pi rho a^2 and divide by the exposed panels' pi rho (s - a)^2 to get (1 + a/s)^2. So
  K_B(F) = (1 + d/b)^2 - K_F(B) holds, and the curves meet at (1.0, 2.0).
- `digitize.py overlay`: K_F(B) 95% 1.00 px, max 1.00 px; K_B(F) 95% 2.24 px (0.38 mm), max 3.16 px. Both are
  "ok" and match round 1.
- My own masked check (gridlines masked, mesh calibration inverted data to pixel, nearest ink run within 6 px
  in each column):
  - K_F(B): |offset| 95% 0.79 px.
  - K_B(F): 95% 3.78 px. The drawn curve lies a mean of 2.6-2.8 px (vertical) below the computed one over d/b
    0.6-0.98 and 1.5 px above it over 0.2-0.4.
  - This agrees with round 1 (95% 3.89 px; 3.9 px at 0.65-0.95).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | Carried over from round 1 (item 1). This is for the orchestrator and needs no figure change. The fixer declined it correctly, because the file is outside its permitted files. `corrections/v2-figures.md` still has no Fig 40 entry beyond the gate lines (39, 52). The text reads K_B(F) = 0.44 and K_F(B) = 1.25 at d/b = .289 off this figure (ch3-sec5b.tex:38-40, used in eq. (147)). The computed redraw gives 0.419 and 1.242, so a reader of the redraw gets 0.66 for the factor (.44 + 1.25 - 1) = 0.69 that the text prints. | corrections/v2-figures.md | Orchestrator: add a minor Fig 40 entry (no note in the book). Computed 0.419/1.242 at d/b = .289, against the text's 0.44/1.25 and the 1973 art's about 0.43/1.25. The 1973 K_B(F) is drawn about 0.03 low over d/b 0.6-0.95: masked overlay 95% 3.8-3.9 px, tool overlay 95% 2.24 px. |
| 2 | note | The computed curves are correct (see checks): the formula was re-evaluated separately at 8 points and the sum rule was derived. The script reproduces the CSV. Both curves start at 1 and 0 and meet at (1.0, 2.0). This is the approved slender-body decision, so the K_B(F) offset from the art is not a defect. | fig40.py:22-37; fig40.csv | none |
| 3 | note | Lettering, ticks, rulings and labels are unchanged from round 1 and as printed. The y title is three lines, $K_{F(B)}$ / or / $K_{B(F)}$, upright. Ticks are 0-2.0 by 0.2 with rulings every 0.1, and 0-1.0 by 0.1 with rulings every 0.05. The x title is $\dfrac{d}{b}$. The curve labels sit in white knock-outs. At 350 dpi the $K_{F(B)}$ knock-out clears its curve and the $K_{B(F)}$ knock-out is clear of the s2 curve. Nothing is clipped. Width is 5.09 in. | fig40.tex:9-22 | none |
| 4 | note | Family consistency holds: the same 4.2 x 2.6 in axes, `tamr grid` with `grid=both` and upright y title as Figs 41 and 42. Two different quantities are drawn as s1 and s2, both solid as printed, with text in ink. | fig40.tex:9-19 | none |

## Verdict: pass (no must-fix)
