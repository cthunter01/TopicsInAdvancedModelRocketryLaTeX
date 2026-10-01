# v2 audit: ch3/fig06 (round 2)

Sources checked: figures/ch3/fig06.png (the scan); figures/v2/ch3/fig06.pdf (rebuilt with `make fig F=ch3/fig06`:
4.34 x 1.94 in, fonts embedded, clean log; rendered at 300 dpi) and build/v2/png/ch3-fig06-compare.png;
figures/v2/ch3/fig06.tex and fig06.calib.json; figures/v2/inventory.csv row ch3-fig06; the caption
(chapters/ch3-intro-sec2a.tex:465-467, u = Uy/h) and the citing text (ch3-intro-sec2a.tex:456-460, 487-489);
STYLE.md sections 14 and 16; corrections/v2-figures.md; the round 1 audit and the fix record; the profile styles
of the other Ch3 profile figures (fig09, fig10, fig13, fig16, fig17, fig18, fig25: their local `\tikzset`).

Round 1 findings:
- R1 #1 (should-fix: the chapter draws velocity profiles three ways): **resolved for this family.** fig06.tex:12-15
  defines `profile` (s1, 1pt) and `profile arrow` (s1, 0.5pt, Stealth 3.4 x 2.4pt). These are character for
  character the definitions in fig16.tex:13-14, fig17.tex:14-15, fig18.tex:14-15 and fig25.tex:15-16, and Fig 9
  uses the same pair. The nine velocity arrows (l.30-31) use `profile arrow`, the profile line (l.32) uses
  `profile`, and the base line (l.29) is an `outline`, as in Figs 16-18. Figs 10 and 13 (not in this family) still
  use the ink form (fig10.tex:12-13, fig13.tex:13-14: ink 0.4pt arrows, `outline` profile line). The chapter is
  therefore uniform only once those two change or the gate picks one form; see note 2.
- R1 #2 (note: hatched-wall depth; Fig 13 is the outlier): no change needed here. The band is 0.22 cm (l.22).
- R1 #3 (note: heavy `vec` for U): house style, unchanged.

Re-checked after the restyle:
- The profile is still exactly u = Uy/h. The nine arrows sit at y = kh/10 and end at x_o + kU/10 on the line
  (k = 5: tip 5.600, line at y = h/2: 5.600). The U arrow spans x_o to x_o + U, the same length as the profile at
  the upper plate, as printed.
- Legibility at 300 dpi: all nine `profile arrow` heads read, including the shortest (k = 1, 0.37 cm, 3.4pt head).
  The heads touch the 1pt profile line, as in Figs 16-18. $u$ clears the line by about 1.4 mm. Nothing overlaps.
  The only ink at the page edge is the plates and their hatched bands, which run to the edge by design.
- Lettering: $U$, $u$, $h$, $y$, all in ink. Nothing is added. The caption and text claims (lower plate fixed,
  upper plate moving right at U, velocity linear from 0 to U) are true of the drawing.
- House rules: the walls use `hatch` (45 deg) on their outer sides, the dimension uses `\dimline` with $h$
  upright in a gap, the data curve is in s1, and the text is ink.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | note | The R1 should-fix is resolved: the profile family styles of Figs 16, 17, 18 and 25 are adopted with identical definitions, and Fig 9 matches. | fig06.tex:12-15, 29-32 | None. |
| 2 | note | Outside this family, Ch3 Figs 10 and 13 still draw their profiles in ink (0.4pt ink arrows, `outline` profile line). This is the only remaining difference from the s1 profile family of Figs 6, 9, 16, 17, 18 and 25. The fixer's style suggestion (move `profile` / `profile arrow` / `profile stroke` into tamrfig.sty) would remove the six local copies. | fig10.tex:12-13, fig13.tex:13-14 | For the chapter consistency pass: bring Figs 10 and 13 to the profile family styles, or record the gate's choice. |

## Verdict: pass (0 must-fix, 0 should-fix)
