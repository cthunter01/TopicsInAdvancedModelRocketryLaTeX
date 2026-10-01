# v2 audit: ch3/fig42 (round 2)

Sources checked: scan `figures/ch3/fig42.png`; redraw `figures/v2/ch3/fig42.tex`, `fig42.py`, `fig42.csv`,
`fig42.calib.json`; rebuilt with `make fig F=ch3/fig42` (4.87 x 3.28 in, all fonts embedded) and rendered at
350 dpi; `build/v2/png/ch3-fig42-compare.png`; inventory row `ch3-fig42`; caption and citing text
`chapters/ch3-sec5b.tex:184-223` (eq. (151), u/U = 0.0172); STYLE.md sections 14, 16; round-1 audit
`audit/v2-ch3-fig42-round1.md` and the round-1 fix report.

Checks run:
- Regression: none of the figure's files has changed since round 1 (fig42.tex 21:50, .py 21:49, .csv 21:51,
  .calib.json 21:52; round-1 audit 21:59). The kit is older than round 1, and the render is unchanged.
- `fig42.py` rerun in memory: its output is byte-identical to `fig42.csv`. 361 traced points (u/U 0.086-2.983).
  The cubic is 0.19828 + 0.03980 x + 0.04994 x^2 - 0.00375 x^3, with rms 0.32 px, 95% 0.64 px and max 1.24 px.
  Values: 0.198 at 0, 0.199 at 0.0172, 0.284 at 1, 0.448 at 2, 0.666 at 3.
- `digitize.py overlay`: 95% 0.00 px, max 2.00 px, "ok", the same as round 1.
- My own masked mesh check: |offset| 95% 0.64 px, max 1.06 px. Mean offsets by band from 0.1 to 2.95 are
  +0.11, -0.08, +0.03, 0.00 and -0.05 px, so the curve sits on the art throughout.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Round-1 item 1 (optional: constrain c0 = 0.20) was declined by the fixer with measurements. The constrained cubic fits the traced ink worse (rms 0.35 against 0.32 px; mean bias 0.34 px over u/U 0-0.5), and the gain is only 0.002 at the masked start (0.17 mm). I accept the decline. Either way, the text's point holds: at u/U = 0.0172 the change (0.199 against 0.198) is "too small to be read from the curve". | fig42.py:82-84 | none |
| 2 | note | The digitized curve sits on the art (tool overlay and masked check above), and the script reproduces the CSV. | fig42.py; fig42.csv | none |
| 3 | note | Lettering is unchanged and as printed. The y title is $\CD$, upright, with ticks 0-0.8 by 0.1. The x title is $\dfrac{u}{U}$, lowercase u over capital U as in the caption. The x ticks are 0, 1, 2, 3 with rulings every 0.5. One unlabelled solid s1 curve. Nothing overlaps or is clipped. Width is 4.87 in. The family frame (4.2 x 2.6 in axes, `tamr grid`, `grid=both`) matches Figs 40 and 41. | fig42.tex:8-15 | none |

## Verdict: pass (no must-fix)
