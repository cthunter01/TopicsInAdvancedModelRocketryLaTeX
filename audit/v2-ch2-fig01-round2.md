# v2 audit: ch2/fig01 (round 2)

Sources checked: figures/ch2/fig01.png (scan; pixel zooms 4-16x with a grid at the origin, the nose and the
tail); figures/v2/ch2/fig01.pdf (current: written 0.8 s after the .tex; 355.6 x 246.9 pt = 4.94 x 3.43 in;
TeXGyreTermesX, NewTXMI, NewTXMI7 all Type 1 embedded); renders at 113.6 dpi (1 unit = 100 scan px, for a colour
overlay on the scan aligned at O), 400 dpi, and 2400 dpi around O; build/v2/png/ch2-fig01-compare.png;
figures/v2/ch2/fig01.tex; figures/v2/inventory.csv row ch2-fig01; caption chapters/ch2-intro-sec1.tex:120-123;
citing text ch2-intro-sec1.tex:104-115, 127-137; STYLE.md sections 13 and 16; corrections/v2-figures.md
(standing rules, pilot decisions); tamrfig.sty (outline, thin vec, centerline, cg mark, angle arc); round 1
audit (audit/v2-ch2-fig01-round1.md) and the round-1 fix notes.

Round-1 findings:
- 1 (F not visible from O to the nose): **resolved.** `\draw[centerline] (tip) -- ($ {\stail}*(F) $)` (line
  132) is drawn after the body and the nose-base ring, so F shows as a dash-dot line from the nose tip through
  O and past the tail, continued by the thin vec arrow beyond the tip. The front fins do not cover it: their
  roots sit 0.058-0.066 units from the axis on the page.
- 2 (occlusion not recorded): **resolved.** Header lines 21-24 record the 1973 f-F face drawn over the lower
  half of the forward body, the body put in front (standing rule 4), and the trimmed f-F mark.
- 3 (body 30% too slim): **resolved.** `\rad` = 0.088 (line 67), a diameter of 17.6 scan px. In the overlay the
  redraw's walls lie on the scan's from O to the nose ring. The f-F arc trim follows: at 400 dpi the upper
  arrowhead touches the nose's lower silhouette.
- Notes 4-6 (in-plane hatching, negative yaw, uniform clear band): unchanged, as accepted.

Checks of the round-1 changes:
- The new OA, Od, OD stubs (lines 133-140). I recomputed which half of the body each line leaves through. The
  test is the sign of (radial direction) . c, with c the camera direction (-cos32 cos45, -cos32 sin45, sin32):
  A +0.684, d +0.684, D +0.549 (near half), and B -0.506, C -0.236, E -0.626, e -0.474, f -0.684 (far half).
  So exactly OA, Od and OD are seen over the body from where they leave it, as drawn. The exit distances are
  rad/cos(pitch) = 0.0907 for A and rad = 0.088 for d and D, both normal to F. Each stub ends at 0.2 units,
  beyond the silhouette, where it overlaps the line drawn under the body. The page distances from the axis at
  0.2 are 0.110 (A), 0.114 (d) and 0.150 (D), against 0.088.
- The Od stub's dash phase: \dphase = 0.088 x |P(d)| (0.729) x 63.598 pt = 4.08 pt. The projection
  coefficients 0.70711, 0.37471, 0.84805 are the view's unit vectors divided by 63.598 pt = 2.2352 cm. At
  2400 dpi the stub's dashes run on into the original line's dashes past the silhouette, with no doubled or
  shifted dash.
- No hatching lies inside the body's silhouette on the near side. The A-d-D hatching starts at 0.245 units,
  0.135-0.184 page units from the axis.
- The O label at -(rad+0.02) n, anchored north east, sits below and left of the C.G. mark, clear of the lower
  silhouette, as in the scan ("O" below and left of the origin dot). Inventory: "O (origin, below the CG
  circle)".
- Lettering (A-F, d, e, f, O, and the six angle labels in their sectors) and line styles (Od, Oe, Of dashed;
  A-F arrowheads; d, e, f none) are unchanged from round 1 and still correct. The caption's C.G. origin and the
  text's "dashed line Of", the plane of A and Of, and the plane of Oe and Od all still hold.
- Legibility: nothing overlaps or is clipped at 400 dpi. The width is 4.94 in (at most 6.5 in).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The tail (tail ring and fins) sits about 15 scan px further aft than the scan's, not the 5 px the round-1 fix's doubt reports. Measured on gridded pixel zooms, the scan's tail-ring centre is at (343.8, 316.9), 93.4 px from the origin dot at (281.3, 247.5). Fig 6's scan gives the same, 92-94 px. The redraw puts it at 1.3 x \|P(F)\| x 100 = 1.3 x 0.8325 x 100 = 108.2 px, which I confirmed on the 113.6 dpi render. So the aft body is about 16% long (about 3.4 mm at final size). The fin sizes match: the right fin tip is 54 px from the ring in the scan and 49.5 px in the redraw. The header claims "body, fins and tail ring in the scan's proportions". The meaning is unchanged. | fig01.tex:67 (`\def\stail{-1.3}`), header lines 17-19 | Set `\stail` to about -1.12 (93.4/83.25). The fins, tail ring and aft centre line are all placed from `\stail`, so they follow. Make the same change in fig06.tex. Or keep -1.3 and correct the doubt and header to say the aft body is about 16% longer than the scan's. |
| 2 | note | The stubs are geometrically right, but they change how the drawing reads near O. In the scan, OA, Od and OD (and every other sector edge) run into the origin over the body. In the redraw they stop about 0.7 mm short of the C.G. mark, where they meet the body's surface. This is consistent hidden-line treatment, and the round-1 fix notes record it as a doubt. | fig01.tex:133-140 | None. Leave it to the owner at the gate (the fix notes say how to remove the stubs). |
| 3 | note | Header line 11, "the 1973 yaw turns E away from F", is loose. E and F stay perpendicular throughout; the yaw turns E away from C (F's starting direction), and F toward B. This is a code comment only and does not show in the figure. | fig01.tex:11 | Optional: "turns E away from C (where F starts)". |

## Verdict: pass

No must-fix. One should-fix (tail station) and two notes.
