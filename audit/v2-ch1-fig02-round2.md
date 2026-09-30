# v2 audit: ch1/fig02 (round 2)

The 1973 Figure 2, shown in the Errata and Supplement Part beside its 1994 replacement.

Sources checked: figures/ch1/fig02.png (scan); figures/v2/ch1/fig02.pdf (current, rendered 150, 300 and 1200 dpi);
figures/v2/ch1/fig02.tex:1-26; audit/v2-ch1-fig02-round1.md; figures/v2/inventory.csv row ch1-fig02; 1973 caption
backmatter/supplement/s-ch1.tex:268-283; figures/v2/tamrfig.sty (`\plumeshapeb`, `plume bulge`, `vec`).

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | should-fix | resolved | The plume now bulges to 1.8 r (`plume bulge=1.8`, fig02.tex:9, and `\plumeshapeb{1.8}`, :12, :16; the agreed plume parameter), so at the slug it is about 16.9pt across inside the outlines. At 1200 dpi the $\Delta m_e$ ink lies inside the band: 0.4pt clear of the left outline, 1.1pt of the right. |
| 2 | should-fix | resolved | The plume outline is redrawn after the `wash` fill (fig02.tex:16). At 1200 dpi the outline is 7 px wide both inside the band and above and below it, so the band's sides no longer thin out. |

## New findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | $\Delta m_e$ is centred on its bounding box, which puts its ink about 0.5pt left of the plume axis. The $\Delta$ therefore clears the left outline by only 0.4pt (0.15 mm), against 1.1pt on the right. It does not touch, and the printed label also fills its band. | fig02.tex:17 | Optional: `xshift=0.4pt` on the node. |

Checked again: single rocket with a spindle plume as wide as the body at the exit plane (as the caption's NOTE
says); grey slug a third of the way down; bold $\vec{F}$ up and $\vec{c}$ down, both `vec` (1.3pt); axis cross +y/+x
with arrowheads; all five inventory labels present.

## Verdict

pass (0 must-fix, 0 should-fix open)
