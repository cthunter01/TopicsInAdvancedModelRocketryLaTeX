# v2 audit: ch3/fig16 (round 1)

Sources checked: scan `figures/ch3/fig16.png` (profile, element and tau_o end zoomed 4x and 8x); redraw
`figures/v2/ch3/fig16.pdf` (current: newer than the .tex and .py; 324.9 x 148.3 pt = 4.51 x 2.06 in; fonts all
embedded), rendered at 400 dpi, and `build/v2/png/ch3-fig16-compare.png`; `figures/v2/ch3/fig16.tex`, `fig16.py`,
`fig16-body.csv`, `fig16-profile.csv`, `fig16-arrows.csv`, `fig16-points.csv`, `fig16.calib.json`; inventory row
`ch3-fig16` (`figures/v2/inventory.csv`:82); caption `chapters/ch3-sec3a.tex`:570-576; citing text :557-565
(eq. (58): tau_o, b, ell, ds, phi "explained pictorially in Figure 16"); Table 1 (Blasius f'); `STYLE.md`
sections 14 and 16; `corrections/v2-figures.md` (standing rule 4); the family's other figures (17, 18, 25).

Checks made:
- **Geometry.** The body is the scan's teardrop, a half ellipse for the nose and two circular tail arcs. The overlay
  gives 95% of the points within 2.00 px (max 3.16 px). I recomputed the element at x = 240: half-thickness 51.77,
  slope 0.4149, so phi = 22.5 deg. The dashed line meets the axis at V = 115.2, as in fig16-points.csv, and it is
  the true tangent (standing rule 4; the scan's line is about 21 deg). The profile's base line is normal to the
  surface and its arrows are parallel to the tangent, as in the scan. tau_o runs along the tangent from the
  element's upstream edge and ends near the printed end (drawn (365, 103), printed about (345, 108)).
- **Profile.** u/U = Table 1's f'(eta) up to eta = 7, as stated. The overlay gives 95% within 1.00 px. There are
  11 arrows at even 10 px spacing (the scan has about 12), and the top arrow is U(x).
- **Lettering.** U(x), u(y), $\tau_o$ (letter o, STYLE 14), ds, $\phi$ (not varphi, STYLE 14), $U_\infty$ and x are
  all present. b and ell are not lettered, as printed. Nothing is added.
- **Marks.** phi is marked by two `angle arc single` arcs from outside, landing on the dashed tangent and on the
  axis, as in the scan. ds is a grey double-arrow dimension between the two normals of the cleared strip, with its
  label below it in the strip, clear of the right line by about 0.6 mm. tau_o carries an arrowhead; the scan's
  line also ends in a small head (8x zoom).
- **Style.** The hatch is 45 deg; the centre line is dash-dot; the flow arrows are thin vec; the profile styles
  are identical to Figs 17, 18 and 25 (s1 1 pt curve, 0.5 pt arrows, 3.4 pt heads, 10 px spacing, 1.2 times the
  printed size). Labels are \small ink. Nothing overlaps or is clipped.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | phi is 22.5 deg on the true tangent at the element, where the 1973 line is about 21 deg and slightly off tangent (standing rule 4). It is not yet in `corrections/v2-figures.md`. | fig16.py:12-14 | record under "Minor (logged only)" with the Ch3 items |
| 2 | note | The ds label sits below the dimension in the cleared strip, not in a gap of the line, because the dimension is only about 5 mm long. This is legible and matches the scan's placement of ds beside its arrow; `\dimout` would put the label outside the strip, away from the element. | fig16.tex:40-41 | none |
| 3 | note | The cleared strip under ds stops at a straight edge 40 px deep with no closing line, as the scan's strip also does. | fig16.tex:35-36 | none |

## Verdict: pass (no must-fix)
