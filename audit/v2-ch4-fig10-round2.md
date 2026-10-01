# v2 audit: ch4/fig10 (round 2)

Sources checked:
- Scan `figures/ch4/fig10.png`, read at 2x and 4x (the corner of curve (c)).
- Redraw `figures/v2/ch4/fig10.pdf`:
  - 200 and 600 dpi renders;
  - a fresh compile in a scratch tree (clean log; the 600 dpi render is pixel-identical to the committed PDF's);
  - `pdffonts` (all embedded); no `/ca`, `/CA` or `SMask` (flat art).
- Sources `fig10.tex`, `fig10.py` (the `FrameAxes` mapping that Figs 12-14 share), `fig10-a/b/c.csv`,
  `fig10-marks.csv` and `fig10.calib.json` (`points`, `xgrid`, `lean`).
- Inventory row `ch4-fig10` (`figures/v2/inventory.csv`:141).
- Caption `chapters/ch4-sec3.tex`:173-184; text :131-168.
- Round-1 report and fix notes; the round-1 sources kept in the fix scratch dir (`fix1/orig/`).
- `corrections/v2-figures.md`.

Checks made:
- **Round-1 should-fix (the family's calibration convention): resolved in the figure files.**
  - All four digitized figures now read x between the drawn x ticks along the drawn y axis, and y by the affine
    fit (`FrameAxes`).
  - The mapping is correct. Every calibration tick maps back to its value within 0.22 m in x and 0.49 m in y.
    `to_pixel` and `to_data` invert each other to 1e-13 m.
  - **Independent check of the evidence.** I measured the shear of the "0" glyphs (second moments of 20-31 zeros
    per scan) myself. The fixer's claim holds: the lettering shares each frame's skew, so the scan, and not just
    the hand-drawn axis, is distorted.

    | figure | zeros, shear dcol/drow | y axis | upright lettering would give |
    |---|---|---|---|
    | Fig 10 | +0.0150 ± 0.0024 | +0.0163 | -0.0060 |
    | Fig 12 | -0.0172 ± 0.0031 | -0.0199 | -0.0028 |
    | Fig 13 | +0.0099 ± 0.0031 | +0.0127 | -0.0005 |
    | Fig 14 | +0.0059 ± 0.0030 | +0.0059 | +0.0042 (too close to separate) |
    | Fig 11 (square frame, control) | -0.0048 ± 0.0030 | +0.0022 | +0.0010 |

  - The convention is still not recorded in `corrections/v2-figures.md` (no "lean" or "frame convention" entry).
    That is for the orchestrator (finding 2).
- **Data reproduce.** I reran `fig10.py` in the scratch tree. It reproduces all four CSVs byte for byte. It also
  does so with the tested `digitize.py` lean patch applied, so applying the patch would not change the data.
- **Overlay.**
  - With the frame mapping (fig10.py's own check, and `digitize.py overlay` with the lean patch in scratch): 95%
    of points within 0.00, 0.00 and 0.00 px for (a), (b) and (c); max 1.0 px.
  - With the stock `digitize.py`, which reads `xgrid` by column alone: 2.83, 1.00 and 0.00 px. All pass, but they
    are off by the lean.
  - On the patched overlay image the three curves lie on the ink everywhere.
- **Caption burnout points**, distance to the densified curves: (a) 1.8 m (0.32 mm); (b) 0.2 m (0.03 mm); (c)
  0.3 m (0.05 mm). Not drawn, as printed.
- **Marks.**
  - Apex (a) (316.1, 402.4), impact 466.0 m; apex (b) (187.4, 200.8), impact 325.0 m; apex (c) (27.7, 26.6),
    impact 49.3 m.
  - The printed leader feet, read in the same mapping just off the curve, are at about (312, 401), (194, 207) and
    (33, 31). The (b) foot is within the curve's flat top, 1.2 mm from the mark at final size.
- **Lettering.** Everything printed is present: titles $x$ (m) and $y$ (m), x ticks 0-600 by 100, y ticks 0-400
  by 100 (axis to 450), tags a, b, c, and the times 6.80 and 18.25 (a), 5.80 and 12.90 (b), 2.40 and 4.90 (c).
  Each leader runs in the printed direction.
- **Legibility** (600 dpi, final size, measured on element-masked renders):
  - Time labels to curves: at least 3.46 mm.
  - Tags to their curves: 0.57-0.58 mm, the family offset.
  - Labels to other labels: at least 4.9 mm.
  - The (c) tag to the 2.40 leader: **0.30 mm** (finding 1).
- **Regression check against round 1.**
  - The .tex differs only in the tags, which are now read from the marks.
  - The tag centres moved by at most 7 m (1.2 mm). The (c) tag moved from (52.2, 28.1) to (52.7, 27.7), so finding
    1 was already present in round 1; it was not measured then.
  - Ascending branches: (b) lies at most 0.7 m (0.12 mm) left of (a), inside the stroke.
- **House rules and family.**
  - `tamr` axes 4.2 in wide, x = y = 0.007 in/m.
  - s1/s2/s3 solid at 1pt; `curve tag`; `leader`; times `\footnotesize` in ink.
  - No local styles. Identical template to Figs 11-14.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The (c) tag nearly touches the 2.40 leader. The circle passes 0.30 mm from the leader line at final size (600 dpi, masked renders), so at reading distance the tag looks pinned to it. Elsewhere in the family a tag clears every leader by at least 1.84 mm: Fig 11 (c) 1.84, Fig 12 (c) 1.98, Fig 13 (c) 2.88, Fig 14 (c) 3.96. In the scan the circled c stands clearly below the 2.40 leader. The cause is that the tag (2.75 mm out from the descending branch at 18.8 m) lies only 2.4 mm from the 35 deg leader's line. | fig10.tex:37 (leader angle); fig10.py:76 (`tags` "c": 18.8) | Tested on a scratch copy. Set the 2.40 leader to 45 deg: `\timemark{\Cax}{\Cay}{45}{6.5mm}{south west}{2.40}`. Set the (c) tag height to 16 m (`"c": 16.0`); rerunning fig10.py then puts the tag at (55.0, 24.2). Result: tag to the 2.40 leader 1.65 mm; tag to (c) 0.57 mm (unchanged); "2.40" to the (a)/(b) launch lines 2.35 mm (it was 3.46); tag to "2.40" 3.6 mm; tag to the x axis 2.2 mm. With only one change: 45 deg alone gives 0.93 mm, and a height of 14 m alone gives 1.19 mm. |
| 2 | should-fix | The family's frame convention, which changed all four digitized figures in round 2, is not yet recorded in corrections/v2-figures.md. The fixer's suggested entry (round-1 fix notes, fig10 "changes") is accurate. My shear measurements above confirm its evidence. | corrections/v2-figures.md, Ch4 digitized trajectories (orchestrator) | Add the entry as the fixer drafted it, status **rule**. |
| 3 | note | The stock `tools/v2/digitize.py overlay` ignores `lean`, so it reads these curves off by the lean. Here they still pass (2.83/1.00/0.00 px); Fig 12 (a) does not. The tested patch is discussed in the Fig 12 report. | tools/v2/digitize.py | See Fig 12, finding 1. |
| 4 | note | The burnout points are not marked, as printed (editorial option). | - | none |

## Verdict

pass (0 must-fix, 2 should-fix: one in the figure (the (c) tag against the 2.40 leader) and one for the
orchestrator)
