# v2 audit: ch2/fig03 (round 1)

Sources checked: scan `figures/ch2/fig03.png` (2x upscale); redraw `figures/v2/ch2/fig03.pdf` (rendered at 350 and
700 dpi, detail crops of the nose, tail, CG and the three rotation arrows) and `build/v2/png/ch2-fig03-compare.png`;
source `figures/v2/ch2/fig03.tex` lines 1-49; inventory row `ch2-fig03` (`figures/v2/inventory.csv`:16);
`chapters/ch2-intro-sec1.tex`:104-120 (body axes D, E, F with the same directions as the right-handed A, B, C),
:196-212 (right-hand screw rule, citing sentence), :224-230 (caption); `STYLE.md` section 16 (3D drawings: true
orthographic view, elevation 32, azimuth 45); `figures/v2/tamrfig.sty`; TikZ `tikzlibrary3d.code.tex`:45-74
(which axes each `canvas is .. plane` maps to).

Checks made:
- **Handedness.** The text makes D, E, F right-handed in the same way as A, B, C: turning D towards E advances
  along F, so E x F = D, F x D = E. The source maps TikZ (x, y, z) = (E, F, D). That is a cyclic permutation,
  so it is right-handed. The screen vectors x = (1.15, 0.61), y = (-1.15, 0.61), z = (0, 1.38) cm are an
  orthonormal projection (both rows have norm 1.626 and are orthogonal). The viewer direction
  u x w = (-0.60, -0.60, +0.53) in (E, F, D) gives elevation 32 degrees, seen from behind (-E, -F) and above. This is
  a proper rotation, not a mirror image. The 1973 view has the same arrangement (D up, E up-right, F up-left, all
  seen from behind and above), and I confirmed that it is also right-handed: seen from +D, E turns
  counter-clockwise onto F.
- **Rotation senses** (verified from the arc parameters and on the 700 dpi render):
  - $\omega_D$: `canvas is xy plane`, angle increasing, so it runs E towards F. The arrowhead is at the left of
    the ellipse moving towards the viewer, which is counter-clockwise seen from +D. Positive.
  - $\omega_E$: `canvas is yz plane` (local x = F, local y = D), increasing, so it runs F towards D. The head is
    at the top moving towards -F. Positive.
  - $\omega_F$: `canvas is xz plane` (local x = E, local y = D), decreasing angle, so it runs D towards E. The
    head is up-left of the F axis moving towards +E. Positive.
  All three agree with the 1973 arrows. I read those off the cone-and-ball heads: $\omega_D$ moves left on the
  far side, $\omega_E$ moves towards +F at -D, and $\omega_F$ moves towards -D at +E.
- **View consistency.** The body silhouette angle is 48.5 degrees, and tan^-1(0.600/0.530) = 48.5. The visible
  half of the nose-base joint is the front half. The tail-end ellipse is correctly drawn in full, because the
  tail faces the viewer. The fins behind the body (+E, -D) and in front of it (+D, -E) are ordered by the depth
  n.p, and the front fins correctly cover the body's silhouette lines.
- **Content.** All of these are present: four swept fins, the dash-dot extension aft of the tail, the CG at the
  origin of the axes, the axes D (up), E (right), F (forward along the rocket, drawn from the nose tip), three
  elliptical rotation arrows ringing their axes ($\omega_F$ ahead of the nose, as printed), and the labels D, E,
  F, $\omega_D$, $\omega_E$, $\omega_F$. The caption (positive yaw, pitch and roll rates) and the citing sentence
  (all components positive) hold.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The CG is the house quartered `cg mark`, where the 1973 art (and the inventory note) has a small open circle. The house style uses this mark for C.G. and the text puts the origin at the C.G., so the meaning is unchanged. | fig03.tex:38 | none |
| 2 | note | The arrowheads are the house Stealth heads (`thin vec`), not the 1973 open cone-and-ball heads named in the inventory note. This is a modernisation; the senses are correct. | fig03.tex:40-44 | none |
| 3 | note | Each $\omega$ label sits beside its ellipse but not beside its arrowhead, as it does in 1973. $\omega_E$ (lower right of its ellipse) is about 4 mm from the +E fin tip, but it still reads with its ellipse at final size. | fig03.tex:45-47 | Optional: move $\omega_E$ up next to its arrowhead or next to the arc's lower end. |
| 4 | note | The inventory says the rocket and axes are reused unchanged in Fig 4, and that the rocket should match Figs 1 and 6. Those redraws do not exist yet, so consistency cannot be checked in this round. | inventory row | Check this when Figs 1, 4 and 6 are drawn. |

## Verdict

pass (0 must-fix, 0 should-fix)
