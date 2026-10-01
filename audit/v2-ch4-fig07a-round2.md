# v2 audit: ch4/fig07a (round 2)

Sources checked: scan `figures/ch4/fig07a.png` (8x zoom of the CB k_min start, cols 70-150); redraw
`figures/v2/ch4/fig07a.pdf` (rendered at 300 and 600 dpi, with a 600 dpi crop of the $k_{\min}$ leaders); source
`figures/v2/ch4/fig07a.tex` lines 1-32; `fig07a.py` (all, including the changed shared helpers `smooth`, `trace`,
`trace_cornered`, `digitize_panel`); `fig07a.csv`; `fig07a.calib.json`. Other sources: inventory row `ch4-fig07a`
(`figures/v2/inventory.csv`:132); caption `chapters/ch4-sec2b.tex`:425-431; `corrections/v2-figures.md`:82-84;
the template `fig06a.tex`; the round-1 report.

Reruns:
- I ran `fig07a.py` on a copy in the scratch directory, with links to the crops and `tools/v2`. The CSV it writes is
  byte-identical to the repository's. The other five panels' scripts, which import the changed helpers, also write
  byte-identical CSVs.
- I ran `tools/v2/digitize.py overlay` on the four curves, split from the CSV:

  | curve | 95% within | max |
  |-------|-----------|-----|
  | FM k_min | 0.00 px | 1.00 px |
  | CB k_min | 2.00 px | 2.24 px |
  | FM k_max | 0.00 px | 0.00 px |
  | CB k_max | 2.00 px | 2.24 px |

  All pass. The CB k_min maximum was 3.0 px in round 1.
- All four leader ends lie on their CSV curves within 0.002 point.

Round-1 follow-up:
- **Note 1 (CB k_min start): resolved.** With `sigma=0.3` for this curve only, the curve now starts at -4.43 at
  $m_o$ = 0.0314. The first printed dash runs from -4.31 to -4.54. In an 8x overlay zoom the trace lies on the first
  dash and then on every later dash. The curve's minimum is still -5.6 near 0.045. Elsewhere the shape is unchanged:
  a fifth-order fit leaves residuals of 0.007 point at most, and the curve has no new ripple. The $k_{\min}$ leader
  end moved to (0.0341, -4.900). On the 600 dpi render it ends on a dash, not in a gap.
- **Note 2 (FM k_min just under the zero line): unchanged.** As round 1 said, no change is needed.
- **Regression check of the shared helpers:** the default path (sigma 0.5, no `pin`) gives the same output as before.
  All six CSVs are byte-identical on rerun. Only `cb_kmin` here and fig08c's `corner` curves use the new keys.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The module docstring's edit left one line at 162 characters. All the other lines are wrapped at about 115. This is cosmetic only and does not affect the figure. | fig07a.py:23 | Optional: rewrap at the next touch. |

Also checked, with no issue:
- **Frame.** The axis box is identical to fig06a: the x axis is at the same row at 600 dpi and is 2402 px long, and
  the page is 340.5 x 219.9 pt.
- **Ticks and titles.** x runs 0.03-0.13, labelled at the odd hundredths with minor ticks at the even ones. y runs
  -15 to 15 in steps of 5. The titles are "Percent error in $v_b$" and "$m_o$ (kg)".
- **Legend and zero line.** The legend is at the upper right, as printed, and the muted zero line runs the full width.
- **Style.** The curves are s1 solid (FM) and s2 dashed (CB). Labels are ink `\footnotesize`, leaders use the
  `leader` style, and there is no local style and no panel letter in the art (`\figurepanel{a}`).
- **Caption.** The caption holds for the redraw.

## Verdict

pass (0 must-fix, 0 should-fix, 1 note). Both round-1 notes are settled; there are no regressions.
