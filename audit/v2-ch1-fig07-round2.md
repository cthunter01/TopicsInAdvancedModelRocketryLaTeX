# v2 audit: ch1/fig07 (round 2)

Sources checked: figures/ch1/fig07.png (scan); figures/v2/ch1/fig07.pdf (rendered 400 and 1200 dpi; C.P. and
arrow-tip regions cropped); figures/v2/ch1/fig07.tex:1-26; audit/v2-ch1-fig07-round1.md; figures/v2/inventory.csv
row ch1-fig07; caption chapters/ch1-sec2b.tex:259-268; figures/v2/tamrfig.sty (`vec` now 1.3pt).

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | should-fix | resolved | fig07.tex:9-11: pic with `centerline=false`, dash-dot centre line from 0.1 to 6.3 (inside the body), thin solid axis only from the nose tip to 0.9 ahead and from the tail to 0.9 behind. At 1200 dpi the dash gaps inside the body are open (the centre line reads dash-dot), as in the scan. |
| 2 | note | accepted: no action | $\vec{N}$ and $\vec{D}_1$ still meet at the tip of $\vec{N}$; at 1200 dpi the two 1.3pt stealth heads stay distinct, side by side, as printed. |

## New findings

None. With the 1.3pt vectors the labels still clear their shafts ($\vec{S} = \vec{N}\cos\alpha$ above $\vec{S}$,
$\vec{N}$ left of $\vec{N}$, $\vec{D}_1 = \vec{N}\sin\alpha$ right of $\vec{D}_1$, $\alpha$ inside its arc), the
shafts of $\vec{N}$ and $\vec{S}$ leave the C.P. mark cleanly (the mark is drawn last), and the lowest
arrowheads stay inside the page. Geometry unchanged from round 1 ($\vec{N} = \vec{S} + \vec{D}_1$ exactly).

## Verdict

pass (0 must-fix, 0 should-fix open)
