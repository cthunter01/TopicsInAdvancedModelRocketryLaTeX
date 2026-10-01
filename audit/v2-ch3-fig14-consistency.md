# v2 consistency check: ch3/fig14

The issue in this round is the panel-letter placement inside the plot axes (Figs 21 and 26; the approved
placement is `\node[panel, anchor=north east] at (rel axis cs:1,1)`). It does not apply here: Fig 14 is a
single plot (the Blasius profile f'(eta), with the dashed displacement-thickness line (lettered 1.73) and its dimension) with no panel letters, either in the scan or in the redraw. I am the verifier only and made
no edits.

Sources checked:
- `figures/v2/ch3/fig14.tex` and `fig14.pdf`, with their CSVs.
- The inventory row `ch3-fig14`: its lettering lists no panel letter.
- `audit/v2-ch3-fig14-round1.md` and `-round2.md`, and the round-2 audit's 300 dpi render.
- My own scratch build of the current source (pdflatex as in the Makefile), rendered at 300 dpi.

Checks made:
- **No panel letter.** `grep panel` finds nothing in the source. The scan has no panel letter either.
- **Not touched.** The fixer reports Fig 14 unchanged. Every file of Fig 14 (tex, py, CSVs, calib, PDF) was last
  written before the round-2 audit (22:05). Only fig21.tex and fig21.pdf were rewritten in this round (23:13).
- **No regression.**
  - My build of the current source renders pixel-identical to the PDF in the tree at 300 dpi (1495 x 1020 px).
  - That render is also pixel-identical to the round-2 audit's 300 dpi render.
  - The page is 358.725 x 244.605 pt, unchanged.
  - The round-2 results (curves, overlay, lettering against the scan and inventory) therefore still stand.

## Findings

None.

## Verdict: pass

The issue does not apply to this figure (no panel letters), and nothing has regressed.
