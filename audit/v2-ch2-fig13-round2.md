# v2 audit: ch2/fig13 (round 2)

Sources checked: figures/ch2/fig13.png (scan); figures/v2/ch2/fig13.pdf (17:55, newer than fig13.tex, fig13.csv
and tamrfig.sty; 4.61 x 2.86 in, 5 fonts all embedded; rendered at 300 and 600 dpi) and
build/v2/png/ch2-fig13-compare.png; figures/v2/ch2/fig13.tex, fig13.py, fig13.csv, fig13.calib.json; inventory
row ch2-fig13; caption chapters/ch2-sec3a.tex:439-449; citing text ch2-sec3a.tex:425-437; eqs. (20), (24)-(26);
STYLE.md sections 13 and 16; corrections/v2-figures.md (standing rule 4); round-1 audit and fix record; Fig 12's
redraw.

Round-1 items: none were must-fix or should-fix, and the figure is unchanged. Notes 1 and 2 were for the
orchestrator (see findings).

Rechecked (no regression):
- Lettering: Slope $=\Omega_{X0}$, $\alpha_{X0}$, 0, $\alpha_X$ (rad), $t$ (sec).
- Data, evaluated in memory, with $\zeta = 1.5$: eq. (25) gives $\tau_1 = 2.618$ and $\tau_2 = 0.382$, and eq. (26)
  gives $A_1 = 1.439$ and $A_2 = -0.439$. The CSV equals eq. (24) to 5e-6. There is a slight hump (1.084 at
  t = 0.33), no overshoot, and the curve is 0.043 at the right end, still visibly above the axis.
- Rule 4: the line (0, 1)-(2.3, 2.38) has slope 0.600 = $-A_1/\tau_1 - A_2/\tau_2$. At 600 dpi it is truly tangent.
- Caption: with Fig 12's $\alpha_{X0}$, $\Omega_{X0}$ and $C_1/I_L$, the curve returns to zero more slowly than
  Fig 12's (at t = 4: 0.31 against 0.14).
- Overlay rerun: mean 1.31 px, 95% 4.47 px (0.76 mm), max 5.39 px, as in round 1. This is a computed curve and is
  accepted.
- Style: identical to Fig 12. Width 4.61 in. Nothing clipped or overlapping.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Still open from round 1, not a redraw defect: the overlay mismatch (95% 4.47 px in t = 0 to 5) is not yet listed under Minor. | corrections/v2-figures.md | Orchestrator: log it as minor if overlay mismatches are listed. |
| 2 | note | Still open: the `tamr sketch` y-label suggestion (tamrfig.sty:135). The local override (fig13.tex:12-13) is still needed and correct. | fig13.tex:13 | Orchestrator/sty owner. |

## Verdict

pass (0 must-fix, 0 should-fix)
