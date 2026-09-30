# v2 audit: ch1/fig10 (round 2)

Sources checked: figures/ch1/fig10.png (scan; panels (a), (d), (e) upscaled 4x; body and plume widths measured row
by row); figures/v2/ch1/fig10.pdf (rendered 400 and 1200 dpi; widths measured the same way); figures/v2/ch1/fig10.tex:1-68;
audit/v2-ch1-fig10-round1.md; figures/v2/inventory.csv row ch1-fig10; caption chapters/ch1-sec3.tex:106-119;
figures/v2/tamrfig.sty (`\pic{rocket}` plume keys, `\plumeshape`/`\plumeshapeb`, `cg mark`, `cp mark`, `panel`);
STYLE.md section 16.

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | must-fix | resolved | fig10.tex:40 now `rotate=8, rotate=-90` (net -82 deg): the plume in (d) points down and to the right. Its point is at (0.167, -1.188); the thrust line (fig10.tex:42, (-0.28, 2.4) to (0.2, -1.3)) passes x = 0.186 at that height, so the line runs down the plume's middle to its point (0.02 cm off), as in the scan. The tail is pushed left, matching the bold arrow. |
| 2 | should-fix | resolved | fig10.tex:24 starts the canted-fin line at (-0.04, 0.66): the C.P. mark's rim is at 0.792 - 0.088 = 0.704, so the line begins 0.04 cm below the mark and no longer crosses it (400 dpi). |
| 3 | should-fix | resolved | fig10.tex:41 adds the thin axis `(0,0) -- (0,-1.3)` in (d), down to the depth of the thrust line, as printed; the angle between axis and thrust line now reads. |
| 4 | note | accepted: adopted | (a) now has 8 visible wind arrows (fig10.tex:18: -0.75 to 3.65, skipping the one behind the bold arrow at 0.79); the lowest is 0.5 cm above "(a)". |
| 5 | note | accepted: adopted | (e) rod at x = r + 0.035, the lug's centre line, with the cross-bar centred on it (fig10.tex:50-51). |
| 6 | note | resolved by STYLE.md section 16 | Letters at the lower right of each panel, (1.4, -1.25) in every scope: one baseline per row. |

## New findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The plumes are far wider than printed. In the scan they are needle-thin spindles narrower than the body: in (a) the body is 19 px wide (outline centres), the plume 12 px at the tail and 14 px at its widest (0.74 of the body's width), 73 px long (0.34L); (d) and (e) are the same. The redraw's plumes, from the pic's `plume` key and `\plumeshape` (bulge 1.3), start at the body's full width and widen to 1.40 times it (400 dpi, (a): body 53 px, plume 74 px), so they read as fat teardrops, about 1.9 times the printed relative width; five of the six panels show one, and in (d) the skewed teardrop dominates the tail. The length (1.1-1.2 = 0.31-0.33L) is right. The tamrfig.sty comment cites "the plumes of Ch1 Fig 10" for the 1.3 spindle, which the scan does not bear out. | fig10.tex:13 (`plume=#3`), 17, 23, 30, 40, 48; tamrfig.sty `\plumeshape` comment | Figure-local, the house default untouched: pass `plume=0` and draw each plume as (d) does, narrower at the nozzle, e.g. `\draw[thin line, shift={(#1,#2)}, rotate=-90] \plumeshapeb{1.25}{0.1}{1.1};` (start half-width 0.1 = 0.6r, widest about 0.13 = 0.78r), and in (d) `\plumeshapeb{1.25}{0.1}{1.2}` with its `rotate=8`. Reword the sty comment. |

## Verdict

pass (0 must-fix, 1 should-fix: new #1, plume width)
