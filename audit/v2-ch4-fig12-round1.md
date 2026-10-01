# v2 audit: ch4/fig12 (round 1)

Sources checked:
- Scan `figures/ch4/fig12.png`, read at 3x, with crops of the apex of (a) and of the origin.
- Redraw `figures/v2/ch4/fig12.pdf`:
  - 300 and 600 dpi renders and `build/v2/png/ch4-fig12-compare.png`;
  - a fresh compile in scratch (clean log, pixel-identical);
  - `pdffonts` (all embedded); no opacity operators or soft masks.
- Sources `fig12.tex`, `fig12.py` (the method in `fig10.py`), `fig12-a/b/c.csv`, `fig12-marks.csv` and
  `fig12.calib.json`.
- Inventory row `ch4-fig12` (`figures/v2/inventory.csv`:143).
- Text: `chapters/ch4-sec3.tex`:139-168 and :195-202 (caption).
- `corrections/v2-figures.md` (Ch4 Figs 5, 7-10, 12-14 digitized: no D4 engine model in the book) and STYLE.md
  section 16.

Checks made:
- **Data reproduce.** I reran `fig12.py` in a scratch copy of the tree. It reproduces all four CSVs byte for
  byte.
- **Overlay** (calibration residual 0.66 px; the x ticks are even, 95.5, 94, 94 and 95.5 px per 200 m): 95% of
  the points are within 0.00, 0.00 and 1.00 px for (a), (b) and (c); the maximum is 1.0 px.
- **Apex of (a).** At 3x the scan's flattened top and sharp shoulder near x = 500-520 m are the printed shape, and
  the trace follows them. They are not a digitizing artifact.
- **Caption burnout points.** These are not drawn, but the curves pass close to them:
  - (a) is 2.8 m from (236, 342);
  - (b) is 0.8 m from (133, 160);
  - (c) is 0.9 m from (57, 38).
  All three are under 0.4 mm at final size.
- **Marks.**
  - Apex and impact of (a): (493, 609) and 566 m.
  - Apex and impact of (b): (357, 304) and 559 m.
  - Apex and impact of (c): (69, 40) and 116 m.
  - The 16.86 and 24.48 leaders start from impacts 7.4 m (1 mm) apart and go left and right, as printed.
- **Lettering against the inventory.**
  - Titles $x$ (m) and $y$ (m); x ticks 0-800 by 200; y ticks 0-600 by 200. The axis runs to 700, half a step
    past 600, because (a) peaks at 609.
  - Tags a, b, c.
  - Times 8.20 and 24.48 on (a), 7.60 and 16.86 on (b), 3.50 and 7.07 on (c), as printed (re-read at 3x). Each
    leader runs in the printed direction.
- **Caption and text.** The times are marked at the apex and impact, and the curves are continued to the ground.
- **Legibility.** Every time label is at least 1.9 mm from every curve, and the tags clear their curves by
  0.6 mm.
- **House rules and family.** The template is identical to Figs 10, 11, 13 and 14:
  - axes 4.2 in wide, at an equal 0.00525 in/m;
  - s1/s2/s3 solid with curve tags;
  - ink times on `leader` lines;
  - no local styles.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The family handles the scan's leaning y axis two ways. Fig 12 uses the affine fit, which follows the lean. The printed y axis leans 5 px right over its height: col 96.4 at the x axis, 101.4 at y = 600. The x axis tilts only 1.4 px over 380 px, so the frame is skewed by about 0.8 deg. Figs 13 and 14 use the column-only `xgrid`, which ignores the lean. Reading the same ink with an `xgrid` from Fig 12's ticks moves the apex region of (a) by 12.5 m (1.7 mm at final size) and the top of (b) by 5.9 m (0.8 mm). The captions' burnout points do not decide between the two readings (2.8 against 2.1 m for (a)). | fig12.calib.json | One convention for Figs 10, 12, 13 and 14 (all `xgrid` or all affine), recorded with its size in corrections/v2-figures.md. Fig 12's even ticks make the affine reading natural here, so the question is only the lean. |
| 2 | note | Curve (c) leaves the shared launch line about 5 scan px (1.6 mm) from the origin. The faired trace separates within about 0.6 mm, which cannot be seen at final size. | fig12-c.csv | none |
| 3 | note | The burnout points are not marked, as printed (an editorial option in the inventory). | - | none |

## Verdict

pass (0 must-fix, 1 should-fix)
