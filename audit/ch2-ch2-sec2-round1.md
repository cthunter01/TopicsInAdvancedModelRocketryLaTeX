# Audit: ch2-sec2 ("2. The Linearized Theory", 2.1-2.4), round 1

## Scope checked

- Scan pages: figures/pages/p111.png through p121.png (book pages -81- to -91-), one Read per page,
  plus p122.png for the boundary paragraph ("valuable features ... sine wave.") that ends the unit
  before "3. Solutions to the Dynamical Equations ...".
- Render: build/unit/ch2-sec2-1.png through ch2-sec2-7.png.
- Items compared (89 total):
  - 5 headings: "2. The Linearized Theory", 2.1, 2.2, 2.3, 2.4 (numbers and wording).
  - 8 numbered equations (7)-(14); (11)-(14) are pairs sharing one number (12 equation lines),
    symbol by symbol; numbering sequence 7..14 matches the book with no offset.
  - 5 unnumbered displays: M_x = I_L dOmega_x/dt (p111); the three-line "M_x = M_x due to ... /
    = -M_c - M_d / = -F(alpha_x) - G(Omega_x)" chain and I_L dOmega_x/dt = -F - G (p113);
    M_x = -C_1 alpha_x - C_2 dalpha_x/dt (p116); the alpha_Y pitch equation (p118).
  - 1 unnumbered "Present Treatment | Gurkin Report" tabular (p116), all four cells, incl. the
    evaluation bars and subscripts, and the headings.
  - 3 captions (Figures 7, 8, 9) word by word; artwork not audited.
  - 25 prose paragraphs sentence by sentence (wording, italics for underlining, paragraph
    indents/breaks, em dashes, quotes); "practial" -> "practical" (p117) is a silently fixed typo.
  - ~42 inline formulas (Omega_Y, omega_Z, M_Y, M_Z, M_c, M_d, F(alpha_X), G(Omega_X), y = mx + b,
    alpha = 0, dalpha/dt = 0, d^2alpha/dt^2 = 0, alpha_X = 0, Omega_X = 0, dalpha_X/dt, alpha_F,
    alpha_Y, f_x(t), f_y(t), ...).
- Zoomed at 300 dpi from the PDF before deciding: the Gurkin "M_q" glyph (p116; the q is
  overwritten but reads q, render M_q accepted); the hand-lettered M_x = I_L dOmega_x/dt (p111);
  the typed "M_Y or M_Z" (p111); the typed "M_X = M_X due to alpha_x + M_X due to" (p113);
  "obtain M_X was incorrect" (p114); "moment curves at alpha_X and Omega_X = 0" (p114);
  "applied moment M_X, we find that" (p118).

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 113 display "M_X = M_X due to α_X + M_X due to dα_X/dt" (typed, subscript is the same capital X glyph as in the typed "M_Y or M_Z" of PDF 111); also PDF 114 "obtain M_X was incorrect", PDF 118 "applied moment M_X, we find that", and the hand-lettered displays PDF 111 "M_x = I_L dΩ_x/dt", PDF 113 "= −M_c − M_d" chain, PDF 116 "M_x = −C_1α_x − C_2 dα_x/dt" (where the M subscript is the same hand-drawn glyph as the α_x/Ω_x subscripts that the render sets as capital X) | M_X (capital X subscript, matching M_Y, M_Z) | M_x (lowercase x subscript) in all seven places, while M_Y and M_Z on render p.1 keep capitals | math |
