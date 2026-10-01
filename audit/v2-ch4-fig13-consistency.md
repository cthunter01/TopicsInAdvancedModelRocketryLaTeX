# v2 consistency check: ch4/fig13

This round's one issue in the trajectory family was the tag (c) placement in Fig 14. It does not apply here:
Fig 13's tags are set by the family rule (`fig13.py`, `fig13-marks.csv`), and tag (c) clears the leaders by
2.88 mm (round 2). I am the verifier only and made no edits.

Sources checked:
- `figures/v2/ch4/fig13.tex`, `fig13.py`, its CSVs, `fig13.calib.json` and `fig13.pdf`.
- The inventory row `ch4-fig13` (`figures/v2/inventory.csv`:144).
- `audit/v2-ch4-fig13-round1.md` and `-round2.md`.
- My own scratch build of the current source (pdflatex as in the Makefile), rendered at 300 dpi.

Checks made:
- **Not touched.** Every Fig 13 file was last written by 08:49, before the round-2 audit (09:05). In this
  round only `fig14.tex` and `fig14.pdf` were rewritten (09:22).
- **No regression.**
  - My build of the current source is pixel-identical to the PDF in the tree at 300 dpi (1478 x 1082 px).
  - The page is 354.698 x 259.514 pt.
  - The round-2 results still stand.
- **Family consistency.** Unchanged: the frame, the equal scale, s1-s3 solid, `curve tag` and `leader`. Fig 13's
  (c) apex time is also 3.80, on a 30 deg, 6.5 mm leader with its tag by the family rule. Fig 14's
  different arrangement is its documented exception: its curve (c) is 2 mm high.

## Findings

None for the figure. The round-2 orchestrator items (record the frame convention; lean support in the overlay
tool) are still open outside its files.

## Verdict: pass

This round's issue does not apply to this figure, and nothing has regressed.
