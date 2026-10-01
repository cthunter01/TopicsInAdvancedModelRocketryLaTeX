# v2 audit: ch4/fig08a (round 2)

Sources checked: scan `figures/ch4/fig08a.png` (8x zoom of cols 80-190, rows 70-160: the k_min drop and the
$k_{\min}$ leaders); redraw `figures/v2/ch4/fig08a.pdf` (rendered at 300 and 600 dpi); source
`figures/v2/ch4/fig08a.tex` lines 1-33; `fig08a.py` (with the changed `fig07a.py` helpers); `fig08a.csv`;
`fig08a.calib.json`. Other sources: inventory row `ch4-fig08a` (`figures/v2/inventory.csv`:135); caption
`chapters/ch4-sec2b.tex`:449-457; the template `fig06a.tex`; the round-1 report.

Reruns:
- I ran `fig08a.py` on a scratch copy against the changed helpers. The CSV it writes is byte-identical to the
  repository's.
- I ran the overlay of the four curves:

  | curve | 95% within | max |
  |-------|-----------|-----|
  | FM k_min | 0.00 px | 1.00 px |
  | CB k_min | 2.00 px | 3.00 px |
  | FM k_max | 0.00 px | 0.00 px |
  | CB k_max | 2.00 px | 2.83 px |

  All pass, and the numbers are identical to round 1.
- All four leader ends lie on their CSV curves within 0.003 point: FM k_max 10.474, CB k_max 4.311, FM k_min 7.812,
  CB k_min 3.188.

Round-1 follow-up: both notes stood with no fix needed, and the files are unchanged:
- **Note 1.** The $k_{\min}$ leaders are short because the label sits in the printed gap.
- **Note 2.** The CB k_min minimum sits about 0.1 point above the dash centres.

In the 8x overlay the S-shaped k_min drops still follow the ink. The rounded S of the print is kept: this panel has
no V corner, unlike 8(c).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| - | - | No findings. | - | - |

Also checked, with no issue:
- **Frame and axes.** The frame is identical to fig06a (the x axis is 2402 px long at 600 dpi). x runs 0.10-0.50,
  labelled every 0.10 with minor ticks at the 0.05s. The titles are "Percent error in $v_b$" and "$m_o$ (kg)". The
  legend is at the lower right, as printed, and the zero line runs the full width.
- **Curves leaving the frame.** The k_max curves enter through the top of the frame, cut at 15 (CB at 0.172, FM at
  0.207).
- **Caption.** The caption's transonic-drag remark is visible as the k_min drop at 0.15-0.17 kg.
- **Style.** The house style is followed; there is no local style and no panel letter in the art.

## Verdict

pass (0 must-fix, 0 should-fix, 0 notes)
