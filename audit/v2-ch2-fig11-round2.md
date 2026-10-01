# v2 audit: ch2/fig11 (round 2)

Sources checked: figures/ch2/fig11.png (scan); figures/v2/ch2/fig11.pdf (17:55, newer than fig11.tex 17:51, the
CSVs 17:54 and tamrfig.sty 16:55; 332.3 x 205.8 pt = 4.61 x 2.86 in, 6 fonts all embedded; rendered at 300 and
600 dpi) and build/v2/png/ch2-fig11-compare.png; figures/v2/ch2/fig11.tex, fig11.py, fig11.csv, fig11-marks.csv,
fig11.calib.json; inventory row ch2-fig11; caption chapters/ch2-sec3a.tex:232-242; citing text ch2-sec3a.tex:
200-209; eqs. (15)-(20); STYLE.md sections 13 and 16; corrections/v2-figures.md (standing rule 1); round-1 audit
and fix record; the family's other redraws.

Round-1 items: none were must-fix or should-fix. The figure is unchanged since round 1 (not rebuilt). The two
notes were for the orchestrator (see findings).

Rechecked (no regression):
- Caption: the envelope is DOTTED (round dots, 1.1 pt every 2.6 pt, ink2: fig11.tex:18-19), as "dotted line" in
  the caption requires (standing rule 1). The time to the first zero and the half period are dimensioned.
- Data, evaluated in memory: the CSV equals eq. (15) to 5e-6 and $Ae^{-Dt}$ to 5e-6. With $\zeta = D = 0.227$,
  $\omega = 0.9739$ (eq. (17)), $\varphi = 0.3719$ (eq. (18)) and $A = 2.752$ (eq. (19)): the first peak is 2.138
  at t = 0.996, the trough -1.028 and the second peak 0.494. The zeros are at 2.844 and 6.070 (marks file). The
  envelope touches the curve at t = 1.231 (the marks file's tc). At t = 0.95, where the envelope starts, it lies
  0.08 above the curve (3.3 pt): the 600 dpi render shows it beginning just above the first peak and closing onto
  the curve, as printed. The tangent (0, 1)-(0.66, 2.498) has slope 2.27 = $-D\alpha_{X0} + A\omega\cos\varphi$.
- The leader from $Ae^{-Dt}$ ends on the envelope at t = 4.9 ($Ae^{-4.9D} = 0.905$). Checked at 600 dpi: its end
  sits on the dots.
- Overlay rerun: the response's mean is 0.50 px and its 95th percentile 1.41 px (0.24 mm), within the target, as
  in round 1. The envelope figures from round 1 (95% 5.83 px) are unchanged.
- Legibility: the curve ends at t = 9.2, 11.5 pt short of the arrowhead. No overlaps. Width 4.61 in.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | Still open from round 1, not a redraw defect: the printed envelope sags below the true $Ae^{-Dt}$ (95% 5.83 px). The computed envelope is accepted, but it is not yet listed under Minor. | corrections/v2-figures.md | Orchestrator: log it as minor if overlay mismatches are listed. |
| 2 | note | Still open: the `tamr sketch` y-label suggestion (tamrfig.sty:135). The local override (fig11.tex:14-15) is still needed and correct. | fig11.tex:15 | Orchestrator/sty owner. |

## Verdict

pass (0 must-fix, 0 should-fix)
