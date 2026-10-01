# v2 audit: ch2/fig33 (round 2)

Sources checked: figures/ch2/fig33.png (scan); figures/v2/ch2/fig33.pdf (rendered at 400 and 1200 dpi;
343.641 x 170.205 pt = 4.77 in wide, all five fonts embedded; PDF 17:53:33 is newer than fig33.tex 17:53:27 and
the CSVs); figures/v2/ch2/fig33.tex:1-54, fig33.py, fig33.calib.json, fig33-{cone,ogive,paraboloid,ellipsoid}.csv;
the round-1 report audit/v2-ch2-fig33-round1.md and the round-1 fix record; figures/v2/inventory.csv row ch2-fig33;
caption chapters/ch2-sec4.tex:226; citing text and eqs. (80a)-(80d) at ch2-sec4.tex:192-222; STYLE.md sections 13
and 16; tamrfig.sty (`cp mark`, `extension`, `centerline`); approved fig39.tex.

Round-1 finding checked:
- Round 1, item 1 (should-fix, centre line overprinting the outline): **resolved**. `\draw[centerline]` is now
  the first command in `\nose` (fig33.tex:17), ahead of the hidden axis that draws the outline and ahead of the
  base line. At 1200 dpi the tips of (a) and (b) are solid black to the apex, and the grey dash-dot shows only
  above the tip and inside the outline. All four base lines are unbroken black where the centre line crosses
  them. The C.P. labels (fill=white, drawn later in `\cpdim`) still knock out the centre line, as in the scan.
  The comments at fig33.tex:14-15 and 23 match the new order.

Regression checks (all pass):
- Data: fig33.py rerun in memory (nothing written) reproduces all four committed CSVs byte for byte. The outlines
  are exact at L/d = 2.4, and I spot-checked the ogive at z = 0.4557 L: rho = 2.5042 L gives r = 0.14848 L, and
  the CSV has 0.148474. `digitize.py overlay` on the scan, 95th percentile / max: cone 0.00/1.41 px, ogive
  0.00/1.00 px, paraboloid 2.00/3.00 px, ellipsoid 2.00/2.24 px. These are unchanged from round 1 and all within
  3 px.
- C.P. positions: `\cpdim` places the marks at 2/3, .466, 1/2 and 1/3 L from the tip (fig33.tex:36, 40, 44, 48),
  as eqs. (80a)-(80d) give them. The text's volume-over-base-area rule gives exactly 2/3, 1/2 and 1/3 L. For the
  tangent ogive it gives 0.4601 L at the drawn fineness, and .466 L is the rule's slender-body limit
  (1 - 8/15 = 0.4667). Keeping the printed .466 L is correct, because the lettering is printed.
- Lettering: 2/3 L, .466L, 1/2 L and 1/3 L are all present, with four C.P.$_n$ labels (the Fig 39 form), L on (d)
  only, and the italic (a)-(d) with Conical, Tangent ogive, Paraboloidal and Ellipsoidal, all on one baseline.
  Nothing is added. At 1200 dpi every C.P. label clears its outline. The tightest is (c), and even there the gap
  is visible.
- Size and style: the width of 4.77 in is unchanged. The scale is the same 1.16x as Figs 34 and 35. The dimension
  arrowheads are visible, and the station extension lines touch the C.P. mark, as the leaders do in Fig 39.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-1 should-fix 1 (drawing order of the centre line) is resolved. The only change since round 1 is that the one `\draw[centerline]` line moved. The outlines, marks, labels, width and fonts are unchanged. | fig33.tex:16-22 | None. |
| 2 | note | The printed ".466L" is the volume rule's slender-body limit. At the drawn L/d = 2.4 the rule gives 0.460 L, which is 0.2 mm different at this scale. The printed value is kept, as the invariants require. | fig33.tex:40; fig33.py docstring | None. |

## Verdict: pass (0 must-fix, 0 should-fix)
