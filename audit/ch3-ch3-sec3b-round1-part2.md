# Audit: ch3-sec3b, round 1, part 2 (PDF 376-389)

Unit: 3.4 through 3.5.3, up to but not including the 3.6 heading on PDF 389. This part covers scan pages PDF 376 to 389. Another auditor checks PDF 362 to 375.

## 1. Pages and items checked

- Scan pages: PDF 376 (Figure 18), 377, 378, 379, 380, 381, 382, 383 (Figures 19 and 20), 384, 385, 386 (Figure 21), 387, 388 and 389 (down to the 3.6 heading). I read one page per Read call.
- Zoomed crops (build/zoom/audit_ch3-sec3b_r1_p2-*):
  - p380disp: the k_crit display. The first sign is a faint, slanted "=", not ≈.
  - p380eqs: (87) to (89).
  - p380eq90, p380eq90b: (90) with its slashed exponents ¼, ¾ and ¼.
  - p381eq91: (91) and R_x = U∞x/ν.
  - p382eq93: (93), the inline (R_k)_t/√R_x, and the (for x given in meters) display.
  - p385eqs: (94) to (96).
  - p388eqs, p388eqs2: (97) to (101).
  - p389top: (102a), (102b), and the R_crit/B tabulation.
- Render pages: build/unit/ch3-sec3b-06.png to ch3-sec3b-13.png. This part's content runs from page 07 (continuing from p375) to page 13. The unit ends on page 13, after "...described in Section ??.", and the 3.6 heading is correctly absent.
- Headings: 2, 3.5.2 (PDF 379) and 3.5.3 (PDF 387, a two-line heading). The numbers and wording match.
- Numbered equations: 17, (87) to (101), (102a) and (102b). This confirms the survey list: (87)-(90) p380, (91) p381, (92)-(93) p382, (94)-(96) p385, (97)-(101) p388, (102a)-(102b) p389. The sequence has no gaps, and the standalone build prints the book's numbers with no offset. I checked each symbol. The points specifically verified:
  - (87): the radical over τ_ok/ρ, under the 7ν fraction bar.
  - (88): f''(0) outside the radical √(U∞/νx).
  - (89): 0.332/√R_x · ρU∞² = τ_ok.
  - (90): 12.2ν(R_x)^{1/4}/U∞ = 12.2(ν/U∞)^{3/4}x^{1/4}.
  - (91): k/2x · √R_x.
  - (92): ku_k/ν.
  - (93): 2xη_k/√R_x.
  - (94): the three forms, including √(U∞x/ν) and √(U∞/νx).
  - (95), and (96) η_B = 2η_3.
  - (97): −(ρ/2)U∞² b x_crit[...], with the square brackets.
  - (98) x_crit/ℓ and (99) R_crit/R_ℓ.
  - (100), and (101) 0.074/R_ℓ^{1/5} − B/R_ℓ, without parentheses as printed.
  - (102a) 0.074/(R_ℓ)^{1/5} and (102b) 1.328/(R_ℓ)^{1/2}, with parentheses as printed.
  - The connectives "Then for a flat plate,", "so that", "or" and "Letting".
- Unnumbered displays: 2. They are:
  - k_crit = 5.67 × 10^−5 meter = 5.67 × 10^−3 cm. (PDF 380);
  - (R_k)_t/√R_x = 0.299/√x (for x given in meters) (PDF 382).

  Both match.
- Unnumbered tabulation (PDF 389): 2 rows × 5 columns, all 10 cells: R_crit | 3×10^5 | 5×10^5 | 1×10^6 | 3×10^6 and B | 1050 | 1700 | 3300 | 8700. It has a rule above and a rule below, and no caption. It matches.
- Captions: 4 (Figures 18, 19, 20 and 21). Each matches word for word, including the inline built-up R_k/√R_x and η_k in the Figure 19 and 20 captions. I did not audit the figure artwork.
- Inline math: about 75 items, all matching. By page:
  - PDF 377: φ = 0° and 180°.
  - PDF 378: 3 × 10^5, R_x = U∞x/ν, R_crit, and R_x = R_crit.
  - PDF 379: R_ℓ, R_c = U∞c/ν, and R.
  - PDF 380: k_crit, τ_ok, f''(0) = 0.332, μ = νρ, U∞ = 60, and x = 3 cm.
  - PDF 381: k_t, η_k, k, R_x = U∞x/ν, and R_k.
  - PDF 382: R_k/√R_x, (R_k)_t, and (R_k)_t/√R_x.
  - PDF 384: 2.08 × 10^−4, 1.66 × 10^−4, 1.206 × 10^5, and 6 × 10^4.
  - PDF 385: η_3, η_B, and √x.
  - PDF 387: R_x, R_crit, and k_t.
  - PDF 388: (C_f)_turb and (C_f)_lam.
  - PDF 389: R_crit = 5 × 10^5, (3 × 10^5 to 3 × 10^6), and B = 1700.
- Prose: I compared every sentence on PDF 377-389 and found nothing wrong. Specifically:
  - Wording: no missing, duplicated or reordered text.
  - Paragraph breaks: they match, including the continuations after displays that are not indented ("S. Goldstein..." continues the "We examine first..." paragraph; "Suppose, now,...", "The two-dimensional...", "The cylindrical wire...", "where the laminar...", "Approximate values of B...").
  - Emphasis: every underlined word or phrase is set in italics: favorable (twice), decreasing, adverse (twice), increases, stabilize, destabilize, deduced, does, order of magnitude, downstream, roughness Reynolds number, critical, cannot be disturbed, can, and "as if it had been turbulent all the way from the leading edge".
  - Dashes: both typed "--" pairs (PDF 378 and 384) are em dashes.
  - Cross-references: those to items in other units print ??, which is intended. They are Figure 24, equations (23), (60) and (63), Table 1, Figure 14, Section 3.3, Section 6, Figure 22, and References 3 and 15. The references within the unit, to Figures 18-21 and equations (86) and (90)-(93), (101), resolve.
- Draft or editorial notes on render pages 07-13: none.

## 2. Discrepancies

none
