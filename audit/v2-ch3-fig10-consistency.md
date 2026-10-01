# v2 audit: ch3/fig10 (consistency fix verification)

Issue checked: velocity profiles are drawn three ways in Chapter 3 (keys ch3/fig10, fig13, fig23, fig33). For
Fig 10 the suggestion was to copy the family styles from fig16.tex:13-16 and draw the profile curve as `profile`
(s1, 1pt) and the arrows as `profile arrow` (s1, 0.5pt, 3.4pt Stealth). The base lines stay in ink.

Sources checked: redraw `figures/v2/ch3/fig10.tex`, `fig10.py`, `fig10-profile.csv`, `fig10-arrows.csv`,
`fig10.calib.json`. I rebuilt it with `make fig F=ch3/fig10` (4.39 x 3.11 in, fonts embedded) and rendered it at
300 and 600 dpi, with the lower profile zoomed. Also checked: `build/v2/png/ch3-fig10-compare.png` beside the scan
`figures/ch3/fig10.png`; inventory row `ch3-fig10`; audits `audit/v2-ch3-fig10-round1.md` and `-round2.md`; the
peer profile figures fig16.tex:12-16, fig18.tex (rendered at 300 dpi for a side-by-side check), fig06.tex and
fig25.tex. I ran the overlay again myself, with the lower profile mirrored into a scratch CSV.

## Issue (velocity profiles): resolved

- fig10.tex:14-17 defines `profile`, `profile arrow` and `profile stroke`. They match fig16.tex:13-15 character for
  character. The old local `profile line` (outline) and the ink `profile arrow` (0.4pt) are gone.
- The arrows (fig10.tex:50) are `profile arrow`. Both profile curves, the upper one and the mirrored lower one
  (fig10.tex:52-53), are `profile`.
- The base lines at the station (fig10.tex:51) stay `outline` (ink), as in Figs 6, 13, 16 and 17. The dashed
  boundary-layer edge (`guide`), the V dimension, the braces and the Free-stream arrow (ink2) and the rocket are
  unchanged.
- At 600 dpi each arrow tip lands on the blue curve and the heads are clear. Side by side with Fig 18, the colour,
  the weights and the heads now match. The heavier-looking row in the 300 dpi render is pixel alignment only; the
  rows are even at 600 dpi.

## Regression check: none found

- The data is unchanged. The CSVs date from before the round-2 audit, and my overlay gives the round-2 numbers
  exactly: upper 95% 2.00 px, max 2.24 px; lower 95% 2.00 px, max 3.00 px.
- Arrow rows as printed and as the inventory gives them: seven arrows plus the V row above the body, and eight
  below (two inside the layer, then the dashed edge). The lettering is complete: $V$ in the gap of its dimension,
  "Boundary layer" and "Free stream" with braces, and the Free-stream brace running on into an arrowhead.
- The axis treatment from round 2 is unchanged: a dash-dot centre line inside the body and thin solid extensions.
  The size is unchanged.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | `profile`, `profile arrow` and `profile stroke` are now copied word for word in Figs 6, 9, 10, 13, 16, 17, 18, 25 and 33 (Figs 6 and 9 carry only the first two). `\csvline` and `\csvarrows` are also duplicated between Figs 10 and 13. Under STYLE s.16 these belong in the kit. | fig10.tex:14-41 | Kit move, as in the fixer's style_suggestions. No figure change. |

## Verdict: pass (no must-fix)
