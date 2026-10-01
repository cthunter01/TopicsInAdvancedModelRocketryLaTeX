# v2 audit: ch4/fig07b (round 2)

Sources checked: scan `figures/ch4/fig07b.png`; redraw `figures/v2/ch4/fig07b.pdf` (rendered at 300 and 600 dpi);
source `figures/v2/ch4/fig07b.tex` lines 1-32; `fig07b.py` (with the helpers it imports from `fig07a.py`, changed
this round); `fig07b.csv`; `fig07b.calib.json`. Other sources: inventory row `ch4-fig07b`
(`figures/v2/inventory.csv`:133); caption `chapters/ch4-sec2b.tex`:433-439; the template `fig06a.tex`; the
round-1 report.

Reruns:
- I ran `fig07b.py` on a scratch copy against the changed `fig07a.py` helpers. The CSV it writes is byte-identical
  to the repository's, so the helper changes do not touch this panel.
- I ran the overlay of the four curves:

  | curve | 95% within | max |
  |-------|-----------|-----|
  | FM k_min | 0.00 px | 2.24 px |
  | CB k_min | 2.00 px | 2.24 px |
  | FM k_max | 0.00 px | 0.00 px |
  | CB k_max | 2.00 px | 4.12 px |

  All pass, and the numbers are identical to round 1.
- All four leader ends lie on their CSV curves within 0.005 point: FM k_max -1.920, CB k_max -6.683, FM k_min
  -2.690, CB k_min -7.870.

Round-1 follow-up: the one note (two leaders cross another method's line before reaching their own, as printed) was
accepted, and the files are unchanged. The PDF was rebuilt after the CSV, and the render matches round 1.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| - | - | No findings. | - | - |

Also checked, with no issue:
- **Frame and axes.** The frame is identical to fig06a (the x axis is 2402 px long at 600 dpi, at the same row). The
  ticks, the titles ("Percent error in $y_b$", "$m_o$ (kg)"), the legend at the upper right and the zero line are as
  printed.
- **Curve identities and labels.** These are as audited in round 1. The dashed curves cross near 0.088. $k_{\max}$
  and $k_{\min}$ are at the printed places.
- **Style.** The house style is followed; there is no local style and no panel letter in the art.
- **Caption.** The caption holds for the redraw.

## Verdict

pass (0 must-fix, 0 should-fix, 0 notes)
