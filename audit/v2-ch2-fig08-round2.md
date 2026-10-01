# v2 audit: ch2/fig08 (round 2)

Sources checked: figures/ch2/fig08.png (the scan); figures/v2/ch2/fig08.pdf (rebuilt with `make fig F=ch2/fig08`:
4.69 x 2.87 in, fonts embedded, rendered at 400 dpi) and build/v2/png/ch2-fig08-compare.png;
figures/v2/ch2/fig08.tex, fig08.py (and the functions it imports from fig07.py), fig08.calib.json, fig08.csv;
figures/v2/inventory.csv row ch2-fig08; caption chapters/ch2-sec2.tex:45-46; citing text ch2-sec2.tex:26-32;
eq. (9) (ch2-sec2.tex:100-104); STYLE.md sections 13 and 16; corrections/v2-figures.md;
audit/v2-ch2-fig08-round1.md and the round-1 fix report.

Round-1 findings: none were raised. The drafter's consistency change, `HERE = pathlib.Path(__file__).resolve().parent`
(fig08.py:21), works. I reran the script from the repository root and from /tmp with `write_text` intercepted, so
nothing was written. Both runs produce output byte-identical to fig08.csv (md5 7a46e819...).

Re-checked (no regressions):
- Lettering: the y title is "Damping moment $M_d$ (dyn-cm)". The y ticks 0, $1\times10^6$ and $2\times10^6$ are
  labelled, with unlabelled minor ticks at $0.5\times10^6$ and $1.5\times10^6$, as in the scan. The x title
  "Angular velocity $\Omega_X$ (rad/sec)" is in the section 13 form. The x ticks are 0, 50, 100 and 150, with
  minor ticks at 25, 75 and 125. The figure has open axes and no grid. Nothing is added. The tex file is unchanged
  since round 1.
- Data: the curve is exactly $C_2\Omega_X$ with $C_2 = 1.25\times10^4$ up to 60 rad/sec (3.125e5 at 25, 6.25e5 at
  50), then concave: 9.338e5 at 75, 1.066e6 at 87, 1.189e6 at 100 and 1.346e6 at 125. The maximum is 1.373e6 at
  139, with a slight fall to 1.359e6 at 150, as in the inventory. At 87 rad/sec it is 1.9% below the tangent,
  which is consistent with the Fig 9 caption.
- Overlay (`digitize.py overlay`) on the scan: mean 0.03 px, 95% 0.00 px, max 1.00 px. This is within the 3 px target.
- Family: fig09-md.csv's `true` column equals fig08.csv exactly (max difference 0). The figure has the same axes
  size and layout as Figs 7 and 9.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| - | - | No findings, and there are no regressions. | - | - |

## Verdict: pass

0 must-fix, 0 should-fix.
