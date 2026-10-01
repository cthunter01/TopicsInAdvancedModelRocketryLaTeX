# v2 audit: supplement/ch2-fig36-1994 (round 1)

Sources checked: figures/supplement/ch2-fig36-1994.png (scan, zoomed 3-4x, pixel-measured);
figures/v2/supplement/ch2-fig36-1994.pdf (built 17:45:30, after the .tex; rendered 400 dpi; 362.8 x 219.6 pt =
5.04 x 3.05 in; all fonts embedded); build/v2/png/supplement-ch2-fig36-1994-compare.png;
figures/v2/supplement/ch2-fig36-1994.tex:1-75; its sibling figures/v2/ch2/fig36.tex (source diffed: the two bodies
are identical except the switch line; renders differ only at the AR numerator and the ell line);
figures/v2/inventory.csv rows sup-ch2-fig36-1994 and ch2-fig36; caption chapters/ch2-sec4.tex:319-337 and citing
text ch2-sec4.tex:303-308; eqs. (85)-(90) ch2-sec4.tex:378-434; ch2-sec6.tex:438-443; supplement Part
backmatter/supplement/s-ch2-1994.tex:136-164, 180-188; s-ch2-2022.tex:98-102; ch2-symbols.tex:114, 137, 144, 146;
corrections/v2-figures.md (standing rules, pilot decisions, Minor list); STYLE.md sections 13 and 16;
figures/v2/tamrfig.sty; approved example figures/v2/ch2/fig39.tex (C.P. leaders).

Checked and correct:
- Lettering, all 15 inventory items present and in the book's notation: $\AR = \dfrac{4s}{c_r + c_t}$ at left
  (`\AR` ligature, lowercase $s$, $c$ as the text writes them); $Z_T$ at the root leading-edge level;
  $\bar{Z}_{T(B)}$ at the fin-set C.P. level (standing rule 2 keeps it against eq. (89)'s $\bar{Z}_T$);
  $\dfrac{c_r}{2}$ ($Z_T$ to mid-root); $c_r$; $s$ (body surface to tip, at top); $\Gamma_c$; $\ell$ on the
  dash-dot mid-chord line with arrowheads at both ends; $\dfrac{c_t}{2}$ and $c_t$ at right; $\bar{Y}_T$
  (centre line to the dashed line through C.P.$_T$); $r_t$ (centre line to body surface); C.P.$_{T(B)}$ and
  C.P.$_T$ with leaders to `cp mark`s; "Rocket centerline" with an arrowed leader to the dash-dot centre line.
  $x_t$ is not marked (as printed; logged in corrections Minor). Nothing added.
- Geometry against the scan (scan px): $c_r$ 322 (scan 322: $Z_T$ row 110, root TE 432), $c_t$ 175 (scan 175:
  tip LE 366, TE 541), $x_t$ 256 (256), $s$ 262 (261-264), $r_t$ 58 (56.5: centre line col 446.5, body col 503),
  mid-root 161 below $Z_T$ (scan row 271 = 161), mid-tip at $x_t + c_t/2$ (scan row 454 = 344). Drawn at 0.87 x
  scan size (x = y = 0.0147 cm per scan px), so the fin keeps the 1994 proportions.
- Equations, evaluated independently: $K = (c_r + 2c_t)/(c_r + c_t) = 1.35211$; eq. (89)
  $\bar Z - Z_T = 256/3 \cdot K + (322 + 175 - 322\cdot175/497)/6 = 115.38 + 63.94 = 179.32$ (tex line 21 matches;
  scan 177, so the Z-bar level is 2 px from the 1994 art and 18 units below mid-root, as printed); eq. (90)
  $\bar Y_T - r_t = 262/3 \cdot K = 118.08$ (tex line 22); $\Gamma_c = \arctan(182.5/262) = 34.86^\circ$ (scan
  34.7 deg), measured from the perpendicular to the axis at mid-root to the mid-chord line, as the Symbols list's
  "mid-chord sweep angle" requires; $\ell$ runs mid-root (0,-161) to mid-tip (262,-343.5), so $\ell = s/\cos\Gamma_c$
  (eq. (87)) holds by construction (319.3 both ways). Tip chord parallel to the axis ("fins of the form shown").
- Caption (ch2-sec4.tex:319-326): $Z_T$ at the root/leading-edge intersection, $\bar Z_{T(B)}$ at the fin-assembly
  C.P. (the mark on the centre line), $\ell$ mid-root to mid-tip, AR of the two-fin wing ($4s$, eq. (86)): all
  true. Supplement text s-ch2-1994.tex:183-185 ($\bar Y_T$, $s$, $c_r$, $r_t$, $c_t$ illustrated): all present;
  $\bar Y_T$ measured from the rocket centre line as eq. (90) defines it.
- Style: outlines 0.6pt ink; centre line, mid-chord line, extensions, dimensions, leaders ink2; C.P. guide dashed
  (`guide`); `\dimline` labels in white gaps; `angle arc` with both heads landing on the mid-root horizontal and
  the mid-chord line; `cp mark` with the Z-bar extension and the leaders shortened to the rim, as in the approved
  fig39. Labels \small, 5.04 in wide.
- Legibility at 400 dpi: no overlaps; the tightest spots are all clear: $r_t$ (58 units = 8.5 mm; label in the gap
  with both arrow shafts visible), the C.P.$_{T(B)}$ label to the $c_r$ dimension line (about 2.5 mm) and to the
  $c_r$ label, $\Gamma_c$ to the C.P.$_T$ mark (about 1.5 mm). Only the ends of the centre line (top) and of the
  body surface (bottom) touch the page edge, which is where they are meant to run out; nothing is clipped visibly.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | C.P.$_T$ and its dashed line are placed by eq. (90) at $\bar Y_T - r_t = 118$ units, 13.6 scan px (about 2 mm at final size) outboard of the 1994 art (scan dashed line at col 607.5, i.e. 104.5 px from the body); the Z-bar level by eq. (89) is within 2 px of the art. This follows the pilot rule (computed from the book's equations), but the owner has an open gate item on the same question for Ch2 Figs 34, 35 (drawn C.P. marks vs the equations). | tex lines 21-22, 30, 40 | No change to the figure. Orchestrator: log Fig 36 (1994 and 1973: the 1973 art has the dashed line at 64.5 px against 75.9 by eq. (90) at its own scale) beside the Figs 34, 35 gate item so the owner decides all three alike. |
| 2 | note | The printed C.P. leaders end in small arrowheads at the marks; the redraw's leaders are plain lines stopping at the mark's rim, while the "Rocket centerline" leader keeps its arrowhead. This matches the approved fig39 (plain leaders to C.P./C.G. marks) and ch1/fig03 (arrowed leader to a line). | tex lines 66-69 | None (house style). |
| 3 | note | The printed $\Gamma_c$ is dimensioned with two short arcs outside the angle pointing inward; the redraw uses the house `angle arc` inside the angle with the label beyond it. Same angle, same letter. | tex lines 61-62 | None (house style). |

## Verdict

pass (0 must-fix, 0 should-fix)
