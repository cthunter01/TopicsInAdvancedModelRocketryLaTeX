# v2 audit: ch2/fig38 (round 1)

Sources checked: scan `figures/ch2/fig38.png` (3x upscale; pixel scan of the extension lines and of the joint
lines crossing the body); redraw `figures/v2/ch2/fig38.pdf` (400 dpi render, 2x crops of the $r_r$/$d_{\max}$
region and of the C.G./C.P. region) and `build/v2/png/ch2-fig38-compare.png`; build log
`build/v2/ch2/fig38.log` (no warnings); `pdfinfo`/`pdffonts` (312.2 x 156.5 pt = 4.34 in wide, all fonts
embedded); source `figures/v2/ch2/fig38.tex` lines 1-42; inventory row `ch2-fig38`; `chapters/ch2-sec4.tex`:560-591
(eqs. (95), (96), static stability margin text, caption), :234-237 and :272-275 (eqs. (81), (83): $r_r$);
STYLE.md sections 13 and 16; the approved `figures/v2/ch2/fig39.tex`.

Checks made:
- **Outline and scale.** The stations, fins, centre line and unit are identical to the approved Fig 39.
- **Stations** (1973 Fig 38 mapped station by station onto the Fig 39 outline; the 1973 joints are at 53 / 107
  / 143.5 / 293 / 330.5 and the tail at 482 scan px), against the redraw:
  - C.G. 281.3 / 283;
  - C.P. 345.8 / 345;
  - $r_r$ arrows 73 / 72, on the forward tube;
  - $d_{\max}$ arrows 203.5 / 205, on the main tube.
  - The C.G. and C.P. agree with Figs 32, 37 and 39.
- **Formulas.** Both lines of the artwork are typeset: $A_r = \pi r_r^2$ and "Static stability margin in
  calibers $= \dfrac{\bar Z - \bar W}{d_{\max}}$". This matches the text (ch2-sec4.tex:575-584: margin
  $\bar Z - \bar W$ divided by the maximum body diameter). The subscript max is upright (STYLE.md 13).
- **Dimensions.**
  - $\bar Z$ (to the C.P.) is above $\bar W$ (to the C.G.), both from the nose-tip datum, as printed.
  - $r_r$ runs from the centre line to the upper surface of the forward tube, whose radius 12.5 is the nose-base
    radius (the reference radius of eqs. (81), (83), (95)). The arrows are outside, as printed.
  - $d_{\max}$ runs across the main tube (radius 17, the largest on the body), with outside arrows as printed.
  - The drawn margin is $(345 - 283)/34 = 1.8$ calibers, with the C.P. behind the C.G. (stable), as the text
    requires.
- **Lettering.**
  - All eight items are present: the two formula lines, $\bar Z$, $\bar W$, $r_r$, $d_{\max}$, C.G., C.P.
  - The $r_r$ and $d_{\max}$ labels are set horizontal where the 1973 labels are rotated. This is a restyle and
    the drafter records it.
  - Nothing has been added: no $Z = 0$ label, as printed.
- **Legibility.**
  - The formula block clears the $\bar Z$ label by about 3.5 mm.
  - The $r_r$ lower arrow crosses the lower tube outline to reach the centre line, as printed.
  - The arrowheads (4 pt) are clear at 400 dpi.
  - Nothing is clipped.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The C.P. at 345 is schematic, as in the 1973 art and in Fig 32. For the drawn rocket, eq. (92) with eqs. (80b), (82), (84), (88)-(90$'$), (89) gives 389 (3 fins) or 401 (4 fins), a margin of 3.1-3.5 calibers against the 1.8 drawn. This is the same question as the Figs 34/35 gate item and Fig 32 finding 1. | fig38.tex:25, 36 | No change by the drafter. For the lead: include in the Figs 34/35 gate question. |
| 2 | note | The C.G. mark (283) comes within about 0.1 mm of the joint line at 289, as in Figs 37 and 39. | fig38.tex:35 | Optional, family-wide only (see Fig 37 finding 3). |
| 3 | note | The local style `dim stub` (an outside arrow for a dimension too short for its label) is defined in the figure, as the rules allow. | fig38.tex:14 | Style suggestion for `tamrfig.sty`: an outside-arrow dimension (e.g. `\dimstub` or a `dimension outside` style) if other figures need one. |

## Verdict: pass (0 must-fix, 0 should-fix)
