# v2 audit: ch2/fig39 (round 1)

Sources checked: scan `figures/ch2/fig39.png` (2x upscale, with 4x crops of the nose and the tail/fins and a
pixel scan of the centre line); redraw `figures/v2/ch2/fig39.pdf` (350 dpi render) and
`build/v2/png/ch2-fig39-compare.png`; source `figures/v2/ch2/fig39.tex` lines 1-30; inventory row `ch2-fig39`
(`figures/v2/inventory.csv`:52); `chapters/ch2-sec4.tex`:594-611 (eqs. (97), (98)), :661-672 (citing
sentence, caption); `corrections/v2-figures.md` standing rule 2 ($\bar Z_{T(B)}$ kept); `macros.tex`:11-12
(`\CG`, `\CP`); `figures/v2/tamrfig.sty` (`\rocketoutline`, `\rocketfins`, `\dimline`, marks).

Checks made:
- **Point stations**, measured on the scan from the nose tip (scan px, 150 dpi):
  - C.P.$_n$ 34, C.P.$_{CS}$ 126.5, C.G. 283, C.P.$_{CB}$ 311, C.P.$_{T(B)}$ 449.
  - The redraw has 34, 127, 283, 312 and 450, in the same order along the body.
  - C.P.$_{CS}$ lies on the conical shoulder (109-144) and C.P.$_{CB}$ on the boattail (289-326.5), as printed.
- **Body stations**, scan against redraw:
  - Joints at 55 / 109 / 146 / 291 / 328 against 54 / 109 / 144 / 289 / 326.5.
  - Tail at 476.5 against 476.
  - Fin root leading edge about 403 against 404.
  - Fin span about 50 against 50.
  - Fin tip chord about 19 (with a chamfered corner) against 15.
- **Dimension lines.** All five start on the extension line from the nose tip (x = 0) and end on the extension
  line of their own point: $\bar Z_n$ at 34, $\bar Z_{CS}$ at 127, $\bar W$ at 283, $\bar Z_{CB}$ at 312,
  $\bar Z_{T(B)}$ at 450. They are stacked with the longest on top ($\bar Z_{T(B)}$, $\bar Z_{CB}$, $\bar W$,
  $\bar Z_{CS}$, $\bar Z_n$), as printed. The extension lines rise from the points, as printed.
- **Lettering and notation.**
  - All ten labels are present: $\bar Z_{T(B)}$, $\bar Z_{CB}$, $\bar W$, $\bar Z_{CS}$, $\bar Z_n$, C.P.$_n$,
    C.P.$_{CS}$, C.G., C.P.$_{CB}$, C.P.$_{T(B)}$.
  - They are typeset in the text's notation ($\bar{Z}_{CS}$, `\CP`, `\CG`).
  - $\bar Z_{T(B)}$ against eqs. (97)/(98) $\bar Z_T$ is standing rule 2.
  - No overall $\bar Z$ has been added.
- **Caption and text.** Every lever arm $[\bar Z_x - \bar W]$ of eqs. (97)/(98) can be read off the figure.
- **Legibility.**
  - No dimension label meets an extension line.
  - The C.P.$_{T(B)}$ leader crosses the lower fin, as the 1973 leader does. Its label starts about 2.5 mm
    right of the fin's trailing edge.
  - Nothing is clipped: the bounding box includes C.P.$_{T(B)}$.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The C.G. leader runs straight down (1973: diagonal with an elbow), so it continues the $\bar W$ extension line into one vertical line through the body. The C.G. label at its foot keeps the meaning clear. | fig39.tex:25 | Optional: slant it like the C.P. leaders. |
| 2 | note | Small shape simplifications: the nose is one tangent ogive to 54 (1973: ogive to about 39, then a short cylindrical base to the joint at 55); the fin tip chord is 15 against about 19; the leaders have no horizontal elbows. None of these changes the notation. | fig39.tex:9-10, 23-27 | none |

## Verdict

pass (0 must-fix, 0 should-fix)
