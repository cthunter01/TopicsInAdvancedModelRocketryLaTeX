# v2 audit: ch3/fig11 (round 1)

Sources checked: figures/ch3/fig11.png (scan, zoomed 3x, the dS group and the V arrow 6-7x); figures/v2/ch3/fig11.pdf
(rebuilt with `make fig F=ch3/fig11`, 3.66 x 2.21 in, fonts embedded; rendered at 300 and 600 dpi) and
build/v2/png/ch3-fig11-compare.png; figures/v2/ch3/fig11.tex, fig11.py, fig11.csv, fig11.calib.json;
figures/v2/inventory.csv row ch3-fig11; caption chapters/ch3-sec2b.tex:341-346; citing text ch3-sec2b.tex:322-336
(eqs. (26), (27), cos(n, V), cos(t, V), dS), ch3-sec3c-sec4a.tex:125-131 (eq. (109), "consulting Figure 11
again"); ch3-symbols.tex:148 (the unit tangent ednote); STYLE.md sections 14 and 16; corrections/v2-figures.md
(standing rules 2, 4); precedent figures/v2/ch1/fig06.tex and the scan figures/ch1/fig06.png; sibling Ch3 drafts
fig01.tex, fig12.tex, fig39.tex (vector lettering).
Overlay run myself: `digitize.py overlay fig11.calib.json --axes page fig11.csv`: 1119 points, mean 1.05 px,
95% 2.83 px (0.48 mm), max 5.00 px: ok. Normal and tangent recomputed (house view, x = 1.57 R, phi = 98.5 deg on
r = R sqrt(x/L), L/R = 5): n page direction 91.7 deg, t 35.4 deg (scan 99 and 39), angle (n, V) 100.1 deg,
(t, V) 10.1 deg; the element is on the seen side (cos(phi - phi_c) = 0.77 > -0.13).

Checked and correct:
- Lettering: $\vec{n}$, $\vec{t}$, $dS$, $\vec{V}$; nothing missing or added. The vectors are set with arrows, as
  the caption and text write them (eqs. (26), (27), (109)); see finding 1 on the chapter's consistency.
- Body: an exact body of revolution in the house view (paraboloid r = R sqrt(x/L), L/R = 5): silhouettes from the
  condition cos(phi - phi_c) = (c_x/|c_yz|) r'(x), checked against the tex (kk = 0.075, the silhouettes join at
  the blunt tip, x = L kk^2 = 0.03), meeting the base rim at phi_c +- acos(-kk); the seen rim arc solid, the far
  arc `hidden`, as printed. It sits on the scan within the 3 px tolerance.
- dS: a curvilinear rectangle on the surface (sides along the meridian and round the body), centred on the
  point from which n and t start, as the caption says; n the outward unit normal (-r', cos phi, sin phi)/norm,
  t the unit tangent along the meridian (n . t = 0); same 3D length. The redraw's true normal is about 7 deg
  steeper on the page than the 1973 line (rule 4: geometry drawn correctly).
- V: the free-stream `vec` on the axis ahead of the nose with a gap before the axis resumes, as printed; the
  axis and the two transverse axes through the base centre as `centerline`s crossing on a dash.
- Legibility: labels clear of their arrows and of the silhouette; $\vec{n}$ crosses the upper silhouette as in
  the scan, readable; nothing clipped; width within 6.5 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The art letters overbars (n-bar, t-bar, V-bar); the redraw sets $\vec{n}$, $\vec{t}$, $\vec{V}$ as the caption and text do. This follows the approved Ch1 Fig 6 precedent (scan V-bar, redraw $\vec{V}$) and the inventory note, but the sibling Ch3 drafts Fig 1 ($\bar V$, $\bar D$), Fig 12 ($\bar V$) and Fig 39 ($\bar U$) keep the overbars. One convention is needed for the chapter. | fig11.tex:66, 68, 72 | None for Fig 11; the consistency pass should bring Figs 1, 12, 39 to $\vec{}$ (or the gate decide otherwise). |
| 2 | note | The 1973 art draws the two transverse axes as solid lines and marks a small dot at the base centre; the redraw draws all three axes as centre lines crossing on a dash, without the dot. House style; no meaning changes. | fig11.tex:42-49 | None. |
| 3 | note | The body's shape is not named in the book; the paraboloid of fineness 2.5 is the best of the kit's exact shapes on the scan (mean 1.05 px), and the far rim arc is drawn as the true ellipse (the 1973 dashed arc is narrower). | fig11.py:4-15 | None. |

## Verdict: pass (0 must-fix, 0 should-fix)
