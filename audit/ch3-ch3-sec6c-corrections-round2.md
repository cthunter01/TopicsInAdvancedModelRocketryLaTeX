# Audit: corrections applied to chapters/ch3-sec6c.tex (round 2)

Unit: `chapters/ch3-sec6c.tex` (6.3 to 6.3.3, PDF 485-505, printed pp. 453-473). I compared
`git diff HEAD -- chapters/ch3-sec6c.tex` with HEAD 7e2087d, the faithful transcription.

Rules read: STYLE.md sections 4, 8, 9, 10, 11 and 14, and corrections/ch3.md (including "Decisions for the
corrections step (2026-09-24)").

Build audited: `build/unit/ch3-sec6c-01.png` to `-12.png`, with the log. The build ran at 09:43:24, after the .tex was
saved at 09:43:22, so it includes the round-1 fix. I did not rebuild. My zoom files are
`build/zoom/audit_ch3-sec6c_r2-*`.

Items for this unit: D6 (check), D20 (note), D21 (check), D22 (note), D23 (note), D24 (check). Round-1 finding: E1
(the wording of the D20 note).

## Sources: authors and dates

- **Errata sheet, PDF 664.** Headed "ERRATA", with the book's citation (Mandell, Caporaso and Bengen, MIT Press,
  1973). It names no author and gives no date. Its Chapter 3 entries are pp. 268, 270, 342, 364, 382, 401 and 480. None
  is in pp. 457-462.
- **Supplement pages, PDF 688-698.** I checked the heads and feet of PDF 688, 690, 691, 695, 696 and 697 in a montage
  (`build/zoom/audit_ch3-sec6c_r2-supp.png`). I also read PDF 694 in full. No page shows an author, a signature or a
  date. They cover:
  - pp. 356-357;
  - Section 5.2.2 (p. 412);
  - Section 5.3 (pp. 422-424);
  - the symbol table: eight entries, none of them $\ell_c$ or $\ell_s$;
  - pp. 445, 449 and 451-452.

  None touches pp. 457-462 (PDF 489-494). So "Neither the errata nor the supplements correct this" is true in all four
  notes.
- **1973 pages read this round.** PDF 489, 490, 491, 492, 493, 494 and 495 (Table 6).

## Checks

