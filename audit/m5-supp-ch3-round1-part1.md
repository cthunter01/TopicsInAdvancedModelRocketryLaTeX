# M5 audit: supplement, Chapter 3 documents, round 1, part 1

Scan pages checked: PDF 688-693 (figures/pages/p688.png to p693.png), with zoomed crops in
build/zoom/audit_supp-ch3_r1_p1-*.png (p688 equation (97), p688 paragraph break, p690 constants row,
p691 underlining of "less").
Render pages checked: build/unit/s-ch3-1.png to s-ch3-4.png (content), s-ch3-5.png (next page);
text also compared through `pdftotext build/unit/s-ch3.pdf`. No .tex file was opened.

## Items checked

- **PDF 688-689, "[Replacement Page 356 and Top of Page 357]"** (label supp:ch3-356, from build/unit/s-ch3.aux):
  centred "-356-" and "-357-"; the full paragraph, with underlined "as if it had been turbulent all the
  way from the leading edge" set in italics; "(15)" twice (ch3:ref:15, "??" standalone); the caret-inserted
  "calculated" in the text; "The change in overall ..." indented paragraph; "or", "Then, letting";
  "equations (86) and (63)" (ch3:eq:86, ch3:eq:63); "[REMAINDER OF TEXT ON PAGE 357 IS UNCHANGED]".
  Equations (97), (98), (99), (100), (101), (102a) and (102b) checked symbol by symbol: signs, ρ/2, U∞²,
  b, x_crit, brackets, (C_f)_turb and (C_f)_lam, R_crit/R_ℓ, R_ℓ^{1/5}, (R_crit)^{1/5}, (R_crit)^{1/2},
  0.074, 1.328, and the printed numbers. The mark above "=" in (97) is a speck (zoomed). "The incremental
  decrease ..." begins a new line with no indent in the typescript. The original page 356 (PDF 388) has
  it inside the same paragraph, so the render correctly keeps it in that paragraph.
- **PDF 690, "Corrections and Additions to Section 5.2.2 of Chapter 3"** (supp:ch3-522): the bracketed
  instruction, word for word, with the quoted sentence, the underlined *distribution* and C_Di. The
  section reference is \ref (ch3:sec:5.2.2). The paragraph "The induced drag coefficient ..." is checked.
  (144A) is C_Di = C_L²/(π e AR). The "where AR = ..." and "and e = ..." list includes (span)²/(area).
  **effective aspect ratio** is bold, as typed. Also checked: the display C_L = (dC_L/dα)α; "equation
  (144A) can also be written ..."; (144B), C_Di = (dC_L/dα)² α²/(π e AR); the bracketed instruction on
  the constant e = 0.863; and the constants row dα°/dC_L = 18.6, dC_D/dC_L² = 0.123, e = 0.863 (zoomed).
- **PDF 691-693, "Corrections to Drag Due to Fin Cant in Chapter 3, Section 5.3"** (supp:ch3-53):
  - The bracketed instructions at the start and the end, including "Furthermore...." and page 424.
  - (152), ω_Z = 0.327259Uθ. ω_Z follows the notation settled in STYLE.md section 14.
  - The prose numbers: 100 radians/second, 6000 cm./sec., 0.05093 radian (2.918°), the underlined
    *less* (only that word is underlined; zoomed), and "canted".
  - The displays α(r) = θ − arctan(ω_Z r/U) and the inline arctan line with ≤, 15°, 0.262, 0.268 and ≅.
  - (153), with "radian"; and the "without significant loss of accuracy" paragraph with *average*.
  - In the prose: r = 0, θ = 0.05093, −0.00857, "equation (115) of Chapter 2", "equation (152) above",
    and the ᾱ display (0.05093 − 0.00857)/2 = 0.02118 radian.
  - The prose from "In equation (145)" to 6.51α², then (154), (C_Di′)_cant = 13.02ᾱ².
  - The *aerodynamic twist* paragraph with Δα and "Hoerner (9)" (ch3:ref:9).
  - The displays (C_Di)_twist = (4 × 10⁻⁵)(Δα)² "for Δα given in degrees" and 0.1313(Δα)²; S_F/S_m.
  - The two-line display ending in 4(3.57 × 2.54)/π(1.03)² = 10.8828(C_Di)_twist, then (155),
    1.43(Δα)².
  - "From equation (147)": 2(8.38ᾱ²) = 16.76ᾱ², then (156), and the lines for (13.02 + 16.76)ᾱ² +
    1.43(Δα)², Δα = 0.05093 − (−0.00857) = 0.0595 radian, "Then", and (0.02118)², (0.0595)² = 0.018433.
  - The closing paragraph: 2.46%, 9.84%, 22.14% and C_{D0}.
  - Paragraph indents match the typescript throughout.
- **Editorial note** after the fin-cant document: it resolves, through build/chapters/ch3.aux, to "equations
  (155) and (156) above are shown as (155′) and (156′), because equations (155) and (156) of Section 5.4
  ... keep those numbers". This is true. In the original book, (155) and (156) are on page 425 (PDF 457),
  in "Drag Due to Surface Roughness in Turbulent Flow" (5.4). Chapter 3's labels ch3:eq:n155 and
  ch3:eq:n156 carry 155′ and 156′.
- The headings and labels supp:ch3-356, supp:ch3-522 and supp:ch3-53 are present and go to the table of
  contents.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| none | | | |
