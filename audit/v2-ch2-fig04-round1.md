# v2 audit: ch2/fig04 (round 1)

Sources checked: figures/ch2/fig04.png (scan, zoomed 2x); figures/v2/ch2/fig04.pdf (rebuilt with `make fig
F=ch2/fig04`, 3.96 x 2.21 in, fonts embedded; rendered at 350 dpi) and build/v2/png/ch2-fig04-compare.png;
figures/v2/ch2/fig04.tex and a diff against the approved figures/v2/ch2/fig03.tex; figures/v2/inventory.csv row
ch2-fig04; caption chapters/ch2-intro-sec1.tex:236-239; citing text ch2-intro-sec1.tex:199-213 (arrow along the
axis, direction by the sign, length proportional to the magnitude); Fig 3 caption ch2-intro-sec1.tex:227-229;
STYLE.md sections 13 and 16; corrections/v2-figures.md.

Checked and correct:
- Rocket, axes and view: the diff with fig03.tex shows the rocket, fins, centre line, C.G. mark and D, E, F axes
  copied unchanged; only Fig 3's three rotation arcs and their labels are replaced by the three vectors. Same
  orthographic view (TikZ x = E, y = F, z = D), right-handed.
- Lettering: D, E, F and $\omega_D$, $\omega_E$, $\omega_F$ (uppercase subscripts as in the book's text and Fig 3),
  each beside its arrowhead as in the scan ($\omega_F$ above the body, $\omega_E$ below right of its head). Nothing
  added; the speck above-right of D in the scan is not drawn.
- Vectors: each from the C.G. along its own positive axis, $\omega_D$ along +D (0 to 1.2), $\omega_E$ along +E (0
  to 1.3), $\omega_F$ along +F on the rocket's axis towards the nose (0 to 1.55), drawn over the body as in the
  scan. These are the advance directions of a right-hand screw turned in the senses of Fig 3 (D: E towards F; E:
  F towards D; F: D towards E), so the caption's comparison with Figs 2 and 3 holds. Proportions match the scan
  (heads at about half of each axis; $\omega_F$ about half-way to the nose base).
- Style: vectors `vec` (1.3 pt, stealth heads) over `thin vec` axes, so the vectors read apart from the axes by
  weight, as the scan's open heads did. C.G. mark drawn last over the vector tails. Labels clear of the body
  lines and axes; arrowheads visible at final size; nothing clipped.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The scan's vectors have open cone-and-ball heads on the thin axis line, with a gap in the axis beyond each head; the redraw uses the house `vec` arrow over a continuous axis. This is the approved modern restyle; the meaning is unchanged. | fig04.tex:42-44 | None. |

## Verdict

pass (0 must-fix, 0 should-fix)
