# v2 audit: ch3/fig51 (round 2)

Sources checked: scan `figures/ch3/fig51.png` (inset and region markers zoomed 4x); redraw
`figures/v2/ch3/fig51.tex` (dated 22:14, after the round-1 fix), `fig51.py`, `fig51.csv` (21:59, unchanged since
round 1), `fig51.calib.json`, `figures/v2/ch3/fig51.pdf` rendered at 400 dpi (whole figure) and at 1200 dpi (the
four curve labels and the inset patch's right-hand edge); `build/v2/png/ch3-fig51.png`; inventory row ch3-fig51;
caption and citing text `chapters/ch3-sec6c.tex` lines 238-411; the round-1 audit and the fix report; STYLE.md
sections 14 and 16; `pdffonts` (all fonts embedded); page 443.0 x 292.6 pt = 6.15 in wide.

Round-1 follow-up:
- Should-fix 1 (no knock-out behind the curve labels) is **resolved**. `curve label` now has `fill=white` (line 23).
  At 1200 dpi the 1.5 ruling stops at $(\CDo)_F$ and $(\CDo)_{FB}$, and the vertical rulings stop at all four
  labels. No box clips a curve. The $(\CDo)_F$ box clears the s3 dashes. The $(\CDo)_B$ box clears the s2 curve
  below it and the s3 curve to its right. The $C_{Db}$ box clears its own curve by about 0.5 mm.
- Should-fix 2 (the $(\CDo)_{FB}$ label sat on its own curve) is **resolved**. The anchor is now (4.9e4, 1.5). At
  1200 dpi the box clears the solid curve by about 1.4 mm at its lower left, and it ends well left of the inset
  patch.
- Note 3 (the patch half-covered the 1e7 ruling) is **resolved**. The patch is set in by 0.2 pt on all four sides,
  which is at least half the width of both the 0.4 pt major and the 0.3 pt minor rulings. At 1200 dpi the 1e7,
  1.0, 1.5 and 1.5e5 rulings keep their full weight, with no gridline stubs at the corners.
- No regression: the curves, axes, region markers and inset are unchanged.

Independent checks (repeated):
- I recomputed the curves with my own code from the printed GCR-x equations ((C_Df)_b = 82.8 (C_f)_B,
  C_Db = .0149/sqrt, (C_Do)_F = 46.4 (C_f)_F, switches at 5e5 (B = 1735) and 5.14e6). They match fig51.csv to
  1.1e-5. Check values: 1e4 gives 0.0142 / 1.114 / 1.972 / 3.086; 5e5 gives 0.473; 2e6 gives 0.433; 5e6 gives
  0.369; 1e7 gives 0.396 (Table 6: 3.080 off the plot, then 0.473, 0.432, 0.370, 0.396).
- Overlay (`digitize.py overlay`, the drafter's calibration on the drawn gridlines; I wrote the overlay CSVs from
  fig51.csv in scratch and did not rerun fig51.py), 95th percentile: C_Db 2.00 px, (C_Do)_B 2.24 px, (C_Do)_F
  3.00 px, (C_Do)_FB 2.00 px. All four are within the 3 px target.
- The text's claims hold on the redraw. (C_Do)_FB is 3.08 at 1e4 (off the plot). It is nearly flat in region (2).
  (C_Do)_B rises from 5e5 to about 2e6 and then falls. C_Db peaks at 5e5 and is about 7% of the total in
  regions (2) and (3). The circled 2 and 3 use `curve tag`.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-1 should-fix 1 and 2 and note 3 are verified fixed at 1200 dpi. Each label box is white and clears every curve, and the patch keeps its four bounding rulings at full weight. | fig51.tex lines 23, 36-37, 45 | none |
| 2 | note | The 1973 art blanks the grid in a band behind the region-marker bars. The redraw knocks out only the circled tags (white `curve tag`). The bar at 0.65 runs midway between the 0.6 and 0.7 rulings and reads clearly, so this is a modern simplification, not a loss of content. | lines 49-55 | none |
| 3 | note | Round-1 notes 4 (four series in three colours, each labelled directly) and 5 (region (3) starts at 5e6 per the caption, kink at 5.14e6, D35) still stand. | | none |

## Verdict: pass (no must-fix)
