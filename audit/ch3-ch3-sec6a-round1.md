# Audit ch3-sec6a, round 1

Unit: 6. Calculation of the Zero-Lift Drag of Simple Model Rockets; 6.1 The United States Air Force
Stability and Control Datcom Method; 6.1.1; 6.1.2 (PDF 461-474), up to but not including 6.2 (PDF 475).

## 1. What was checked

- Scan pages: figures/pages/p461.png to p474.png (14 pages; p461 from the heading "6." down), each read
  in full. Zoomed 300-dpi crops (build/zoom/audit_ch3-sec6a_r1-*) of (158), (159)-(162), the unnumbered
  repeat of (159) on p465, (163)-(165), (166), (167)-(170) with the inline (S_m)_cyl. formula, (171a)-(171e),
  (172a)-(172b), (173), (174) and the inline 0.0025 l_b/d_m on p474.
- Render: build/unit/ch3-sec6a-1.png to -8.png (8 pages), all read.
- Items: 22 numbered equations ((158)-(170), (171a)-(171e), (172a), (172b), (173), (174)), each in its
  place in the sequence; 1 unnumbered display (the repeat of (159) with S_F/S_m, p465); the inline formulas
  (C_D, S_F, S_m, S_E, sigma_F, n sigma_F, C_DI, t/c, (C_f)_F, R_c = U_inf c/nu, l_b/d_m, P = pi d_m,
  (S_m)_cyl. = pi r_m^2 = pi d_m^2/4, S_s/S_m, d_m, d_b, a, C_f, 0.0025 l_b/d_m); 4 headings (6., 6.1, 6.1.1,
  6.1.2); 5 figure captions (Figures 43-47; artwork not audited); no tables on these pages.
- Prose: read sentence by sentence against the scan, and also a word-level diff of the OCR text layer
  (drafts/p461-p474) against the compiled text. Every difference was an OCR error, math, or a float
  position. Emphasis checked (underlined Datcom x8 including all four on p474, the partial Dat/Com of
  Data Compendium, the Datcom title, USAF title, will, pair, streamwise thickness ratio, sum, imaginary
  extension into the body tube, thickness, chord, only, bodies of revolution, fineness ratio, not,
  equivalent diameter, wetted area, truncated). Paragraph indents and unindented continuations after
  displays and where-lists match.
- Survey list (build/ch3-notes/ch3-sec6a.md) verified: equation pages and figure pages are as listed.
  One small correction to the survey's emphasis note: p474 has four underlined "Datcom", not three. The
  compiled text sets all four in italics.
- References to items in other units show as "??" (Section 3.6, equation (108), references (6) and (18),
  equations (63) and (101), Figure 22, Sections 7, 6.2, 3.6 and 4.4). This is intended.
- Numbering: equations start at (158) and figures at 43, both matching the book.

## 2. Discrepancies

none
