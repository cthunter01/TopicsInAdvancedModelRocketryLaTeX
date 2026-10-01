# v2 audit: ch3/fig53 (round 2)

Sources checked: round 1 report `audit/v2-ch3-fig53-round1.md` and the fixer's reply; redraw
`figures/v2/ch3/fig53.tex` (patch at line 25), `fig53-a-ogive.csv`, `fig53-a-half.csv`, `fig53-b-ogive.csv`,
`fig53-b-half.csv` (unchanged since 22:08, before round 1), `fig53.calib.json`; `figures/v2/ch3/fig53.pdf`
(5.00 x 5.64 in, fonts embedded, newer than the .tex) rendered at 400 dpi; `build/v2/png/ch3-fig53-compare.png`;
scan `figures/ch3/fig53.png`; inventory row `ch3-fig53`; caption and citing text `chapters/ch3-sec7.tex:160-195,
208-254`, eqs. (214a)-(215b), Table 8.

Checks run:
- Round 1 should-fix (grid stubs at the right edge): fig53.tex:25 now runs the white patch to `axis cs:2.0`, set
  in by 0.2 pt. In the 400 dpi render, the 0.8 ruling (row 636) and the 0.4 ruling (row 786) have no ink
  between the inset (last ink at col 1748) and the M = 2.0 ruling (cols 1949-1951). The M = 2.0 ruling is
  3 px wide at rows 620-800 inside the patch, the same as above and below it. The patch top (0.95) is clear of
  the flat 1.0 curve (rows 559-564), and the patch's left edge (M 0.85) still ends the 0.4 and 0.8 rulings
  near the scan's 0.82. **Resolved.**
- Round 1 note 2 (art 1.25 against Table 8's 1.27 at M 2.0): the fixer put it in its doubts for the
  corrections file, as asked, and left the figure unchanged. **Resolved** (pending the gate entry, which the
  orchestrator writes).
- (b) re-evaluated against eqs. (214), (215) at every CSV point: max deviation 0.0012 (ogive) and 0.0021
  (half-round), only at the two peaks, where the two formulas of each pair differ by that much. Values at
  M 0.95-2.0: ogive 1.089, 1.355, 1.799, 1.679, 1.513, 1.356, 1.300, 1.281, 1.274; half-round 1.181, 1.388,
  1.606, 1.831, 2.298, 2.095, 2.030, 2.010, 2.003, matching Table 8's analytical column.
- `digitize.py overlay` re-run (points with M >= 0.85): (a) ogive 95% 0.00 px (max 1.00), half-round 95%
  2.00 px (max 2.24); (b) ogive 95% 1.00 px (max 1.41), half-round 95% 2.00 px (max 3.00). All ok, and the
  same as round 1.
- Regressions: none. Only line 25 and its comment changed. Labels clear the curves: (b) "Ogive" box bottom
  at 1.33 against the curve at 1.285 at M 1.74, about 2.6 pt clear; (a) is similar. Panel letters, frame,
  series styles and inset are as in round 1.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round 1 should-fix 1 is done. The patch now ends at the M = 2.0 ruling, set in by half a ruling. There are no 0.4 or 0.8 stubs at the right edge, and the 2.0 ruling keeps its full weight behind the inset. | fig53.tex:23-25 | none |
| 2 | note | Round 1 note 2 (the (a) ogive ends at 1.25, faithful to the art; Table 8 and the text give 1.27) is in the fixer's doubts for corrections/v2-figures.md as **minor**. | fig53-a-ogive.csv (end) | Orchestrator: log as minor at the Chapter 3 gate. |
| 3 | note | The family is consistent: y fraction titles upright here and in Fig 55; panel letters at the upper right inside the axes; series1 solid and series2 dashed. | fig53.tex:14-20, 30, 51 | none |

## Verdict: pass (no must-fix)
