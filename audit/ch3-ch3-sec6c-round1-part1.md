# Audit ch3-sec6c, round 1, part 1 (PDF 485-494)

## 1. Scope checked

Scan pages: figures/pages/p485.png through p494.png, one page per Read. I zoomed the scan (build/zoom/audit_ch3-sec6c_r1_p1-*) at p486 (175)-(179), p487 (the typed S_s/S_m), p489 (182), (183a) and (183b), p490 (193), p491 (199)-(202), p492 (203a)-(204b), p493 (the parameter array, the braced system and the where-lines), and p494 (the top where-line and the (C_Do)_FB total).

Render pages: build/unit/ch3-sec6c-01.png through -06.png. Pages 01-05 carry the content of PDF 485-494. Page 06 (Table 6, PDF 495) is the page on the far side, and the part-2 auditor checks it.

Items checked:
- Headings (3): 6.3 (last line of p485), 6.3.1 (p486) and 6.3.2 (p492, two lines). Their numbers and wording match.
- Numbered equations (35), each checked symbol by symbol: (175)-(182), (183a), (183b), (184)-(202), (203a), (203b), (204a), (204b), (205), (206). The sequence has no gaps and every number sits on the page the survey gives.
- Unnumbered displays (4 blocks, 13 lines):
  - p493, the 2 x 4 GCR-x parameter array with (R_crit = 5 x 10^5).
  - p493, the braced system: (C_Df)_b = 82.8(C_f)_B, C_Db = .0149/sqrt((C_Df)_b), the brace, and the result (C_Df)_b + C_Db = (C_Do)_B. Below it, C_DI = 4.25(C_f)_F and (C_Do)_F = 46.4(C_f)_F.
  - p493-494, four where-lines with their side conditions, including 17,900.
  - p494, the (C_Do)_FB total with its nested radical.
- Figure captions (1): Figure 50 (p488). I did not check its artwork.
- Tables: none on these pages. Table 6 is on p495 and belongs to part 2.
- Inline formulas (about 35), including:
  - the quoted "G_1 of B, R_l, l_b/d_m, S_s/S_m" (p486);
  - the braced set of four ratios in the prose (p489);
  - S_s/S_m, S_F/S_m, S_F and t/c (p487);
  - R_c (p490);
  - t/c, c/d_m, (C_Do)_FB and B and R_l (p491);
  - R_l, U_inf, l_b, nu and C_D (p492-493);
  - l_b/d_m (p493);
  - the scientific notation, (C_Do)_FB, (C_Do)_B and R_l = 1 x 10^4 (p494).
- Prose (about 18 paragraphs), checked sentence by sentence:
  - wording and punctuation;
  - underlined words set as emphasis: Datcom, functional dependence, nonzero angle of attack, increase;
  - paragraph indents and flush continuation lines after displays;
  - rejoined hyphenation (con-stituents, inter-action);
  - "--" set as an em dash (p492);
  - "methematical" corrected silently to "mathematical" (a typing slip).
- Survey briefing (build/ch3-notes/ch3-sec6c.md): its lists of numbered equations, headings, displays and side conditions for PDF 485-494 agree with the scan.

Everything above matches except the item below.

## 2. Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 492, between (203b) and (204a) | The four lines (203a), (203b), (204a) and (204b) are one evenly spaced block under "where". | There is an extra vertical gap of about one blank line between (203b) and (204a), probably an empty paragraph between the two subequations groups. The equations themselves are correct. | layout |
