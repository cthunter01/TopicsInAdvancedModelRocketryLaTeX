# v2 audit: ch1/fig06 (round 2)

Sources checked: figures/ch1/fig06.png (scan); figures/v2/ch1/fig06.pdf (rendered 400 dpi); figures/v2/ch1/fig06.tex:1-21;
audit/v2-ch1-fig06-round1.md; figures/v2/inventory.csv row ch1-fig06; caption chapters/ch1-sec2b.tex:101-110;
figures/v2/tamrfig.sty (`vec` now 1.3pt, `angle arc`, `cg mark`, `centerline`); fig07.tex and fig08.tex for consistency.

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | should-fix | resolved | fig06.tex:9-11 now draws the pic with `centerline=false`, the dash-dot centre line inside the body only (0.1 to 6.3 of 6.4) and the thin solid axis only outside it (nose tip to 0.9 ahead, tail to 0.9 behind), exactly as fig07.tex:9-11. The render shows dash-dot inside, solid beyond nose and tail, as the scan. Figs 6 and 7 now agree. |
| 2 | note | accepted: no action | The arc's axis-end head still sits on the centre line inside the body (fig06.tex:17); legible. |
| 3 | note | accepted: no action | Double-headed arc here, plain arc in Fig 7, both as printed. |

## New findings

None. The 1.3pt $\vec{V}$ keeps its head clear of the $\vec{V}$ label and of the arc; the C.G. mark (drawn last)
covers the shaft's start as intended; no ink touches the page edge except line caps.

## Verdict

pass (0 must-fix, 0 should-fix open)
