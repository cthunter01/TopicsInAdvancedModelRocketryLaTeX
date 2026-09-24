# Audit ch2-sec3a, round 1, part 1 (scan PDF 122-135)

## 1. Scope and item counts

Scan pages: figures/pages/p122.png through p135.png. On p122 I checked only the part from the
heading "3. Solutions to the Dynamical Equations for Particular Cases of Interest" down.
Render pages: build/unit/ch2-sec3a-01.png through -08.png. Page 08 is the seam into p136; its
content belongs to part 2.

Zoomed crops of the scan (build/zoom/audit_ch2-sec3a_r1_p1-*): p125 derivation lines (including
the two clipped lines), p126 eqs. (16)-(17), p129 Gurkin table and eq. (20), p131 eq. (21) (the
identity sign), p133 "C_1 - C_2^2/4I_L = 0", p134 eq. (24) (tau_1, tau_2).

Items checked:
- Headings: 3 ("3." p122, "3.1" and "3.1.1" p123). All match.
- Numbered equations: 10, (15) p124, (16) (17) (18) p126, (19) p127, (20) p129, (21) p131,
  (22) p132, (23) and (24) p134. Numbers in sequence, no offset. All match symbol by symbol.
- Unnumbered display lines: 28. p124: 1. p125: 8 (two derivatives, the three-line substitution,
  the two clipped lines, the sine/cosine pair, the divided pair). p126: 6. p127: 1. p132: 4.
  p133: 6. p133-134: 2 (alpha_X0 = A_1, Omega_X0 = A_2 - DA_1). All match.
- Unnumbered table "Present Treatment | Gurkin Report" (p129): 2 header cells and 2 rows x 3
  cells. All match.
- Inline formulas: about 45, all match.
- Figure captions: 3 (Figure 10 p128, Figure 11 p130, Figure 12 p135). All match word for word.
- Prose: about 30 paragraphs and continuation blocks, checked sentence by sentence for wording,
  emphasis (every underlined term on these pages is set in italics), quotation marks and paragraph
  breaks.
- Editorial additions: E1 (p125, AomegaD factor), E2 (p133, "C_2/I_L" printed) and the draft note
  on the clipped p125 lines. All three statements about the scan are true.

## 2. Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 129, sentence "For values of C_1, C_2, and I_L such that 0 < C_2^2/4I_L^2 < C_1/I_L we have the case of underdamped motion" (after the Present Treatment / Gurkin Report table) | Line is indented: a new paragraph starts here | Set flush left at the margin with no paragraph indent (render page 3), so it continues the paragraph that holds the table | layout |