1. **E1 (the round-1 finding, D20 note at "For the conical boattail,"): fixed.** The note now reads: "Both equations
   are printed with a minus sign in the leading factor: $(d_m - d_b)$ before the radical in (183a) and
   $(1 - d_b/d_m)$ in (183b), as are equations (172a) and (172b)." It then says that the $(d_m - d_b)$ under the radical
   is correct, because it is part of the slant height $\ell_T[1 + ((d_m - d_b)/2\ell_T)^2]^{1/2}$. This matches the scan
   of PDF 489:
   - (183a) is $2(d_m-d_b)\ell_T/d_m^2$ times $\sqrt{1+((d_m-d_b)/2\ell_T)^2}$;
   - (183b) is $2(1-d_b/d_m)\ell_T/d_m$;
   - (184) carries the same factor.

   The wording now matches the companion D19 note in ch3-sec6a (line 336). I redid the arithmetic:
   - The lateral area of the frustum is $\pi(r_1+r_2)s = \pi(d_m+d_b)/2\cdot s$.
   - With $d_b = d_m$ the printed sign gives 0, while (182) gives $4\ell_T/d_m$.
   - For the GCR-x, $2(0.2)(3) = 1.2$ and $2(1.8)(3) = 10.8$. The exact (183a) gives 1.2007 and 10.806.

   The claim "carried into (184) and (199)" is right. (202) also has a factor $(1-d_b/d_m)$, but that factor comes from
   the fin-root area inside the boattail (195), where the minus sign is correct. The note rightly leaves (202) out. The
   note is placed legally, in prose before the display. It follows the Chapter 2 style ("evidently meant ... Neither the
   errata nor the supplements correct this; the equations are kept as printed"). Rendered page 2 shows the footnote in
   full with correct math. The (172a)/(172b) references print "??" only because they are in another unit, and the
   labels exist in ch3-sec6a.tex.
2. **D6, (182).** PDF 489 prints an unambiguous $\ell_c$. It is the length $\ell_s$, for four reasons:
   - (184) replaces the CYL term with $4\ell_s/d_m$.
   - (188) is $\ell_b/d_m = \ell_N/d_m + \ell_s/d_m + \ell_T/d_m$.
   - The GCR-x values include $\ell_s/d_m = 11.5$.
   - Figure 50 labels the cylindrical section $\ell_s$.

   Setting `\ell_s` silently follows the Decisions block. Rendered page 2 shows $4\,\ell_s/d_m$.
3. **D21, E3 (at "we obtain").** I recomputed (199) with the GCR-x values:
   - first bracket: $1 + 60/5832 + 0.045 = 1.05529$;
   - second bracket as printed: $9.45 + 46 + 1.2 = 56.65$, which gives 59.78, rounded to 59.8;
   - with the + sign: 66.25, which gives 69.91, rounded to 69.9;
   - $82.8/1.05529 = 78.46$, rounded to 78.5.

   Table 6 (PDF 495) is computed with 82.8:
   - Row $10^4$: $C_{Db} = .0142$ and $(\CDo)_B = 1.114$. Both match the print. With 59.8 the row would give .0167 and
     .811.
   - Row $5\times10^5$: $C_{Db} = .0376$, printed .038. $(\CDo)_{FB} = .473$, which matches.

   Table 7 is taken from Table 6: $D_e(10^4) = 3.33\times10^{-13}\times3.080\times10^8 = 1.03\times10^{-4}$, and $D_a$
   uses .473. The note's statement about Tables 6 and 7 and Figures 51 and 52 is therefore accurate. The other
   coefficients follow from the printed equations: $46.35 \to 46.4$ and $4.248 \to 4.25$, both with $(1+2t/c) = 1.04$,
   and $.0149 = .029\times.512$. The note is placed in prose before the display, which is legal. Its text is on
   rendered page 8 (see the observation below).
4. **D22, E2 (at "where" before (203a)).** PDF 492 prints $(R_\ell<R_{\mathrm{crit}})$ and
   $(R_\ell\ge R_{\mathrm{crit}})$ on (204a) and (204b), as for the body. With $R_c = (c/\ell_b)R_\ell$ (192), the
   condition $R_c < R_{\mathrm{crit}}$ is the same as $R_\ell < (\ell_b/c)R_{\mathrm{crit}}$. That gives
   $(18/1.75)\times5\times10^5 = 5.143\times10^6$, which is the 5.14 x 10^6 of PDF 493-494. The PDF 493 coefficients
   agree:
   - $\sqrt{10.286}\times1.328 = 4.259$;
   - $10.286^{1/5}\times0.074 = 0.1179$;
   - $10.286\times1735 = 17{,}846$.

   The note is accurate. It sits before the `\refstepcounter` lines, and the labels (203) and (204) still resolve
   (page 5: "(199) through (204)"). Rendered page 4 shows it in full.
5. **D23, E4 (after "about 0.6 meter/second.").** $1.495\times10^{-5}\times10^4/0.30 = 0.498$, and
   $4.975\times10^{-5}\times10^4 = 0.4975$. Both round to 0.50 m/s. The relation $U_\infty = 4.975\times10^{-5}R_\ell$
   for a 30 cm rocket is in this unit (line 418), "below" the note. The note is accurate and in prose. Rendered page 8
   shows it.
6. **D24 (check; no note).** The claim is not confirmed. (194) on PDF 490 defines $C_{DI}$ as "one component of the
   fin drag coefficient". Section 6.1.1 (ch3-sec6a lines 135-150) explains that $(\CDo)_F$ computed on the gross area
   $S_F$ exceeds the exposed-area friction by exactly $C_{DI} = 2(C_f)_F(1+2t/c)(S_F-S_E)/S_m$. So (205) already
   contains $C_{DI}$ inside $(\CDo)_F$, and adding it again would count it twice. Table 6 agrees: row $10^4$ has
   $(\CDo)_F = 1.970$, which is $46.4\times.0425$ (the coefficients $46.35$ or $46.4$ give 1.970 or 1.972), not
   $50.65\times.0425 = 2.153$. Leaving D24 without a note is sound. The D24 Status cell in corrections/ch3.md should
   record this reason. That is a checklist entry, not a defect in this unit.
7. **Scope.** The diff has five hunks: `\ell_c` to `\ell_s` in (182), and E1-E4. It totals 33 insertions and 5
   deletions. The one re-wrap, "we / obtain", changes no words. Nothing else changed.
8. **Labels.** No equation was added, removed or renumbered. The 1973 labels are intact.
9. **Section 14 notation in the notes.** The notes use `\ell_s`, `\ell_b`, `\ell_T`, `R_\ell`, `R_c`,
   `R_{\mathrm{crit}}`, `(C_{Df})_b`, `(C_f)_B`, `S_s/S_m`, `U_\infty`, `\nu`, $\times$ powers of ten, and prose units.
   All of these are the section 14 forms.
10. **Log.** There are no errors and no overfull boxes. The undefined references (158, 162, 172a, 172b, Section 2.1)
    are all in other units.

Observation, not listed as a discrepancy: in this standalone unit build, the E3 marker is on page 5 but its text is on
page 8, after the Table 6 and Figure 51 float pages. The note's content renders correctly, and its source placement
follows section 9. Where the note text lands depends on how the pages break around the floats (manyfoot `Ed` class). The
assembled chapter will break its pages differently, so this should be checked there, not changed in the source.

## Discrepancies

none
