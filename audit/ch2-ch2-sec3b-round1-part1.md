# Audit ch2-sec3b, round 1, part 1 (scan PDF 149-158)

## (1) Scope and item counts

Scan pages checked: figures/pages/p149.png (only from the 3.1.3 heading at the foot of the page) through
figures/pages/p158.png, one page per Read. Zoomed scan crops (build/zoom/audit_ch2-sec3b_r1_p1-*) were
rendered for the t-condition glyph on PDF 150, the paragraph start after that display, and equations
(41a), (41b) and the two unnumbered derivative equations on PDF 158.

Render pages compared: build/unit/ch2-sec3b-01.png to -05.png (page 5 carries the end of PDF 158 and the
start of PDF 159; nothing before the 3.1.3 heading appears on page 1).

- Headings: 1 (3.1.3 Complete Response to Impulse Input); matches.
- Numbered equations: 9, all present in sequence with no offset: (37a), (37b) PDF 154; (38) PDF 154;
  (39), (40) PDF 156; (41a), (41b), (42a), (42b) PDF 158. Each was checked symbol by symbol (signs,
  subscripts X/L/m, tau1/tau2 placement, exponents, fractions and brackets).
- Unnumbered displays: 13 (the three-line impulse definition with (t gtrless 0), (t = 0), (t = 0); omega =
  Mt/I; alpha = (1/2)(M/I)t^2; omega = H/I; alpha = (H/2I)t; Omega_X = H/I_L; phi = arctan(0) = 0;
  A = H/(I_L omega); A_1 = 0, A_2 = H/I_L; the overdamped A_1, A_2; the underdamped, critically damped and
  overdamped zero-velocity equations, including the printed "t" in the overdamped numerators). All match.
- Connective lines ("from which we obtain", "so that", "from which", "and", "which gives us"): 5, all match.
- Figure captions: 4 (Figures 20, 21, 22, 23), compared word by word; all match.
- Prose: about 28 paragraphs and continuation blocks, compared sentence by sentence (wording, italics for
  underlining, quotes, em dashes, "??" for Section 3.1.2, Figure 5 and equations (15)-(19), (16), (17),
  (22), (23), (24)-(26), (25), all in other units). About 35 inline formulas were checked. Paragraph
  indents and flush continuations after displays match except for the one item below.

## (2) Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 150, sentence "While there are more rigorous definitions of impulse inputs ..." after the impulse-definition display | The line starts at the left margin, flush with "obtainable" below it, so it continues the paragraph that ends "may be defined as follows:" (no new paragraph) | Set as an indented new paragraph (render page 1, after Figure 20) | layout |
