# v2 audit: ch3/fig25 (round 1)

Sources checked: scan `figures/ch3/fig25.png` (left half, right half and the vortex label zoomed 4-6x); redraw
`figures/v2/ch3/fig25.pdf` (current; 333.6 x 172.8 pt = 4.63 x 2.40 in; fonts all embedded), rendered at 400 dpi,
with the c-e region at 900 dpi, and `build/v2/png/ch3-fig25-compare.png`; `figures/v2/ch3/fig25.tex`,
`fig25.py`, `fig25-{wall,band,edge,a,b,c,d,e,zero,stream,heads,arrows,points}.csv`, `fig25.calib.json`; inventory
row `ch3-fig25` (`figures/v2/inventory.csv`:91); caption `chapters/ch3-sec3c-sec4a.tex`:245-251; citing text
:232-243 (full, stable profile at point a; at c an inflection point and zero wall gradient, eq. (110)),
:254-256 (reversal, vortex, rapid thickening at points d and e), :270-275 (photographs compared with the profile
of point c and with points d and e; a line of stationary fluid, forward flow outside it); `STYLE.md` sections 14
and 16; the house consistency rules (curve tag for cited points), as applied in Ch3 Fig 23 (A, B, C, S) and Fig 33
(R); `corrections/v2-figures.md`.

Checks made:
- **Lettering.** Everything in the inventory is present: "Undisturbed outer flow" with flow arrows, $U_\infty$
  and u over short arrows (outside and inside the layer), delta (a `\dimline` from the wall to the dashed edge,
  upright, 53 px = edge(30), checked), a-e at the profiles' feet, "Positive / pressure / gradient" with an arrow
  parallel to the wall below it, and "vortex". Nothing is added that changes the meaning.
- **Geometry.** The overlay, which I ran myself, gives 95% within 2.83 px for the wall and 2.24 px for the
  dashed edge. The profiles stand normal to the wall: n = (sin th, cos th) leans downstream on the falling wall,
  as in the scan, and their arrows run along the wall tangent.
- **Profiles.** All five are Falkner-Skan solutions of eqs. (38)-(39). a is full (beta = +0.05). b is inflected
  (-0.12). c is the separation profile with f''(0) = 0, eq. (110); at 900 dpi the curve leaves the wall tangent
  to its base line, so the text's "zero velocity gradient at the wall" is visibly true. d and e are on the lower
  branch with reversed flow at the wall: the curve crosses to the upstream side of the base line, with short
  reversed strokes. Overlay at 95%: a 2.83, b 2.00, c 2.24, d 8.06, e 2.83 px; the 1973 d has a deeper reversed
  layer.
- **Line of stationary fluid.** The dash-dot line is the computed u = 0 locus from c, and the d and e profiles
  cross zero exactly on it. The U-shaped streamlines (contours of psi) turn on it: their noses lie on the line at
  900 dpi. Arrowheads point downstream on the upper branches and upstream on the lower ones, with reverse-flow
  arrows along the wall at d, e and beyond. This is everything the text relies on ("a line of stationary fluid ...
  as at points d and e"; external flow forward outside it). Overlay: u = 0 line 11.0 px; streamlines 6.1-15.7 px
  (the scan's are freehand).
- **Family.** The profile styles, 10 px spacing, heads only on arrows of 9 px or more, the 10 px 45-deg wall band
  and the 1.2x scale are the same as in Figs 16-18. `streamline`, `stream head` and `stationary` are local styles
  under new names.
- **Layout.** No overlaps: c, d and e clear the pressure-gradient arrow and the reverse-flow arrows; "vortex"
  clears the streamlines. Nothing is clipped.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | must-fix | The station letters a-e are set as plain upright text. The text cites them as points ("at point a", "the separation point c", "points d and e"), so the house rule for letters that tag points cited by the text applies: `curve tag`. Chapter 3 already does this in the same section, Fig 23 (A, B, C, S) and Fig 33 (R). | fig25.tex:67 | `\node[curve tag] at ($(\p)!12pt!180:(\p top)$) {\p};` (move the tag a little further from the wall so that the 11 pt circle clears the hatch band) |
| 2 | should-fix | "vortex" floats in the recirculation zone with no leader. The inventory lists "vortex (with leader)": in the scan, the innermost recirculating streamline (near e) runs to the label. fig25.py already exports a point `noseD` on that streamline's turn, but the .tex does not use it. | fig25.tex:80; fig25-points.csv (noseD) | add a straight `leader` from the label to a point on the innermost U-shaped streamline (for example its lower branch near x = 500, or noseD), as in Ch2 Fig 39 |
| 3 | note (gate) | Computed against the 1973 art: d's reversed layer is shallower (95% 8.1 px), the u = 0 line is up to 11 px above the drawn dash-dot near d, and the streamlines are up to 15.7 px off (freehand in 1973). These are listed in the .tex header but not yet in `corrections/v2-figures.md`. | fig25.tex:7-9 | orchestrator: log them with the Ch3 items |
| 4 | note | The dash-dot line is the locus u = 0, which is the text's "line of stationary fluid" and "dividing line". The inventory calls it the "dividing streamline", but strictly psi = 0 lies a little above u = 0. The redraw follows the text, which is right. | fig25.py:24-27 | none |

## Verdict: fix
