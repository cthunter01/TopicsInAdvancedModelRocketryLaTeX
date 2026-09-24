# Audit ch2-sec3c, round 1, part 2 (scan PDF 181-193)

## Scope and counts

Scan pages checked: figures/pages/p181.png to p193.png, one per Read. On p193 only the part above the
3.2.2 heading was checked. Zoomed 300/600 dpi crops of the scan are in
build/zoom/audit_ch2-sec3c_r1_p2-*. They cover:

- p181: the A/B roots and the start of "Thus A and B ..."
- p182: (55)-(57b) and D = ...
- p183: the four-line initial-condition system, the D1/D2 Omega pair and both bracketed equations
- p184: every display
- p185: (58a)
- p189: the squared inequality
- p191: the radical expression and the inline fractions
- p192: the equality and the "Now ... and therefore" inequalities

Render pages checked: build/unit/ch2-sec3c-07.png to -15.png. My content starts at "so that if
omega_Z > 0," on render page 8 and ends with "for any model rocket, rolling or not." on render page 15,
the last page of the unit. Render page 7 was read as the seam page and holds only p180 material.

- Headings: 0 in range. The 3.2.2 heading on p193 belongs to the next unit and is correctly absent.
- Numbered equations: 11. (55), (56a), (56b), (57a), (57b), (58a), (58b), (59a), (59b), (60a) and
  (60b) are all present and in sequence, and the standalone build shows no number offset. Each was
  checked symbol by symbol: nested radicals and their extent, fraction bars, brackets, subscripts,
  primes, signs, and the two-row numerator and denominator of (58a).
- Unnumbered displays: 32, checked symbol by symbol.
  - p181: 3 (the two A/B pairs and the script-F abbreviation)
  - p182: 2 (D = C_2 omega/(...), and the four-line initial-condition list)
  - p183: 4 (the four-line alpha_X0 ... Omega_Y0 system, the D_1/D_2 Omega pair and two bracketed
    two-row equations)
  - p184: 5 (the A_1 sin phi_1 fraction, the omega_1/omega_2 Omega pair, two bracketed equations and
    the A_1 cos phi_1 fraction)
  - p185: 1 (the A_2 sin/cos pair)
  - p186: 2 (F for C_2 = 0, and the omega_1/omega_2 pair)
  - p187: 1 (the inequality)
  - p189: 4 (the inequality, its radical form, its squared form and the bound on F)
  - p191: 3 (C_1 > 0, the radical expression and the "<" inequality)
  - p192: 5 (the critical-damping condition, the equality, the "Now" inequality, the half-radical
    inequality and the "It follows that" inequality)
  - p193: 2 (both C_1/I_L versus C_2^2/(4I_L^2) inequalities)
- Inline formulas: about 60. They include omega_Z, omega_1, omega_2, F, C_1, C_2, D_1, D_2, I_L,
  A_1, A_2, phi_1, phi_2, C_2/(2I_L), alpha_X0 - A_2 sin phi_2, alpha_Y0 - A_2 cos phi_2, the two
  "factor" parentheses, (-1), C_2 = 0, C_1 = 0, the inline fractions I_R^2 omega_Z^2/(4I_L^2) and
  -I_R omega_Z/I_L, and C_2/I_L.
- Cross-references: (51) four times, (55) three times, (59) twice, and Figures 26 and 27.
- Captions: 2 (Figure 26 on p188 and Figure 27 on p190), word by word. The artwork was not audited.
- Prose: about 25 paragraphs, checked sentence by sentence for wording, emphasis and paragraph
  breaks. The emphasis checked was:
  - "this" (p183)
  - nutations (p186)
  - decay (p187)
  - "more slowly decaying" and "reduce the effectiveness of damping" (p189)
  - the underlined sentence "Positive static stability ... centerline", slow, approaches zero,
    negative, also becomes negative and increases with time (p191)
  - is, and "the same condition ... critically-damped response" (p192)
  - large and long periods of time (p193)
- Paragraph indentation after displays was checked everywhere.
- No editorial footnotes or draft notes appear on these render pages.
- Accepted and not reported:
  - p183, the first bracketed equation: the scan omits the closing parenthesis in its second
    right-hand row, "(D_2^2 + omega_2^2 - D_1D_2 - omega_1omega_2 ]". The render closes it. This is
    an obvious slip, silently fixed.
  - p183: faint specks, one at mid-height after "sin phi_2" at the end of the Omega_Y0 line and one
    between "A_2" and "cos phi_2" in the first D_1 Omega line. I read both as specks, not symbols.
  - p184, second line: "+ A_1 sin phi_1 (omega_1D_2 - omega_2D_1)" is confirmed as printed (A_1,
    phi_1), and the render matches.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 181, "Thus A and B are the physical roots ..." (after the A = -X omega_Z, B = 0 display) | typed flush left, at the same margin as "so that if" and "while if": the paragraph continues after the display, with no new-paragraph indent (compare the indented "From this point on" below it) | set as a new, indented paragraph (render page 8) | layout |
| PDF 189, display "C_2^2 I_R^2 omega_Z^2/(4I_L^4) > I_R^4 omega_Z^4/(4I_L^4) - F . I_R^2 omega_Z^2/I_L^2" | a low multiplication point after the script F, "F · (I_R^2 omega_Z^2/I_L^2)" (zoomed at 600 dpi) | "F I_R^2 omega_Z^2/I_L^2" by juxtaposition, with no dot (render page 14) | math |
