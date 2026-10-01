# v2 audit: ch4/fig08b (round 2)

Sources checked: scan `figures/ch4/fig08b.png` (8x zoom of cols 78-200, rows 10-90: the crowded strands and the
leaders); redraw `figures/v2/ch4/fig08b.pdf` (rendered at 300 and 600 dpi); source `figures/v2/ch4/fig08b.tex`
lines 1-33; `fig08b.py` (all, including the corrected docstring); `fig08b.csv`; `fig08b.calib.json`. Other
sources: inventory row `ch4-fig08b` (`figures/v2/inventory.csv`:136); caption `chapters/ch4-sec2b.tex`:459-467; the
template `fig06a.tex`; the round-1 report.

Reruns:
- I ran `fig08b.py` on a scratch copy against the changed helpers. The CSV it writes is byte-identical to the
  repository's.
- I ran the overlay of the four curves:

  | curve | 95% within | max |
  |-------|-----------|-----|
  | FM k_min | 0.00 px | 2.24 px |
  | CB k_min | 2.00 px | 3.00 px |
  | FM k_max | 0.00 px | 2.00 px |
  | CB k_max | 2.00 px | 2.24 px |

  All pass, and the numbers are identical to round 1.
- All four leader ends lie on their CSV curves within 0.004 point: FM k_max 10.617, CB k_max 2.819, FM k_min
  12.642, CB k_min 9.106.

Round-1 follow-up:
- **Note 1 (white gap where the $k_{\min}$ leader passes the FM junction): declined, with a reason.** The leader's
  target reads correctly. The family template (fig06a, fig07b) lets leaders cross curves. The gap is kept for fig07c,
  the one place where the target is ambiguous between two same-style lines. I accept this. In the redraw, the
  leader runs on about 1.6 mm past the merged solids to the dashed curve.
- **Note 2 (which FM strand is which inside 0.165-0.20): kept as a doubt.** The columns differ by 0.05 point at
  most there, so nothing visible depends on it.
- **Note 3 (docstring ranges): resolved.** I checked fig08b.py:12-19 against the CSV at each 0.01:
  - The FM strands are apart from 0.21 (+0.06) to 0.32 (+0.10), with a peak of +0.42 at 0.26-0.27.
  - The FM strands are within 0.05 from 0.33.
  - CB k_min meets the lower strand near 0.25-0.26 (-0.11, then -0.02).
  - The three curves are one band from about 0.33.

  This all agrees with the new text.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| - | - | No findings. | - | - |

Also checked, with no issue:
- **Frame and axes.** The frame is identical to fig06a (the x axis is 2402 px long at 600 dpi). The ticks, the titles
  ("Percent error in $y_b$", "$m_o$ (kg)"), the legend at the lower right and the zero line are as printed.
- **Left-hand solids.** In the 8x overlay the solids at 0.107-0.165 lie on the print's near-straight lines. The
  break in the print at 0.163-0.171 is bridged straight.
- **Caption.** The caption's transonic-drag remark holds: the k_min curves are steep below about 0.17 kg.
- **Style.** The house style is followed; there is no local style and no panel letter in the art.

## Verdict

pass (0 must-fix, 0 should-fix, 0 notes)
