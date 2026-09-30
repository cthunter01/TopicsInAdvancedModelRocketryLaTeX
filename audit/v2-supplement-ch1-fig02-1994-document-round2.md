# v2 audit: supplement/ch1-fig02-1994-document (round 2)

The June 1994 Figure 2 in its document form, for the Errata and Supplement Part: ch1-fig02-1994.tex compiled with
`\documentform`. The drawing is shared with the chapter form (see audit/v2-supplement-ch1-fig02-1994-round2.md).

Sources checked: figures/supplement/ch1-fig02-1994.png (scan; equation row checked at 2x);
figures/v2/supplement/ch1-fig02-1994-document.pdf (current, rendered 150, 300 and 1200 dpi);
figures/v2/supplement/ch1-fig02-1994-document.tex:1-4; figures/v2/supplement/ch1-fig02-1994.tex:1-65 (`\documentform`
branch :53-59); audit/v2-supplement-ch1-fig02-1994-document-round1.md; supplement caption
backmatter/supplement/s-ch1.tex:250-266. I also diffed the 1200 dpi renders of the two forms: they differ only in
the equation row (rows 5122-5225 of 5411), so the drawing findings are the chapter form's.

| round-1 # | severity | status | evidence |
|---|---|---|---|
| 1 | must-fix | resolved | `\overrightarrow{-c\vphantom{d}}` (ch1-fig02-1994.tex:54) raises the arrow to ascender height. At 1200 dpi the arrow shaft clears the minus sign by 6.2pt (2.2 mm): the minus reads as a separate sign under the arrow, as in the 1994 art. The arrow spans "-c" only. |
| 2 | should-fix | resolved | Shared with the chapter form, round-1 #1: the side exit arrows at x = ±0.13 now stand clear of the bold centre arrow (gap about 0.8pt between heads). |
| 3 | should-fix | resolved | Shared with the chapter form, round-1 #2: the pressure arrows now run to d = 5.40, 0.2 cm above the fin trailing edge. |
| 4 | should-fix | not resolved (in part) | Shared with the chapter form, round-1 #3. The $\Delta m_e$ ink now fits inside the wider plume (bulge 1.8). Its white box (:22), drawn after the plume outline (:21), still erases both outlines over 8.5pt (3.0 mm) beside the label. The 1994 art keeps them unbroken. Fix as in the chapter-form report (draw the node before the outline). |
| 5 | note | accepted: note, no action required | The arrow over "-c" is the art's own lettering, kept as printed (standing rule 2); the supplement caption beneath writes $-\vec{c}(dm_e/dt)$. |

## New findings

None. The pressure term $\overrightarrow{(P_e - P_a)A_e}$ has its arrow over the whole term, as lettered in the 1994
art and in the supplement caption (s-ch1.tex:258, 262).

## Verdict

pass (0 must-fix, 1 should-fix open: #4, shared with the chapter form)
