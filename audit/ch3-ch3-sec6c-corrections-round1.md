# Audit: corrections applied to chapters/ch3-sec6c.tex (round 1)

Unit: `chapters/ch3-sec6c.tex` (6.3 to 6.3.3, PDF 485-505, printed pp. 453-473). I audited
`git diff HEAD -- chapters/ch3-sec6c.tex` against HEAD 7e2087d, the faithful transcription. The diff has five hunks:
one symbol change in (182) and four \ednote insertions (E1-E4). There are no other changes. The build audited is
`build/unit/ch3-sec6c-01.png` to `-12.png` with `ch3-sec6c.pdf`. It was built at 09:37:16 from the .tex saved at
09:37:11, so the build is current. I did not rebuild. Rules read: STYLE.md sections 4, 8, 9, 10, 11 and 14, and
corrections/ch3.md, including the "Decisions for the corrections step (2026-09-24)" block.

Items for this unit: D6 (check), D20 (note), D21 (check), D22 (note), D23 (note), D24 (check).

## Sources and their authors and dates

- **1973 errata sheet, PDF 664.** It is headed "ERRATA" and gives the book's citation (Mandell, Caporaso and Bengen,
  MIT Press, 1973). It shows no author of the sheet and no date. Its Chapter 3 entries are pages 268, 270, 342, 364,
  382, 401 and 480. PDF 665 ("TOPICS IN ADVANCED MODEL ROCKETRY / Errata") is a second typing of the same list. It also
  has no author or date, and it has the same page entries. Neither sheet has an entry for pp. 453-473.
- **Chapter 3 supplement pages, PDF 688-698.** I checked each page's head and foot (montage
  `build/zoom/audit_ch3-sec6c_r1-supp-a.png` and `-supp-b.png`), and PDF 690 and 694 in full. None shows an author, a
  signature or a date. They cover:
  - pp. 356-357 (PDF 688-689);
  - Section 5.2.2, p. 412 (PDF 690);
  - Section 5.3, pp. 422-424 (PDF 691-693);
  - the symbol table (PDF 694): eight entries, none of them $\ell_c$ or $\ell_s$;
  - pp. 445, 449 and 451-452 (PDF 695-698).

  None touches pp. 457-462 (PDF 489-494), so "Neither the errata nor the supplements correct this" is true for all four
  notes.
- **1973 pages read.** PDF 488 (Figure 50), PDF 489-494, PDF 497 and PDF 499. I also rendered a zoomed crop of (182):
  `build/zoom/audit_ch3-sec6c_r1-p489-489.png`.

## What was checked

1. **D6, (182).** The zoomed scan shows an unambiguous $\ell_c$. It is the same length as $\ell_s$, for four reasons:
   - (184) substitutes $4\,\ell_s/d_m$ for the CYL term of (180) and (182).
   - (188) is $\ell_b = \ell_N + \ell_s + \ell_T$.
   - The GCR-x values give $\ell_s/d_m = 11.5$.
   - Figure 50 labels the cylindrical section $\ell_s$.

   $\ell_c$ occurs nowhere else in Chapter 3, and neither $\ell_c$ nor $\ell_s$ is in the Symbols list. Setting
   `\ell_s` silently follows the Decisions block. No note is correct. Rendered page 2 shows $4\,\ell_s/d_m$.
2. **D20, E1 (at "For the conical boattail,").** The scan (PDF 489, 491) confirms these prints:
   - (183a): $2(d_m-d_b)\ell_T/d_m^2$ before the radical, and $(d_m-d_b)/2\ell_T$ inside it;
   - (183b): $(1-d_b/d_m)$;
   - (184) and (199): the $(1-d_b/d_m)$ term.

   I redid the arithmetic. The frustum's lateral area is $\pi(r_1+r_2)s = \pi(d_m+d_b)/2\cdot s$, and dividing by
   $S_m$ gives $2(d_m+d_b)s/d_m^2$. With $d_b = d_m$ the printed sign gives 0, while $+$ gives $4\ell_T/d_m$. For the
   GCR-x: $2(0.2)(3) = 1.2$ and $2(1.8)(3) = 10.8$. The exact (183a) with $+$ gives 10.806. The note is placed legally,
   and its statement of the print is accurate. There is one precision issue, in the table: the term under the radical
   is correct as printed.
3. **D21, E3 (at "we obtain").** I recomputed from (199):
   - the first bracket is $1 + 60/18^3 + 0.0025(18) = 1.05529$;
   - the printed second bracket is $9.45 + 46 + 1.2 = 56.65$, which gives $59.78 \to 59.8$;
   - with $+$ it is $66.25$, which gives $69.91 \to 69.9$;
   - $82.8/1.05529 = 78.46 \to 78.5$.

   Table 6 is computed with 82.8. Row $10^4$ gives $(C_f)_B = .01328$, $(C_{Df})_b = 1.0996$, $C_{Db} = .0142$ (printed
   .014) and $(\CDo)_B = 1.114$. Row $5\times10^5$ gives $C_{Db} = .0378$ (printed .038). With 59.8 the $10^4$ row would
   have $C_{Db} = .0167$. Table 7's $D_e$ is $3.33\times10^{-13}\,\CD R^2$ from Table 6: $1.03\times10^{-4}$ at
   $10^4$. Its $D_a$ uses .473 from Table 6. So "Table 6 and Figure 51, and the drag forces of Table 7 and Figure 52,
   are computed with 82.8" holds. The other coefficients follow: .0149 ($= .029 \times .512$), 4.25 (4.248) and 46.4
   (46.35). The note is accurate. It does not speculate on where 82.8 came from, which is right.
