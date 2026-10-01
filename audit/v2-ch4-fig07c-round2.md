# v2 audit: ch4/fig07c (round 2)

Sources checked: scan `figures/ch4/fig07c.png`; redraw `figures/v2/ch4/fig07c.pdf` (rendered at 300 and 600 dpi,
plus a 1200 dpi crop of the $k_{\max}$ leader and the white gap); source `figures/v2/ch4/fig07c.tex` lines 1-35;
`fig07c.py`; `fig07c.csv`; `fig07c.calib.json`. Other sources: inventory row `ch4-fig07c`
(`figures/v2/inventory.csv`:134); caption `chapters/ch4-sec2b.tex`:441-447; the template `fig06a.tex`; the
white-casing precedents `figures/v2/ch2/fig02.tex`:46 and `figures/v2/ch3/fig23.tex`:31-32; the round-1 report.

Reruns:
- I ran `fig07c.py` on a scratch copy against the changed helpers. The CSV it writes is byte-identical to the
  repository's.
- I ran the overlay of the four curves:

  | curve | 95% within | max |
  |-------|-----------|-----|
  | FM k_min | 0.00 px | 2.00 px |
  | CB k_min | 2.00 px | 2.24 px |
  | FM k_max | 0.00 px | 0.00 px |
  | CB k_max | 2.00 px | 2.24 px |

  All pass. The calibration residual is 0.78 px.
- All four leader ends lie on their CSV curves within 0.002 point: FM k_max -0.422, CB k_max -4.050, FM k_min
  -2.096, CB k_min -6.005.

Round-1 follow-up:
- **Should-fix 1 (the $k_{\max}$ leader crossing the k_min solid): resolved.** The flat white casing
  `\draw[white, line width=2.4pt, shorten >=1.9pt] (kmax.north) -- (axis cs:0.0611,-0.421);` (fig07c.tex:27) is
  drawn before the leader (:28).
  - At 1200 dpi the lower (k_min) solid has a clean gap about 2 pt wide where the leader passes, as in the 1973 art.
  - The upper (k_max) solid is unbroken, and the leader ends on it.
  - The zero line above is untouched.
  - The casing starts at the node's north anchor, so the top of the "k" glyph is not clipped.

  The gap can also be seen in the 300 dpi render, so at final size the leader now marks the upper solid without
  ambiguity. The casing is flat white with no transparency. The same device is already used in Ch2 Fig 2 and
  Ch3 Fig 23.
- **Notes 2 and 3** (the crop is turned, so the inventory's eyeball values differ; the other leaders cross no curve)
  still stand and need no change to the figure.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | This is the only panel of the family with a white gap. fig08b's optional gap was declined, for a stated reason: there the leader's target reads correctly. This panel needs the gap because its two same-style solids are only 0.47 point apart. I accept the difference: the gap answers a real ambiguity and follows the print, and it does not change the family's look. | fig07c.tex:25-28 | None needed. |
| 2 | note | Carried forward, not in this figure's files: the inventory row still reads the solids' ends as about -2 and -3.2 and calls the rising zero line a drafting slip. The crop is turned by 0.55 degrees, and the redraw's -2.31 and -3.69 are right. | inventory.csv:134 | Update the inventory text when its status changes. |

Also checked, with no issue:
- **Frame and axes.** The frame is identical to fig06a (the x axis is 2402 px long at 600 dpi). The ticks, the titles
  ("Percent error in $y_{\max}$", "$m_o$ (kg)"), the legend at the upper right and the level zero line are as
  audited.
- **Curve identities.** The upper solid is k_max (it gets the $k_{\max}$ leader) and the lower one is k_min. The
  dashed curves cross near 0.079.
- **Style.** The house style is followed; there is no local style and no panel letter in the art.
- **Caption.** The caption holds for the redraw.

## Verdict

pass (0 must-fix, 0 should-fix, 2 notes). The round-1 should-fix is resolved, with no regression.
