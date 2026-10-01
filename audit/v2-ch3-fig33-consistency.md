# v2 audit: ch3/fig33 (consistency fix verification)

Issue checked: velocity profiles drawn three ways in Chapter 3 (keys ch3/fig10, fig13, fig23, fig33). The
suggestion for Fig 33: copy the family styles from fig16.tex:13-16, draw the profile curve as `profile` (s1, 1pt)
and the headless velocity lines as `profile stroke` (s1, 0.5pt), and keep the base line in ink.

Sources checked: redraw `figures/v2/ch3/fig33.tex`, rebuilt with `make fig F=ch3/fig33` (4.76 x 2.96 in) and
rendered at 400 dpi (profile zoomed); scan `figures/ch3/fig33.png` (profile zoomed 6x); inventory row `ch3-fig33`;
round-1 audit `audit/v2-ch3-fig33-round1.md`; the peer profile figures fig06, fig09, fig10, fig13, fig16, fig17,
fig18 and fig25; `tamrfig.sty` (line weights); STYLE.md section 16. I also ran my own ink overlay on the scan:
the PDF rendered at 119.8 dpi (one drawing unit per scan pixel), with a search for the best shift.

## Issue 1 (velocity profiles): resolved

- fig33.tex:26-30 defines `profile`, `profile arrow` and `profile stroke`, character for character as in
  fig16.tex:13-15 (and fig10, fig13, fig17, fig18, fig25).
- The profile curve (fig33.tex:59-60) is `profile` (s1, 1pt). The three headless velocity lines (fig33.tex:56-57)
  are `profile stroke` (s1, 0.5pt), headless as printed. They are drawn first, so the curve lies on top. Each one
  ends exactly on the curve, because both use the same expression u = U(1 - (1 - eta)^2.5) at eta = 0.3, 0.55
  and 0.8.
- The base line (fig33.tex:58) stays in ink. The circulation loops, the shear-layer lines and the dividing
  streamlines stay in ink `thin line`, as before.
- At 400 dpi the curve starts on the dividing streamline at (325, 33.6) and ends on the outer edge of the shear
  layer. The blue profile no longer reads as part of the flow-line ink.

## Regression check: none found

- Geometry is unchanged. My overlay gives 95.3% of the redraw's ink within 3 px of the scan's ink. This matches
  the header and round 1 (95.2%). All of the blue profile pixels lie within 3 px of the scan's ink (95th
  percentile 2.4 px).
- Lettering is unchanged: $\epsilon$, $\delta$, $p_b$ (twice), R as a curve tag. It agrees with the inventory
  row. Nothing was added or lost.
- The round-1 notes (break line, axial velocity lines, R placement, flow lines left of the break) are unchanged
  and still notes.
- The local `\tikzset` block is the sanctioned family copy (round 1 said "no local styles"; the issue asked for
  this copy). The kit suggestion stands: move profile, profile arrow and profile stroke into tamrfig.sty.

## Findings

| # | severity | finding | where | suggested fix |
|---|---|---|---|---|
| 1 | should-fix | The profile's base line is `thin line` (0.45pt). In the rest of the chapter's profile family the u = 0 base line is `outline` (0.6pt): fig06.tex:29, fig09.tex:37, fig10.tex:51, fig13.tex:48, fig16.tex:65, fig17.tex:56. (Fig 18's base lines are its y axes, `thin vec`.) This is the only weight in Fig 33's profile that still differs from its peers. | fig33.tex:58 | `\draw[outline] (325,33.6) -- (325,64.4);` |
| 2 | note | The fixer counts nine figures with local copies of the profile styles. Figs 06 and 09 carry only `profile` and `profile arrow`, because they have no headless lines. Where present, the definitions are identical. | n/a | kit move, as suggested |

## Verdict: pass (no must-fix; one should-fix on the base-line weight)
