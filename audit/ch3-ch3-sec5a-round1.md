# Audit: ch3-sec5a, round 1

Unit: "5. Other Contributions to Model Rocket Drag" and 5.1 Introduction through 5.2.2 Fin Drag at Angle of Attack, up to but not including the 5.2.3 heading.

## 1. Pages and items checked

- Scan pages: PDF 432 (from the section 5 heading), 433, 434, 435, 436, 437 (Figures 35 and 36), 438, 439, 440 (Figure 37), 441, 442 (Figure 38 artwork and caption, Figure 39 caption), 443 (Figure 39 artwork), 444, 445. I read one page per call. PDF 446 was also read. Its upper two-thirds, from "actual span of the fins" to "competition modelers.", comes before the 5.2.3 heading, belongs to this unit and is in the render. The stated range "PDF 432-445" therefore stops one page short.
- Zoomed crops (build/zoom/audit_ch3-sec5a_r1-*): eq136-434, p434b-434, eq137-435, eq138-436 ((138) and (139)), eq140-436, eq141-438 ((141) and (142)), eq143-439, p441a/b/c/d-441 (the α ≤ 0.022 line, the typed "=" signs, and the unnumbered displays), eq144-441, p442cap-442 (Figure 38 caption and its arrows), p444b/c-444 (α_i, C_Di, and the pair of constants), p445a/b-445 (dα/dC_L, C_Di, S_F/S_m and (145)).
- Render: build/unit/ch3-sec5a-1.png to ch3-sec5a-7.png (7 pages).
- Headings: 5 (5, 5.1, 5.2, 5.2.1, 5.2.2). The numbers and wording match.
- Numbered equations: 10, (136) to (145), with no gaps. The standalone build uses the book's numbers (no offset). I checked each one symbol by symbol:
  - the sub-subscript C_{D_B} on both sides of (136), (139), (142) and (144), and (C_{D_0})_B;
  - S_o outside the fraction in (137) and inside the numerator in (138) and (139);
  - the ≅ in the lead-in to (139);
  - x_o = 0.55x_1 + 0.36ℓ_B (capital B as printed);
  - the integral limits x_o and ℓ_b in (141) to (143), and α, α², α³ and the ηr_xC_Dc dx integrand;
  - the (ℓ_b − x_o) factor in (143);
  - 1.94α² + 8.86α³ in (144);
  - C_Di' = 5.42 × 1.2α² = 6.51α² in (145).
- Unnumbered displays: 7. They are:
  - x_o = .55(8.9) + .36(33) = 16.8 cm.;
  - 2(k_2 − k_1)(S_o/S_m)α² = 1.94α²;
  - the two-line 2α³/S_m ηr_xC_Dc(ℓ_b − x_o) = α³[2 × .74 × 1.03 × 1.2 × 16.2 / π × (1.03)²] = 8.86α³, with the bracket spanning the fraction;
  - the pair dα°/dC_L = 18.6 and dC_D/dC_L² = .123 on one line;
  - dα/dC_L = 0.32;
  - C_Di = .123C_L² = .123(α/.32)² = 1.2α²;
  - S_F/S_m = 7.14 × 2.54/π(1.03)² = 5.42.

  All 7 match.
- Inline math: all of the following match the scan.
  - α, 10°, C_D, U_∞ and C_L.
  - (C_{D_0})_B = 0.27 and 1 × 10^6.
  - C_{D_B}(α) and the quoted "C_{D_B} of α".
  - sin(α) ≅ α, (k_2 − k_1), x, x_o, x_1, dS_x/dx, S_x, S_o and S_m.
  - η, C_Dc, r_x, S_o/S_m = 1.0 and dx.
  - ℓ_b/d = 16, (k_2 − k_1) = 0.97, x_1 = 8.9 cm., η = 0.74 and ℓ_b.
  - α ≤ 0.022 (a typed ≤), 1.25°, α² and α³, α = 12.5°.
  - N, α_i, C_Di, AR = span/chord = 3 and S_F/S_m.
  - x-axis and y-axis, and ΔAR (twice, on PDF 446).
- Captions: 5 (Figures 35 to 39). Each matches word for word, including the arrows over F, L and D_i and the α_i in the Figure 38 caption, and the aspect-ratio ligature in the Figure 39 caption. I did not audit the figure artwork.
- Tables: none. The p444 constant pair is a display, as the brief says. Corrections item 9 (e = 0.863) is not applied, which is correct for the faithful pass.
- Emphasis (underlining set as italics): normal; viscous cross-flow forces; finite; infinite; radians; normal force; induced drag; distribution; one side; trailing vortices; elliptical. All are present.
- Paragraphs: the breaks and indents agree, including the unindented continuations after displays and "where" lists: "so that the lift coefficient", "Applying the approximation", "These terms will be clarified", "Since x_o is located", "From Figure 36", "Finally, we obtain", "Then for α given in radians", "so that", "This coefficient, based on fin planform area", "You should note here".
- Ink insertions: the caret "coefficient" on PDF 434 appears twice ("The total drag coefficient of a model rocket body" and "(C_{D_0})_B is the body drag coefficient"). Both are transcribed.
- Cross-references: these show "??", as intended for other units:
  - Sections 3.5.2, 4, 5.3, 5.4 and 6;
  - 5.2.3 and 5.2.4;
  - References 6, 9 and 18.

  Article 5.2, Sections 5.2.1 and 5.2.2, Figures 35 to 39 (with the 39a and 39b panel suffixes) and the equations resolve.
- I verified the survey brief (build/ch3-notes/ch3-sec5a.md). Its equation pages (136)-(145), figure pages and heading pages are correct. Figure 39's caption is on p442 and its artwork on p443, which agrees with both the brief's "Figure 39 (p442)" and its file line "PDF 443".
- Not a discrepancy: (140) prints ℓ_B with an unambiguous capital B, while the Symbols list and (141)-(143) have ℓ_b. It is transcribed as printed, per STYLE section 14. It is noted here for the corrections step. The source slip "due to spin in usually small" (PDF 433) is kept as printed. The render shows no draft notes.

## 2. Discrepancies

none
