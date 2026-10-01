# v2 audit: ch3/fig23 (consistency fix, verification)

Sources checked:
- The 1973 scan `figures/ch3/fig23.png`, with a 6x crop of the profile box at B.
- The redraw `figures/v2/ch3/fig23.pdf`, built 23:16:00, after the tex (23:15:58), so it is current.
  - Renders: 300 dpi whole; 900 dpi crop of the box at B, the B tag and the hatch around it.
  - `pdfinfo`: 344.2 x 142.1 pt (4.78 x 1.97 in), the same as round 2.
  - `pdffonts`: all fonts embedded.
- `build/v2/png/ch3-fig23-compare.png`.
- Sources: `figures/v2/ch3/fig23.tex`, and the dates of `fig23.py` (22:19) and `fig23-*.csv` (22:21). Both are older than the round-1 audit, so the data did not change.
- The round-1 and round-2 audits, the consistency issue and the fixer's report.
- Inventory row `ch3-fig23`.
- The family references: Ch3 Figs 16, 17, 18, 25 (`.tex` styles, and a 200 dpi render of 16, 18, 25 side by side).
- `STYLE.md` s.16; `tamrfig.sty` (dated 21:33, unchanged).

## Consistency issue: velocity-profile convention

The issue: the profile box at B was drawn in ink with headless ink hairlines. The family (Figs 06, 09, 16, 17,
18, 25) draws profiles in s1. **Resolved.**

- **Styles.** fig23.tex:21-26 carries `profile`, `profile arrow` and `profile stroke` exactly as in fig16.tex:12-16. The comment names the family.
- **Profile curve.** The Blasius u(y) (fig23-profile.csv) is drawn as `profile` (s1, 1pt, round join) at fig23.tex:62-63.
- **Velocity lines.** They are headless, as printed, and drawn as `profile stroke` (s1, 0.5pt) at :59-61. At 900 dpi they are clearly thinner than the 1pt profile and run from the base line to the curve.
- **Ink parts.** The base line (the wall normal at B, :64) and the cylinder are ink 0.6pt, as in Fig 18.
- **Drawing order.** White fill, then the strokes, then the profile, then the base line. The base line lies over the strokes' left ends. The profile lies over their right ends.

### The fixer's departure from the suggestion

The suggestion said to keep "Fig 23's box sides" in ink. The fixer drew two parts of the box in s1 instead. **Accepted.**
- **Right side.** Above the layer edge it is drawn in s1. It is the profile at u = U_inf.
  - The approved family carries the profile straight up in s1 above delta. Figs 16, 18 and 25 do this, and Fig 17's U_inf references are `profile` too (fig17.tex:51).
  - An ink right side would split one physical curve into two colours.
- **Top line.** It is drawn as `profile stroke`. It is the top velocity line, and has the same length U_inf as the lines below it, so the stroke style is correct.
- **Only true edges stay ink.** The base line is the profile's y-axis and the cylinder is the wall. Ink for those two matches the rule in Fig 18.
- **Effect.** Side by side with Figs 16, 18 and 25, the Fig 23 profile now reads as the same kind of object: a blue profile and blue lines on an ink base.

## Regression check against the scan, the inventory and the earlier audits

- **Box.** It is unchanged against the scan: a box standing on the wall normal at B, its lines filling it, and the profile curving into the wall at B.
  - Hatching shows to the right of the curve below the layer edge, as printed (6x scan crop).
  - The streamlines stop at the base line and at the right side, as printed.
- **Geometry.** Unchanged: the box is 0.44 a wide and its top is at 2.05 a. The CSVs have not changed since round 1.
- **Earlier audits.**
  - The round-2 arrow fix (the separated-layer arrows from beside S, fig23.tex:53) is intact.
  - The eddy arrows, the A, B, C, S tags and points, the cross-hair and $U_\infty$ in its gap are all unchanged.
  - The round-1/2 streamline overlay figures stand: the data did not change.
- **Inventory lettering.** $U_\infty$, A, B, C and S are all present. The inventory's "horizontal hatch lines" in the profile are the velocity lines.
- **Style.** Flat colour, no transparency. Text and tags stay ink. No kit style is redefined: `streamline`, `flow arrow` and `eddy` are local names, and `profile*` are not in the kit.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The issue is resolved. The profile, velocity lines and base line now follow the family convention (Figs 16, 17, 18, 25), and nothing else regressed. | fig23.tex:21-26, 56-64 | None. |
| 2 | note | The box's right side above delta and its top line are s1, not ink as the suggestion said. They are the profile at U_inf and the top velocity line, drawn as the family draws them (Figs 17, 18, 25). This departure is justified. | fig23.tex:61-63 | None. |
| 3 | note | Kit: ten Ch3 figures now carry identical local copies of `profile`, `profile arrow` and `profile stroke` (Figs 06, 09, 10, 13, 16, 17, 18, 23, 25, 33). Fig 21 has a separate pgfplots axis style also named `profile`, a different key path, so the two do not collide. | fig23.tex:21-26 | For the orchestrator: move the three TikZ styles into `tamrfig.sty`. If that is done, consider renaming Fig 21's axis style so the name means one thing. |

## Verdict: pass

No must-fix and no should-fix.
