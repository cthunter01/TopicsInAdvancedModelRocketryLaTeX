# v2 audit: ch4/fig12 (round 2)

Sources checked:
- Scan `figures/ch4/fig12.png`, read at 2x.
- Redraw `figures/v2/ch4/fig12.pdf`:
  - 200 and 600 dpi renders;
  - a fresh compile in a scratch tree (pixel-identical);
  - `pdffonts` (all embedded); no transparency.
- Sources `fig12.py`, `fig10.py` (the method), `fig12-a/b/c.csv`, `fig12-marks.csv` and `fig12.calib.json`.
- `tools/v2/digitize.py` (`Axes`), and the fixer's patch `fix1/tooltest/lean.patch`.
- Inventory row `ch4-fig12` (`figures/v2/inventory.csv`:143).
- Caption `chapters/ch4-sec3.tex`:195-202.
- Round-1 report and fix notes, and `fix1/orig/`.

Checks made:
- **Round-1 should-fix (the convention): resolved in the figure files.**
  - fig12.calib.json carries `xgrid` (even ticks, 95.5/94/94/95.5 px per 200 m) and `lean`. Its note records the
    0.83 deg skew.
  - The tick points map back within 1.9 m (x) and 1.1 m (y).
  - My independent shear measurement of the zeros (-0.0172 ± 0.0031 against the axis's -0.0199; upright lettering
    would give -0.0028) confirms that the lettering shares the skew (table in the Fig 10 report).
- **Data reproduce.** The rerun reproduces the CSVs byte for byte, with or without the lean patch applied to the
  tool.
- **Overlay.**
  - Frame mapping (fig12.py's check, and `digitize.py overlay` with the lean patch in scratch): 95% within 0.00,
    0.00 and 1.00 px, max 1.0. The patched overlay image puts all three curves on the ink.
  - **Stock `digitize.py overlay`:** (a) 95% 3.54 px, max 4.0, **MISMATCH**; (b) 1.00; (c) 1.00. The stock tool
    reads `xgrid` by column alone and ignores `lean`, so this is the lean (5 px over the axis height), not a trace
    error (finding 1).
- **Caption burnout points**, distance to the densified curves: (a) 3.0 m (0.40 mm); (b) 0.3 m; (c) 0.8 m.
- **Marks.**
  - Apex (a) (496.8, 609.8), impact 567.3 m; apex (b) (359.7, 303.7), impact 560.0 m; apex (c) (69.0, 40.2),
    impact 116.1 m.
  - The printed 8.20 leader leaves the flat top of (a) a little further right (its foot, just off the curve, reads
    (511, 621)). The mark is the highest digitized point of a top that is flat to about ±10 m (finding 2).
  - The 16.86 (left) and 24.48 (right) leaders fan out from impacts 7.3 m apart, as printed.
- **Lettering.** All present: titles; x ticks 0-800 by 200; y ticks 0-600 by 200 (axis to 700); tags a, b, c;
  the times 8.20, 24.48, 7.60, 16.86, 3.50, 7.07.
- **Legibility** (600 dpi, masked renders):
  - Labels to curves: at least 3.97 mm.
  - Tags to curves: 0.56-0.60 mm. Tags to leaders: at least 1.98 mm.
  - Labels to labels: at least 6.5 mm.
- **Regression check.** The .tex changes only in the tags, which are now read from the marks; their centres are
  within 2 m of the round-1 ones. The flattened apex with its shoulder at x of about 500-520 m is still the printed
  shape.
- **House rules and family.** The template is identical (4.2 in axes, 0.00525 in/m, s1-s3 solid, `curve tag`,
  `leader`). Flat art.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The house check tool now fails this figure. `python3 tools/v2/digitize.py overlay figures/v2/ch4/fig12.calib.json ...` reports (a) MISMATCH (95% 3.54 px, over the 3 px limit), because `Axes` reads `xgrid` by column and ignores the new `lean` key. The figure is right: the frame mapping and the patched tool both give 95% within 0.00 px. But anyone rerunning the documented check will see a false MISMATCH. Figs 10, 13 and 14 pass the stock tool only because their lean is smaller. | tools/v2/digitize.py `Axes` (orchestrator; outside the figure's files) | Apply the fixer's tested patch, `fix1/tooltest/lean.patch` (12 lines, gated on the `lean` key). I checked it in scratch. It applies cleanly. It round-trips Figs 10, 12, 13 and 14 at 95% within 0.00-1.00 px. The figure scripts give byte-identical CSVs with it, because `FrameAxes` uses only the y mapping and `A` from `Axes`. No other calibration in the repo has a `lean` key, so nothing else changes. It could later be folded into the "mesh" calibration for leaning scans already proposed in corrections/v2-figures.md:336. |
| 2 | note | The 8.20 leader starts at the highest digitized point of (a)'s flat top, x = 496.8 m. The printed leader leaves the top about 10 m (1.3 mm) further right. Either point is "the apex" to within the flatness of the drawn top. | fig12-marks.csv | none |
| 3 | note | Recording the convention in corrections/v2-figures.md is open (see the Fig 10 report, finding 2). | corrections/v2-figures.md | as in Fig 10 |
| 4 | note | The burnout points are not marked, as printed. | - | none |

## Verdict

pass (0 must-fix, 1 should-fix for the orchestrator: the overlay tool's lean support)
