# v2 audit: supplement/ch1-fig02-1994-document (round 1)

The June 1994 Figure 2 in its document form, for the Errata and Supplement Part: ch1-fig02-1994.tex compiled with
`\documentform`, which keeps the 1994 document's lettering of the equation row (arrow over "-c" and over the whole
pressure term). The drawing is shared with the chapter form.

Sources checked: figures/supplement/ch1-fig02-1994.png (scan, upscaled 2x); figures/v2/supplement/
ch1-fig02-1994-document.pdf (rendered 150, 350 and 1200 dpi); figures/v2/supplement/ch1-fig02-1994-document.tex:1-4;
figures/v2/supplement/ch1-fig02-1994.tex:1-63 (the `\ifdefined\documentform` branch, :51-57); inventory row
sup-ch1-fig02-1994; supplement Part backmatter/supplement/s-ch1.tex:1-9 (header comment), 244-266 (figure at :247
and its caption); corrections/v2-figures.md ("Ch1 Fig 2 (1994)"); the chapter-form report
audit/v2-supplement-ch1-fig02-1994-round1.md.

Checked and correct: the equation row reads $\overrightarrow{-c}\,(dm_e/dt) + \overrightarrow{(P_e - P_a)A_e} =
\vec{F}$, as lettered in the 1994 art, and the pressure term agrees with the supplement caption beneath it
(s-ch1.tex:258, 262). Everything else is the chapter form's drawing (see that report).

## Findings

| # | severity | finding | where | suggested fix |
|---|----------|---------|-------|---------------|
| 1 | must-fix | `\overrightarrow{-c}` puts the arrow at x-height, about 0.6pt above the minus sign (which sits on the math axis), so the arrow shaft and the minus read together as an equals sign with an arrowhead ("⇀ over =" followed by c). At 150 dpi the minus cannot be told apart from the shaft, so the sign of the printed momentum term is not legible. In the 1994 art the arrow clears "-c" by a full line gap. | ch1-fig02-1994.tex:52 | Raise the arrow to ascender height, e.g. `\overrightarrow{-c\vphantom{d}}` or `\overrightarrow{-c\mathstrut}` (strut after the c, so the minus stays unary). |
| 2 | should-fix | Shared with the chapter form, finding 1: the three exit-plane arrows at x = -0.1, 0, +0.1 have overlapping heads and print as one cluster. | ch1-fig02-1994.tex:37-39 | As in the chapter-form report. |
| 3 | should-fix | Shared with the chapter form, finding 2: the `\foreach` list drops the station d = 5.4 through rounding, so the ambient-pressure arrows stop 0.55 cm above the exit plane instead of reaching the fin trailing edge as printed. | ch1-fig02-1994.tex:30 | As in the chapter-form report. |
| 4 | should-fix | Shared with the chapter form, finding 3: $\Delta m_e$ is wider than the plume; it overhangs both outlines and its white box cuts them. | ch1-fig02-1994.tex:11, 21 | As in the chapter-form report. |
| 5 | note | The row's momentum term keeps the art's arrow over "-c" while the supplement caption beneath writes $-\vec{c}(dm_e/dt)$ (arrow over c only). This is the art's own lettering, kept as printed (standing rule 2); the source comment (ch1-fig02-1994.tex:3-6) says so. | ch1-fig02-1994.tex:52; s-ch1.tex:254, 262 | None. |

## Verdict

fix (1 must-fix, 3 should-fix)
