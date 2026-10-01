# v2 audit: ch2/fig14 (round 2)

Sources checked: figures/ch2/fig14.png (scan); figures/v2/ch2/fig14.pdf (17:55, newer than fig14.tex, fig14.csv
and tamrfig.sty; 4.61 x 2.86 in, 5 fonts all embedded; rendered at 300 and 600 dpi) and
build/v2/png/ch2-fig14-compare.png; figures/v2/ch2/fig14.tex, fig14.py, fig14.csv, fig14.calib.json; inventory
row ch2-fig14; caption chapters/ch2-sec3a.tex:469-480; citing text ch2-sec3a.tex:450-467; eqs. (24)-(26);
STYLE.md sections 13 and 16; corrections/v2-figures.md; round-1 audit and fix record; the family's other redraws.

Round-1 items: none were must-fix or should-fix, and the figure is unchanged. Notes 1 and 2 were for the
orchestrator (see findings).

Rechecked (no regression):
- Lettering: $\alpha_{X0}$, 0, Slope $=\Omega_{X0}$ at the right end of the line (as printed), $\alpha_X$ (rad),
  $t$ (sec).
- Data, evaluated in memory, with $C_1/I_L = -0.42$ and $C_2/2I_L = 0.13$: eq. (25) gives $\tau_1 = -1.883$
  (negative, as the text says) and $\tau_2 = 1.264$; eq. (26) gives $A_1 = 0.320$ and $A_2 = 0.050$. The CSV
  equals eq. (24) to 1e-5. The curve reaches the frame top (2.8) at t = 4.085 and is clipped there. The CSV runs
  on to 3.0 at t = 4.216.
- Tangent: the line (0, 0.37)-(3.45, 0.8185) has slope 0.130 = $-A_1/\tau_1 - A_2/\tau_2 = \Omega_{X0}$. At 600 dpi
  it is truly tangent. At its end the curve is at 2.00, well above it, so the label sits clear of the curve.
- Caption and text: the yaw angle increases without bound ("divergent").
- Overlay rerun: mean 2.66 px, 95% 8.38 px (1.42 mm), max 21.1 px, as in round 1. This is a computed curve and is
  accepted.
- Style: the family frame. Width 4.61 in. Nothing overlapping, and the clip at the top is intended.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Still open from round 1, not a redraw defect: the overlay mismatch is not yet listed under Minor. The printed curve turns up more steeply above $\alpha_X \approx 2.2$, and below 1.5 the 95th percentile is 5.0 px. | corrections/v2-figures.md | Orchestrator: log it as minor if overlay mismatches are listed. |
| 2 | note | Still open: the `tamr sketch` y-label suggestion (tamrfig.sty:135). The local override (fig14.tex:13-14) is still needed and correct. | fig14.tex:14 | Orchestrator/sty owner. |

## Verdict

pass (0 must-fix, 0 should-fix)
