# v2 audit: ch2/fig05 (round 1)

Sources checked: figures/ch2/fig05.png (scan, zoomed 2-8x); figures/v2/ch2/fig05.pdf (rebuilt with `make fig
F=ch2/fig05`, 2.36 x 2.41 in, fonts embedded; rendered at 350 and 700 dpi) and build/v2/png/ch2-fig05-compare.png;
figures/v2/ch2/fig05.tex; figures/v2/inventory.csv row ch2-fig05; caption chapters/ch2-intro-sec1.tex:334-336;
citing text ch2-intro-sec1.tex:278-321 (M = I gamma, gamma = M/I, omega = (M/I)t, alpha = (M/2I)t^2,
"illustrated in Figure 5"); frontmatter/about-this-edition.tex:257 ("the formulas beneath the flywheel");
STYLE.md sections 13 and 16; corrections/v2-figures.md; approved example ch2/fig03.tex (same view).

Checked and correct:
- Formulas, typeset and aligned on "=", beneath the wheel at the left as printed: $\omega = \gamma t$,
  $= \frac{M}{I}\,t$, $\alpha = \frac{\gamma}{2}\,t^2$, $= \frac{M}{2I}\,t^2$; they match the inventory, the scan
  and the text (gamma = M/I). about-this-edition.tex:257 stays true.
- Lettering: $M$ (inner arrow), $\omega(t)$ (outer arrow), $\alpha(t)$ (angle arc); nothing missing or added.
- Geometry: the Fig 3 view; the wheel turns on the TikZ y axis, which projects at 28 deg to the horizontal, as the
  scan's axis (27 deg). Wheel opaque, hub standing out of the face towards the viewer, axis (centre line)
  emerging behind the wheel's upper-left rim and running out through the hub to the lower right. The $M$ and
  $\omega(t)$ arcs (radii 0.5 and 0.76) both run clockwise on the page, from the lower right round to arrowheads
  just above the reference line, as in the scan.
- Angle: the reference line is the 3D horizontal along x (projects up-right at 28 deg, as the scan's up-right
  line); the wheel's line is turned from it by 25 deg (scan 24 deg; a face line at -23.9 deg projects exactly
  horizontal, which the scan's line is). The arc runs from the reference to the wheel's line with its one
  arrowhead at the wheel's line, as in the scan (zoomed: no head at the upper end), i.e. in the sense of $M$ and
  $\omega$, so a positive $\alpha = (M/2I)t^2$ is drawn consistently. The opposite reading (page-horizontal line
  fixed) would put the wheel's line counter to the drawn rotation, so the drafter's reading is the consistent one.
- Legibility: labels \small, formulas \small; $M$ clear of the dashed line (about 0.6 mm), $\alpha(t)$ clear of
  its arc; the leader to the outer arc is short and unambiguous; nothing clipped.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The redraw draws the fixed reference line dashed (`guide`) and the wheel's line solid; in the scan both are solid lines broken only where they cross the rim and the arrowheads. The added distinction agrees with the arrowhead and the rotation sense and changes no meaning (no text names the lines). | fig05.tex:31-32 | None; mention at the gate if the owner wants the scan's two solid lines. |
| 2 | note | $\omega(t)$ is set outside the face with a leader to the outer arc; the scan sets it on the face between the outer arc and the rim. At \small the label (about 0.35 cm high) does not fit the 0.33 cm gap, so the leader is reasonable. | fig05.tex:40-41 | None. |
| 3 | note | The 1973 art draws the axis across the face (dashed near the rim, solid near the hub, dashed inside the hub); the redraw treats the wheel as opaque and hides the axis behind it (the file header says so). The axis still visibly passes through the wheel. | fig05.tex:20-21, 49-50 | None. |
| 4 | note | The single-headed $\alpha(t)$ arc is drawn with an inline style (0.5 pt, one Stealth head) because the house `angle arc` has heads at both ends; the scan has one head. | fig05.tex:33-34 | Style suggestion: a one-headed `angle arc` variant in tamrfig.sty. |

## Verdict

pass (0 must-fix, 0 should-fix)
