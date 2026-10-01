# v2 audit: ch4/fig10 (round 1)

Sources checked:
- Scan `figures/ch4/fig10.png`, read at 3x, with crops of the origin and of the ascending branches.
- Redraw `figures/v2/ch4/fig10.pdf`:
  - 300 and 600 dpi renders and `build/v2/png/ch4-fig10-compare.png`;
  - a fresh compile in scratch (clean log, pixel-identical to the committed PDF);
  - `pdffonts` (all embedded) and a scan for opacity operators or soft masks (none).
- Sources `fig10.tex`, `fig10.py` (the digitizing method shared with Figs 12-14), `fig10-a/b/c.csv`,
  `fig10-marks.csv` and `fig10.calib.json`.
- Inventory row `ch4-fig10` (`figures/v2/inventory.csv`:141).
- Text: `chapters/ch4-sec3.tex`:131-168 (method, cases, "Times in seconds from launch have been marked on the
  curves"), :173-184 (caption) and :276-291 (shape above burnout, "humped over").
- `corrections/v2-figures.md` (Ch4 Figs 5, 7-10, 12-14 digitized) and STYLE.md sections 15 and 16.

Checks made:
- **Data reproduce.** I reran `fig10.py` in a scratch copy of the tree. It reproduces all four CSVs byte for
  byte.
- **Overlay** (`digitize.py overlay`, calibration residual 1.94 px): 95% of the points are within 0.00, 0.00 and
  0.20 px of the ink for (a), (b) and (c); the maximum is 1.0 px. This is expected for a trace (a round trip).
- **Caption burnout points.** These are not drawn and not used, but the digitized curves pass close to them:
  - (a) is 1.8 m from (23, 40);
  - (b) is 0.2 m from (9, 15);
  - (c) is 1.2 m from (3, 5).
  All three are under 0.35 mm at final size.
- **Marks.** Each apex leader starts at the curve's highest point and each impact leader at its foot:
  - (a): (321, 403) and 466 m;
  - (b): (196, 201) and 327 m;
  - (c): (26, 27) and 49 m.
  These match the inventory's readings and the points where the printed leaders touch.
- **Lettering against the inventory.**
  - Titles $x$ (m) and $y$ (m); x ticks 0-600 by 100; y ticks 0-400 by 100.
  - Curve tags a, b, c (`curve tag`).
  - Times 6.80 and 18.25 on (a), 5.80 and 12.90 on (b), 2.40 and 4.90 on (c), as printed (re-read on the 3x
    scan). Each leader runs in the printed direction.
- **Caption and text.** The caption says the apex and impact times are marked on the curves, and they are. All
  three curves are continued to the ground.
- **Legibility.** On the 600 dpi render, every time label is at least 1.8 mm from every curve, and the tags clear
  their curves by 0.6 mm (the family's tag offset).
- **House rules and family.**
  - `tamr` open axes, 4.2 in wide, equal x and y scale (0.007 in/m); the y axis runs to 450, half a step past 400,
    because (a) peaks at 403.
  - s1/s2/s3 solid at 1pt; aqua carries its tag.
  - Times in ink at `\footnotesize` on straight `leader` lines; no local styles.
  - The macros (`\getmark`, `\timemark`), sizes and placements are identical to those of Figs 11-14.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The family handles the scan's leaning y axis two ways, and the choice moves the curves by up to 1.9 mm here. Fig 10 (like Fig 12) uses the affine fit, which follows the lean. The 1973 frame is skewed by about 1.3 deg: the y axis leans 4.5 px left over 280 px of height, while the x axis falls only 2.7 px over 425 px. The x ticks are also uneven (73.0, 71.8, 70.5, 70.0, 69.7, 70.0 px per 100 m; affine residual 1.9 px = 2.7 m). Figs 13 and 14 switch to the column-only `xgrid` for the same unevenness, and that ignores the lean. Mapping the same ink with an `xgrid` built from Fig 10's ticks moves the apex of (a) by 10.8 m (1.9 mm at final size) and that of (b) by 7.0 m (1.25 mm). Neither the captions' burnout points (both readings within 1.8 m) nor the text decides which reading is right. | fig10.calib.json; fig10.py SPEC | Use one convention for Figs 10, 12, 13 and 14: either `xgrid` for all four, or the affine fit for all four. Record the choice and its size (up to about 2 mm at the apexes) in corrections/v2-figures.md under the Ch4 digitized trajectories. |
| 2 | note | Over y = 10-60 m the digitized (b) lies up to 1 m left of (a) and crosses it at about 80 m. Physically (b) should not lie left of (a), but 1 m is 0.18 mm here, inside the 1pt stroke, and the two printed lines coincide there. | fig10-a/b.csv | none |
| 3 | note | The burnout points (x_b, y_b) are not marked, as printed. The inventory lists burnout dots as an editorial option. | - | none (owner's option) |

## Verdict

pass (0 must-fix, 1 should-fix)
