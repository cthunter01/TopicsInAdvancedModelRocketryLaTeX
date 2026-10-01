# v2 audit: ch3/fig27 (round 1)

Sources checked: scan `figures/ch3/fig27.png` (2x); redraw `figures/v2/ch3/fig27.pdf` (300 dpi; `pdffonts`); source
`figures/v2/ch3/fig27.tex` (the body is computed in TikZ; no .py/.csv); inventory row `ch3-fig27`
(`figures/v2/inventory.csv`:93); caption and citing text `chapters/ch3-sec4b.tex`:33-57 and eqs. (111)-(118);
`corrections/v2-figures.md` standing rule 1 (Ch3 Fig 27 named); `STYLE.md` sections 14 and 16; `tamrfig.sty`
(dotted guide, vec, leader, hatch, \breakline); Fig 28's script for the shared half-body.

Checks made:
- **Control surface.** It is drawn in the kit's `dotted guide`, as the text says ("as indicated by the dotted
  line"; printed dashed). This is standing rule 1, which names this figure. Its left face is 4.36 R ahead of the
  nose (scan 4.5 R). Its right face runs through the middle of the slot (16.56-17.06 R; face at 16.81 R), as
  printed. Its top and bottom lie just inside the tube wall (4.66 R against 4.9 R).
- **Half-body.** It is the axisymmetric Rankine half-body, w = R cos(t/2) at X = R/2 + R cos t/(2 sin(t/2)). I
  rederived it from psi = w^2/2 - m cos(theta), m = R^2/4: the nose (t = 180 deg) is at X = 0, and at the slot
  (t = 3.57 deg) X = 16.53 R, w = 0.9995 R. This is the same body as Fig 28, whose computed contour sits on the
  Fig 28 scan within 1 px.
  - The front body is a closed outline: nose to the slot face.
  - The after-body runs from the far face of the slot to the kit's `\breakline` (the cut-off tube break, as in
    Ch2 Fig 36). The 1973 art draws a tube-break loop there.
- **Lettering.** Every inventory item is present and placed as printed, all in book notation (lowercase p, u;
  italic subscripts 1, 2; STYLE s.14):
  - $p_1$ left of the upstream face and $p_2$ right of the downstream face, near the top.
  - $u_1$ over a `vec` on the axis crossing the upstream face.
  - $u_2$ over a `vec` below the body crossing the downstream face.
  - $A_1$ with a straight leader to the upstream face of the control surface (the scan's leader has a small
    hook; house rule: straight).
  - $A_2$ with a straight leader to the after-body's face at the slot, as printed.
- **Caption and text.**
  - A_1 is the frontal area of the control surface.
  - A_2 is the frontal area of the half-body.
  - The half-body is enclosed in a wide hollow cylinder.
  - The slot is "at a sufficient distance from the nose".
  - All four are true of the redraw.
- **Walls.** The walls of the hollow cylinder are drawn in section: thin hatched bands, `outline, hatch`, 45 deg.
  The 1973 art has heavy solid lines. The section is a fair modern reading of "a wide, hollow cylinder", and the
  hatch keeps its meaning (a cut surface).
- **Size.** Page 5.12 x 1.67 in; fonts embedded. No label touches a line: u_1 clears the dotted face by about
  2 mm, and the A_2 leader stays right of the face.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The tube walls are hatched bands (in section), not the 1973 heavy lines. The change is consistent and keeps the meaning. | fig27.tex:19-21 (the `\foreach` over the two walls) | None; the gate may prefer plain heavy `outline` lines if it wants the 1973 look. |
| 2 | note | The u_1, u_2 arrows are the heavy house `vec`; the 1973 arrows are light. This is consistent with Fig 28's u_o. | fig27.tex:32-35 | None. |

## Verdict: pass

No must-fix and no should-fix.
