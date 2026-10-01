# v2 audit: ch2/fig46 (round 1)

Sources checked: scan crop `figures/ch2/fig46.png` (panels zoomed x2-x5); inventory row `ch2-fig46`; caption
and citing text `chapters/ch2-sec5.tex:277-313` (points marked with a small x, a smooth curve, a straightedge
tangent at the origin, $C_1$ = moment / deflection of a point on the line); redraw `figures/v2/ch2/fig46.tex`,
`fig46.py`, `fig46.csv`, `fig46-points.csv` and `fig46.calib.json`; the PDF (rebuilt with `make fig F=ch2/fig46`:
4.40 x 6.72 in, all fonts embedded), the compare render and a 400 dpi render. I re-ran `fig46.py` in memory with
no files written: it reproduces both CSVs byte for byte. Also checked: `tools/v2/digitize.py overlay` on panels (b)
and (c), STYLE.md sections 8, 13 and 16, and `corrections/v2-figures.md`.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Panel (a) has all 11 rows exactly as printed (0.0/.0000 ... 8.125/.2315), with the heads "Moment ($10^5$ dyn-cm)" and "Deflection angle (rad)". It is set with booktabs and S columns (STYLE section 8). The angles keep the printed form without a leading zero; the leading-zero rule applies to tick labels only. | fig46.tex:31-47 | none |
| 2 | note | Panels (b) and (c) have y ticks 0, 5, 10, x ticks 0.0-0.3 (in (c) the 0.0 label is hidden under the straightedge, as printed), axis titles as printed and 10 x marks (none at the origin), all at the table's values. The redraw keeps the inventory's two deviations: (0.1610, 6.875) lies below the curve and (0.2315, 8.125) above its end. | fig46.tex:19-28, 74-76 | none |
| 3 | note | Overlays on the scan. Faired curve on panel (b): 95% within 0.00 px, maximum 1.00 px. The curve beyond the straightedge in panel (c) (x > 0.16): 95% within 1.00 px. The computed line $y = 50x$ on the scan's dash-dot line: 95% within 1.41 px. So $C_1 = 5\times10^6$ dyn-cm matches the printed line. The curve is flattened to zero slope over its last 0.014 rad (`maximum.accumulate`). This agrees with the text (instability where the slope reaches zero; Fig 7). | fig46.py:89-91 | none |
| 4 | note | The faired curve's slope at the origin is 46.5 (spline derivative; 46.8 from the CSV), against 50 for the linear-approximation line. So, strictly, the line is not tangent at the origin. The curve lies up to 0.046 units below the line near 0.03 rad and up to 0.026 above it at 0.08-0.10 rad. That is about 0.2 mm at final size, narrower than the 1pt curve, and in (c) this part is hidden under the straightedge. Nothing visible depends on it. | fig46.py:80-87; fig46.csv rows 2-30 | Optional, only if the curve is regenerated: pin the spline's slope at the origin to 50, e.g. with weighted points on $y = 50x$ for $x < 0.01$. |
| 5 | note | In (c) the construction is correct. Dashed guides run from (0, 5) to (0.1, 5) on the straightedge's edge and down to (0.1, 0). The opaque straightedge hides the vertical guide where they cross, and it reappears below. The dash-dot line starts exactly at the straightedge's end: computed 270.3 px along the edge, against the 270.5 px straightedge. The point at 0.161 straddles the straightedge's end; the scan shows it half hidden there. The $C_1$ formula is typeset and clears the guide and the straightedge. | fig46.tex:49-81 | none |
| 6 | note | Colours and styles: the faired curve is `s1` solid in both panels; the linear approximation is `s2` with the printed dash-dot kept; marks and text are in ink. The panel letters (b) and (c) sit at the upper right inside the axes, and (a) at the lower right of the table. The scan's double rules between panels are replaced by whitespace (modern restyle). Nothing is clipped or overlapping at 400 dpi. | fig46.tex | none |

## Verdict: pass
