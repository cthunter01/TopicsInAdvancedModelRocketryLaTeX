# v2 consistency check: ch4/fig10

This round's one issue in the trajectory family was the tag (c) placement in Fig 14. It does not apply here:
Fig 10's tags (a), (b) and (c) are all set by the family rule, 2.75 mm out along the normal of each descending
branch (`fig10.py` `tag()`, `fig10-marks.csv`). I am the verifier only and made no edits.

Sources checked:
- `figures/v2/ch4/fig10.tex`, `fig10.py`, its CSVs, `fig10.calib.json` and `fig10.pdf`.
- The inventory row `ch4-fig10` (`figures/v2/inventory.csv`:141).
- `audit/v2-ch4-fig10-round1.md` and `-round2.md`.
- My own scratch build of the current source (pdflatex as in the Makefile), rendered at 300 dpi. I also made a
  600 dpi element-masked build to measure the (c) tag.

Checks made:
- **Not touched.** Every Fig 10 file was last written by 08:49, before the round-2 audit (09:04). In this
  round only `fig14.tex` and `fig14.pdf` were rewritten (09:22).
- **No regression.**
  - My build of the current source is pixel-identical to the PDF in the tree at 300 dpi (1472 x 1084 px).
  - The page is 353.118 x 260.013 pt.
  - The round-2 results (curves, overlay, lettering against the scan and the inventory) still stand.
- **Family consistency after the Fig 14 fix.** Fig 14 (c) now stands on its 3.80 baseline as printed, a
  documented exception. Fig 10 keeps the family rule (tag (c) 0.57 mm from its curve). The frame, the scale
  convention, the styles and the leader lengths (4.5-8.5 mm here) are unchanged.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix (carried over from round 2; not part of this round's issues) | Round-2 finding 1 is still open. The (c) tag passes 0.30 mm from the 2.40 leader (I re-measured this on a 600 dpi masked build of the current source). Every other tag in the family clears every leader by at least 1.84 mm. Since this round's fix, Fig 14 (c) clears its leaders by 6.4 mm or more. | fig10.tex:37; fig10.py:76 | As in round 2: leader at 45 deg (`\timemark{\Cax}{\Cay}{45}{6.5mm}{south west}{2.40}`) and tag height 16 m (`"c": 16.0`), then rerun fig10.py. |
| 2 | note | Round-2 finding 2 (record the family's frame convention in corrections/v2-figures.md) is still open there. It is outside the figure's files. | corrections/v2-figures.md | for the orchestrator |

## Verdict: pass

This round's issue does not apply to this figure, and nothing has regressed. One round-2 should-fix is still
open (finding 1).
