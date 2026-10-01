# v2 audit: ch2/fig06 (round 1)

Sources checked: figures/ch2/fig06.png (scan, zoomed 3-12x); figures/v2/ch2/fig06.pdf (current: newer than the
.tex; 358.4 x 245.7 pt = 4.98 x 3.41 in, three Type 1 fonts all embedded; rendered at 300 and 600 dpi) and
build/v2/png/ch2-fig06-compare.png; figures/v2/ch2/fig06.tex, diffed against figures/v2/ch2/fig01.tex;
figures/v2/inventory.csv row ch2-fig06; caption chapters/ch2-intro-sec1.tex:415-419; citing text
ch2-intro-sec1.tex:377-386 (Z always coincides with F; $\alpha_X = \alpha_D$, $\alpha_Y = \alpha_E$, $\alpha_Z =
0 \ne \alpha_F$); STYLE.md sections 13 and 16; corrections/v2-figures.md (standing rule 2: lowercase f, no O);
the Fig 1 audit (audit/v2-ch2-fig01-round1.md), whose geometry checks carry over because the code is identical.

Checked and correct:
- It is Fig 1's drawing: the rotations, view, sectors, angle arcs, hatching and rocket code are line for line
  Fig 1's. Only these differ: the lettering macros; the `de line` style (solid, 0.6 pt, no arrowheads, in place
  of dashed); and the origin, which has no O label.
- Lettering against the scan and the inventory: A, B, C, D, E, "F, Z" (at the F arrow), X (end of Od), Y (end of
  Oe), lowercase f (end of the dashed Of, kept: standing rule 2). Sectors: A-X $\alpha_Y$, X-D $\alpha_F$, B-Y
  $\alpha_X$, Y-E $\alpha_F$, C-f $\alpha_X$, f-F $\alpha_Y$. These match the scan and follow the text's
  $\alpha_X = \alpha_D$, $\alpha_Y = \alpha_E$. No origin letter (the scan has only the small circle; here the
  house C.G. mark). Uppercase subscripts (STYLE 13).
- Geometry against the caption: X = Od and Y = Oe are the body axes after yaw and pitch, before roll, which is
  what "follow the rocket in yaw and pitch but maintain a zero roll angle" requires. Z is along F. D and E are X
  and Y rolled by $\alpha_F$ in the plane of X and Y.
- Line styles: OX is solid with no arrowhead in the scan (12x zoom: a plain stroke past the corner to the X); OY
  is solid in the scan (the fold between the B-Y and Y-E faces is a continuous line, unlike Fig 1's dashed Oe).
  The redraw draws both solid and without heads. Of stays dashed.
- Size and legibility: 4.98 in wide (under 6.5 in); "F, Z" clear of the arrow and the nose; X, Y, B, E clear of
  each other; nothing clipped.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | As in Fig 1 (finding 1): F, Z is not visible between O and the nose. The scan draws the sector's edge along the forward body's axis; the redraw's centre line stops at O. Here it matters more, because the text's point is that Z always coincides with F, and the axis that carries both letters is shown only by the arrow beyond the nose. | fig06.tex:114 | Same fix as Fig 1: `\draw[centerline] (O) -- ($ {\snb}*(F) $);` (or to the tip) after the body outline. Keep the two files identical apart from lettering. |
| 2 | should-fix | As in Fig 1 (finding 3): the body radius 0.062 gives a body about 30% slimmer than the scan's (17.5 px at 150 dpi, that is, 0.175 units). | fig06.tex:49 | Same value as Fig 1 after its fix (about 0.088). |
| 3 | should-fix | As in Fig 1 (finding 2): the scan draws the hatched f-F face over the lower half of the forward body (the strip of hatching along the body's lower side is visible in this scan too); the redraw puts the body in front, which is correct for the right-handed view but not recorded. | fig06.tex:1-6 (header) | Have the header say that it follows Fig 1's documented occlusion change (once Fig 1's header records it). |
| 4 | note | Doubt: in the scan the end of OY past the corner (about (525-532, 153-156) at 150 dpi) thickens and tapers to a point. It could be a small arrowhead, but it is much smaller than the B and E heads and cannot be read with certainty. OX clearly has none. Drawing both without heads is consistent, and either reading leaves the meaning unchanged. | fig06.tex:18, 89-90 | None. Mention in the gate notes if the owner wants arrowheads on X and Y like the other axes. |

## Verdict

pass (0 must-fix, 3 should-fix)
