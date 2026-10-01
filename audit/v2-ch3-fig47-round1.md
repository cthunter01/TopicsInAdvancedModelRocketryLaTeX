# v2 audit: ch3/fig47 (round 1)

Sources checked: scan `figures/ch3/fig47.png` (zoomed x3, both halves); redraw `figures/v2/ch3/fig47.tex`,
`fig47.py`, `fig47.csv`; rebuilt with `make fig F=ch3/fig47` (5.89 x 3.57 in; one font, TeXGyreTermesX-Italic,
embedded) and rendered at 300, 600, 1200 and 3000 dpi (cells and the apexes of (b), (c)); inventory row `ch3-fig47`;
caption and citing text `chapters/ch3-sec6a.tex:289-329`; `figures/v2/tamrfig.sty` (phantom, hidden, hatch, panel);
approved Ch2 Figs 41, 43; STYLE.md sections 14, 16.

Checks run (fig47.py's `run()` evaluated in memory; no file written):
- Cone R = 1, H = 2.5, half-angle alpha = 21.80 deg. Planes at beta = 48, 68.20 (= 90 - alpha) and 76 deg from
  the horizontal, so 42, 21.80 and 14 deg to the axis. The caption needs "greater than", "equal to" and "less
  than" the half-angle, and that holds. Eccentricity sin(beta)/cos(alpha) = 0.800, 1.000, 1.045: ellipse,
  parabola, hyperbola. Every section point lies on the cone (|r - k(H - z)| at most 2e-16). The ellipse closes
  above the base (z 0.70-1.81); the parabola and hyperbola end on the base chord.
- Noses: (a) a half spheroid with the section's semi-axes A = 0.745, B = 0.446 (l/d 0.83), the same 1.5x scale
  as the middle ellipse; (b), (c) the segments cut off by the base chord, revolved about their axes (l/d 1.74,
  1.42); (d) a tangent ogive whose length is the half chord (0.626 rho) and whose base radius is the segment
  height (0.22 rho), profile tangent at the base and r = 0 at the tip (l/d 1.42); (e) the triangle's own altitude
  2.2 and base 1.13. Each nose matches its top drawing. The (d) and (e) generating regions keep the orientation
  of the hatched half-segment and the triangle.
- Hidden lines (house view, C = (-0.600, -0.600, 0.530)): the base arcs and silhouette generators are coded
  correctly in all three cones. The back of the base is hidden by the cone, edges behind the opaque plane are
  hidden, and the piece on the viewer's side is cut away. The silhouette generators meet the section curves
  tangentially, as they must.
- Overlap of the cut-away lines (code 7) with solid outlines, from the page coordinates: within 0.3 mm of an
  outline for 0.46 cm in (a), 1.05 cm in (b) and 1.80 cm in (c).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | In (c), and less so in (b), the cut-away cone's right silhouette (ink2 dashes) runs on top of the section's right edge from the vertex down. For 1.8 cm in (c) and 1.0 cm in (b) it is within 0.3 mm of the black outline, so at final size the hatched region's edge reads as a ragged double line (page x about 7.6-8.4 cm, y -0.6 to -1.6 cm in (c)). The geometry is right: the edge must touch that generator. But the planes are placed so that the near-straight hyperbola arm runs along it, from a vertex close to the apex to a chord end close to the base's silhouette point. The 1973 (c) puts the plane so the hatched sliver stays well inside the outline. | fig47.py:74-75 (PLANES "b", "c": z0, gamma); fig47.py:184 | Re-place the (c) plane, and if needed the (b) plane, by changing gamma and/or z0, so that the plane does not cut the right silhouette generator except near the apex (a narrower sliver in front of the axis, as printed). Alternatively, drop the code-7 points within about 0.4 mm of a section outline. Check again at 600 dpi. |
| 2 | should-fix | The cone piece on the viewer's side of the plane is drawn in `hidden, draw=ink2`: the hidden-edge dash pattern, only greyer. The kit defines `phantom` as "an outline in an alternate position, or a part shown for context only ... ink2 for context", and approved Ch2 Fig 41 draws its context parts in `phantom, draw=ink2`. At 0.45 pt the grey dashes are hard to tell from the black hidden dashes of the kept piece. In (a), for example, the right generator changes from hidden to cut-away at the ellipse with no visible change. | fig47.tex:28 (code 7) | `\addplot[phantom, draw=ink2, ...only code=7]`, as Ch2 Fig 41. The kept piece's hidden edges stay `hidden` in ink. |
| 3 | note | Content matches the caption and inventory. (a)-(c): one cone cut at the three inclinations, sections hatched (cut surfaces, 45 deg, `hatch`), the apex piece dashed, the plane drawn as an opaque rectangle. (a): the middle ellipse face-on, divided along its minor axis, upper half hatched, centre line on the major axis. (d): circle with centre lines, chord, solid radial bisector, the left half-segment hatched ("shaded" in the caption), as printed. (e): right triangle with right-angle box. Noses: the axis as a centre line, a rotation arrow round it below the base in each cell (left to front to right, as printed), the base circle phantom, the (d) and (e) other half in phantom (an alternate position; printed dashed). The text's description of (d) (a diameter and the half-chord perpendicular to it) bounds the same region as the caption's (a chord and a radial bisector), so the drawing satisfies both. | fig47.py:166-301 | none |
| 4 | note | The noses are drawn as their generating sections in the meridian plane facing the viewer, foreshortened by cos 32 deg, plus the swept base circle. They are not the true silhouettes of the solids, which would be tangent to the base ellipses. This is the 1973 convention and the construction the caption describes, so there is no change. One side effect: in (e) the phantom left generator meets the dashed base ellipse at a shallow angle near its left end, and the two dash patterns tangle over about 2 mm. | fig47.py:203-226; cell (e) bottom left | Optional: none needed; if revisited, end the phantom generator at the ellipse without overlap. |
| 5 | note | Lettering: the circled (a)-(e) are set in the house panel style, italic, at the lower right of each cell on one baseline. The caption cites them as "(a):" and so on, so these are panel letters, not curve tags. No other lettering, as printed. The ruled box becomes ink2 rules between the cells without an outer frame, as in Ch2 Fig 43. The (d) half-segment is small (about 2 x 6 mm, 3 hatch lines), as printed, and legible. | fig47.tex:36-39 | none |

## Verdict: pass (no must-fix)
