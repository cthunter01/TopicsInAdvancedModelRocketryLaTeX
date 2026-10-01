# v2 audit: ch3/fig41 (round 1)

Sources checked: scan `figures/ch3/fig41.png` (zoomed x3, lettering x6-7); redraw `figures/v2/ch3/fig41.tex`,
`fig41.py`, `fig41.csv`, `fig41.calib.json`; rebuilt with `make fig F=ch3/fig41` (4.91 x 3.15 in) and rendered
at 350 dpi; inventory row `ch3-fig41`; caption and citing text `chapters/ch3-sec5b.tex:60-104, 147-170`
(eqs. (148), (149), Table 4); `corrections/ch3.md` D35 (Table 4 last-digit cells); STYLE.md sections 14, 16;
leader practice in `figures/v2/ch2/fig39.tex`.

Checks run:
- Dashed curve = 0.75 + eq. (149), 16.83 a^2 + 8.9 a^3 (a in rad), evaluated independently: increments 0.0052,
  0.0209, 0.0474, 0.0851, 0.1341, 0.1948, 0.2674, 0.3523, 0.4498, 0.5600 at 1-10 deg (Table 4 total column
  .005 ... .559; its .136 at 5 deg is the v1 table's last-digit slip already in corrections/ch3.md D35). 1.310 at
  10 deg.
- `fig41.py` rerun into the scratch dir reproduces `fig41.csv` byte for byte. Stine fit
  C_D = 0.75 + 0.008972 a^2 - 0.0001282 a^3 (a in deg): residual rms 0.73 px, 95% 1.46 px, max 3.04 px.
- `digitize.py overlay`: Stine 95% 0.00 px, max 1.00; trial 95% 2.00 px (0.34 mm), max 2.83 px: both "ok".
  Gridline-masked mesh check: Stine |offset| 95% 1.64 px; the dashed curve within about 1 px of the dashes from
  4 to 10 deg (the masked check at 2-3 deg picks up the solid curve through the dash gaps, not a misfit).
- Text: "For the Aerobee-Hi model, the drag coefficient is doubled at an incidence of ten degrees": redraw
  1.519 at 10 deg = 2.03 x 0.75, true. Both curves start at 0.75 (caption: same zero-angle drag), true.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Lettering "Aerobee-Hi" (not the inventory's "Aerobee-HI"): verified on the scan at x7 — this letterer's i is a dotless stroke rising to cap height in Stine, experiment, Figure and semiempirical, so the last letter is that i; matches the caption and text. | fig41.tex:4-7, 30-31 | none |
| 2 | note | "Figure 37" kept as literal lettering (family brief); the inventory note's "\ref" suggestion is superseded (a standalone figure cannot \ref, and Ch3 Figure 37 keeps its number). | fig41.tex:33-34 | none |
| 3 | note | Callouts follow the house rule: straight leaders (the print's shoulders dropped), ending exactly on the curves at 4.8 deg (Stine, solid) and 6.4 deg (trial, dashed), read from CSV rows 48 and 64, where the print's leaders meet them (about 4.85 and 6.5 deg). Labels in white knock-outs at the printed places (upper middle; lower right), three lines each as printed; no curve passes through either knock-out. | fig41.tex:12-14, 29-35 | none |
| 4 | note | Solid/dashed kept as the secondary encoding for the two methods (series1 Stine solid, series2 trial dashed), matching the print. Ticks and rulings as printed: x 0-10 every 1 deg; y 0-1.6 labelled every 0.2, rulings every 0.1; titles $\CD$ and "$\alpha$ (deg)". | fig41.tex:19-27 | none |
| 5 | note | The Stine fit runs about 2 px (0.01) under the drawn curve at 9.9 deg (drawn about 1.52, fit 1.505; 1.519 at 10): within tolerance and the "doubled at ten degrees" reading holds. | fig41.csv (stine) | none |
| 6 | note | Legibility good at final size (labels \small, leaders ink2 0.45 pt visible, dashes distinct where the curves part above 1-2 deg, as in the print); width 4.91 in; family frame 4.2 x 2.6 in as Figs 40 and 42. | rendered PDF | none |

## Verdict: pass (no must-fix)
