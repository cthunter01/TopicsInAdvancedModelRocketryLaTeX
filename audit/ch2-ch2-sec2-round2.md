# Audit: ch2-sec2 ("2. The Linearized Theory", 2.1-2.4), round 2

## Scope checked

- Scan pages: figures/pages/p111.png through p122.png, one Read per page (p122 only up to the
  paragraph ending "... such as a sine wave." before the "3. Solutions to the Dynamical
  Equations ..." heading).
- Render: build/unit/ch2-sec2-1.png through ch2-sec2-7.png (not rebuilt).
- Round-1 item re-verified: the moment subscript M_X is now a capital X in all seven places
  (PDF 111 display M_X = I_L dOmega_X/dt; PDF 113 typed/hand-lettered chain
  "M_X = M_X due to alpha_X + M_X due to dalpha_X/dt = -M_c - M_d = -F(alpha_X) - G(Omega_X)";
  PDF 114 "obtain M_X was incorrect"; PDF 116 display M_X = -C_1 alpha_X - C_2 dalpha_X/dt;
  PDF 118 "applied moment M_X, we find that"). Fixed; consistent with STYLE.md section 13.
- Items compared (89 total):
  - 5 headings: "2. The Linearized Theory", 2.1 Corrective and Damping Moment, 2.2 The
    Linearization Approximations, 2.3 Coupled and Decoupled Systems of Equations, 2.4
    Homogeneous, Particular, and Steady-State Solutions (numbers and wording).
  - 8 numbered equations (7)-(14), with (11)-(14) as two-line pairs (12 equation lines), symbol by
    symbol (evaluation bars and their subscripts in (8), (9); signs of the I_R omega_Z coupling
    terms in (12), (14); f_x(t), f_y(t) right sides in (13), (14)); numbering 7..14 matches the
    book with no offset.
  - 5 unnumbered displays: M_X = I_L dOmega_X/dt (p111); the three-line M_X chain (p113);
    I_L dOmega_X/dt = -F(alpha_X) - G(Omega_X) followed by the connective "or" (p113);
    M_X = -C_1 alpha_X - C_2 dalpha_X/dt (p116); the alpha_Y pitch equation (p118).
  - 1 unnumbered "Present Treatment | Gurkin Report" tabular (p116): 2 headings (italic for
    underlining) and 4 cells (C_1, C_2, M_alpha, M_q with their evaluation bars).
  - 3 captions (Figures 7, 8, 9) word by word; artwork not audited.
  - 25 prose paragraphs sentence by sentence (wording, italics for underlining, paragraph
    indents/flush continuations after displays, em dashes, quotes); "practial" -> "practical"
    (p117) is a silently fixed typo.
  - ~42 inline formulas (Omega_Y, omega_Z, M_Y, M_Z, M_c, M_d, M_X, F(alpha_X), G(Omega_X),
    "y = mx + b", alpha = 0, dalpha/dt = 0, d^2alpha/dt^2 = 0, alpha_X = 0, Omega_X = 0,
    dalpha_X/dt, alpha_F, alpha_Y, f_x(t), f_y(t), ...).
- No editorial footnotes or draft notes appear in this unit's render.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
