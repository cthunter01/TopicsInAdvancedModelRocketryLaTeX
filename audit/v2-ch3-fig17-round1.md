# v2 audit: ch3/fig17 (round 1)

Sources checked: scan `figures/ch3/fig17.png` (left and right halves zoomed 3.3-4x); redraw
`figures/v2/ch3/fig17.pdf` (current; 321.6 x 187.7 pt = 4.47 x 2.61 in; fonts all embedded), rendered at 400 dpi,
with the A and O roots at 900 dpi, and `build/v2/png/ch3-fig17-compare.png`; `figures/v2/ch3/fig17.tex`,
`fig17.py`, `fig17-edge.csv`, `fig17-O.csv`, `fig17-B.csv`, `fig17-arrows.csv`, `fig17.calib.json`; inventory row
`ch3-fig17` (`figures/v2/inventory.csv`:83); caption `chapters/ch3-sec3b.tex`:161-168; citing text :121-128
(the corner points $AA_1B_1B$, $A_1B_1$ in the undisturbed $U_\infty$, AB contributing nothing by symmetry); Table 2
(:136-158, segments AB, AA_1, BB_1, A_1B_1, integrals 0 to h); eqs. (73)-(76), (80); `STYLE.md` sections 14 and 16;
`corrections/v2-figures.md`.

Checks made:
- **Lettering.** Everything in the inventory is present: "control surface" (a straight leader to the top band),
  $A_1$, A, $B_1$, B, O (an open circle at the trailing edge), y, x, $\ell$, $\tau_o$, h, $\delta$, $u(x,y)$ and
  $U_\infty$ under each of the three profiles. The notation follows STYLE 14 ($\tau_o$, $\ell$, $U_\infty$). The
  dimension letters are upright.
- **Control surface.** It is a rectangle with all four sides hatched on the inside. The scan hatches $AA_1$
  across the upstream profile and AB along the plate's plane, so this matches. $A_1B_1$ lies in the uniform
  flow, as the text requires. The two curved flow arrows leave through $A_1B_1$, and h runs from the plate to
  $A_1B_1$. The profile at $BB_1$ stands on the right side, as in the scan and as Table 2 uses it. The plate is
  drawn as a 1.6 pt line from the leading edge to O; this is a figure-local `plate` style under a new name.
- **Curves.** I checked fig17.py against the chapter. The edges are delta ~ x^0.8, eq. (80), reaching 58 px at
  O. The profile at O is (y/delta)^(1/7), eq. (74). The wake at B is a Gaussian defect whose one-side momentum
  thickness equals theta = 7/72 delta, eqs. (73) and (76), with its width set so that it reaches 0.99 U at the
  wake lines (+-delta). I re-solved this independently: a = 0.2331, b = 32.7 px, u(0) = 0.767 U. This makes
  the drag the momentum deficit at $BB_1$, as the text's argument requires.
- **Overlay.** I ran it myself. 95% of the points lie within 12.2 px (upper edge), 16.0 px (lower edge),
  6.0 px (profile at O) and 11.5 px (wake). These are the drafter's figures. The 1973 edges are
  laminar-looking (about x^0.4), and its wake dips to about 0.35 U. These are computed curves, used under the
  pilot decision.
- **Line styles.** Between O and B the edges continue dashed, and beyond B they are solid, as printed. The
  U_inf references at O and B are dashed verticals, as printed.
- **Layout.** Nothing is clipped. u(x,y) clears the solid wake lines. B and O sit at the lower left of their
  points, as printed.

I ran fig17.py once while checking the wake parameters, which rewrote its four CSVs. I then recompiled
fig17.tex into my scratch directory: the render is pixel-identical to the existing fig17.pdf, so the data are
unchanged.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note (gate) | The computed curves differ visibly from the 1973 art. The edges by eq. (80) are almost straight wedges (the art: parabola-like, about x^0.4, up to 16 px off). The wake's dip, set by momentum conservation, eqs. (73)/(76), is 0.77 U, against about 0.35 U printed. The .tex header cites `corrections/v2-figures.md` for this, but there is no Fig 17 entry there yet. The wake depth is a modelling choice: the book gives no wake equation, and the shape is Schlichting's Gaussian. The owner should see it. | fig17.tex:5-8; fig17.py:8-12 | orchestrator: add a Ch3 gate item (edges by eq. (80); wake depth by the momentum balance rather than the scan) |
| 2 | note | The profile arrows at y = +5 px at A and at O lie inside the 8 px hatched band of AB. They stay legible at 900 dpi, and the scan has the same clutter, but the hatch shows between the arrows. | fig17.py:34; fig17.tex:28 | optional: start the rows at +-10, or stop the AB band at the profiles' base lines |
| 3 | note | The corner letters $A$, $A_1$, $B$, $B_1$ (and O) stay math italic without curve-tag circles. Table 2 and the text use them as segment names in math ($AA_1$, $A_1B_1$), and circled subscripted letters would not match Table 2. This is a deliberate exception to the "cited points use curve tag" rule. | fig17.tex:64-68 | confirm at the consistency pass |
| 4 | note | The vertical from the leading edge to the x and ell dimensions is a solid `extension` line, where the scan's is dashed. This is the house dimension style and does not change the meaning. | fig17.tex:76 | none |

## Verdict: pass (no must-fix)
