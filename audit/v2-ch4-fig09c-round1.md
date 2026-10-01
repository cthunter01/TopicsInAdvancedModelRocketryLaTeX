# v2 audit: ch4/fig09c (round 1)

Sources checked: scan `figures/ch4/fig09c.png` (2x view, 6x crops at both k labels, pixel columns at 100, 130, 400,
440, 495); redraw `figures/v2/ch4/fig09c.pdf` (built with `make fig F=ch4/fig09c`, log clean; 300 and 600 dpi
renders, `pdffonts`), `build/v2/png/ch4-fig09c-compare.png`; sources `fig09c.tex`, `fig09.py`, `fig09c.csv`,
`fig09c.calib.json`; template `figures/v2/ch4/fig06a.tex` (and fig06c, whose y title this panel shares);
inventory row `ch4-fig09c` (`figures/v2/inventory.csv`:140); caption and citing text
`chapters/ch4-sec2b.tex`:306-372 and :495-501; `corrections/v2-figures.md`; STYLE.md section 16.

Checks made:
- **Data reproduced.** A copy of `fig09.py` run in my scratch directory writes a `fig09c.csv` byte-identical to the
  committed one.
- **Calibration.**
  - `digitize.py ticks` puts the x ticks at columns 73.5, 129.5, 185, 239.5, 293, 346, 398.5, 450.5 and 501. They
    close up from 56 to 50.5 px across the panel because the page bends, as the script says.
  - The y ticks are at rows 21.5, 65.5, 109 and 153. The lower ticks, at rows 197.5 and 242, sit where the leaning
    y axis has moved right, at columns 72.6-73.
  - The affine fit leaves 3.45 px, so the drafter's piecewise `xgrid`/`ygrid` calibration is the right choice.
  - It ignores the lean (3.5 px over the axis height). Given how flat the curves are, that is under 0.001 kg in
    $m_o$, as the docstring says.
- **Overlay** (`digitize.py overlay`, piecewise calibration, each curve as its own CSV):

  | curve | mean | 95% | max |
  |---|---|---|---|
  | FM k_min | 0.01 px | 0.00 px | 1.00 px |
  | CB k_min | 0.46 px | 2.00 px (0.34 mm) | 2.00 px |
  | FM k_max | 0.01 px | 0.00 px | 1.00 px |
  | CB k_max | 0.47 px | 2.00 px (0.34 mm) | 3.61 px |

- **Independent traces** (`digitize.py trace`, my seeds, where the lines are apart; one point is 8.8 px on this
  scan):

  | curve | span (kg) | 95% (points) | max (points) |
  |---|---|---|---|
  | FM k_min | 0.109-0.134 | 0.02-0.03 | |
  | FM k_min | 0.218-0.277 | 0.03-0.09 | |
  | FM k_max | 0.218-0.299 | 0.03-0.11 | |
  | CB k_max | 0.148-0.274 | 0.03 | |
  | CB k_min | 0.112-0.299 | 0.04 | 0.09 |

  Where the two solids share one stroke (about 0.17-0.23), the 8x overlay shows both fitted curves inside it. They
  cross at about 0.20 (-1.04 and -1.05 at 0.205).
- **Curve identity.** At 6x the 1973 leaders end as follows:
  - k_max: one leader ends on the flatter solid (column 165, row 156, just under the steeper solid). The other ends
    on the upper dashed (column 173, row 175).
  - k_min: one leader ends on the steeper solid near the right end (column 467, row 180). The other ends on the
    lower dashed (column 464, row 230).

  So FM k_max is the flatter solid (+0.09 to -2.22), and FM k_min is the steeper one (+1.08 to -3.39), as the CSV
  has them. The redraw's leader ends all lie on the intended curves:
  - (0.141, -0.218) is FM k_max (FM k_min is +0.27 there).
  - (0.150, -2.659) is CB k_max.
  - (0.283, -2.934) is FM k_min.
  - (0.282, -8.664) is CB k_min.
- **Values against the inventory.**
  - FM k_max: +0.09 to -2.22 (inventory about 0.2 and -2.2).
  - FM k_min: +1.08 to -3.39 (about 1.2 and -3.4).
  - CB k_max: -1.43 to -7.17 (about -1.4 and -7.2).
  - CB k_min: -4.78 to -8.70 (about -4.8 and -8.8).
- **Lettering.**
  - y title "Percent error in $y_{\max}$"; x title "$m_o$ (kg)".
  - y ticks -15 to 15 by 5; x ticks 0.10-0.30 by 0.05 with minor ticks at the midpoints.
  - $k_{\max}$ near 0.14 and $k_{\min}$ near 0.285, each with two straight leaders.
  - Legend at the upper right as printed; `muted` zero line.
- **Template and family.**
  - Same options as fig06a/fig06c.
  - Page 341.05 x 219.91 pt, identical to fig06c's.
  - Fonts embedded. Nothing clipped or overlapping.
- **Caption and text.**
  - The caption ("Maximum altitude error ... Type F7 engine") is true of the redraw.
  - The largest error is -8.70%, under the text's 10% (ch4-sec2b.tex:325-330).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | **The upper $k_{\min}$ leader is shallow and starts off to the side.** It leaves from the label's north-west corner at about 22 degrees and starts about 1.5 mm left of and above the "k", so at 600 dpi it reads a little detached from the label. The 1973 leader rises at about 60 degrees from the top of the k. The leader's end, (0.283, -2.934), lies almost straight above the label's centre (0.2845). The fork is still legible, and the template uses corner anchors as well, so this is optional. | fig09c.tex:27 | Optional: start it from `kmin.north`. |
| 2 | note | **The $k_{\max}$ leaders cross lines, as printed, but one crossing falls on a dash.** The upper $k_{\max}$ leader crosses the CB $k_{\max}$ dashed line just after it leaves the label; 1973 crosses in a dash gap. It ends on FM $k_{\max}$, which is 0.49 points (about 1 mm) below FM $k_{\min}$ at that point, so the end is unambiguous at final size. | fig09c.tex:24-25 | None. |
| 3 | note | **The inventory places the solids' crossing at the wrong mass.** Its curves column says "the two FM solids cross near .15". In the scan and the redraw they cross near 0.20; near 0.15 it is FM $k_{\min}$ that crosses the zero line. The redraw follows the ink. | inventory.csv:140 (curves column) | Correct the inventory description when the row is updated (orchestrator). |

## Verdict: pass

No must-fix and no should-fix. The curves sit on the scan (95% within 2 px). They agree with independent traces to
about 0.1 point, under the bent-page piecewise calibration. The k assignment matches the printed leaders, and the
panel is identical in frame and style to fig06a/fig06c.
