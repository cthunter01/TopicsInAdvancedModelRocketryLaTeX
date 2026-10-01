# v2 audit: ch3/fig55 (round 2)

Sources checked: round 1 report `audit/v2-ch3-fig55-round1.md` and the fixer's reply; redraw
`figures/v2/ch3/fig55.tex`, `fig55.py`, `fig55-10.csv`, `fig55-25.csv`, `fig55-50.csv`, `fig55-100.csv`
(unchanged since 22:08, before round 1), `fig55.calib.json`; `figures/v2/ch3/fig55.pdf` (5.13 x 3.31 in, fonts
embedded, newer than the .tex) rendered at 400 dpi; `build/v2/png/ch3-fig55-compare.png`; scan
`figures/ch3/fig55.png`; inventory row `ch3-fig55`; eqs. (223)-(230) and caption `chapters/ch3-sec8.tex:105-223`;
standing rule 3 in `corrections/v2-figures.md`; y titles of the approved and sibling figures (`ch3/fig02.tex`,
`fig51.tex`, `fig52.tex`, `fig53.tex`).

Checks run:
- Round 1 should-fix 1 (record the mismatch with the 1973 art): the header comment (fig55.tex:6-9) and the
  fig55.py docstring (11-17) now give the drawn and computed times at k/m = 0.094, the 100 m crossing of
  t = 10 s (0.068 drawn, 0.084 computed), the agreement below about 0.02, and the 25 m overlay MISMATCH. The
  fixer's doubts carry the item for corrections/v2-figures.md (agents may not edit corrections/; there is
  no Fig 55 entry yet). **Resolved** (pending the gate entry, which the orchestrator writes).
- Round 1 note 2 (y title): it is now upright, with the unit on a second line (fig55.tex:24). This matches
  Figs 2, 51, 52 and 53, which all set the y title upright. At 400 dpi "(m^-1)" ends about 40 px left of the
  tick labels, with no overlap. **Resolved.**
- Round 1 note 4 (calibration points): the note in fig55.calib.json now says the affine `points` are only a
  fallback (46.7 px residual) and that `xgrid`/`ygrid` replace them. The JSON parses. **Resolved.**
- Curves re-checked against eq. (230) itself: substituting each CSV (t, k/m) pair into
  x = -(m/2k) ln[1 - tanh^2(t sqrt(gk/m))] with g = 9.8 returns x within a relative 7e-6 of 10, 25, 50 and
  100 m. Spot values: t = 1.431, 2.268, 3.221, 4.593 s at k/m = 1e-3; 1.674, 3.224, 5.751 s at 0.1. The
  100 m curve ends at (k/m = 0.08356, t = 10.000).
- `digitize.py overlay` re-run: 10 m 95% 2.83 px, 25 m 4.00 px (MISMATCH), 50 m 2.83 px, 100 m 2.24 px. These
  are the same as round 1 and are the recorded, approved computed-curve mismatch.
- Legibility: the curves are a continuous 5-6 px wide (at 400 dpi) through the label band (rows 495-575), so
  no knock-out cuts a curve. The knock-outs (rows 523-573) blank only the t = 1.5, 2.5 and 6 rulings behind
  "10", "25" and "100", as the printed labels do. The tightest clearance is the 100 box's lower-left corner,
  about 3 px (0.2 mm) from the curve. The axes are true log, and the rulings and labels are as printed.
- Regressions: none. The width grows from 5.09 to 5.13 in (6.5 in limit).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round 1 should-fix 1 is done in the files agents may write: the header comment and the .py docstring state the mismatch with the 1973 art, and the fixer reported it for the corrections file. | fig55.tex:6-9; fig55.py:11-17 | Orchestrator: add the Fig 55 item to corrections/v2-figures.md (status **gate** or **rule**: computed curves kept, as Ch2 Fig 25 / Ch3 Fig 22). |
| 2 | note | The y title is now upright, with (m^-1) on a second line. This is consistent with Fig 53 in the family and with Ch3 Figs 2, 51 and 52, and is clear of the tick labels. | fig55.tex:10, 24 | none |
| 3 | note | Calibration note clarified; JSON valid. | fig55.calib.json "note" | none |

## Verdict: pass (no must-fix)
