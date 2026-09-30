# v2 audit: ch1/fig08 (round 1)

Sources checked: figures/ch1/fig08.png (scan, upscaled 2x); figures/v2/ch1/fig08.pdf (rendered 150, 350 and 1200
dpi); figures/v2/ch1/fig08.tex:1-22; figures/v2/inventory.csv row ch1-fig08; caption chapters/ch1-sec3.tex:26-34
(float placement comment :21-25); citations ch1-sec2b.tex:307-313; corrections/v2-figures.md;
figures/v2/tamrfig.sty; the Fig 6 and Fig 7 redraws for consistency.

Geometry verified from the source (axis 27 deg, $\alpha$ = 33 deg): $\vec{V}$ from the C.G. (0.62L) at 60 deg;
$\vec{W}$ straight down from the C.G.; $\vec{D}$ from the C.P. (0.75L) at 240 deg, antiparallel to $\vec{V}$;
$\vec{S}$ from the C.P. at -30 deg, perpendicular to $\vec{V}$ and on the same side as Fig 7's $\vec{S}$;
$\vec{F}$ along the axis, pushing into the tail from 2.6 cm behind it. The axis is extended ahead of the nose as a
dash-dot line (as printed). The caption's five quantities (thrust, drag, weight, side force, velocity), the
general attitude ($\alpha \neq 0$, not vertical) and the absence of wind all hold. All printed labels present and
typeset ($\vec{V}$, $\vec{F}$, $\vec{D}$, $\vec{W}$, $\vec{S}$). Same rocket, attitude and stations as Figs 6 and 7.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The $\vec{W}$ label (pos 0.8, right of the shaft, about 1.2 cm below the C.G.) sits on the $\vec{S}$ arrow: $\vec{S}$ crosses the vertical through the C.G. 0.81 cm below it and descends at 30 deg, passing through the label's vector accent. At 150 dpi the accent merges with the $\vec{S}$ shaft and the label reads as a plain W. | fig08.tex:15 | Put the label on the other side, `node[pos=0.8, left=1pt] {$\vec{W}$}` (clear: $\vec{D}$ is about 1.2 cm to the left at that height), or below the tip (`pos=1, below`). |
| 2 | note | $\vec{W}$ crosses $\vec{S}$ 0.81 cm below the C.G.; the printed $\vec{W}$ also crosses $\vec{S}$ just below the C.G. | fig08.tex:15, 17 | None. |
| 3 | note | $\vec{D}$ crosses the lower fin close to its leading-edge tip corner, at about 20 deg to the leading edge, which makes a small cluttered spot; the printed $\vec{D}$ also runs over the lower fin (the inventory notes the fin "partly hidden behind the D arrow"). Legible as drawn. | fig08.tex:9, 16 | None needed. |

## Verdict

pass (0 must-fix, 1 should-fix)
