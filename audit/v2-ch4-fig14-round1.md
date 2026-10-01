# v2 audit: ch4/fig14 (round 1)

Sources checked:
- Scan `figures/ch4/fig14.png`, read at 3x, with a crop of the curve-(c) corner.
- Redraw `figures/v2/ch4/fig14.pdf`:
  - 300 and 600 dpi renders, with a 600 dpi crop of the curve-(c) corner, and
    `build/v2/png/ch4-fig14-compare.png`;
  - a fresh compile in scratch (clean log, pixel-identical);
  - `pdffonts` (all embedded); no opacity operators or soft masks.
- Sources `fig14.tex`, `fig14.py` (the method in `fig10.py`), `fig14-a/b/c.csv`, `fig14-marks.csv` and
  `fig14.calib.json` (affine points plus `xgrid`).
- Inventory row `ch4-fig14` (`figures/v2/inventory.csv`:145).
- Text: `chapters/ch4-sec3.tex`:156-168 (F7, "power prang", times marked) and :215-224 (caption).
- `corrections/v2-figures.md` and STYLE.md section 16.

Checks made:
- **Data reproduce.** I reran `fig14.py` in a scratch copy of the tree. It reproduces all four CSVs byte for
  byte.
- **Overlay:** 95% of the points are within 0.00 px for (a), (b) and (c); the maximum is 1.0 px.
- **Calibration.** The `xgrid` handles the uneven x ticks: 96.5 px per 400 m at the left, 88.0 at the right
  (affine residual 4.0 px). The y axis leans only slightly against the x axis (about 0.2 deg), so the y-axis
  calibration points map to x = +1.2, -1.2, -3.8 and -6.2 m at y = 0-1200, at most 0.3 mm at final size.
- **Caption burnout points.** These are not drawn, but the curves pass close to them:
  - (a) is 6.2 m from (1050, 1079), 0.3 mm at final size;
  - (b) is 2.2 m from (696, 311).
- **Curve (c).** It strikes the ground under power at 199 m, and its foot is lettered 6.84, as the caption says.
- **Marks.**
  - Apex and impact of (a): (1558, 1354) and 2058 m.
  - Apex and impact of (b): (854, 324) and 1415 m.
  - Apex and impact of (c): (80, 41) and 199 m.
  - The printed leaders touch at the same places.
- **Lettering against the inventory.**
  - Titles $x$ (m) and $y$ (m); x ticks 0-2000 by 400; y ticks 0-1200 by 400.
  - The axes run to 2200 and 1400, half a step past the last ticks, because (a) lands at 2058 m and peaks at
    1354 m. This settles the inventory's "extend the axis or keep the overshoot".
  - Tags a, b, c.
  - Times 15.20 and 41.03 on (a), 10.40 and 20.01 on (b), 3.80 and 6.84 on (c), as printed (re-read at 3x).
  - Each leader runs in the printed direction: 15.20 below the apex, 41.03 from the left. The (c) tag stands
    beside the 3.80, as printed; `fig14.tex` documents this exception to the family's tag rule.
- **Caption and text.** The "power prang" of the heavy, high-drag case holds. All curves are continued to the
  ground, with the times marked.
- **House rules and family.** The template is identical to Figs 10-13:
  - axes 4.2 in wide, at an equal scale (4.2 in per 2200 m);
  - s1/s2/s3 solid with curve tags;
  - ink times on `leader` lines;
  - no local styles.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | must-fix | The time label "3.80" touches curve (b). On the 600 dpi render, the top of its "3" is 0.04 mm from the orange stroke near x = 210 m: column 620, stroke rows 114-116, label ink from row 117 of the crop. Every other label in Figs 10-14 clears the curves by at least 1.5 mm. The 31 deg, 6.5 mm leader puts the label in the narrow wedge under (b). In the scan the label sits lower and clears (b). | fig14.tex:36 (and the tag at :40) | Lower the leader to `\timemark{\Cax}{\Cay}{20}{6.5mm}{south west}{3.80}`. Move the tag right with it: in line 40, change `xshift=7.4mm` to `xshift=8.2mm` and keep the `(31:6.5mm)` base. I tested this on a scratch copy: "3.80" then clears (b) by 1.25 mm, the tag clears "3.80" by 1.2 mm and (b) by 2.6 mm, and the tag stays 0.47 mm above "6.84", as it is now. |
| 2 | note | The (c) tag sits only 0.47 mm above the "6.84" label (they overlap horizontally). This is legible, and the printed arrangement is the same, but it is the tightest clearance in the family. | fig14.tex:40 | Optional: raise the tag about 0.5 mm (`yshift=0.5mm`) when making fix 1. |
| 3 | note | The family handles the scan's leaning y axis two ways: affine in Figs 10 and 12 follows the lean, and `xgrid` in Figs 13 and 14 ignores it. Here the lean is small (at most 6.2 m, 0.3 mm), and an affine reading would differ by up to 27.5 m (1.3 mm) on (a) and 17.9 m (0.9 mm) on (b), mostly from averaging the uneven ticks. So `xgrid` is the better reading for Fig 14. The family-wide choice is raised as should-fix in the Fig 10, 12 and 13 reports. | fig14.calib.json | Include Fig 14 in the family's recorded convention. |
| 4 | note | The burnout points are not marked, as printed (an editorial option in the inventory). | - | none |

## Verdict

fix (1 must-fix: the 3.80 label touching curve (b); 0 should-fix)
