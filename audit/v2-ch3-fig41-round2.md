# v2 audit: ch3/fig41 (round 2)

Sources checked: scan `figures/ch3/fig41.png`; redraw `figures/v2/ch3/fig41.tex`, `fig41.py`, `fig41.csv`,
`fig41.calib.json`; rebuilt with `make fig F=ch3/fig41` (4.91 x 3.15 in, all fonts embedded) and rendered at
350 dpi and 800 dpi (leader ends zoomed); `build/v2/png/ch3-fig41-compare.png`; inventory row `ch3-fig41`;
caption and citing text `chapters/ch3-sec5b.tex:60-104, 147-170` (eqs. (148)-(150), Table 4); STYLE.md
sections 14, 16; `tamrfig.sty` (`series1`, `series2`, `leader`, `every picture` font); round-1 audit
`audit/v2-ch3-fig41-round1.md` and the round-1 fix report.

Checks run:
- Regression: none of the figure's files has changed since round 1 (fig41.tex 21:51, .py 21:47, .csv 21:51,
  .calib.json 21:52; round-1 audit 21:59). The kit is older than round 1, and the render is unchanged.
- `fig41.py` rerun in memory: its output is byte-identical to `fig41.csv`. Stine fit
  0.75 + 0.008972 a^2 - 0.0001282 a^3 (a in deg): rms 0.73 px, 95% 1.46 px. Values: 1.519 at 10 deg (2.03 x
  0.75); trial 1.310 at 10 deg.
- I evaluated eq. (149) + 0.75 separately at 0-10 deg. It matches the trial column to five places: 0.75000,
  0.75517, 0.77089, 0.79742, 0.83506, 0.88408, 0.94478, 1.01744, 1.10234, 1.19976, 1.30999. These agree with
  Table 4's total column, apart from the known last-digit cell recorded in corrections/ch3.md D35.
- `digitize.py overlay`: Stine 95% 0.00 px, max 1.00 px; trial 95% 2.00 px (0.34 mm), max 2.83 px. Both are
  "ok", the same as round 1.
- My own masked mesh check:
  - Stine: |offset| 95% 1.55 px; mean offsets by band -0.67, +0.25, +0.06, -0.02, +0.16 px.
  - Dashed curve: within -0.45 to -0.79 px (mean) of the dashes from 4.4 to 9.9 deg. Below about 4 deg the
    check picks up the solid curve through the dash gaps.
- `\pgfplotstablegetelem` rows 48 and 64 are alpha = 4.80 and 6.40 (step 0.1 from row 0), as the comment says.
- Dash phase along the dashed curve, measured in the 800 dpi render, alpha 6.0-6.8:
  - dashes at 6.05-6.15, 6.25-6.35, 6.45-6.55 and 6.65-6.70;
  - gaps at about 6.0, 6.2, 6.4, 6.6 and 6.75.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | New in round 2 (cosmetic). The leader of "Rocket of / Figure 37 / semiempirical" ends at alpha = 6.4 deg, which falls in a gap of the s2 dash pattern. Its tip stops on the curve's centreline, about 0.3-0.4 mm from the nearest dash ends on either side, so it does not visibly touch the dashed curve (seen at 800 dpi). The print's leader meets the curve at about 6.5 deg. | fig41.tex:14 (`\pgfplotstablegetelem{64}`), fig41.tex:32 (`axis cs:6.4`) | End the leader at 6.5 deg: row 65 and `(axis cs:6.5,\trialend)`. That point is mid-dash (6.45-6.55) and closer to the print. Update the comment on line 11 to read 6.5. |
| 2 | note | Data are correct (see checks). The dashed curve is computed from eq. (149) + 0.75. The Stine curve is digitized and sits on the art. The script reproduces the CSV. The text's claims hold: both curves start at 0.75 (caption), and the Aerobee-Hi drag "is doubled at an incidence of ten degrees" (1.519 = 2.03 x 0.75). | fig41.py; fig41.csv | none |
| 3 | note | Round-1 notes are confirmed with no regression. "Aerobee-Hi" and the literal "Figure 37" are as printed. The Stine leader is straight and ends on the solid curve at 4.8 deg (checked in the 350 dpi zoom). Series1 is solid and series2 is dashed, as printed. Ticks run 0-10 by 1 and 0-1.6 by 0.2, with rulings every 0.1. Labels are `\small` (kit default) in white knock-outs and clear of both curves. Width is 4.91 in, and the axes match the family's 4.2 x 2.6 in. | fig41.tex:17-35 | none |

## Verdict: pass (no must-fix)
