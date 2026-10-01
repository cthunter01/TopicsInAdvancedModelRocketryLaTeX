# v2 audit: ch3/fig06 (round 1)

Sources checked: figures/ch3/fig06.png (scan, zoomed 3x); figures/v2/ch3/fig06.pdf (rebuilt with `make fig
F=ch3/fig06`, 4.34 x 1.94 in, fonts embedded; rendered at 300 dpi) and build/v2/png/ch3-fig06-compare.png;
figures/v2/ch3/fig06.tex and fig06.calib.json; figures/v2/inventory.csv row ch3-fig06; caption
chapters/ch3-intro-sec2a.tex:465-467 (u = Uy/h); citing text ch3-intro-sec2a.tex:456-460 (lower plate fixed, upper
plate at height h moving right at U) and 487-489 (velocity linear from zero to U); STYLE.md sections 14 and 16;
corrections/v2-figures.md; the other Ch3 profile figures for consistency (figures/v2/ch3/fig10.tex, fig13.tex,
fig16.tex, fig17.tex, fig18.tex; fig13 and fig18 rendered).

Checked and correct:
- Lettering complete against the inventory: $U$ above the upper plate with its arrow to the right; $u$ beside the
  profile line; $h$ (dimension between the plates, label in a gap); $y$ (axis arrow at the left). Nothing added.
- The profile is exactly the caption's u = Uy/h: the line runs from (x_o, 0) to (x_o + U, h); the nine arrows at
  y = kh/10 end at x_o + kU/10, on the line (k = 5: tip (5.60, 1.75), line at y = 1.75: x = 3.74 + 3.72/2 = 5.60).
  Nine arrows at 0.1 h spacing as printed (scan: arrows at 0.097 h ... 0.90 h).
- The U arrow spans the profile's base line to its top, U = 1.064 h, as printed (scan 190 px against h = 179.5 px).
- Walls hatched on their outer sides (`hatch`, 45 deg) as printed; plates as `outline`; the lower plate fixed, the
  upper moving right, as the text says.
- Legibility: $u$ clears the slanting profile line by about 1.4 mm at its top; arrowheads visible down to the
  shortest arrow (0.37 cm); nothing clipped; width within 6.5 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | Velocity profiles are drawn three ways in Chapter 3: Figs 6 and 9 (this family) a 1 pt s1 profile line with ink `thin vec` arrows (5 pt heads); Figs 10 and 13 an ink `outline` profile line with ink 0.4 pt arrows (3.4 pt heads); Figs 16, 17, 18 (25) an s1 profile line with s1 0.5 pt arrows (3.4 pt heads, the "profile family" styles). The same kind of drawing should look the same across the chapter. | fig06.tex:24-26 | Adopt the one profile convention the chapter consistency pass settles (e.g. the Figs 16-18 `profile`/`profile arrow` styles, or the Figs 10/13 ink form), and apply it to Figs 6 and 9 together. |
| 2 | note | Hatched-wall depth: Fig 6 0.22 cm, Fig 18 about 0.18 cm, Fig 13 about 0.43 cm (the inventory names one wall style for Figs 6, 13, 16, 17, 18, 25). Fig 6 is in line with Fig 18; Fig 13 is the outlier. | fig06.tex:16-19 | None for Fig 6; settle one band depth in the consistency pass. |
| 3 | note | The U arrow is the heavy house `vec`; the printed U arrow is a thin line like the profile arrows. House style for a velocity vector; no meaning changes. | fig06.tex:29 | None. |

## Verdict: pass (0 must-fix, 1 should-fix)
