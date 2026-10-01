# v2 audit: ch4/fig14 (round 2)

Sources checked:
- Scan `figures/ch4/fig14.png`, read at 2x and 4x (the corner of curve (c)).
- Redraw `figures/v2/ch4/fig14.pdf`:
  - 200 and 600 dpi renders, with a 600 dpi crop of the (c) corner;
  - a fresh compile in a scratch tree (pixel-identical);
  - `pdffonts` (all embedded); no transparency.
- Sources `fig14.py`, `fig10.py`, `fig14-a/b/c.csv`, `fig14-marks.csv` and `fig14.calib.json`.
- Inventory row `ch4-fig14` (`figures/v2/inventory.csv`:145).
- Caption `chapters/ch4-sec3.tex`:215-224 and the text at :156-168 ("power prang").
- Round-1 report and fix notes, and `fix1/orig/fig14.tex`.

Checks made:
- **Round-1 must-fix ("3.80" touching curve (b)): resolved.** The leader is now at 15 deg (fig14.tex:38), and the
  tag moves with it (fig14.tex:44). Measured on 600 dpi element-masked renders:
  - "3.80" to the nearest curve ((b)): 1.76 mm. It was 0.04 mm.
  - "3.80" to the (c) tag: 1.50 mm.
  - "3.80" to "6.84": 2.14 mm.
  - "3.80" to the 6.84 leader: 2.83 mm.
  - The (c) tag to curve (b): 2.12 mm.
  - The (c) tag to "6.84": 0.97 mm. It was 0.47 mm, so round-1 note 2's optional raise is done.

  The fixer chose 15 deg rather than the tested 20 deg, and said why: 1.78 mm instead of 1.25 mm from (b). That is
  sound.
- **Convention.**
  - fig14.calib.json adds `lean` (a skew of 0.17 deg) to its `xgrid` (96.5 down to 88.0 px per 400 m). Its note
    records that (a) runs past the 2000 tick.
  - The tick points map back within 1.25 m (x) and 2.2 m (y).
  - At this skew the zeros' shear (+0.0059) cannot separate a skewed scan from a rotated one (+0.0042). The lean
    is small either way: the curves moved at most 0.45 mm.
- **Data reproduce.** The rerun reproduces the CSVs byte for byte (also with the tool's lean patch).
- **Overlay.**
  - Frame mapping (fig14.py's check; patched tool): 95% within 0.00 px for all three curves, max 1.0.
  - Stock tool: 1.00, 0.00 and 0.00 px.
- **Caption burnout points**, distance to the densified curves: (a) 1.2 m (0.06 mm); (b) 2.0 m (0.09 mm).
- **Curve (c).** It strikes the ground under power at 198.6 m, and the foot is lettered 6.84, as the caption says.
- **Marks.** Apex (a) (1566.5, 1354.1), impact 2057.6 m; apex (b) (856.5, 324.1), impact 1414.5 m; apex (c)
  (80.0, 41.2). These agree with the printed leader feet (about (1563, 1345) and (858, 335) just off the curves).
- **Lettering.** All present:
  - titles; x ticks 0-2000 by 400 (axis to 2200); y ticks 0-1200 by 400 (axis to 1400);
  - tags a, b, c;
  - the times 15.20, 41.03, 10.40, 20.01, 3.80 and 6.84. 15.20 hangs below the apex and 41.03 is set to the left,
    as printed.
- **Legibility.** Away from the (c) corner:
  - Labels to curves: at least 4.28 mm.
  - The (a) and (b) tags to their curves: 0.56-0.58 mm.
- **Regression check.** Only the (c) group moved. The (a) and (b) tag centres are within 7 m (0.35 mm) of round 1.
- **House rules and family.** The template is identical (4.2 in axes, 4.2 in/2200 m, s1-s3 solid, `curve tag`,
  `leader`). The (c) tag's placement in the .tex is a documented exception (the curve is too small to carry it).
  Flat art.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The (c) tag now stands up and to the right of "3.80" (2.17 mm above its anchor), over "6.84". In the print it stands beside "3.80" on the same line. It still reads as belonging to the (c) labels: it is closest to "3.80" (1.50 mm) and "6.84" (0.97 mm), with curve (b) 2.1 mm above it, as in the print. | fig14.tex:44 | none |
| 2 | note | Recording the frame convention (Fig 10 report, finding 2) and the overlay tool's lean support (Fig 12 report, finding 1) are open for the orchestrator. This figure passes the stock tool. | corrections/v2-figures.md; tools/v2/digitize.py | as in Figs 10 and 12 |
| 3 | note | The burnout points are not marked, as printed. | - | none |

## Verdict

pass (0 must-fix, 0 should-fix; the round-1 must-fix is resolved)
