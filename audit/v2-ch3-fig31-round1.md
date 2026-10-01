# v2 audit: ch3/fig31 (round 1)

Sources checked: scan `figures/ch3/fig31.png` (664 x 822 px; the icon column zoomed 2x); redraw
`figures/v2/ch3/fig31.pdf` (current: same time as the .tex; 399.8 x 304.5 pt = 5.55 x 4.23 in; fonts embedded),
rendered at 400 dpi, and `build/v2/png/ch3-fig31-compare.png`; `figures/v2/ch3/fig31.tex`; inventory row
`ch3-fig31` (`figures/v2/inventory.csv`:97); caption `chapters/ch3-sec4b.tex`:209-219 (columns; parentheses =
with launch lug; brackets = unsanded, unpainted, lug, no airfoiling); citing text :187-204 (five lowest-drag
shapes BC-70, -78, -72, -76, -74), :244-249 (0.70 → 2.35, 236%), :273-275, :286-288; `STYLE.md` sections 8, 14
and 16 (tables in figures: booktabs); `tamrfig.sty` (`\rocketoutline` nose shapes).

Checks made:
- **Every entry.** I checked every entry against the scan.
  - The column heads are "Nosecone shape", "Nosecone designation", "$\CD$ of Javelin with airfoiled fins" and
    "$\CD$ of Javelin with square edged fins".
  - The twelve rows (designation, airfoiled, square-edged) are: BC-70 0.41 2.10; BC-78 0.41 2.13; BC-72 0.42
    2.12; BC-76 0.42 2.14; BC-74 0.43 (0.70) 2.15 (2.35) [2.76]; BC-79 0.51 2.14; Hemisphere 0.51 2.16;
    $60\dg$ cone 0.59 2.24; $45\dg$ cone 0.61 2.24; Slightly rounded 0.87 2.51; Flat 1.32 2.77; Plug 1.75 3.26.
  - All match. The parenthesised and bracketed values are kept, hanging to the right so the main values stay
    aligned.
  - The text's 0.70 → 2.35 can be read straight off the BC-74 row.
- **Table form.** The table uses booktabs with no vertical rules or row rules (STYLE sections 8 and 16; the
  inventory left booktabs or ruled open). The rules span the hanging "[2.76]" (the `\ohang` padding works: the
  rule ends about 1 mm past it). "Slightly rounded" is set on one line. Those are layout choices only.
- **Icons.** All point right, on one diameter, at 1.25 times printed size. Lengths against the scan (zoomed):
  - BC-70: ellipsoid, 58.5 (scan ≈ 58.5).
  - BC-78: base band, straight taper to the joint, then an ogive; 119 (≈ 119).
  - BC-72: ogive, 68.5 (≈ 68.5).
  - BC-76: ellipsoid, 115 (≈ 115).
  - BC-74: ogive, 130 (≈ 130).
  - BC-79: band and cone, 134 (≈ 133.5).
  - Hemisphere: stub with a hemispherical end and no joint line, as printed.
  - $60\dg$ cone: cone 23.4 long on R 13.5, a 30 deg half-angle (scan ≈ 23.5).
  - $45\dg$ cone: cone 13.5 long, a 45 deg half-angle (scan ≈ 13.5), so both angles are read from the base
    plane, consistently.
  - Slightly rounded: front corners of radius 0.13 d.
  - Flat: a plain stub.
  - Plug: a C-shaped open end with the wall thickness shown.
- **Icon placement.** The icons are centred in their column and on the text line (`baseline=-3.3pt`), as the
  scan centres them.
- **Legibility.** The table is `\small`, nothing collides, and the hanging figures do not reach the next column
  (3 em separation). The width is 5.55 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | note | siunitx `S` columns (STYLE section 16) are not used. Every value has the form x.xx, so the centred `c` columns already align on the decimal point, and `\hang` keeps the parenthetical figures out of the alignment. | fig31.tex:27, 34 | None. |
| 2 | note | The 1973 ruled grid (vertical rules, a rule under every row, a double header rule) becomes booktabs, per STYLE sections 8 and 16. | fig31.tex:34-55 | None. |

## Verdict: pass (no must-fix)
