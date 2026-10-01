# v2 audit: ch2/fig07 (round 1)

Sources checked: figures/ch2/fig07.png (scan, upscaled 3x); figures/v2/ch2/fig07.pdf (rebuilt with `make fig
F=ch2/fig07`, 4.68 x 2.86 in, fonts embedded; rendered at 150 and 300 dpi) and build/v2/png/ch2-fig07-compare.png;
figures/v2/ch2/fig07.tex, fig07.py, fig07.calib.json, fig07.csv; figures/v2/inventory.csv row ch2-fig07; caption
chapters/ch2-sec2.tex:37-38; citing text ch2-sec2.tex:21-26, ch2-sec5.tex:252-255 and 287-288; Fig 9 caption
ch2-sec2.tex:114-119 and eq. (8) (ch2-sec2.tex:93-97); STYLE.md sections 13 and 16; corrections/v2-figures.md
(standing rules, pilot decisions, the minor Fig 7 item); approved examples ch2/fig25.tex, ch1/fig03.tex,
ch4/fig06a.tex.

Checked and correct:
- Lettering: y title "Corrective moment $M_c$ (dyn-cm)", x title "Angular deflection $\alpha_X$ (rad)" (the
  section 13 uppercase subscript); y ticks 0 to $4\times10^5$ in steps of $1\times10^5$, all labelled; x ticks 0,
  0.1, 0.2, 0.3 labelled with leading zeros and minor ticks at 0.05, 0.15, 0.25, as in the scan; open left and
  bottom axes (`tamr`), no grid, as printed. Nothing added.
- Data: fig07.py reruns (from the repository root) to a byte-identical fig07.csv; trace fit residual rms 0.71 px,
  95% 1.57 px. `digitize.py overlay` of fig07.csv on the scan: mean 0.11 px, 95% 1.00 px (0.17 mm), max 1.00 px:
  within the 3 px target. Values: 1.00e5 at 0.1, 2.00e5 at 0.2, 2.22e5 at 0.224, 2.345e5 at 0.25, 2.418e5 at
  0.275, 2.447e5 at 0.3, matching the inventory's reading (2.22e5, 2.35e5, flat top about 2.44e5).
- Governing constraints: the curve is exactly $C_1\alpha_X$ with $C_1 = 1\times10^6$ dyn-cm up to 0.20 rad (the
  tangent at zero of eq. (8) equals the Fig 9 lettering); the B-spline join is C2 (first three clamped
  coefficients zero); the curve is concave throughout (slope/C_1: 0.94 at 0.21, 0.58 at 0.23, 0.31 at 0.26, 0.10 at
  0.29) and reaches zero slope at 0.3 rad (end slope +0.001 C_1), i.e. at 17.2 deg, inside the 12-18 deg that
  ch2-sec5.tex:252-255 relies on. At 0.225 rad it lies 1.6% below the tangent, consistent with the Fig 9 caption's
  linear range. The data are the same as Fig 9's true $M_c$ (fig09-mc.csv column `true` equals fig07.csv exactly).
- Legibility and style: width 4.68 in; single `series1` curve; same 3.8 x 2.3 in axes as Figs 8 and 9.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | fig07.py builds `HERE = pathlib.Path(__file__).parent` without `.resolve()`, so `ROOT` is `.` when the script is run as `python3 fig07.py` from inside figures/v2/ch2 and the crop is not found (FileNotFoundError on figures/ch2/fig07.png). `make figdata` (run from the root) and fig08.py's import both work, so the data are unaffected. | fig07.py:25-26 | Optional: `HERE = pathlib.Path(__file__).resolve().parent` (as tools/v2/digitize.py does). |

## Verdict

pass (0 must-fix, 0 should-fix)
