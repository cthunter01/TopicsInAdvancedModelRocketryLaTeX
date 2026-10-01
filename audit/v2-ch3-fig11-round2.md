# v2 audit: ch3/fig11 (round 2)

Sources checked: figures/ch3/fig11.png (the scan); figures/v2/ch3/fig11.pdf (rebuilt with `make fig F=ch3/fig11`:
3.66 x 2.21 in, fonts embedded; rendered at 300 dpi) and build/v2/png/ch3-fig11-compare.png; figures/v2/ch3/fig11.tex,
fig11.py, fig11.csv, fig11.calib.json; figures/v2/inventory.csv row ch3-fig11; the caption
(chapters/ch3-sec2b.tex:341-346) and the citing text (ch3-sec2b.tex:322-336, eqs. (26)-(27);
ch3-sec3c-sec4a.tex:125-131, eq. (109)); STYLE.md sections 14 (Vectors: `\vec{}` wherever an arrow is drawn) and 16;
corrections/v2-figures.md; the round 1 audit and the fix record; the sibling vector lettering in
figures/v2/ch3/fig01.tex, fig12.tex, fig39.tex and the precedent figures/v2/ch1/fig06.tex.

Overlay, run myself (`digitize.py overlay fig11.calib.json --axes page fig11.csv`): outline 1119 points, mean
1.05 px, 95% 2.83 px (0.48 mm), max 5.00 px (ok). These are the same figures as round 1.

Changes since round 1: none. fig11.tex, fig11.py, fig11.csv and fig11.calib.json are unchanged (21:57-22:02,
before the round 1 audit), and tamrfig.sty is unchanged (21:33).

Round 1 findings:
- R1 #1 (note: `\vec` here, overbars in the siblings). Still open at chapter level. Fig 11 follows STYLE s.14
  ("`\vec{}` wherever an arrow is drawn") and the approved Ch1 Fig 6 precedent (fig06.tex:15, `$\vec{V}$`). Ch3
  Figs 1 (`$\bar{V}$`, `$\bar{D}$`, fig01.tex:25-26), 12 (`$\bar{V}$`, fig12.tex:79) and 39 (`$\bar{U}$`,
  fig39.tex:43) still keep the overbars. Nothing to change in Fig 11. The consistency pass or the gate should bring
  those three into line.
- R1 #2 (note: centre lines instead of the 1973 solid transverse axes, no base-centre dot) and R1 #3 (note: the
  paraboloid L/R = 5 and the true far-rim ellipse): house choices, kept.

Re-checked:
- The base rim's seen and hidden halves are right for the view. The viewer looks at the body from the nose side
  (c_x < 0). The rim point nearest the viewer (phi = phi_c) projects up and to the right of the base centre, and
  that arc is solid. The arc behind the body is `hidden`, as printed.
- dS, n and t: n at 91.7 deg and t at 35.4 deg on the page, n . t = 0, both starting at the centre of dS (as the
  caption says), on the seen side. $\vec{V}$ is the free stream along the axis ahead of the nose.
- Lettering: $\vec{n}$, $\vec{t}$, $dS$, $\vec{V}$; nothing is missing or added.
- Legibility at 300 dpi: all labels are clear of their arrows and of the silhouette, and nothing is clipped. Width
  3.66 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The chapter's vector lettering is still mixed: `\vec` here and in Ch1 Fig 6 (STYLE s.14), overbars in Ch3 Figs 1, 12 and 39. Fig 11 is the form the style sheet prescribes. | fig01.tex:25-26, fig12.tex:79, fig39.tex:43 | For the chapter consistency pass or the gate. No change to Fig 11. |
| 2 | note | The round 1 house-style notes (centre lines and no base-centre dot; the paraboloid L/R = 5; the true far-rim ellipse) stand. | fig11.tex:40-49 | None. |

## Verdict: pass (0 must-fix, 0 should-fix)
