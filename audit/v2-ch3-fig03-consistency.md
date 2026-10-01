# v2 consistency check: ch3/fig03

This figure had no consistency issue of its own. The family "u01-atmosphere" (Figs 3, 4, 7, 8) had one issue, on
Fig 4: its y title was the only rotated one among the five atmosphere charts. The fix was confined to fig04.tex.
I checked this figure for regression and for its fit with the fixed Fig 4. I only verified and made no edits.

Sources checked:
- `figures/v2/ch3/fig03.tex`, `fig03.py`, `fig03.csv`, `fig03.calib.json` and `fig03.pdf`. All are dated
  before the fix, and the PDF and PNGs have not been rebuilt since round 1.
- The round-1 auditor's 400 dpi render (`scratchpad/ch3/u01-atmosphere/audit1/fig03-400.png`).
- My own build of the current source (pdflatex as in the Makefile, output to scratch).
- `audit/v2-ch3-fig03-round1.md`; `audit/v2-ch3-fig04-consistency.md`.

Checks made:
- **Unchanged.** The repo PDF rendered at 400 dpi is pixel-identical to the round-1 render. My build of the
  current source is pixel-identical to the repo PDF. The page is 372.96 x 212.31 pt (5.18 x 2.95 in), the size round 1 recorded.
- **Family fit.** The y title is "T (°K)", upright, as printed (`ylabel style={rotate=-90, anchor=east}`). Fig 4 now uses the same
  option string. The gap from the title to the tick labels is 7.48 pt; Fig 4 is now 7.46 pt.
- I viewed Figs 3, 4, 7 and 8 right-aligned at 400 dpi. They share the 4.2 x 2.4 in axes, the 0-2500 m altitude
  axis, the grid, the s1 curve and the upright y titles, and they read as one set.
- **Round 1.** The verdict (pass, 0 must-fix, 0 should-fix) and its notes stand. The figure has not changed.

## Findings

None.

## Verdict: pass
