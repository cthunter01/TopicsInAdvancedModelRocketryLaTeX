# Audit: ch1-sec2b (2.2 Weight, 2.3 Drag and Side Force) — round 1

## Scope checked

- Scan pages: figures/pages/p061.png – p072.png (book pp. 31–42, incl. the two unnumbered figure
  pages 36 and 41), plus p073.png (book p. 43) for the boundary paragraph "In Figure 8 a complete
  vector diagram ..." that precedes the section-3 heading and belongs to this unit.
- Render pages: build/unit/ch1-sec2b-1.png – ch1-sec2b-5.png.
- Items compared (103 total):
  - 15 numbered equations, (8)–(22), symbol by symbol, including the "≅ N" continuation line of (22)
  - 2 unnumbered displays (ε = ½ρC_nα A_r ; f(α) = α²)
  - 2 headings (2.2 Weight; 2.3 Drag and Side Force) and their numbers
  - 2 captions (Figure 6, Figure 7), word by word incl. vector arrows and the D_1 subscript
  - 31 prose paragraphs / fragments (incl. list items (a), (b)), sentence by sentence, with emphasis
    (underline → italic), paragraph indents, and cross-reference "??" placeholders
  - ~50 inline formulas (g⃗, R_0, g_0, t_b, m_f, ρ, v, A_r, C_D, α, R_e, μ, L, vL, ρ/μ, numeric
    values with powers of ten, C_D0, k, ε, f(α), C_nα, N sin α, N cos α, 15°, 57.3°, S, α²)
  - Symbol-list rows: none in this unit.

All equations, inline formulas, headings, captions, emphasis and paragraphing are faithful.
The only differences found are two cosmetic placements of connective words next to displays.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 63, eq. (11) | "or, since" is typed on the same line as eq. (11), to the right of the integral (a side annotation), immediately followed by eq. (12) | "or, since" is set as a separate prose line between the (11) and (12) displays | layout |
| PDF 72, unnumbered display after "one might be tempted to deduce that" | "and" is typed on the same line as "ε = ½ρC_nα A_r", at the right, with "f(α) = α²" on the next display line | "and" is set as a separate prose line between the two unnumbered displays | layout |
