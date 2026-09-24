# Audit: ch2-symbols corrections (item 4 note, D1), round 1

## Sources compared

- Diff: `git diff HEAD -- chapters/ch2-symbols.tex` (2 hunks, 15 insertions, 2 deletions): a two-line
  LaTeX comment and the `$\CNa$` row (item 4 note), and the `$F(\alpha_X)$` row (D1 note). No other row
  is touched.
- 1973 Symbols list: figures/pages/p085.png (CNa and (CNa)_B ... (CNa)_T(B)), p086.png ((CNa)_1,
  F(alpha_X), G(Omega_X)), p089.png (f_x(t), f_y(t)), p090.png (Omega_X, Omega_X0, Omega_Y, Omega_Y0,
  alpha_X, alpha_Xm, alpha_X0, alpha_Y), p091.png (alpha_Y0).
- 1994 supplement: p676.png-p677.png ("Correction to original pages 186 through 196 of Chapter 2"),
  p678.png-p679.png (fin correction; checked that it does not touch the Symbols list).
- Errata p664.png (Chapter 2 entries pages 108, 113, 144-145; nothing on the Symbols pages 55-62) and the
  2022 correction header p683.png (pages 251-254 and 259 only): neither touches the Symbols list.
- Text evidence cited by the D1 note: p118.png (printed page 88, "Returning to the dynamical equation for
  our case of yaw displacement", Section 2.2) and p150.png (printed page 120, "An impulsive input in yaw
  may be defined as follows:" with f_x(t), Section 3.1.3); both match chapters/ch2-sec2.tex line 177 and
  chapters/ch2-sec3b.tex line 20, and both lie inside the sections the note cites (ch2:sec:2.2 starts at
  ch2-sec2.tex line 80, 2.3 at line 203; ch2:sec:3.1.3 is the unit's first heading).
- Render: build/unit/ch2-symbols-1.png, -2.png (built 05:25:58, after the last edit of the .tex at
  05:25:52). Log: no Overfull hbox; the only undefined references are ch2:sec:4.1, ch2:fig:34-36,
  ch2:sec:2.2, ch2:sec:3.1.3 (other units, expected).

## What was checked (16 items)

Item 4 note (1994, PDF 676-677)
1. One note, on the `$\CNa$` row, as specified; the 1973 gloss "normal force coefficient" is kept (p085).
2. "(correction to pages 186--196)" matches the supplement heading "Correction to original pages 186
   through 196 of Chapter 2".
3. Definition: "the slope of the curve of the normal force coefficient $C_N$ versus angle of attack at
   $\alpha = 0$" agrees with p676 ("the derivative (or 'slope') of the curve of the normal force
   coefficient versus angle of attack measured at the point ($C_N = 0$, $\alpha = 0$)") and "normal force
   curve slope" with the paragraph after it.
4. Rename instruction: the exception "paragraph on body tube sections" and the captions of Figures 34, 35
   and 36 agree with p677. The scope "in Section 4.1" is broader than the source: see the table.
5. "The supplement does not update this Symbols list" is true (p676-679 have no Symbols entry; the fin
   correction's new symbol for the mid-chord length is not added to any list either).
6. "the 1973 entries for $\CNa$ and for $(\CNa)_B$ through $(\CNa)_1$ are kept as printed": the seven rows
   are byte-identical to HEAD and read as on p085-p086; "through" covers B, n, S, T, T(B), 1 in list order.

D1 note (PDF 85-92)
7. Glosses verified on the scan: F(alpha_X) "function of pitch angle", G(Omega_X) "function of pitch
   angular velocity" (p086); f_x(t) "pitch forcing function", f_y(t) "yaw forcing function" (p089);
   Omega_X0 "yaw angular velocity at t = 0", Omega_Y0 "pitch angular velocity at t = 0", alpha_X "yaw
   angle", alpha_Xm "maximum yaw angle", alpha_X0 "yaw angle at t = 0", alpha_Y "pitch angle" (p090);
   alpha_Y0 "pitch angle at t = 0" (p091). The note's two lists (pitch: F, G, f_x; yaw: f_y; yaw:
   alpha_X, alpha_Xm, alpha_X0, Omega_X0; pitch: alpha_Y, alpha_Y0, Omega_Y0) are exact and complete.
8. The inference "pitch and yaw are evidently interchanged" in the F, G, f_x, f_y entries is supported:
   Section 2.1 sets M_c = F(alpha_X), M_d = G(Omega_X) for a rotation "about its X axis", the X rotation is
   the yaw (Section 1: yaw about D, X, Y follow in yaw and pitch), equation (10) is "our case of yaw
   displacement", and 3.1.3 writes the impulse "in yaw" with f_x(t). The wording agrees with the D2 note
   already in chapters/ch2-sec2.tex.
9. "Neither the errata nor the supplements correct this; the entries are kept as printed": true (p664,
   p676-687); the F and G rows and the f_x, f_y rows are unchanged from HEAD.

Placement and form (STYLE.md section 9)
10. Both notes sit in one-line `\multicolumn{1}{l@{}}{...}` cells, the ch1-symbols precedent; not in a
    `p{}` cell or the longtable head. The added two-line comment is not typeset.

Scope, labels, notation
11. Whole diff inspected: only the two rows and the comment; every other row, the header and the
    longtable spec are identical to HEAD.
12. No labels added, removed or changed; the note `\ref`s point to existing labels (ch2:sec:4.1 in
    ch2-sec4.tex, ch2:fig:34-36 in ch2-sec4.tex, ch2:sec:2.2 in ch2-sec2.tex, ch2:sec:3.1.3 in
    ch2-sec3b.tex).
13. Notation per STYLE.md section 13: `\CNa`, `C_N`, `\alpha_X`, `\alpha_{Xm}`, `\alpha_{X0}`,
    `\Omega_{X0}`, `\alpha_Y`, `\alpha_{Y0}`, `\Omega_{Y0}`, `f_x(t)`, `f_y(t)` (typewritten lowercase
    kept).

Render
14. Page 1: "normal force coefficient^E1" and "function of pitch angle^E2", E1 and E2 in sequence, both
    footnotes printed in full at the foot of page 1; the one-line cells do not overflow the column.
15. The `??` in the footnotes are the six other-unit references only (expected in a unit build);
    pdftotext finds `??` on no other line.
16. Page 2 (G(Omega_X) row onward): table continues with its repeated head; no layout change.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| chapters/ch2-symbols.tex line 25, item-4 note on the `$\CNa$` row: "replaces ``normal force coefficient'' by ``normal force curve slope'' in Section~\ref{ch2:sec:4.1} and in the captions ..." | p677: the phrase is replaced "In the rest of Section 4.1, from page 189 thorough page 196 and in the captions of Figures 34, 35, and 36"; the rewritten opening paragraphs (p676) keep "normal force coefficient" for $C_N$ ("the concept of the normal force coefficient $C_N$", the $A_r$ gloss, the definition of $\CNa$). Suggested wording: "rewrites the opening of Section~\ref{ch2:sec:4.1} and, in the rest of that section (1973 pages 189--196) and in the captions of Figures ..., replaces ``normal force coefficient'' by ``normal force curve slope'', except in the paragraph on body tube sections" | the note states the rename for Section 4.1 without qualification, which the corrected section's own opening (still "normal force coefficient $C_N$") contradicts | note |
