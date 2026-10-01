# v2 audit: ch2/fig07 (round 2)

Sources checked: figures/ch2/fig07.png (the scan); figures/v2/ch2/fig07.pdf (rebuilt with `make fig F=ch2/fig07`:
4.68 x 2.86 in, fonts embedded, rendered at 400 dpi) and build/v2/png/ch2-fig07-compare.png;
figures/v2/ch2/fig07.tex, fig07.py, fig07.calib.json, fig07.csv; figures/v2/inventory.csv row ch2-fig07; caption
chapters/ch2-sec2.tex:37-38; citing text ch2-sec2.tex:21-26, ch2-sec5.tex:252-255 and 287-288; eq. (8)
(ch2-sec2.tex:93-97); STYLE.md sections 13 and 16; corrections/v2-figures.md; audit/v2-ch2-fig07-round1.md and the
round-1 fix report.

Round-1 findings:
- Note 1 (fig07.py did not resolve `__file__`, so the crop was not found when the script was run from inside
  figures/v2/ch2): **resolved**. fig07.py:24 is now `HERE = pathlib.Path(__file__).resolve().parent`. I reran the
  script from the repository root and from /tmp with `write_text` intercepted, so nothing was written. Both runs
  produce output byte-identical to fig07.csv (md5 43511499...).

Re-checked (no regressions):
- Lettering: the y title "Corrective moment $M_c$ (dyn-cm)" and the x title "Angular deflection $\alpha_X$ (rad)"
  are in the section 13 form. The y ticks run from 0 to $4\times10^5$ and are all labelled. The x ticks are 0, 0.1,
  0.2 and 0.3, with minor ticks at 0.05, 0.15 and 0.25. There are no minor y ticks, as in the scan. The figure has
  open left and bottom axes and no grid. Nothing is added. The tex file is unchanged since round 1.
- Data: the curve is exactly $C_1\alpha_X$ (1.00e5 at 0.1, 2.00e5 at 0.2), then 2.221e5 at 0.225, 2.345e5 at 0.25,
  2.418e5 at 0.275 and 2.447e5 at 0.3. It is concave throughout. The slope as a fraction of $C_1$ is 0.174 at
  0.28, 0.104 at 0.29 and 0.012 at 0.30 (the fit's end slope is +0.001 $C_1$), so the curve flattens to zero
  slope at about 17 deg, as ch2-sec5.tex:252-255 requires. At 0.225 rad it is 1.3% below the tangent.
- Overlay (`digitize.py overlay`) on the scan: mean 0.11 px, 95% 1.00 px (0.17 mm), max 1.00 px. This is within the
  3 px target.
- Family: fig09-mc.csv's `true` column equals fig07.csv exactly (max difference 0). The figure has the same 3.8 x
  2.3 in axes as Figs 8 and 9 and the same width (4.68 against 4.69 in).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| - | - | No findings. The round-1 note is resolved, and there are no regressions. | - | - |

## Verdict: pass

0 must-fix, 0 should-fix.
