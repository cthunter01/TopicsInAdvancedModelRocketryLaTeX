# v2 audit: ch4/fig13 (round 2)

Sources checked:
- Scan `figures/ch4/fig13.png`, read at 2x.
- Redraw `figures/v2/ch4/fig13.pdf`:
  - 200 and 600 dpi renders;
  - a fresh compile in a scratch tree (pixel-identical);
  - `pdffonts` (all embedded); no transparency.
- Sources `fig13.py`, `fig10.py`, `fig13-a/b/c.csv`, `fig13-marks.csv` and `fig13.calib.json`.
- Inventory row `ch4-fig13` (`figures/v2/inventory.csv`:144).
- Caption `chapters/ch4-sec3.tex`:205-212.
- Round-1 report and fix notes, and `fix1/orig/`.

Checks made:
- **Round-1 should-fix (xgrid ignored the lean): resolved.**
  - fig13.calib.json keeps the `xgrid` (ticks 76.8 down to 70.1 px per 200 m) and adds `lean`. Its note records
    the 0.79 deg skew and the convention.
  - The tick points map back within 0.37 m (x) and 1.0 m (y).
  - The zeros' shear (+0.0099 ± 0.0031 against the axis's +0.0127; upright lettering would give -0.0005)
    confirms that the lettering shares the skew (Fig 10 report).
- **Round-1 note 2 (the reason given for the xgrid extension): resolved.** The note now reads "as a safeguard for
  a point past the last tick".
- **Data reproduce.** The rerun reproduces the CSVs byte for byte (also with the tool's lean patch).
- **Overlay.**
  - Frame mapping (fig13.py's check; patched `digitize.py overlay`): 95% within 0.00 px for (a), (b) and (c), max
    1.0. The overlay image puts all three curves on the ink, the apexes included.
  - Stock tool: 2.24, 1.41 and 0.80 px. All ok.
- **Caption burnout points**, distance to the densified curves: (a) 2.4 m (0.21 mm); (b) 0.6 m; (c) 1.0 m.
- **Marks.** Apex (a) (633.6, 830.7), impact 924.9 m; apex (b) (492.7, 573.7), impact 787.6 m; apex (c)
  (91.8, 101.8), impact 135.7 m. These agree with the printed leader feet, about (631, 826) and (495, 569) just off
  the curve, and with the inventory (about 630/830 and 490/575).
- **Lettering.** All present: titles; x ticks 0-1200 by 200; y ticks 0-800 by 200 (axis to 900); tags a, b, c;
  the times 9.40, 26.47, 9.00, 21.84, 3.80 and 9.40 (twice, as printed). 9.40 and 9.00 hang below their apexes and
  21.84 is set to the left, as printed.
- **Legibility** (600 dpi, masked renders):
  - Labels to curves: at least 4.27 mm.
  - Tags to curves: 0.56-0.57 mm. Tags to leaders: at least 2.88 mm.
  - Labels to labels: at least 7.6 mm.
- **Regression check.**
  - The .tex changes only in the tags, now read from the marks; their centres are within 9 m of round 1.
  - Ascending branches: (b) at most 1.3 m (0.12 mm) left of (a), inside the stroke.
  - The slight bends in (b) near (400, 520) and (620, 490) are still those of the 1973 ink.
- **House rules and family.** The template is identical (4.2 in axes, 0.0035 in/m, s1-s3 solid, `curve tag`,
  `leader`). Flat art.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Recording the frame convention in corrections/v2-figures.md is open (Fig 10 report, finding 2). So is adding lean support to the overlay tool (Fig 12 report, finding 1). This figure passes the stock tool. | corrections/v2-figures.md; tools/v2/digitize.py (orchestrator) | as in Figs 10 and 12 |
| 2 | note | The burnout points are not marked, as printed. | - | none |

## Verdict

pass (0 must-fix, 0 should-fix)
