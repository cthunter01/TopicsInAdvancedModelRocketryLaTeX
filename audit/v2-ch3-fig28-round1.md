# v2 audit: ch3/fig28 (round 1)

Sources checked: scan `figures/ch3/fig28.png` (2x; ink columns read at 10 stations); redraw
`figures/v2/ch3/fig28.pdf` (300 dpi whole, 600 dpi crops of the (a) nose and ordinate and of the (b) nose;
`pdffonts`); sources `figures/v2/ch3/fig28.tex`, `fig28.py`, `fig28-*.csv`, `fig28.calib.json`; inventory row
`ch3-fig28` (`figures/v2/inventory.csv`:94); caption and citing text `chapters/ch3-sec4b.tex`:33-41, 97-119;
`corrections/v2-figures.md` (pilot gate on outside formulas; no Fig 28 entry yet); `STYLE.md` sections 14 and 16;
Fig 27 (the same half-body).

Checks made:
- **Potential flow.** I rederived it independently: point source m = R^2/4 in a unit stream, Stokes psi =
  w^2/2 - m cos(theta), body psi = m, u = 1 + m x/r^3, v = m w/r^3, C_p = 1 - (u^2 + v^2). On a fine grid:
  - The body satisfies psi = m to 1e-16.
  - C_p min is -0.33333 at X = 0.789 R (w = 0.8165 R); C_p = 0 at X = 0.296 R.
  - C_p is -0.3125 at 1 R, -0.139 at 2 R, -0.066 at 3 R and -0.007 at 9 R.
  - The script's docstring and CSVs agree.
- **Overlay** (`digitize.py overlay`, the drafter's three calibrations, residual 0.00 px):
  - (a) body: 95% 1.00 px.
  - Streamlines s1-s4: 95% 1.00, 2.83, 1.68, 2.00 px. The upstream radii 0.35, 0.70, 1.05 and 1.40 R match the
    scan's 0.358, 0.704, 1.05 and 1.396 R; downstream they are 1.06, 1.22, 1.45, 1.72 R against drawn about
    1.01 (merged with the body), 1.23, 1.47, 1.64 R.
  - (b) body: 95% 1.00 px.
  - (b) positive envelope: 95% 3.00 px.
  - (b) suction envelope: 95% 2.00 px, but only because it lies inside the scan's dense stroke field. The
    printed suction lobe reaches about 1.6 R from the axis; the computed one reaches 1.33 R.
  - **(a) pressure curve: 95% 9.0 px (1.5 mm), MISMATCH.** The 1973 curve dips to about -0.39 near X = 1.1 R
    and returns to zero almost linearly at about X = 9 R. The computed one dips to -1/3 at 0.79 R and is back to
    -0.03 by X = 4 R.
- **Text.**
  - The streamlines of (a) are convex toward the body near the stagnation point and concave further aft.
  - (b) shows positive pressure on the forward part of the nose and suction on its after portion, in balance.
  - Both hold on the computed drawing.
- **Lettering.**
  - (a): the ordinate title $\dfrac{p}{(\rho/2)u_o^2}$ (letter o, STYLE s.14).
  - Ordinate ticks 0.2-1.0 on a short axis rising from the nose, with the zero on the dash-dot axis.
  - $u_o$ over a `vec` on the axis upstream; the centre line starts after the arrowhead, as printed.
  - (b): the dash-dot axis. The positive lobe's envelope is dashed. The suction lobes are solid, then a dashed
    tail as the suction dies away (as printed). The strokes lie along the outward normal at every 0.12 R of arc.
  - The panel letters (a), (b) are in the `panel` style at the lower right of each drawing (the 1973 circled
    letters are centred below).
- **Encoding.** The pressure curve (a) and the pressure diagram (b) are s1. The body, streamlines and lettering
  are ink, and the ordinate is ink2 at axis weights. The local styles (`streamline`, `pressure stroke`,
  `positive/suction envelope`, `suction tail`) have new names. `streamline` matches Fig 23's.
- **Size.** Page 5.14 x 2.94 in; fonts embedded. Nothing overlaps: the ordinate title clears u_o, and (a) sits
  below the lowest streamline.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The computed potential-flow curve in (a) misses the 1973 curve (overlay 95% 9 px, 1.5 mm): its minimum is -1/3 at 0.79 R against a drawn -0.39 at 1.1 R, and it recovers much faster. The (b) suction lobes are correspondingly lower (1.33 R from the axis against about 1.6 R). The Rankine half-body is an outside formula, but not one the pilot gate approved by name (USSA-1962, Lamb, slender-body, Mangler). fig28.py says the difference is in corrections/v2-figures.md, but there is no Fig 28 entry there. | fig28.py docstring (line 18); corrections/v2-figures.md | Orchestrator: add a Ch3-gate item to corrections/v2-figures.md (computed Rankine half-body, C_p min -1/3 at 0.79 R, against drawn about -0.39 at 1.1 R with slow recovery; Fig 27 uses the same body). It should also be named in About This Edition with the other outside formulas. The figure itself needs no change if the gate keeps the computed curve. |
| 2 | note | The 1973 (b) is not drawn to the scale of its own (a): its suction lobe implies about -0.5 at the positive lobe's 1.5 R per unit. The redraw sets both lobes to one scale, so they are consistent. | fig28.py (K = 1.5) | None. |
| 3 | note | The u_o arrow is the heavy house `vec`; the 1973 arrow is light. This is consistent with Fig 27. | fig28.tex:25 | None. |

## Verdict: pass

No must-fix. One should-fix, for the orchestrator: log the computed-versus-drawn difference for the gate.
