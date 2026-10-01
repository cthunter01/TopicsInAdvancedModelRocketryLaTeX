# v2 audit: ch4/fig09a (round 1)

Sources checked: scan `figures/ch4/fig09a.png` (2x view, 6x crops at both k labels); redraw
`figures/v2/ch4/fig09a.pdf` (built with `make fig F=ch4/fig09a`, log clean; 300 and 600 dpi renders, `pdffonts`),
`build/v2/png/ch4-fig09a-compare.png`; sources `fig09a.tex`, `fig09.py`, `fig09a.csv`, `fig09a.calib.json`;
template `figures/v2/ch4/fig06a.tex` (and siblings fig06b/c, fig05a); inventory row `ch4-fig09a`
(`figures/v2/inventory.csv`:138); caption and citing text `chapters/ch4-sec2b.tex`:306-372 and :479-485;
`corrections/v2-figures.md` (Figs 5, 7-10, 12-14 digitized: compute-else-digitize rule); STYLE.md section 16.

Checks made:
- **Data reproduced.** A copy of `fig09.py` run in my scratch directory (same calibrations, output redirected)
  writes a `fig09a.csv` byte-identical to the committed one.
- **Calibration.** `digitize.py lines/ticks` on the scan: x axis at row 288, ticks at columns 72.5, 128.5, 185,
  242, 297.5, 353, 409.5, 464.5, 521.5; y ticks at rows 20, 64.5, 109.5, 153.5, 199, 243.5, 288.5. The calibration
  points agree within 0.5 px; affine residual 0.74 px.
- **Overlay** (`digitize.py overlay`, the drafter's calibration, each curve as its own CSV):

  | curve | mean | 95% | max |
  |---|---|---|---|
  | FM k_min | 0.00 px | 0.00 px | 0.00 px |
  | CB k_min | 0.53 px | 2.00 px (0.34 mm) | 2.00 px |
  | FM k_max | 0.03 px | 0.00 px | 1.00 px |
  | CB k_max | 0.48 px | 2.00 px (0.34 mm) | 3.00 px |

  The 2 px are the dashes' gaps. Distance to ink is weak where lines run together. So I also checked:
  - The overlay picture at 8x where the two solids share one stroke (0.11-0.14). Each fitted curve sits on its own
    ink.
  - Pixel columns 440-520, where FM k_min runs into the zero line. The scan's run there is 4 px (two touching
    lines), and the fitted row is within 0.4 px of where it should be.
- **Independent traces** (`digitize.py trace`, my own seeds, between the leader crossings):
  - CB k_min over 0.112-0.300: mean difference from the CSV +0.008 points, 95% 0.043, max 0.44 (at a dash end).
  - FM k_max over 0.146-0.237: 95% 0.03-0.08 points.
  - FM k_max over 0.269-0.300: 95% 0.03 points.
  - One point is 8.9 px on this scan.
- **Curve identity.** At 6x the 1973 leaders end as follows:
  - k_max on the rising solid (column 388, row 129) and on the upper dashed (column 417, row 143).
  - k_min on the falling solid (column 383, row 148) and on the lower dashed.

  The redraw's leader ends (CSV interpolation) all lie on the intended curves:
  - (0.237, 2.619) is FM k_max (2.619).
  - (0.2535, 1.116) is CB k_max (1.116).
  - (0.2385, 0.704) is FM k_min (0.704).
  - (0.2327, -6.549) is CB k_min (-6.549).

  So the columns' k assignment matches the printed leaders.
- **Values against the inventory.**
  - FM k_max: +1.95 at 0.11 and +3.17 at 0.30 (inventory about 2 and 3.3; my trace gives 3.15 at 0.2998).
  - CB k_max: +1.59 to +0.65.
  - FM k_min: +1.95 to +0.05.
  - CB k_min: -3.20, then a minimum of -6.95 at about 0.195, then -5.19.
  - The curves run 0.110-0.300 as printed, from the engine-alone mass 0.110 kg (ch4-sec3.tex:219).
- **Lettering.**
  - y title "Percent error in $v_b$"; x title "$m_o$ (kg)".
  - y ticks -15 to 15 by 5.
  - x ticks 0.10-0.30 by 0.05 (house leading zero), with minor ticks at 0.125 ... 0.275 as printed.
  - $k_{\max}$ and $k_{\min}$, each with a forked pair of straight `leader`s.
  - Legend: solid Fehskens-Malewicki and dashed Caporaso-Bengen, at the upper right as printed.
  - A thin `muted` zero line, as in the template.
  - No panel letter in the art; the caption's `\figurepanel{a}` numbers it, as for fig06a.
- **Template and family.**
  - Same frame and options as fig06a: `tamr`, 4.0 x 2.5 in, the same tick-label format, series1 = FM and series2
    = CB for both k, `\footnotesize` k labels, and the same legend style.
  - Page 340.51 x 219.91 pt against fig06a's 340.51 x 219.91 pt.
  - Fonts embedded. Nothing clipped or overlapping.
- **Caption and text.**
  - The caption ("Burnout velocity error ... Type F7 engine") is true of the redraw.
  - The collective claim that the errors stay below the 10% impulse scatter (ch4-sec2b.tex:325-330) holds in this
    panel (largest magnitude 6.95%).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | As in the scan, two leaders cross a line on the way to their curves. The right $k_{\max}$ leader crosses the FM $k_{\max}$ solid on its way to the CB $k_{\max}$ dashed line. The upper $k_{\min}$ leader crosses the zero line. Both still end clearly on their curves at 600 dpi: FM $k_{\min}$ is 0.7 points (about 1.5 mm) above the zero line there. | fig09a.tex:24-28 | None. |
| 2 | note | FM $k_{\min}$ runs into the zero line from about 0.29 kg (+0.05 at 0.30). This is printed: the scan's stroke merges with the zero line from column 490. | fig09a.csv, last rows | None. |

## Verdict: pass

No must-fix and no should-fix. The digitized curves sit on the scan (95% within 2 px) and agree with independent
traces to under 0.1 percentage point. The k assignment matches the printed leaders, and the panel is identical in
frame and style to the approved fig06a.
