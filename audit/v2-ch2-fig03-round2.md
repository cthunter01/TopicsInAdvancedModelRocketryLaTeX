# v2 audit: ch2/fig03 (round 2)

Sources checked: scan `figures/ch2/fig03.png` (4x crop of the nose); redraw `figures/v2/ch2/fig03.pdf` (rebuilt
16:55 for the style change; rendered at 400 dpi whole, 800 and 1000 dpi crops of the F axis, nose, C.G. and tail);
source `figures/v2/ch2/fig03.tex`:1-49 (unchanged since round 1, mtime 15:43); round-1 report; inventory row
`ch2-fig03` (`figures/v2/inventory.csv`:16); caption and citing text `chapters/ch2-intro-sec1.tex`:200-230;
`figures/v2/tamrfig.sty` (current `thin vec`, `cg mark`, `centerline`, `outline`); STYLE.md section 16.

The source is unchanged, so only the style change could alter the figure. The figure uses `thin vec` (unchanged,
0.6pt), not `vec`, so the 1.3pt force-vector change does not reach it; `cg mark` is the quartered circle already
seen in round 1. The render matches the round-1 description: right-handed axes, positive senses of all three
rotation arrows, depth order of the four fins, tail ellipse, dash-dot extension, labels D, E, F, $\omega_D$,
$\omega_E$, $\omega_F$. I measured the nose silhouettes perpendicular to the projected axis at eight stations
(offsets 12/11, 26/25, 39/38, 47/45, 50/49, 51/50 px at 1000 dpi): the nose is symmetric and convex. The figure
has no panels.

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | note | accepted: note, no action | The C.G. is still the house quartered `cg mark` (fig03.tex:38), drawn last, so it covers the axis origin cleanly. The meaning is unchanged. |
| 2 | note | accepted: note, no action | The rotation arrows are still house Stealth heads (`thin vec` scope, fig03.tex:40-44). The senses were re-checked on the render and are correct. |
| 3 | note | accepted: note, no action | $\omega_E$ still sits at the lower right of its ellipse (fig03.tex:46), about 4 mm from the +E fin tip and away from the arrowhead at the top. It still reads with its ellipse. |
| 4 | note | not resolved: not yet checkable | The rocket and axes must match Ch2 Figs 1 and 6 and be reused in Fig 4. None of those is redrawn yet (only ch2/fig03, fig25 and fig39 exist in `figures/v2/ch2/`). Check this when they are drawn. |

## New findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The F axis is drawn in two pieces: a 0.45pt `thin line` from the nose tip, then a 0.6pt `thin vec`. At 800 dpi the weight step shows where the two meet, just at the crossing of the $\omega_F$ arc; the D and E axes are one 0.6pt stroke. It is hardly visible at final size. | fig03.tex:36-37 | Optional: draw it as one stroke, `\draw[thin vec] (tip) -- (0,\yn+1.5,0) node[above left=-1pt] {F};`. |

## Verdict

pass (0 must-fix, 0 should-fix)
