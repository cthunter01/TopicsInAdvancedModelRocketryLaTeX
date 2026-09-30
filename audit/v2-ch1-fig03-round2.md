# v2 audit: ch1/fig03 (round 2)

Sources checked: figures/ch1/fig03.png (scan); figures/v2/ch1/fig03.pdf (rendered 300, 600 and 800 dpi);
figures/v2/ch1/fig03.tex:1-47; figures/v2/ch1/fig03.py and fig03.csv; figures/v2/inventory.csv row ch1-fig03;
caption chapters/ch1-sec2a.tex:92-101 and citing text ch1-sec2a.tex:86-90; STYLE.md section 16;
figures/v2/tamrfig.sty. Overlay: a calibration of panel (a) written for this audit (all labelled ticks, max
residual 0.73 px) and `digitize.py overlay` of fig03.csv and of the tangent line m = 12.8 - 9(t - 0.4).

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | should-fix | resolved | fig03.py:10-11 now has T = [0, 0.05, 0.075, 0.10, 0.125, 0.15, 0.2, ...], M = [21.0, 19.2, 18.3, 17.3, 16.35, 15.85, 15.1, ...], the values suggested. fig03.csv reads 19.2, 18.30, 17.3, 16.36, 15.85 g at 0.05-0.15 sec and passes through every table value (15.1, 12.8, 11.3, 10.2, 9.4, 9.0). Overlay: 95% 0.0 px, max 1.0 px (was 95% 2.24, max 4.0). The slope at t = 0.4 is -9.10 g/sec, so the tangent is still tangent. The knee now turns over 0.11-0.14 sec (slope -40 to -19 g/sec), matching the printed knee. |
| 2 | should-fix | resolved | fig03.tex:19 ends the leader at (1.046, 7.0). The tangent crosses m = 7.0 at t = 1.0444, so the tip is 0.004 in past the line's centre horizontally, about 0.03 mm perpendicular to it: inside the 1pt stroke. At 800 dpi the head touches the line and the whole head is visible. |

Also checked, unchanged and correct: axes and labels of (a); tangent line (overlay 95% 1.0 px); dashed legs
and the lettering of (a); the table and brackets of (b) and its lettering; the caption's "tangent" line, table and
negative $\Delta m$.

## New findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | Panel letters do not follow STYLE.md section 16. (a) is a plot, so its letter belongs at the upper right inside its axes; it sits 2.45 in right of the axes, beyond the lettering block, at the figure's right edge. (b) is a table (not a plot), so its letter belongs at the lower right of its panel, where the 1973 circled (b) is; it sits at the upper right, level with the table header. | fig03.tex:24, 45 | (a): `\node[panel, anchor=north east] at (rel axis cs:1,1) {(a)};` inside the axis (the corner t = 1.2, m = 21 is empty; the curve is at 9 g there). (b): at the same right edge, on the baseline of the table's last row (1.2 / 9.0), e.g. `anchor=base east` at the x of the current node and the y of `(t7.base)`. |

## Verdict

pass (0 must-fix, 1 should-fix)
