# Audit: ch4-symbols (Chapter 4 Symbols list), round 1

## Scope checked

- Scan pages: figures/pages/p531.png through p536.png (book pages -499- to -504-), one Read per page.
- Render: build/unit/ch4-symbols-1.png through ch4-symbols-3.png. I also rasterized
  build/unit/ch4-symbols.pdf at 300 dpi (build/zoom/audit_ch4-symbols_r1-render*) to check the dots,
  arrows and subscripts. Nothing was rebuilt, and no .tex file was opened.
- Items: 1 heading (SYMBOLS, set as the unnumbered "Symbols"), 1 longtable with the repeating
  "Symbol / Meaning" head (the underlined "Symbol" and "Meaning" on every scan page are the table head),
  and 127 rows. The scan has 22 + 25 + 24 + 25 + 25 + 6 = 127 rows on p531 to p536. The render has
  43 + 46 + 38 = 127 rows on its pages 1 to 3. The rows are in the same order, including the alpha row,
  which ends p534, and alpha(t), which starts p535.
- I compared every row symbol by symbol:
  - letters and case
  - subscripts: A_f, A_r, A_o, A_1, A_2, C_D, C_1, C_2, I_L, I_R, I_sp, I_t, M_x, M_y, H_x, H_y,
    the F_, k_, m_, t_, v_, x_, y_ families, alpha_xo, alpha_yo, omega_cres, omega_f, omega_n,
    omega_xo, omega_yo, omega_z, omega_zo, omega_o
  - vector arrows: E, F, a, c, p, dp, dp_E, dp_e, v (the arrow sits over p only in dp_E and dp_e, as
    in the scan)
  - dots: m-dot, x-dot, Delta x-dot_a, Delta x-dot_t, y-dot, Delta y-dot_a, Delta y-dot_t, and the
    "( )" rows with one dot and with two dots
  - Delta rows, and the compound rows d( )/dt, dm_e/dt, f(alpha), f_x(t), f_y(t), F(t), m(t), alpha(t),
    alpha_x(t), alpha_y(t)
  - the integral row "∫[ ] d( )"
  - Greek letters: alpha, gamma, the lunate epsilon, zeta (the curly hand glyph on p535), theta,
    theta_o, rho, omega
  - two grouped symbols, "A, B" and "A_1, A_2", each with one meaning, as in the scan
- I compared the meanings word by word. That includes "value of A_f" in the A_o row, "value of omega_f"
  in the omega_o row, "t_o" in the four "at time t_o" rows, "in-flight", "drag-free" (all four rows),
  "Napierian ... approximately 2.718", and "(alternate notation)" in all six rows. The one underlined word,
  "also" in the m row, is set in italics.
- Zoomed at 300 dpi from the PDF before deciding: the whole symbol column and the meaning column of
  p531 to p536 (build/zoom/audit_ch4-symbols_r1-p531a/b, p532a/b, p533a/b, p534a/b, p535a/b,
  p536a). This settled the f subscript inside the A_o meaning (the same glyph as in the A_f row, not r),
  the typed 1 in C_1, A_1, m_1, t_1, v_1, y_1 (the typewriter 1 looks like l), and the hand subscripts
  on p535 to p536.

## Notes (not discrepancies)

- o versus 0: the subscripts in A_o, m_o, t_o, theta_o, alpha_xo, alpha_yo, omega_xo, omega_yo,
  omega_zo and omega_o are small round glyphs, typed on p531 to p533 and hand-drawn on p535 to p536.
  The render sets the letter o everywhere. A digit-zero reading would also be acceptable, especially
  for the larger hand o of omega_zo.
- x/X, y/Y, z/Z case: the hand-lettered subscripts of alpha_x, alpha_y, omega_x, omega_y, omega_z,
  omega_zo (p535 to p536) do not show case. The z of omega_z has a crossbar. The render sets them
  lowercase, matching the typed M_x, M_y, H_x, H_y, v_x, v_y, f_x(t), f_y(t) of this list. An uppercase
  reading, as in Chapter 2's omega_Z, would also be acceptable.
- "nth" in the F_n, k_n, m_n, t_n, v_n and y_n meanings is set with an italic math n ("*n*th").
  The typescript types a plain "nth" with no underline. I read this as the usual convention for a
  variable rather than as added emphasis, so it is not listed as a discrepancy.
- The subscript "sp" of I_sp and "cres" of omega_cres are upright, following STYLE.md (the \Isp macro
  and Chapter 2's upright word-like subscripts).
- The two derivative rows print the dot or dots above the blank inside "( )". The render puts them
  over the blank between the parentheses, which is the same symbol.
- Long meanings that the typescript wraps (H, e, k_n, m_n, m_1, dp_E, dp_e, t_o, u, x-dot,
  Delta x-dot_t, y_2, theta, theta_o, and the two derivative rows) fit on one line in the render. That is
  only a layout difference.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
