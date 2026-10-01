# v2 audit: ch2/fig33 (round 1)

Sources checked: figures/ch2/fig33.png (scan, upscaled 2x); figures/v2/ch2/fig33.pdf (rendered 400 and 1200 dpi;
343.6 x 170.2 pt = 4.77 in wide, all fonts embedded, PDF newer than its .tex and CSVs);
build/v2/png/ch2-fig33-compare.png; figures/v2/ch2/fig33.tex:1-52, fig33.py (rerun as a copy in the scratch dir: its
four CSVs are byte-identical to the committed fig33-cone/-ogive/-paraboloid/-ellipsoid.csv), fig33.calib.json;
`digitize.py overlay` of each outline on the scan; figures/v2/inventory.csv row ch2-fig33; caption
chapters/ch2-sec4.tex:226, citing text and eqs. (80a)-(80d) ch2-sec4.tex:194-222; corrections/v2-figures.md;
STYLE.md sections 13 and 16; tamrfig.sty (`outline`, `centerline`, `extension`, `\dimline`, `cp mark`, `panel`);
approved fig39.tex (`\CP$_n$` lettering).

Checked and correct:
- Outlines generated exactly from their definitions at one fineness L/d = 2.4 (scan: L = 183 px, base half-widths
  37-39 px): cone; tangent ogive of radius rho = (R^2 + L^2)/(2R) = 2.504 L with its centre on the base plane
  (tangent to the body at the base, r = 0.0000 at the tip, checked); paraboloid of revolution r^2 = R^2 z/L with
  its vertex at the tip (rounded tip as printed); half prolate spheroid (vertical tangent at the base). Overlay on
  the scan, 95th percentile / max: cone 0.0 / 1.4 px, ogive 0.0 / 1.0 px, paraboloid 2.0 / 3.0 px, ellipsoid
  2.0 / 2.2 px (all within the 3 px target).
- C.P. positions from the tip, measured on the 400 dpi render (tip row 113, base row 680, L = 567 px =
  3.6 cm): (a) 0.667 L, (b) 0.467 L, (c) 0.501 L, (d) 0.333 L, i.e. eqs. (80a)-(80d) (2/3, .466, 1/2, 1/3 L),
  which are measured from the nose tip as the text's volume-over-base-area rule gives (the script's rule check:
  0.6667, 0.4601 at L/d = 2.4, 0.5000, 0.3333; the printed .466 is kept for the ogive, correctly).
- Lettering complete and as printed: 2/3 L, .466L, 1/2 L, 1/3 L (stacked fractions), four C.P.$_n$ (same form as
  approved Fig 39), L on (d) only with its extension lines at tip and base rows, (a)-(d) with Conical, Tangent
  ogive, Paraboloidal, Ellipsoidal. Dash-dot centre lines run past tip and base; C.P. labels knocked out of the
  centre line as in the scan and clear of the outlines (cone half-width at the label 83 px against label
  half-width 57 px at 400 dpi). Nothing added.
- Scale 3.6 cm per L = 1.16 x the printed size, the same as Figs 34 and 35; type \small throughout, no overlaps,
  arrowheads visible, base corners closed cleanly (round caps).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The centre line is drawn after the nose outline (`\nose` then `\cpdim`), so the 0.4pt ink2 dash-dot overprints the 0.6pt black outline where they meet: at 1200 dpi the sharp tips of (a) and (b) turn grey over their top ~0.1 mm and a grey dash crosses each black base line. Figs 34, 35 and the approved Fig 39 draw the centre line first. | fig33.tex:22 (centre line inside `\cpdim`), calls at 35-50 | Draw the centre line before the outline: move `\draw[centerline] (#1,0.2) -- (#1,-1.2);` from `\cpdim` to the start of `\nose` (or wrap it in `\begin{scope}[on background layer]`). |
| 2 | note | Panel letters are centred under each nose with the shape name below (as printed), not at the lower right of the panel as STYLE.md 16 describes for drawings; here the letter and name read as a sub-caption and the centred placement is the clearer choice. All four on one baseline. | fig33.tex:30-32 | None needed. |
| 3 | note | ".466L" keeps its printed form without a leading zero; the leading-zero rule applies to tick labels, and eq. (80b) prints .466L. | fig33.tex:40 | None. |

## Verdict

pass (0 must-fix, 1 should-fix)
