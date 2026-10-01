# v2 audit: ch2/fig09 (round 1)

Sources checked: figures/ch2/fig09.png (scan, each plot upscaled 3x); figures/v2/ch2/fig09.pdf (rebuilt with `make
fig F=ch2/fig09`, 4.81 x 6.12 in, fonts embedded; rendered at 150, 300 and 600 dpi) and
build/v2/png/ch2-fig09-compare.png; figures/v2/ch2/fig09.tex, fig09.py, fig09.calib.json, fig09-mc.csv, fig09-md.csv
(and fig07.csv, fig08.csv they copy); figures/v2/inventory.csv row ch2-fig09; caption chapters/ch2-sec2.tex:114-119;
citing text ch2-sec2.tex:104-108 and eqs. (8), (9) (ch2-sec2.tex:93-104); STYLE.md sections 13 and 16;
corrections/v2-figures.md; approved examples ch2/fig25.tex, ch1/fig03.tex (tangent line as `series2, solid`),
ch4/fig06a.tex.

Checked and correct:
- Lettering, upper: y title "Corrective moment $M_c$ (dyn-cm)", ticks 0 to $4\times10^5$ step $1\times10^5$
  labelled; x title "Angular deflection $\alpha_X$ (rad)", ticks 0-0.3 labelled, minor at 0.05, 0.15, 0.25; "Range
  of validity"; "Linear approximation" (two lines); "True $M_c$"; "$C_1 = 1\times10^6$ dyn-cm". Lower: y title
  "Damping moment $M_d$ (dyn-cm)", ticks 0, $1\times10^6$, $2\times10^6$ labelled, minor at $0.5\times10^6$,
  $1.5\times10^6$; x title "Angular velocity $\Omega_X$ (rad/sec)", ticks 0-150 labelled, minor at 25, 75, 125;
  "Range of validity"; "Linear approximation" (two lines); "True $M_d$"; "$C_2 = 1.25\times10^4$ dyn-cm-sec" (two
  lines). All present, all in the section 13 forms, no panel letters (none printed). Nothing added.
- Caption: dashed limits at 0.225 rad (guide from 0 to 2.97e5) and 87 rad/sec (0 to 1.5e6); the "Range of validity"
  dimension lines run from the y axis to the dashed lines at 2.8e5 and 1.35e6, as in the scan.
- Linear approximations: eq. (8) and eq. (9) with the lettered coefficients: fig09-mc.csv `linear` = 1e6 alpha
  exactly (3.0e5 at 0.3), fig09-md.csv `linear` = 1.25e4 Omega exactly (1.875e6 at 150).
- True curves: byte-for-byte the Fig 7 and Fig 8 data (fig09-*.csv `true` equals fig07.csv `Mc` and fig08.csv `Md`,
  max difference 0); fig09.py reruns to identical CSVs. Both are tangent to their lines at zero (the text: the
  approximations "are just the slopes of the moment curves" at zero) and lie 1.6% below the line at 0.225 rad and
  1.9% below at 87 rad/sec, so the caption's ranges of linearity hold on the redraw.
- Overlay on this scan (`digitize.py overlay`, calibration fig09.calib.json): true $M_c$ mean 0.80 px, 95% 2.00 px;
  linear $M_c$ mean 1.26 px, 95% 2.83 px; true $M_d$ mean 0.63 px, 95% 1.41 px; linear $M_d$ mean 1.73 px, 95%
  4.12 px (0.70 mm, MISMATCH): the printed line reaches about 1.9e6 at 150 rad/sec, the lettered $C_2$ gives 1.875e6.
  Computed from the lettering, so accepted under the pilot decision (see finding 2).
- Legibility: no overlaps (nearest clearance: "Linear approximation" upper about 3 pt above the line's end; "True
  $M_c$", "True $M_d$" about 0.06-0.08 in below their curves; the $C_2$ label ends at about 78 rad/sec, clear of the
  dashed line at 87); dimension arrowheads visible and touching the axis and the dashed lines; width 4.81 in. Both
  plots use the Fig 7/8 axes (3.8 x 2.3 in), left edges aligned.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The linear approximation is invisible along the range where it matters most: the true curves equal $C_1\alpha_X$ exactly up to 0.20 rad and $C_2\Omega_X$ up to 60 rad/sec, and the blue true curve is drawn over the orange line at the same 1pt width, so the orange "Linear approximation" appears only where the curves visibly part (from about 0.21-0.22 rad and 75-80 rad/sec) and reads as a branch starting there, not as the tangent through the origin that the text relies on ("the approximations are just the slopes of the moment curves at $\alpha_X$ and $\Omega_X = 0$", ch2-sec2.tex:104-106). In the monochrome scan the one line from the origin simply splits in two; with colour coding the identity of the shared segment is lost. | fig09.tex:20-21, 36-37 | Keep the true curve first and draw the linear approximation over it thinner, e.g. `\addplot[series2, solid, line width=0.5pt]` after the true curve, so the shared segment shows both colours from the origin; or draw the linear approximation on top at full width (as ch1/fig03 draws its tangent after the curve). |
| 2 | note | The computed lower linear approximation misses the printed line by 95% 4.12 px (0.70 mm), above the 3 px target; STYLE.md section 16 asks for such a mismatch to go to corrections/v2-figures.md. The drafter may not edit corrections/. | corrections/v2-figures.md (Minor) | Orchestrator: log "Ch2 Fig 9 (lower): the printed linear approximation ends at about 1.9e6 at 150 rad/sec, about 1% steeper than the lettered $C_2$ (1.875e6); computed from $C_2$". |
| 3 | note | The upper "Linear approximation" label is centred at $\alpha_X = 0.288$ and overhangs the right end of the x axis by about 0.24 in, which makes the figure 0.13 in wider than Figs 7 and 8 (4.81 against 4.68 in), so the plots sit slightly off-centre relative to them on the page. The scan's label also overhangs a little. | fig09.tex:22 | Optional: `anchor=south east` at `(axis cs:0.3,3.07e5)`; the label then spans about 0.238-0.3 rad, clear of the dashed line at 0.225 and of the line below it. |

## Verdict

pass (0 must-fix, 1 should-fix)
