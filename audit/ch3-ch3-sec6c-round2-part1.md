# Audit ch3-sec6c, round 2, part 1 (PDF 485-494)

## (1) Pages and items checked

Scan pages PDF 485-494 (one page per Read; zoomed 300 dpi crops of PDF 486, 489, 490, 491, 492, 493 and 494 in
build/zoom/audit_ch3-sec6c_r2_p1-*). Compared with render pages build/unit/ch3-sec6c-01.png to -06.png
(render pages 01-05 carry this content; 06 is the next page, Table 6).

- Headings: 3 (6.3 as the last line of PDF 485, 6.3.1 on PDF 486, 6.3.2 on PDF 492). All correct.
- Numbered equations: 36 ((175)-(202), (203a), (203b), (204a), (204b), (205), (206)), checked symbol by symbol.
  All correct and in sequence. The survey list for PDF 486-493 is correct.
- Unnumbered displays: 3 groups (PDF 493 parameter array of 8 values plus the R_crit side condition; the PDF 493
  braced system with its four "where" lines, one of which runs onto PDF 494; the PDF 494 (C_Do)_FB sum). All correct.
- Inline formulas: about 25 (in the quoted "G_1 of B, R_l, ..." phrase, the braced set in the PDF 489 prose,
  S_s/S_m, S_F/S_m, S_F, t/c, c/d_m, R_c, R_l, U_inf, l_b, nu, C_D, (C_Do)_FB, (C_Do)_B, the scientific
  notation on PDF 494). All correct.
- Figure 50 caption (PDF 488): correct.
- Prose: 14 paragraphs checked sentence by sentence, including emphasis (functional dependence; nonzero angle of
  attack; increase; Datcom), "Phase I" and "Phase 2" as printed, and the em dash on PDF 492. Correct. The typing slip
  "methematical" on PDF 486 is silently fixed, as intended.
- Tables: none on these pages. Table 6 is on PDF 495 and is checked in part 2.

Earlier-round item, PDF 492, between (203b) and (204a): **fixed.** The extra blank-line gap is gone, and the four
lines are now evenly spaced. One residual layout difference remains (row 1 below).

## (2) Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 492, (203a)-(204b) block under "where" | The four lines form one block. Their "=" signs line up in one column, as do the side conditions (R_l < R_crit), (R_l >= R_crit), give or take hand placement. | Vertical spacing is now even (the round-1 gap is fixed), but the lines are two separately aligned pairs. The "=" of (204a)/(204b) sits about 0.4 in left of the "=" of (203a)/(203b), and the (204) side conditions sit about 0.8 in right of the (203) side conditions. Minor. It could be one align* with \tag{203a} ... \tag{204b} per line. | layout |
