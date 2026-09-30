# v2 audit: supplement/ch1-fig02-1994 (round 1)

The June 1994 Figure 2 in its chapter form (Chapter 1, `ch1:fig:2`), lettered by Mandell's 1994 vector rule. Its
document form (`supplement/ch1-fig02-1994-document`) has a report of its own.

Sources checked: figures/supplement/ch1-fig02-1994.png (scan, upscaled 2x); figures/v2/supplement/ch1-fig02-1994.pdf
(rendered 150, 350 and 1200 dpi); figures/v2/supplement/ch1-fig02-1994.tex:1-63; figures/v2/inventory.csv row
sup-ch1-fig02-1994; chapter caption chapters/ch1-sec2a.tex:45-73 (figure at :50, label :72); text
ch1-sec2a.tex:28-31; supplement Part backmatter/supplement/s-ch1.tex:1-9, 24-43, 230-266 (symbols $\vec{A}_e$
"direction is forward along the vehicle centerline"); corrections/v2-figures.md ("Ch1 Fig 2 (1994)" decision);
figures/v2/tamrfig.sty.

Checked and correct: three identical rockets (the 1973 Figure 2 rocket). Left: hatched slug $\Delta m_e$, bold
$\vec{c}$ down (-y), axis cross +y/+x with arrowheads, no thrust arrow. Centre: $P_a$ left of the body; inward
ambient-pressure arrows on both sides of nose, body and fin root plus one down arrow on the nose tip; three upward
arrows at the exit plane (centre bold) labelled $\vec{A}_e$ (forward, as the symbol list says); $P_e$ inside the
plume. Right: bold $\vec{F}$ up at the exit. Equation row $-\vec{c}\,(dm_e/dt) + (P_e - P_a)\vec{A}_e = \vec{F}$
under the three rockets, with the arrow over $A_e$ only as the chapter caption (ch1-sec2a.tex:60, 64) and the
standing decision require. All inventory lettering present; nothing added.

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | should-fix | The three exit-plane arrows are 0.1 cm apart (x = -0.1, 0, +0.1) with heads 3.2pt (thin) and 4.6pt (bold) wide, so the heads overlap (the bold head reaches 0.081 cm from the axis, the thin heads start at 0.044 cm): at final size they print as one black cluster, not the three distinct arrows (thin, bold, thin) of the 1994 art. | ch1-fig02-1994.tex:37-39 | Spread the side arrows (e.g. x = ±0.14, still inside the body radius 0.17) and/or give them smaller heads, or stagger the side arrows lower so the heads do not touch. |
| 2 | should-fix | The ambient-pressure rows stop 0.55 cm above the exit plane. The list `{0.3,0.6,0.9,1.2,1.55,...,5.4}` expands (tested) to 1.55, 1.90001, 2.25002, ..., 5.05006: accumulated rounding of the 0.35 step drops the intended last station 5.4, so there are 15 arrows a side, the last at d = 5.05, only 0.2 cm into the fin root (fins start at d = 4.85, tail at 5.6). The 1994 art carries the arrows down to the fin trailing edge (lowest pair at about 97% of the length), so pressure is shown acting on the whole outside of the rocket. | ch1-fig02-1994.tex:30 | List the stations explicitly (`...,4.7,5.05,5.4`) or end the range at 5.41. |
| 3 | should-fix | $\Delta m_e$ (`\footnotesize`, about 15.5pt wide, `fill=white`) is wider than the plume at the slug (about 12.3pt): it overhangs both plume outlines, and its white box cuts both outlines over the label height. In the scan the label fits inside the hatched band, which leaves a white box for it. Same root cause as ch1/fig02 finding 1: the body is slimmer than printed (d/L 0.061 against 0.081 in the 1994 art), and the plume is as wide as the body. | ch1-fig02-1994.tex:11 (`\r{0.17}`), 21 | Widen the rocket toward the printed proportion (`\r` about 0.22; the plume then clears about 16pt at the slug), or set the label `\scriptsize` inside the band. Widening also relieves findings 1 and 4. |
| 4 | note | $\vec{A}_e$ and $P_e$ fit inside the plume with only about 1pt clearance each side; at 150 dpi their subscripts appear to touch the plume outline. | ch1-fig02-1994.tex:40-41 | Resolved by the wider plume of finding 3; otherwise none needed. |
| 5 | note | The row sets `-\vec{c}\,(dm_e/dt)` with a thin space before the parenthesis; the chapter caption displays $-\vec{c}(dm_e/dt)$ without one. Invisible to most readers. | ch1-fig02-1994.tex:55 (and :52) | Optional: drop the `\,` to match the caption. |
| 6 | note | Pressure-arrow count: 15 a side (16 after finding 2) against 14 printed; the count carries no meaning, and the arrows cross the fin leading edge at the fin root as in the 1994 art. | ch1-fig02-1994.tex:30-34 | None. |

## Verdict

pass (0 must-fix, 3 should-fix)
