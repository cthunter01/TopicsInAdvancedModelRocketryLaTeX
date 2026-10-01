# v2 audit: ch2/fig32 (round 1)

Sources checked: scan `figures/ch2/fig32.png` (3x upscale; pixel scan of the extension lines above the body and
of the joint lines crossing the body); redraw `figures/v2/ch2/fig32.pdf` (400 dpi render, 2x crops of the
boattail/C.P. region) and `build/v2/png/ch2-fig32-compare.png`; build log `build/v2/ch2/fig32.log` (no
warnings); `pdfinfo`/`pdffonts` (342.9 x 171.6 pt = 4.76 in wide, all fonts embedded); source
`figures/v2/ch2/fig32.tex` lines 1-37; inventory row `ch2-fig32`; `chapters/ch2-sec4.tex`:146-174 (citing text,
caption), :205-300 (eqs. (80)-(84)), :375-450 (eqs. (85)-(92)); `corrections/v2-figures.md` (standing rule 2,
Figs 34/35 gate item); STYLE.md sections 13 and 16; the approved `figures/v2/ch2/fig39.tex` and its audits.

Checks made:
- **Outline and scale.** `\rocketoutline{54/12.5, 109/12.5, 144/17, 289/17, 326.5/13.5, 476/13.5}`,
  `\rocketfins{476}{13.5}{72}{15}{50}{57.5}`, centre line -14 to 505 and `x = y = 0.0212cm` are identical to the
  approved Fig 39. The 1973 Fig 32 body is about 3% longer (joints at 58 / 116 / 155 / 308 / 346, tail 494 scan
  px from the tip); drawing it at Fig 39's size is what the family asks.
- **Point stations** (1973 Fig 32 mapped station by station onto the Fig 39 outline, against the redraw):
  - C.P.$_n$ 33.5 / 34;
  - C.P.$_{CS}$ 124.7 / 127;
  - C.P.$_{CB}$ 308.7 / 312;
  - C.P. 345.7 / 345;
  - C.P.$_{T(B)}$ 448.8 / 450.
  - Every mark is on the same body segment as printed: C.P.$_{CS}$ on the shoulder, C.P.$_{CB}$ on the boattail,
    C.P. just aft of the boattail, C.P.$_{T(B)}$ within the fin root chord.
- **Datum and sense.** The datum line rises from the nose tip, with $Z = 0$ above it. The arrow is marked
  $+Z$ and points aft. This matches ch2-sec4.tex:151-153.
- **Dimension lines.** All five start at the datum and end on the extension line of their own mark. They are
  stacked longest on top ($\bar Z_{T(B)}$, $\bar Z$, $\bar Z_{CB}$, $\bar Z_{CS}$, $\bar Z_n$), as printed.
  $\bar Z_n$ has its label outside to the right, the same device as Fig 39.
- **Lettering.**
  - All 12 labels are present: $Z = 0$, $+Z$, the five dimension labels and the five C.P. callouts.
  - They are typeset as the text has them ($\bar{Z}_{CS}$, $\bar{Z}_{CB}$, $\bar{Z}_{T(B)}$, `\CP`).
  - $\bar Z_{T(B)}$ against eq. (92)'s $\bar Z_T$ is standing rule 2.
  - Nothing has been added.
- **Marks.** All five points use the circle-dot `cp mark`, as printed. There is no C.G. in this figure.
- **Legibility.**
  - No label meets a line.
  - The C.P.$_{CB}$ label (centred below its vertical leader) clears the C.P. leader by about 45 units.
  - The C.P.$_{T(B)}$ leader crosses the lower fin, as in Fig 39 and in the 1973 drawing.
  - Nothing is clipped.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The C.P. marks are schematic (as the inventory says, and as the 1973 art and the approved Fig 39 place them), but they do not agree with the book's equations for the drawn rocket. Eq. (80b) (tangent ogive, $L = 54$) gives $\bar Z_n = 25$ against 34 drawn. Eq. (82) gives $\bar Z_{CS} = 117$ against 127. Eq. (84) gives $\bar Z_{CB} = 319$ against 312. Eq. (89) ($x_t = 57.5$, $c_r = 72$, $c_t = 15$) gives $\bar Z_T = 439$ against 450. Eq. (92) with eqs. (81), (83), (88), (89$'$), (90$'$) ($r_r = 12.5$, $s = 50$, $r_t = 13.5$) puts the overall C.P. at 389 (3 fins) or 401 (4 fins), against 345 drawn. The overall C.P. would move from 1.8 to 3.1-3.5 calibers behind the C.G. of Figs 37-39. This is the same question as the Figs 34/35 gate item. | fig32.tex:21, 28 | No change by the drafter. For the lead: add Figs 32, 38 and 39 to the Figs 34/35 gate question in `corrections/v2-figures.md` (keep as drawn, or place by the equations). |
| 2 | note | The C.P.$_{CB}$ leader runs straight down, so its label sits half a line lower than the other callouts, where Fig 39 slants it. This clears the C.P. callout at 345 and is the same device as Fig 39's C.G. leader. | fig32.tex:32 | none |

## Verdict: pass (0 must-fix, 0 should-fix)
