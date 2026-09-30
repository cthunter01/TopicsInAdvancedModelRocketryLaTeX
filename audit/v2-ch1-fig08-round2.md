# v2 audit: ch1/fig08 (round 2)

Sources checked: figures/ch1/fig08.png (scan); figures/v2/ch1/fig08.pdf (rendered 400 dpi); figures/v2/ch1/fig08.tex:1-22;
audit/v2-ch1-fig08-round1.md; figures/v2/inventory.csv row ch1-fig08; caption chapters/ch1-sec3.tex:26-34;
figures/v2/tamrfig.sty (`vec` now 1.3pt).

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | should-fix | resolved | fig08.tex:15 now sets `node[pos=0.8, left=1pt] {$\vec{W}$}`. The label sits left of the $\vec{W}$ shaft, 1.2 cm below the C.G.; $\vec{S}$ crosses the vertical 0.81 cm below the C.G. on the right-hand side and $\vec{D}$ passes about 1.2 cm further left, so the accent and letter touch nothing (400 dpi). |
| 2 | note | accepted: no action | $\vec{W}$ still crosses $\vec{S}$ just below the C.G., as printed. |
| 3 | note | accepted: no action | $\vec{D}$ still crosses the lower fin near its leading-edge tip, as printed; legible at 1.3pt. |

## New findings

None. The 1.3pt vectors keep every label clear ($\vec{V}$ at its tip, $\vec{S}$ above right, $\vec{D}$ right of
its shaft below the fin, $\vec{F}$ below its shaft); the $\vec{F}$ head ends at the tail on the axis as printed;
the dash-dot axis still continues ahead of the nose, as printed (fig08.tex:10).

## Verdict

pass (0 must-fix, 0 should-fix open)
