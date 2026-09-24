# Audit ch3-sec2b, round 1

Unit: 2.2 Dimensionless Coefficients and Quantities, 2.2.1 The Reynolds Number, 2.2.2 The Drag Coefficient,
2.2.3 The Coefficient of Pressure, 2.3 Constituents of the Total Drag Coefficient (PDF 324-340, up to the "3." heading).

## 1. Pages and items checked

- Scan pages: figures/pages/p324.png through p339.png, plus the top of p340 (the unit's last three paragraphs
  sit above the "3." heading there). Each was read in full. Zoomed 300/600 dpi crops (build/zoom/audit_ch3-sec2b_r1-*)
  of every hand-lettered display, eq (13) to (32), and of the typed "P_tot" and "(p_s)_stag" on p334.
- Render: build/unit/ch3-sec2b-1.png to -8.png (8 pages), all read.
- Headings: 5 (2.2, 2.2.1, 2.2.2, 2.2.3, 2.3). Their numbers and wording match.
- Numbered equations: 20, (13) to (32). Each was checked symbol by symbol: signs, fraction bars, the partials and
  their orders, the 1/2 fractions, rho/mu/nu/tau, the subscripts (s1, s2, stag, tot, r, b, f, v, alpha,
  full-scale, model), the vector arrows in (26)-(28), the integral limits S, S_b and S_s, and the three-bar relations
  in (24)-(25). The typed labels "pressure drag:" and "skin-friction drag:" in (26)-(27) are present. The numbers
  run 13 to 32 in sequence.
- Unnumbered displays: 1 (V_model = 100V_full-scale, p329). It matches.
- Inline formulas: all of them. They include rho u du/dx and VL/nu stacked, V/L and V/L^2, ν = 1.495 × 10^-5
  meter^2/second, R = 1.205 × 10^6, ½ρV^2, ½ρC_D A_r, q = ½ρV^2, (p_s)_stag = p_o + ½ρV^2, p_o, P_tot, p_s1, p_s2,
  u_1, u_2, p_∞, C_p = +1.0, dS, S, S_b, S_s, D_b, D_f, D_α, ½ρV^2 A_r, C_D, L_full-scale = L_model × 100, and
  10° and 0°.
- Figure captions: 3 (Figures 9, 10, 11). Their wording matches, including the vector arrows in the Figure 11 caption.
- Tables: none on these pages.
- The enumerated list on p339: 5 items. The lead-in terms are emphasised and the percentages match.
- Prose: I compared every sentence, every emphasis (underlining rendered as italics) and every paragraph break
  (indented or flush after a display).
- Editorial note E1, about "(2.20)" and "(2.18)" on p333, is true of the scan.

Survey briefing (build/ch3-notes/ch3-sec2b.md) check: the equation list (13)-(32) and the pages it gives are
correct, and so are Figures 9 and 10 (p326) and Figure 11 (p337). One statement is wrong: "Cross-references into
earlier units: 'equation (16)' on p331 (ch3-intro-sec2a)". Equation (16) is in this unit, on p328. The render
links it correctly.

Observations, not discrepancies:
- p334 types a capital "P_tot" ("the total pressure P_tot is a constant"). The zoom shows it plainly as a capital,
  and the render keeps it as printed. The hand-lettered p_tot of (22)-(23) is lowercase. Under STYLE.md section 14,
  the corrections step decides.
- The typed range hyphens "(1842-1912)" on p324, and "25%-30%" and "35%-45%" on p339, are set as en dashes. I take
  this as normal typesetting.
- The list items are spaced more loosely than in the typescript (layout).

## 2. Discrepancies

none
