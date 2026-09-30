# v2 audit: ch1/fig06 (round 1)

Sources checked: figures/ch1/fig06.png (scan, upscaled 2x); figures/v2/ch1/fig06.pdf (rendered 350 and 1200 dpi);
figures/v2/ch1/fig06.tex:1-19 (working-tree version using `model`); figures/v2/inventory.csv row ch1-fig06; caption
chapters/ch1-sec2b.tex:101-110 and citation ch1-sec2b.tex:91-94; corrections/v2-figures.md; figures/v2/tamrfig.sty
(`model`, `angle arc`, `cg mark`, `vec`, `centerline`); the Fig 7 and Fig 8 redraws for consistency.

Checked and correct: the rocket (`model`) nose up and to the right, axis at 27 deg; bold $\vec{V}$ from the C.G.
mark (quartered circle at 0.62L from the nose) at 60 deg, labelled at its tip; the angle arc between $\vec{V}$ and
the axis, measured to the axis (arc end on the centre line at 2.5 cm ahead of the C.G., near the nose shoulder as
printed), labelled $\alpha$ = 33 deg (the scan measures about 31 deg: axis about 30 deg, $\vec{V}$ about 61 deg;
unstated, so fine). No wind vector, as the caption's no-wind assumption requires. Both printed labels present and
typeset. Same rocket, attitude, $\alpha$ and C.G. station as Figs 7 and 8.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The 1973 figure extends the axis beyond the nose tip and past the tail as a thin solid line (the reference from which $\alpha$ is taken), with the dash-dot centre line only inside the body; the Fig 7 redraw reproduces this (fig07.tex:9). This redraw has only the pic's dash-dot centre line, 0.08L (0.51 cm) beyond each end, so Figs 6 and 7 now differ in how the same axis is drawn although the 1973 pair agree. | fig06.tex:9 | Add the thin solid extensions as in Fig 7 (outside the body only; see the Fig 7 report, finding 1), e.g. `\draw[thin line] (0,0) -- (27:0.9); \draw[thin line] (207:6.4) -- (207:7.3);`, or adopt one convention for Figs 6-8. |
| 2 | note | The arc's axis-end head lies on the centre line inside the body tube, so it crosses the upper outline; in the scan the arc stops on the upper outline. The redraw is the geometrically exact reading ($\alpha$ is the angle to the axis) and is legible. | fig06.tex:15 | None. |
| 3 | note | Double-headed `angle arc` here; Fig 7's $\alpha$ arc is plain. Both follow the 1973 art (an arrowhead at least at the axis end in Fig 6, a plain arc in Fig 7). | fig06.tex:15; fig07.tex:21 | None. |

## Verdict

pass (0 must-fix, 1 should-fix)
