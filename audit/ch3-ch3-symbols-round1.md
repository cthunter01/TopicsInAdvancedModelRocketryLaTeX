# Audit: ch3-symbols (Chapter 3 Symbols list), round 1

## Scope checked

- Scan pages: figures/pages/p293.png through p300.png (book pages -263- to -270-), one Read per page.
- Render: build/unit/ch3-symbols-1.png through ch3-symbols-4.png. I also rasterized the symbol column
  of build/unit/ch3-symbols.pdf at 300 dpi (build/zoom/audit_ch3-symbols_r1-render*) to check primes,
  subscripts, bars and arrows. Nothing was rebuilt.
- Items: 1 heading (SYMBOLS, set as the unnumbered "Symbols"), 1 longtable with the repeating
  "Symbol / Meaning" head, and 160 rows. The scan has 18 + 22 + 17 + 24 + 24 + 24 + 22 + 9 = 160
  rows across p293 to p300. The render has 41 + 36 + 45 + 38 = 160 rows across its pages 1 to 4.
  The rows are in the same order.
- I compared every row symbol by symbol: letters and case, subscripts (including nested C_{D_B}(alpha),
  K_{B(F)}, K_{F(B)}, p_{s(stag.)}), primes (C_Df', C_Di', (C_Di')_cant, (C_f')_lam, (C_f')_turb),
  the AR ligature and Delta-AR, the vector arrow on V, the overbar on alpha, and the Greek letters
  (gamma, delta, lunate epsilon, eta, theta, mu, nu, rho, sigma, tau, straight phi versus curly phi,
  psi, omega). I also checked the partial-derivative rows and the two brace groups G_1( ) to G_5( )
  and H_1( ) to H_6( ), each enclosed in left and right braces around a single meaning. I compared
  the meanings word by word, including the book's punctuation ("standard, sea-level" for T_std. and
  c_std. but "standard sea-level" for rho_std.), its hyphenation ("boundary-layer", "cross-sectional"
  on some rows versus "cross sectional" on others), the typo "d_eqiv." as printed, and every
  underlined "also", which is set as italics in all 13 places.
- Zoomed at 300 dpi from the PDF before deciding:
  - the whole symbol column of p293 to p300. This settled C_DI (capital I) versus C_Di (dotted
    lowercase i), S_E versus S_e, the script l in R_l, l_b and l_T, the hand-lettered subscripts
    eta_B (capital B), eta_k and eta_3, sigma_E and sigma_F, and omega_Z (a crossed capital Z).
  - the plain n / n and t / t pairs ("unit normal vector", "unit tangent vector"). Neither is bold
    and neither has an arrow in the scan; the render matches.
  - the h row on p297. The bar over "integral b" is the underline of "also" in the line above, not
    extra emphasis.
  - the x_1 row on p298 ("dS_x/dx").
  - the blank symbol cell of the last row ("infinity") on p300. The scan prints no symbol there, and
    the render faithfully leaves that cell empty.

## Notes (not discrepancies)

- o versus 0: the typewriter and hand-lettered subscripts in (C_Do)_B, (C_Do)_F, (C_Do)_FB, S_o,
  V_o, p_o, x_o, rho_o, tau_o and tau_ok are small round glyphs. They read as the letter o, which is
  how the render sets them; a digit-zero reading would also be acceptable.
- Primes: the typescript types the prime after the subscript (C_Df', (C_f')_lam). LaTeX sets it
  above the subscript (C'_Df). This is a typographic convention; the symbol is the same.
- Word-like subscripts (lug, cant, lam, turb, crit, adm, std., eqiv., tot, stag.) are upright in the
  render, which is the typographic style used in Chapter 2.
- "Chapter ??" in the k and epsilon rows and "reference ??" in the eta_3 row are unresolved
  cross-references in the standalone unit build. The log shows `ch4` and `ch3:ref:3` as undefined.
  Both targets match the scan ("Chapter 4", "reference 3"), and STYLE.md section 6 says unresolved
  references are expected at this stage.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