4. **D22, E2 (at "where", before (203a)-(204b)).** The scan (PDF 492) prints $(R_\ell<R_{\mathrm{crit}})$ and
   $(R_\ell\ge R_{\mathrm{crit}})$ for all four lines. (204a) is $1.328/\sqrt{R_c}$ and (204b) is
   $0.074/R_c^{1/5} - B/R_c$, each with $R_c = (c/\ell_b)R_\ell$ from (192). Laminar flow on the fins therefore holds for
   $R_\ell < (\ell_b/c)R_{\mathrm{crit}} = (18/1.75)(5\times10^5) = 5.143\times10^6$, and PDF 493, PDF 497 ("At a
   Reynolds number of 5.14 x 10^6, the fins ...") and PDF 499 ($4.975\times10^{-5}\times5.14\times10^6 = 256$ m/s) all
   use this value. The PDF 493 coefficients agree: $\sqrt{10.286}\times1.328 = 4.26$, $10.286^{1/5}\times0.074 = 0.118$
   and $10.286\times1735 = 17{,}846$. The note is accurate. The `\ednote` comes before the `\refstepcounter` lines, and
   the labels ch3:eq:203 and ch3:eq:204 still resolve: page 5 shows "(199) through (204)".
5. **D23, E4 (after "about 0.6 meter/second.").** $1.495\times10^{-5}\times10^4/0.30 = 0.498$ m/s, and
   $4.975\times10^{-5}\times10^4 = 0.4975$ m/s. The scan of PDF 499 confirms both $\nu = 1.495\times10^{-5}$
   meter²/second and $U_\infty = 4.975\times10^{-5} R_\ell$ for a 30 cm rocket. The note is accurate, and it sits legally
   in prose.
6. **D24, no note (check).** I verified the claim and it is not confirmed. Omitting $C_{DI}$ from (205) is not an error
   in the Datcom scheme the chapter uses:
   - Section 6.1.1 (ch3-sec6a, the text after Figure 44) defines $C_{DI}$ as the difference between $(\CDo)_F$ computed
     on the gross fin area $S_F$ and the true friction on the exposed area $S_E$, so $2(C_f)_F(1+2t/c)S_F/S_m$ is
     already the exposed-fin friction plus $C_{DI}$.
   - PDF 490 calls $C_{DI}$ "one component of the fin drag coefficient".
   - The Javelin example (Section 6.2) sums only $(C_{Df})_b + C_{Db} + (\CDo)_F$.
   - PDF 493 gives $C_{DI} = 4.25(C_f)_F$ beside $(\CDo)_F = 46.4(C_f)_F$ and adds only the 46.4. Table 6 row $10^4$
     has $(\CDo)_F = 1.970 \approx 46.4\times.0425 = 1.972$, where adding $C_{DI}$ would give 2.153.

   Adding $C_{DI}$ to (205) would count it twice. Leaving D24 without a note is sound. The D24 row in corrections/ch3.md
   still reads "check (note if confirmed)". The reason above should go into the Status column (not a unit defect).
7. **Scope.** The whole diff consists of the five hunks above. The one re-wrap ("we / obtain") changes no words. There
   are no other edits, and no equation other than (182) is touched.
8. **Labels.** No equation was added or renumbered. The 1973 labels are unchanged.
9. **Section 14 notation in the notes.** The notes use these forms, which match section 14: `\ell_s`, `\ell_b`,
   `\ell_T`, `R_{\mathrm{crit}}`, `R_c`, `R_\ell`, `(C_{Df})_b`, `(C_f)_B`, `U_\infty`, `\nu`, `S_s/S_m`, the $\times$
   powers of ten, and "meter$^{2}$/second" as prose units.
10. **Rendering.** Pages 2, 4, 5 and 8 show E1-E4 as footnotes with correct math. (182) shows $\ell_s$. The only "??"
    are the cross-unit references (172a), (172b) and Section 2.1, which the standalone unit build tolerates.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| E1 (D20 note, ch3-sec6c.tex line 76-77) | (183a) prints $(d_m-d_b)$ twice: in the leading factor $2(d_m-d_b)\ell_T/d_m^2$, which should be $(d_m+d_b)$, and under the radical, $((d_m-d_b)/2\ell_T)^2$, which is the slant height and is correct. The companion D19 note in ch3-sec6a says "a minus sign in the leading factor: $(d_m - d_b)$ before the radical". | "Equations (183a) and (183b) print the factors $(d_m - d_b)$ and $(1 - d_b/d_m)$ ... The factors $(d_m + d_b)$ and $(1 + d_b/d_m)$ are evidently meant". This does not say which $(d_m-d_b)$ of (183a) is meant, so it can be read as changing the radical too. Suggest: "print a minus sign in the leading factor: $(d_m - d_b)$ before the radical in (183a) and $(1 - d_b/d_m)$ in (183b)". | note |
