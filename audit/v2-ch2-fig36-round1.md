# v2 audit: ch2/fig36 (round 1)

Sources checked: figures/ch2/fig36.png (1973 scan, page 194; zoomed 2-5x, pixel-measured);
figures/v2/ch2/fig36.pdf (built 17:45:30, after the .tex; rendered 400 dpi; 362.8 x 219.6 pt = 5.04 x 3.05 in; all
fonts embedded); build/v2/png/ch2-fig36-compare.png; figures/v2/ch2/fig36.tex:1-78; its sibling
figures/v2/supplement/ch2-fig36-1994.tex (source diffed: identical bodies except the switch, fig36.tex:19
`\ellmarkedfalse \def\ARnum{2s}`; the two 400 dpi renders differ only at the AR numerator and the mid-chord line);
figures/v2/inventory.csv rows ch2-fig36 and sup-ch2-fig36-1994; the 1973 caption as reproduced in
backmatter/supplement/s-ch2-1994.tex:151-164 and quoted in the editorial note chapters/ch2-sec4.tex:327-336;
ch2-sec4.tex:356-361 (the 1973 drawing's $2s/(c_r + c_t)$); eqs. (89), (90) ch2-sec4.tex:425-434;
s-ch2-1994.tex:180-188 ($\bar Y_T$, $s$, $c_r$, $r_t$, $c_t$ "illustrated in Figure 36 on page 194");
ch2-symbols.tex:114, 137, 144, 146; corrections/v2-figures.md; STYLE.md sections 13 and 16; figures/v2/tamrfig.sty;
approved example figures/v2/ch2/fig39.tex.

Checked and correct:
- Lettering, all 14 inventory items present, in the 1973 figure's own form: $\AR = \dfrac{2s}{c_r + c_t}$ at left
  (the scan reads "2s" clearly: zoomed crop of the formula), $Z_T$, $\bar{Z}_{T(B)}$ (standing rule 2),
  $\dfrac{c_r}{2}$, $c_r$, C.P.$_{T(B)}$, $\Gamma_c$, C.P.$_T$, $\bar{Y}_T$, $s$, $\dfrac{c_t}{2}$, $c_t$, $r_t$,
  "Rocket centerline". No $\ell$ (the 1973 art does not mark it; the switch removes the arrowheads and the label).
  $x_t$ not marked (as printed; corrections Minor). Nothing added.
- Geometry: the fin is the 1994 drawing's (as the family notes ask, so the two compare directly). The 1973 art's
  own proportions, measured on the scan ($Z_T$ row 65.5, root TE 263.5, tip LE 226.5, tip TE 335.5, tip col 493,
  body col 325, centre line col 288.5): $c_r/s$ 1.18, $c_t/s$ 0.65, $x_t/s$ 0.96, $r_t/s$ 0.22 against the
  redraw's 1.23, 0.67, 0.98, 0.22; the header comment's "4% at most" is right. The drawing type is the same (swept
  trapezoid, tip chord parallel to the axis, body strip with a break line, dash-dot centre line).
- Equations (same code as the 1994 file, evaluated independently): eq. (89) $\bar Z - Z_T = 179.32$
  (0.557 $c_r$; the 1973 art has 0.547 $c_r$), eq. (90) $\bar Y_T - r_t = 118.08$, $\Gamma_c = 34.86^\circ$ from the
  perpendicular to the axis at mid-root to the mid-chord line (the 1973 arc is between the same two lines).
- 1973 caption: $Z_T$ at the root/leading-edge intersection, $\bar Z_{T(B)}$ at the fin-assembly C.P. on the
  centre line, AR of a single fin ($2s$): all true. s-ch2-1994.tex:183-185: $\bar Y_T$ (from the centre line),
  $s$, $c_r$, $r_t$, $c_t$ all shown.
- Style and legibility: as for the 1994 file (house outline/centre line/extension/dimension/leader/`cp mark`/
  `angle arc`; labels \small; 5.04 in wide; no overlaps at 400 dpi; the $r_t$ label fits its 8.5 mm gap with both
  arrow shafts visible).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The 1973 mid-chord line is printed solid from the root to the $\Gamma_c$ arc, then short dashes past C.P.$_T$, then long dashes with small gaps to the tip (probably a centre line poorly reproduced; inventory: "solid with a short dashed stretch"). The redraw draws it dash-dot throughout, like the 1994 form, as the family notes ask ("one consistent way"). Nothing in the 1973 caption or text names its line style. | fig36.tex:53-55 | None. |
| 2 | note | C.P.$_T$ is placed by eq. (90) at 118 units from the body; the 1973 art has its dashed line at 64.5 px against 75.9 px by eq. (90) at the 1973 scale (about 15% of $\bar Y_T - r_t$ inboard), the same kind of offset as in the 1994 art (104.5 against 118). Follows the pilot rule, but the owner has the same question open for Ch2 Figs 34, 35. | fig36.tex:24-25, 33, 43 | No change. Orchestrator: log beside the Figs 34, 35 gate item (see the 1994 report, finding 1). |
| 3 | note | C.P. leaders are plain lines to the mark's rim (the 1973 C.P.$_T$ leader ends in a small arrowhead); $\Gamma_c$ uses the house inside `angle arc` where the 1973 art has two short arcs outside the angle. Both as the approved fig39 and the house style. | fig36.tex:64-65, 69-70 | None. |

## Verdict

pass (0 must-fix, 0 should-fix)
