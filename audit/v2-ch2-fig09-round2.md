# v2 audit: ch2/fig09 (round 2)

Sources checked: figures/ch2/fig09.png (the scan, both plots upscaled 2x); figures/v2/ch2/fig09.pdf (rebuilt with
`make fig F=ch2/fig09`: 4.69 x 6.12 in, all fonts embedded, rendered at 400 dpi with 1200 dpi zooms of the
origin and of the point where the curves part, in both plots) and build/v2/png/ch2-fig09-compare.png;
figures/v2/ch2/fig09.tex, fig09.py, fig09.calib.json, fig09-mc.csv, fig09-md.csv (and the fig07.csv and fig08.csv
they copy); figures/v2/inventory.csv row ch2-fig09; caption chapters/ch2-sec2.tex:114-119; citing text
ch2-sec2.tex:104-108; eqs. (8) and (9) (ch2-sec2.tex:93-104); STYLE.md sections 13 and 16; tamrfig.sty (`guide`,
`\dimline`, fonts); corrections/v2-figures.md; audit/v2-ch2-fig09-round1.md and the round-1 fix report.

Round-1 findings:
- Should-fix 1 (the linear approximation was hidden under the true curve along their shared segment):
  **resolved**. In each plot the true curve is drawn first, as `series1` at 1pt (fig09.tex:22 and 38). The linear
  approximation is drawn after it, as `series2, solid, line width=0.5pt` (fig09.tex:23 and 39). At 1200 dpi the
  shared segment shows an orange core inside the blue line from the origin all the way to the parting point. The
  orange line then runs on alone, tangent to the curve, from about 0.21 rad and from about 75 rad/sec. It now
  reads as a tangent through the origin, which is what ch2-sec2.tex:104-106 relies on. The printed art draws
  both lines solid, so solid is kept.
- Note 2 (the computed lower linear approximation is not within 3 px of the printed line): **still open, for
  the orchestrator**. corrections/v2-figures.md has no Ch2 Fig 9 entry under Minor yet. The data are unchanged,
  and so is the overlay (below).
- Note 3 (the upper "Linear approximation" label overhung the end of the x axis): **resolved**. The label now
  has `anchor=south east` at `(axis cs:0.3,3.07e5)` (fig09.tex:24). In the render it spans about 0.235-0.299 rad.
  That leaves about 0.13 in clear of the dashed limit at 0.225, and the label sits above the line's end (3.0e5).
  The figure is now 4.69 in wide, which matches Figs 7 (4.68) and 8 (4.69).

Re-checked (no regressions):
- Lettering against the scan and the inventory. Upper plot: the y title "Corrective moment $M_c$ (dyn-cm)", y
  ticks from 0 to $4\times10^5$, all labelled; the x title "Angular deflection $\alpha_X$ (rad)", x ticks
  0-0.3 with minor ticks at 0.05, 0.15 and 0.25; "Range of validity"; "Linear approximation" (two lines); "True
  $M_c$"; "$C_1 = 1\times10^6$ dyn-cm". Lower plot: the y title "Damping moment $M_d$ (dyn-cm)", y ticks 0,
  $1\times10^6$ and $2\times10^6$ with minor ticks at $0.5\times10^6$ and $1.5\times10^6$; the x title "Angular
  velocity $\Omega_X$ (rad/sec)", x ticks 0-150 with minor ticks at 25, 75 and 125; "Range of validity"; "Linear
  approximation" (two lines); "True $M_d$"; "$C_2 = 1.25\times10^4$ / dyn-cm-sec". Everything is present and in
  the section 13 forms. All text is `\small` in ink. Nothing is added.
- Caption: the dashed limits are at 0.225 rad and 87 rad/sec (`guide`, dashed as printed). The "Range of
  validity" dimension lines run from the y axis to the dashed lines, at 2.8e5 and 1.35e6, and both arrowheads
  are visible. Neither dimension line crosses a curve: the linear lines reach those levels only at 0.28 rad and
  108 rad/sec.
- Data: fig09.py reruns, from the root and from /tmp with writes intercepted, to byte-identical CSVs. The `true`
  columns equal fig07.csv and fig08.csv (max difference 0). The `linear` columns are exactly $10^6\alpha_X$ and
  $1.25\times10^4\Omega_X$ (eqs. (8) and (9) with the lettered coefficients). The true curves lie 1.3% below the
  line at 0.225 rad and 1.9% below it at 87 rad/sec, so the caption's ranges of linearity hold. They lie 0.09% and
  0.13% below at 0.21 rad and 70 rad/sec.
- Overlay on the scan (`digitize.py overlay`, fig09.calib.json): upper true $M_c$ 95% 2.00 px, linear $M_c$
  2.83 px; lower true $M_d$ 1.41 px, linear $M_d$ 4.12 px (0.70 mm, MISMATCH). These are the same as in round 1.
  The lower line is computed from the lettering, so it is accepted under the pilot decision. Only the log entry
  in note 2 is outstanding.
- Legibility: there are no overlaps. "True $M_c$" and "True $M_d$" sit below their curves. The upper label of
  the lower plot clears the line by about 0.14 in. The $C_2$ label spans about 42-78 rad/sec and stays clear of
  the line and the dashed limit at 87. Both plots use the Fig 7/8 axes (3.8 x 2.3 in), and their left edges and y
  titles are aligned.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Still open from round 1, and outside the drafter's scope: the computed lower linear approximation misses the printed line by 95% 4.12 px (0.70 mm), which is above the 3 px target. STYLE.md section 16 asks for the mismatch to be logged, and corrections/v2-figures.md still has no Ch2 Fig 9 entry. | corrections/v2-figures.md (Minor) | Orchestrator: add "Ch2 Fig 9 (lower): the printed linear approximation ends at about 1.9e6 at 150 rad/sec, about 1% steeper than the lettered $C_2$ (1.875e6); computed from $C_2$." |

## Verdict: pass

0 must-fix, 0 should-fix. The round-1 should-fix and note 3 are resolved, and there are no regressions.
