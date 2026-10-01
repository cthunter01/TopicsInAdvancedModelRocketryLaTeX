# v2 audit: ch3/fig16 (round 2)

Sources checked: the scan `figures/ch3/fig16.png`; the redraw `figures/v2/ch3/fig16.pdf` (current by `make -q`;
324.9 x 148.3 pt = 4.51 x 2.06 in; fonts all embedded), rendered at 400 dpi, with the element, ds and phi region
at 900 dpi; `build/v2/png/ch3-fig16-compare.png`; `figures/v2/ch3/fig16.tex`, `fig16.py`, `fig16-*.csv` and
`fig16.calib.json`; the inventory row `ch3-fig16`; the caption and eq. (58) text in `chapters/ch3-sec3a.tex`:554-576;
the kit styles in `figures/v2/tamrfig.sty`; the round-1 report and the fix notes. Round 1 passed with no
must-fix or should-fix items. The fix round changed nothing: fig16.tex and its CSVs predate the round-1 report.

Checks made:
- **Overlay**, run myself: body 95% within 2.00 px (max 3.16), Blasius profile 1.00 px (max 1.41). These are
  the same as round 1.
- **Geometry at 900 dpi.** The dashed tangent from V to the element lies outside the convex nose and touches it
  only at P, so it is the true tangent (standing rule 4, phi = 22.5 deg). tau_o runs on along the same line. The
  profile's base line is normal to the surface, and its arrows are parallel to the tangent. The two
  `angle arc single` arrows come from outside onto the tangent and the axis, with phi between them.
- **Lettering and meaning.** U(x), u(y), $\tau_o$, ds, $\phi$, $U_\infty$ and x are all present. Eq. (58)'s b
  and ell are not lettered, as in 1973. Nothing is added.
- **Style.** All styles are kit styles (`thin line`, `outline`, `thin vec`, `guide`, `centerline`, `hatch`,
  `angle arc single`, `\dimline`), apart from the family's three profile styles, which are identical in Figs 16,
  17, 18 and 25. The labels are `\small` (every picture). Nothing overlaps or is clipped.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note (gate) | Carried from round 1: phi is 22.5 deg on the true tangent, against about 21 deg in 1973. There is still no entry in `corrections/v2-figures.md`. | fig16.tex:4; fig16.py:12-14 | orchestrator: log under "Minor (logged only)" |
| 2 | note | No regressions: the file is unchanged since round 1, the overlay numbers are the same, and the PDF is up to date. | -- | none |

## Verdict: pass (no must-fix)
