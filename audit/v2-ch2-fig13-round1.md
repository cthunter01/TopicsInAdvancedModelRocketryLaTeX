# v2 audit: ch2/fig13 (round 1)

Sources checked: figures/ch2/fig13.png (scan, upscaled 2x); figures/v2/ch2/fig13.pdf (4.62 x 2.86 in, all fonts
embedded; rendered at 300 dpi) and build/v2/png/ch2-fig13-compare.png; figures/v2/ch2/fig13.tex, fig13.py,
fig13.csv, fig13.calib.json; inventory row ch2-fig13; caption chapters/ch2-sec3a.tex:439-448; citing text
ch2-sec3a.tex:425-437; eqs. (20), (24)-(26) (ch2-sec3a.tex:358-425); STYLE.md sections 13 and 16;
corrections/v2-figures.md (standing rule 4 names this figure); Fig 12's redraw for the caption's comparison.

Checked and correct:
- Lettering, all present: Slope $=\Omega_{X0}$; $\alpha_{X0}$ (y tick); 0; $\alpha_X$ (rad); $t$ (sec).
- Data: fig13.py rerun in scratch gives a byte-identical fig13.csv. With $\zeta = 1.5$ (D = 1.5): eq. (25)
  $\tau_1 = 2.618$, $\tau_2 = 0.382$; eq. (26) $A_1 = 1.439$, $A_2 = -0.439$; the CSV equals eq. (24) to 5e-6.
- Rule 4: the line (0, 1)-(2.3, 2.38) has slope 0.6, and $-A_1/\tau_1 - A_2/\tau_2 = 0.600 = \Omega_{X0}$: truly
  tangent.
- Caption and text: no overshoot (minimum 0.043 at the right end, still visibly above the axis); slight hump
  (1.08 at t = 0.33); returns to zero more slowly than Fig 12 with the same $\alpha_{X0}$, $\Omega_{X0}$ and
  $C_1/I_L$: at t = 2, 4, 6, 8 Fig 13 has 0.67, 0.31, 0.15, 0.068 against Fig 12's 0.57, 0.14, 0.026, 0.005.
- Style: the family's frame and styles, identical tangent to Fig 12; width 4.62 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Overlay of the computed curve on the scan: mean 1.31 px, 95% 4.47 px (0.76 mm), max 5.4 px; the excess is in t = 0 to 5 (the printed curve keeps its hump a little longer before falling), t > 5 is within 2 px. Computed curve accepted (pilot decision). | fig13.csv | Orchestrator: log as minor in corrections/v2-figures.md if every overlay mismatch is to be listed. |
| 2 | note | Style suggestion (as Fig 10): local `every axis y label` override works around `rotate=-90` in `tamr sketch`. | fig13.tex:13; tamrfig.sty:135 | Fix in tamrfig.sty. |

## Verdict

pass (0 must-fix, 0 should-fix)
