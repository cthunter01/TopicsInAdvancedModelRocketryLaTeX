# v2 consistency check: ch4/fig11

This round's one issue in the trajectory family was the tag (c) placement in Fig 14. It does not apply here:
Fig 11's tags sit 0.57-0.58 mm from their own curves, the family's spacing. They are placed by hand in
`fig11.tex`:39-41 (round-2 note 2). I am the verifier only and made no edits.

Sources checked:
- `figures/v2/ch4/fig11.tex`, `fig11.py`, its CSVs and `fig11.pdf`.
- The inventory row `ch4-fig11` (`figures/v2/inventory.csv`:142).
- `audit/v2-ch4-fig11-round1.md` and `-round2.md`.
- My own scratch build of the current source (pdflatex as in the Makefile), rendered at 300 dpi.

Checks made:
- **Not touched.** Every Fig 11 file was last written by 08:49, before the round-2 audit (09:04). In this
  round only `fig14.tex` and `fig14.pdf` were rewritten (09:22).
- **No regression.**
  - My build of the current source is pixel-identical to the PDF in the tree at 300 dpi (1472 x 1084 px).
  - The page is 353.118 x 260.013 pt.
  - The round-2 results still stand: the curves computed by the book's method with the computed times marked
    (owner decision 2026-10-01), and the lettering.
- **Family consistency.** Fig 14's documented exception (tag (c) on its 3.80 baseline, as printed) does not
  bear on Fig 11, whose computed curve (c) is large enough to carry its tag.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-2 should-fix 1 is still open outside the figure's files. The Fig 11 record in corrections/v2-figures.md:69-73 is stale: it names the vertical method and ends with the gate question. | corrections/v2-figures.md | for the orchestrator, as in round 2 |

## Verdict: pass

This round's issue does not apply to this figure, and nothing has regressed.
