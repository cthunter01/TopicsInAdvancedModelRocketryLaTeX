# Audit: ch4-sec2a, round 1, part 2

Unit: "2. The Non-Oscillating Rocket: Solutions for Vehicles Launched Vertically" (2.1, 2.2). This part covers
scan pages PDF 561-570: the end of the 2.2 opening paragraph, 2.2.1 Extended Caporaso-Bengen Solution,
2.2.2 Extended Fehskens-Malewicki Solution and the closing summary before 2.3 (PDF 571).
I compared scan images only and did not open any .tex source.

## 1. Pages and items checked

- Scan pages read: p561, p562, p563, p564, p565, p566, p567, p568, p569 and p570, one Read per page.
- Render pages read: build/unit/ch4-sec2a-4.png to -9.png. Page 4 holds the end of p560 and all of p561's first
  paragraph. Pages 5-9 carry the rest. Page 9 ends the unit.
- Zoomed crops (build/zoom/audit_ch4-sec2a_r1_p2-*):
  - scan: (40); (45)-(47); (48)-(49); (50)-(51); (52)-(55); (56)-(57); (58); (59); (60); the line
    "mass. we obtain" (p564).
  - compiled PDF at 300 dpi: (57), (58), (60), to count brackets and parentheses.
- Headings (2): 2.2.1 Extended Caporaso-Bengen Solution (p561) and 2.2.2 Extended Fehskens-Malewicki Solution
  (p567). The wording and numbers match.
- Numbered equations (21): (40)-(60). I checked each one symbol by symbol, including radicals and their extent,
  bracket and brace extent, small t_2/2, t_n/2, t_2/m_2, (t-t_1)/m_2 and t_n/m_n fractions, tanh^{-1}, the
  (53) evaluation bracket with limits v_1 and v_2, and the (47) t_2^2/2 and y_2^2/2 terms. The sequence is
  continuous and the numbers match the print, with no offset.
  - (48)-(51) keep the printed '- m_2v_1' and '- m_nv_{n-1}' under the radical.
  - (51) is two lines, the second beginning with '+'. Its closing '}' is missing, as printed.
  - (58) and (60) are two lines, the second beginning with '+'. In each, the 'cosh(' is left unclosed and the
    last line ends with ')' ')' ']', as printed.
- Unnumbered displays (1): the identity cosh(A + B) = cosh(A)cosh(B) + sinh(A)sinh(B) (p568). It matches,
  parentheses included.
- Notation key (9 entries, p562): y_1 = y_b, v_1 = v_b, v_2, y_2 (with its parenthesis), m_1, m_2, k_2, t_2 and
  t_1 = t_b. The order and wording match.
- Inline formulas (about 45): these all match.
  - m_2(v_2 - v_1); k_2v_1^2 (twice); k, k_2 and k_1 in the emphasised sentence and the next one; v_1, y_1 and
    y_2.
  - k = k_2, F = F_2, t_b = t_2, m = m_2.
  - F_n, t_n, k_n, m_n; nth and (n-1)th.
  - v, t, t_1, t_1 + t_2 (p567); t = t_1 to t = t_1 + t_2 (p568); A and B; t_2^2 (p569); v_2, y_2, v_n and
    y_n (p570).
- Cross-references: these all match.
  - Equations: (27), (28), (22), (23) twice, (44), (40), (45), (47), (48), (49), (46), (50), (51), (19b), (52)
    twice, (54), (55), (56), (57), (58), (60).
  - Sections: 2.1 four times and 2.2.1. "Section 2.5" (p561) is set as ??, which is expected for a reference to
    another unit.
- Emphasis (14 underlined passages): these are all italic in the render.
  - "initial conditions and limits of integration" (p561).
  - "from a nonzero quantity up through its second-stage burnout value" (p563).
  - "as it would have been if the drag parameter k had been k2 throughout the flight" (p564).
  - "constants" and "not" (p565); "increment" (p566); "terminal velocity" (p569).
  - "the burnout velocity of an upper stage can be less than the first-stage burnout velocity", "from above",
    "slowed down", "burnout velocity", "burning-phase altitude increment", "Caporaso-Bengen" and
    "Fehskens-Malewicki" (p570).
- Prose (15 paragraphs plus the continuation lines after displays): I checked it sentence by sentence, and the
  wording matches. Paragraph indents match the typescript. The non-indented starts of p565 "You should note",
  p566 "In more general terms", "where F_n and t_n" and p568 "The altitude increment" continue their
  paragraphs. So do p564 "It is essential" and "As a check on (48)". The quotes around "weathercocking" and
  "breaking the sound barrier", the two '--' dashes, "mid-1960's" and "340-meter-per-second" all match.
- Silently fixed typing slip (intended): p564 "mass. we obtain" (period before lowercase "we") is set
  "mass, we obtain".
- Tables and figure captions: none on these pages.
- Boxed draft notes: none on render pages 4-9.
- Survey briefing (build/ch4-notes/ch4-sec2a.md): I verified the entries for PDF 561-570, and they are correct.
  - The numbered list, (40)-(60), has the right pages.
  - The remarks on (40)-(60) are accurate: the wide displays, the '- m_2v_1' sign, the missing '}' of (51) and
    the unclosed 'cosh(' of (58) and (60).
  - The 9-line notation key, the headings, the emphasis list, the one unnumbered display (the cosh identity) and
    the page-break sentences all match.
- Layout note, not a discrepancy: the y_2 entry of the notation key wraps its second and third lines under the
  meaning text ("second-stage engine...", "burnout altitude)"). In the render, "burnout altitude)" wraps back to
  the item's left edge. This is a line-break difference in the section 15 where-list form.

## 2. Discrepancies

none
