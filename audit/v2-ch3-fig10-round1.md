# v2 audit: ch3/fig10 (round 1)

Sources checked: figures/v2/ch3/fig10.tex, fig10.py, fig10-profile.csv, fig10-arrows.csv, fig10.calib.json and the
PDF (rendered at 300 and 600 dpi; `make fig F=ch3/fig10`: 4.39 x 3.11 in, fonts embedded); the scan
figures/ch3/fig10.png (zoomed 2x); inventory row ch3-fig10; caption and citing text chapters/ch3-sec2b.tex:55-81;
Table 1 (chapters/ch3-sec3a.tex:397-454) and eq. (54); STYLE.md sections 14 and 16; tamrfig.sty (`model` rocket,
`\dimline`, `guide`). I ran the overlay myself (tools/v2/digitize.py overlay with fig10.calib.json).

Checks that passed:
- Lettering complete and as printed: $V$ (plain italic, as the text types it) in the gap of a dimension between the
  base line and the tip line on the top row; "Boundary layer" and "Free stream" with braces; the Free-stream brace's
  lower leg runs on into an arrowhead at the bottom, as printed.
- Arrow rows as printed: seven arrows plus the $V$ row above the body, and eight below (two inside the boundary
  layer, then the dashed edge, then six). The station is behind the nose joint (x = 2.33; the scan gives 2.30).
- The computed profile (Blasius, $u = V f'(5y'/\delta)$ from Table 1, $\delta = 0.65$): spot check of the first upper
  arrow, $y' = 0.219$, $\eta = 1.685$, $f' = 0.5417$, so $u = 0.628$ (CSV 0.6283). The Hermite interpolation parses
  all 45 rows of Table 1. Overlay on the scan's profile lines: upper 95% 2.0 px (0.34 mm), max 2.2 px; lower 95%
  2.0 px, max 3.0 px; the boundary-layer parts alone 95% 2.0 px. All ok.
- The caption's points hold: the free stream at $V$ is outside the layer, the layer is slowed near the wall (zero at
  the surface), and the thickness is visibly exaggerated (1.6 diameters). The station lies ahead of Fig 12's
  transition point (2.90), so a laminar profile is consistent across the family.
- Legibility: nothing clipped or overlapping; profile arrowheads (3.4 pt) are visible at the 0.288-unit row spacing;
  width within 6.5 in. Local styles have new names and redefine nothing from the kit.

## Findings
| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The rocket's axis is the kit default: dash-dot through the body and on past the nose and tail. Figs 1 and 12 of this family (and the 1973 art of all three) draw the extensions as a thin solid line, with the dash-dot only inside the body. Fig 10 has no angle measured from the axis, so the default is acceptable. | fig10.tex:42 | Optional for family uniformity: `centerline=false`, then `\draw[centerline] (0.1,0) -- (6.3,0); \draw[thin line] (-0.5,0) -- (0,0) (6.4,0) -- (6.9,0);`. |
| 2 | note | `\csvline`, `\csvarrows`, `profile arrow` and `profile line` are duplicated word for word in Fig 13. | fig10.tex:10-37 | Report them as a kit candidate (style_suggestions). |
| 3 | note | The exaggeration of the boundary layer differs from Fig 12's ($\delta = 0.65$ here at x = 2.33, against 0.093 in Fig 12 at the same station). Each matches its own 1973 drawing, and both captions say "greatly exaggerated". | fig10.py:33 | None. |

## Verdict: pass (no must-fix)
