# v2 audit: ch2/fig02 (round 1)

Sources checked: figures/ch2/fig02.png (scan, zoomed 4-5x); figures/v2/ch2/fig02.pdf (rebuilt with `make fig
F=ch2/fig02`, 2.92 x 2.06 in, font embedded; rendered at 350 and 800 dpi) and build/v2/png/ch2-fig02-compare.png;
figures/v2/ch2/fig02.tex; figures/v2/inventory.csv row ch2-fig02; caption chapters/ch2-intro-sec1.tex:218-220;
citing text ch2-intro-sec1.tex:199-207 (right-handed screw, A toward B advances along C) and the Fig 4 caption
ch2-intro-sec1.tex:236-239; the axis definitions ch2-intro-sec1.tex:104-109; STYLE.md sections 13 and 16;
corrections/v2-figures.md; approved example ch2/fig03.tex (same view); ch2/fig01 render (A, B, C directions).

Checked and correct:
- Lettering: A, B, C, upright, at the axis ends, as in the scan and as D, E, F in the approved Fig 3. Nothing
  added; no lettering missing.
- View and handedness: the same true orthographic view as Fig 3 (x = (1.15, 0.61), y = (-1.15, 0.61), z = (0,
  1.38) cm: vertical/horizontal 0.53 = sin 32 deg, z/horizontal 1.20 = cos 32 deg / cos 45 deg). Completing the
  projection to an orthonormal screen frame with positive determinant puts the depth of x and y at -0.975 and of
  z at +0.862, so the TikZ frame is right-handed as viewed; with x = B, y = C, z = A, A x B = C (right-handed,
  ch2-intro-sec1.tex:204-207). Directions match the scan and Fig 1 (A up, B right and up, C left and up).
- Turning arrow: in the A-B plane at the head (`canvas is xz plane at y=0`), drawn from 267 deg down through
  180, 90 (A) and 0 (B) to -62 deg, so it turns A towards B; on the page it runs clockwise with its arrowhead at
  the lower right, as in the scan. A positive rotation about C, so a right-hand screw advances along +C: the
  point is towards C, the slotted head at the origin. The caption is true of the drawing.
- Screw: the thread is a right-handed helix about +C (code psi = 228.5 - u with y rising: A = cos t, B = sin t,
  C = ct, c > 0); the visible half (48.5 < psi < 228.5) is the side facing the viewer, so each crest appears as an
  arc bulging towards the point, and the head's visible side band lies up-left of its face, both consistent with
  the view. Cone silhouettes from the cylinder's silhouette points are symmetric about the projected axis (26 deg
  each side). Depth order right: the turning arrow (plane y = 0) passes in front of the shank (y >= 0.15, white
  knock-out), and the A and B axes in front of the head's side.
- Style and legibility: `thin vec` axes and turning arrow as in Fig 3; outlines 0.6 pt; hairline thread; labels
  \small; arrowheads clear at final size; nothing clipped or overlapping.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The screw is simplified: the scan's screw has a short threaded neck at the head, a plain shank, a threaded section, a thin rod and a small point (and a domed head with a curved slot); the redraw has one threaded shank, a conical point and a flat cylindrical head with a straight slot. The inventory allows simplification and nothing in the text depends on the detail. | fig02.tex:16-48 | None. |

## Verdict

pass (0 must-fix, 0 should-fix)
