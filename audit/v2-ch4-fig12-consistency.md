# v2 consistency check: ch4/fig12

This round's one issue in the trajectory family was the tag (c) placement in Fig 14. It does not apply here:
Fig 12's tags are set by the family rule (`fig12.py`, `fig12-marks.csv`), and tag (c) clears the leaders by
1.98 mm (round 2). I am the verifier only and made no edits.

Sources checked:
- `figures/v2/ch4/fig12.tex`, `fig12.py`, its CSVs, `fig12.calib.json` and `fig12.pdf`.
- The inventory row `ch4-fig12` (`figures/v2/inventory.csv`:143).
- `audit/v2-ch4-fig12-round1.md` and `-round2.md`.
- My own scratch build of the current source (pdflatex as in the Makefile), rendered at 300 dpi.

Checks made:
- **Not touched.** Every Fig 12 file was last written by 08:49, before the round-2 audit (09:04). In this
  round only `fig14.tex` and `fig14.pdf` were rewritten (09:22).
- **No regression.**
  - My build of the current source is pixel-identical to the PDF in the tree at 300 dpi (1471 x 1241 px).
  - The page is 352.896 x 297.638 pt.
  - The round-2 results still stand.
- **Family consistency.** Unchanged: the frame, the equal scale, s1-s3 solid, `curve tag` and `leader`.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Two round-2 items are still open outside the figure's files: the overlay tool's lean support (should-fix 1) and recording the frame convention (note 3). | tools/v2/digitize.py; corrections/v2-figures.md | for the orchestrator, as in round 2 |

## Verdict: pass

This round's issue does not apply to this figure, and nothing has regressed.
