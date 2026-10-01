# v2 audit: ch2/fig14 (round 1)

Sources checked: figures/ch2/fig14.png (scan, upscaled 2x); figures/v2/ch2/fig14.pdf (4.62 x 2.86 in, all fonts
embedded; rendered at 300 and 600 dpi) and build/v2/png/ch2-fig14-compare.png; figures/v2/ch2/fig14.tex, fig14.py,
fig14.csv, fig14.calib.json; inventory row ch2-fig14; caption chapters/ch2-sec3a.tex:469-479; citing text
ch2-sec3a.tex:449-467; eqs. (24)-(26); STYLE.md sections 13 and 16; corrections/v2-figures.md; the family's other
redraws (Figs 10-13).

Checked and correct:
- Lettering, all present: $\alpha_{X0}$ (y tick); 0; Slope $=\Omega_{X0}$ at the right end of the line, as printed;
  $\alpha_X$ (rad); $t$ (sec).
- Data: fig14.py rerun in scratch gives a byte-identical fig14.csv. With $C_1/I_L = -0.42$, $C_2/2I_L = 0.13$:
  eq. (25) $\tau_1 = -1.883$ (negative, as the text says for $C_1 < 0$), $\tau_2 = 1.264$; eq. (26) $A_1 = 0.320$,
  $A_2 = 0.050$ (sum 0.37 = $\alpha_{X0}$); the CSV equals eq. (24) to 1e-5.
- Tangent: the line (0, 0.37)-(3.45, 0.8185) has slope 0.13, and $-A_1/\tau_1 - A_2/\tau_2 = 0.130 = \Omega_{X0}$:
  truly tangent (600 dpi check); its printed length is kept.
- Caption and text: the yaw angle grows without bound ("divergent"); the curve leaves the frame top (clipped at
  ymax 2.8, the height of the y-axis arrow) at t = 4.09, 0.43 of the axis length, against about 0.40 printed;
  $\alpha_{X0}$ sits close to the t axis (0.37 of Figs 11-13's), as printed.
- Style: the family's frame and styles; width 4.62 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Overlay of the computed curve on the scan: mean 2.66 px, 95% 8.38 px (1.42 mm), max 21.1 px. By segment: $\alpha_X < 1.5$ mean 1.9 px, 95% 5.0 px; 1.5 to 2.2 mean 3.3 px, 95% 9.1 px; above 2.2 mean 16 px: the printed curve turns up more steeply than the exponential near the frame top. Computed curve accepted (pilot decision). | fig14.csv | Orchestrator: log as minor in corrections/v2-figures.md if every overlay mismatch is to be listed. |
| 2 | note | Style suggestion (as Fig 10): local `every axis y label` override works around `rotate=-90` in `tamr sketch`. | fig14.tex:14; tamrfig.sty:135 | Fix in tamrfig.sty. |

## Verdict

pass (0 must-fix, 0 should-fix)
