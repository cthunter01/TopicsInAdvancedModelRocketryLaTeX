# v2 audit: ch4/fig13 (round 1)

Sources checked:
- Scan `figures/ch4/fig13.png`, read at 3x, with a crop of the overlay around the apexes.
- Redraw `figures/v2/ch4/fig13.pdf`:
  - 300 and 600 dpi renders and `build/v2/png/ch4-fig13-compare.png`;
  - a fresh compile in scratch (clean log, pixel-identical);
  - `pdffonts` (all embedded); no opacity operators or soft masks.
- Sources `fig13.tex`, `fig13.py` (the method in `fig10.py`), `fig13-a/b/c.csv`, `fig13-marks.csv` and
  `fig13.calib.json` (affine points plus `xgrid`).
- `tools/v2/digitize.py` (`Axes`: `xgrid` replaces the x mapping by column alone).
- Inventory row `ch4-fig13` (`figures/v2/inventory.csv`:144).
- Text: `chapters/ch4-sec3.tex`:139-168 and :205-212 (caption).
- `corrections/v2-figures.md` and STYLE.md section 16.

Checks made:
- **Data reproduce.** I reran `fig13.py` in a scratch copy of the tree. It reproduces all four CSVs byte for
  byte.
- **Overlay:** 95% of the points are within 0.00 px for (a), (b) and (c); the maximum is 1.0 px.
- **Bends in (b).** The slight bends in (b) near (400, 520) and (620, 490) reproduce the 1973 curve-joins; the
  overlay crop shows them in the ink.
- **Caption burnout points.** These are not drawn, but the curves pass close to them:
  - (a) is 2.3 m from (61, 103);
  - (b) is 1.9 m from (28, 47);
  - (c) is 0.9 m from (13, 21).
  All three are about 0.2 mm or less at final size.
- **Marks.**
  - Apex and impact of (a): (623, 831) and 925 m.
  - Apex and impact of (b): (485, 574) and 788 m.
  - Apex and impact of (c): (91, 102) and 136 m.
  - The printed apex leaders touch at the same places.
- **Lettering against the inventory.**
  - Titles $x$ (m) and $y$ (m); x ticks 0-1200 by 200; y ticks 0-800 by 200. The axis runs to 900 because (a)
    peaks at 831.
  - Tags a, b, c.
  - Times 9.40 and 26.47 on (a), 9.00 and 21.84 on (b), 3.80 and 9.40 on (c). The label 9.40 appears twice, as
    printed (re-read at 3x). Each leader runs in the printed direction: 9.40 and 9.00 below their apexes, 21.84
    from the left.
- **Caption and text.** The times are marked at the apex and impact, and the curves are continued to the ground.
- **Legibility.** Every time label is at least 1.8 mm from every curve, and the tags clear their curves by
  0.6 mm.
- **House rules and family.** The template is identical to Figs 10-12 and 14:
  - axes 4.2 in wide, at an equal 0.0035 in/m;
  - s1/s2/s3 solid with curve tags;
  - ink times on `leader` lines;
  - no local styles.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The `xgrid` calibration ignores the lean of the printed y axis, which Figs 10 and 12 (affine) follow. The x ticks are uneven (76.8 px per 200 m at the left, 70.1 at the right; affine residual 3.4 px), so `xgrid` handles the spacing. But `xgrid` maps x by column alone. The y axis leans 3.8 px left over its height (col 103.6 at the x axis, 99.9 at y = 800), while the x axis is level, a skew of about 0.75 deg. The y-axis calibration points therefore map to x = -2.1, -4.6, -7.0 and -9.5 m at y = 200-800. An affine reading of the same ink puts the apex region of (a) 25 m (2.2 mm at final size) and the top of (b) 20 m (1.8 mm) further right. The burnout points do not decide between the two readings (2.3 m for (a) either way). | fig13.calib.json | One convention for Figs 10, 12, 13 and 14 (all `xgrid` or all affine), recorded with its size (up to about 2 mm at the apexes) in corrections/v2-figures.md. If `xgrid` stays, say in the calibration note that the y-axis lean is ignored. |
| 2 | note | The calibration note says the `xgrid` is "extended by one tick spacing at both ends ... since curve (a) runs past the last labelled tick". In Fig 13, (a) lands at 925 m, short of the 1200 tick. The extension is harmless but unused; the reason given is true of Fig 14, not of Fig 13. | fig13.calib.json "note" | Drop the clause, or say the extension is a safeguard. |
| 3 | note | The burnout points are not marked, as printed (an editorial option in the inventory). | - | none |

## Verdict

pass (0 must-fix, 1 should-fix)
