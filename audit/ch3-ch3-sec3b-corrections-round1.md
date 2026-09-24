# Audit: corrections applied to chapters/ch3-sec3b.tex (round 1)

Unit: `chapters/ch3-sec3b.tex` (3.4 and 3.5.1-3.5.3, PDF 362-389, printed pp. 330-357). I audited
`git diff HEAD -- chapters/ch3-sec3b.tex` against HEAD 7e2087d, the faithful transcription. The diff has five hunks: the
D14 note on (69), and four hunks for item 8 (the first paragraph of 3.5.3 and the "where" sentence after (97), "Then,
letting", the "where" sentence after (101), and (102a)-(102b)). The build audited is `build/unit/ch3-sec3b-01.png` to
`-13.png` with `ch3-sec3b.pdf`. It was built at 09:35:14 from the .tex saved at 09:35:08, so the build is current. I did
not rebuild. Rules read: STYLE.md sections 4, 8, 9, 10, 11 and 14, and corrections/ch3.md, including the "Decisions for
the corrections step (2026-09-24)" block.

Items to apply:
- **Item 8** (supplement, PDF 688-689): replace printed p. 356 and the top of p. 357 (PDF 388 and the top of PDF 389)
  with the supplement's text and equations (97)-(101), (102a), (102b), with one \ednote.
- **D14** (PDF 367): a doubt note on the "- uU_inf" in the integrand of (69).
- **Item 3** (errata, p. 342, PDF 374): already applied silently in the faithful pass.

## Sources and their authors and dates

- **1973 errata sheet, PDF 664.** It is headed "ERRATA" and gives the book's citation (Mandell, Caporaso and Bengen,
  MIT Press, 1973). It shows no author of the sheet and no date. PDF 665 is a second typing of the same list, headed
  "TOPICS IN ADVANCED MODEL ROCKETRY / Errata". It also has no author or date. The only entry in pp. 330-357 is the one
  for p. 342, line 15: "forces due to rotation of the body, and whether or not heat". Both typings give the same wording.
- **Chapter 3 supplement pages, PDF 688-698.** I read PDF 688-698 in full. None shows an author, a signature or a date.
  - PDF 688-689 are headed "-356-" and "-357-". A circled "calculated" is inserted by caret after "laminar skin friction"
    on PDF 688. PDF 689 ends "[REMAINDER OF TEXT ON PAGE 357 IS UNCHANGED]".
  - The other documents are PDF 690 (Section 5.2.2), PDF 691-693 (Section 5.3, pages numbered 2 and 3), PDF 694 (the
    symbol table) and PDF 695-698 (pp. 445, 449, 451 and 452). None of them touches pp. 330-357.
- **1973 pages read:** PDF 367 (printed p. 335, equations (69)-(70)), PDF 368 (Table 2), PDF 388 (p. 356) and PDF 389
  (p. 357).

## What was checked

1. **Item 8, extent.** PDF 388 (p. 356) begins with "One can estimate..." (the 3.5.3 heading is on the page before it)
   and ends with "equations (86) and (63):". The top of PDF 389 has (102a) and (102b), followed by "Approximate values of
   B...". The supplement's p. 356 also begins at "One can estimate", and its p. 357 ends after (102b) with "[REMAINDER OF
   TEXT ON PAGE 357 IS UNCHANGED]".
   - The unit replaces exactly this span (lines 716-773).
   - The heading `\subsubsection{Skin-Friction Drag of Boundary Layers with Transition}` is untouched.
   - Everything from "Approximate values of $B$ for several possible values of $R_{\mathrm{crit}}$" on is unchanged: the
     tabulation, the "In order to apply" paragraph, and the Figure 22 sentence with B = 1700.
   - Nothing that the supplement replaces is left behind, and nothing that it keeps was removed.
2. **Item 8, prose sentence by sentence against PDF 688-689.** Every sentence matches the supplement word for word:
   - "One can estimate the skin-friction drag on a flat plate of length = ℓ on which boundary-layer transition occurs if
     it is assumed that, behind the transition point, the turbulent boundary layer behaves *as if it had been turbulent
     all the way from the leading edge*." The underline runs from "as" to "edge", with the period outside it, so it is
     set as `\emph{}` with the period outside.
   - "Since the laminar region reduces the drag from what it would be if the entire boundary layer were turbulent, we
     can just substitute the laminar drag from the leading edge to the transition point for the turbulent drag over the
     same distance (15)." The reference is set `(\ref{ch3:ref:15})`.
   - "The incremental decrease in drag force due to the laminar region is then". On PDF 688 this line starts at the left
     margin without the 5-space paragraph indent, so the unit keeps it in the same paragraph. That is correct.
   - "where (C_f)_turb and (C_f)_lam are the respective coefficients of turbulent and laminar skin friction calculated at
     the transition point, which is located a distance x_crit downstream from the leading edge." The caret word
     "calculated" is in its place after "friction".
   - "The change in overall skin-friction coefficient becomes" is an indented new paragraph in both the supplement and
     the unit.
   - The connectives "or", "Then, letting" and "we derive the overall skin-friction coefficient as (15):" match.
   - "where the laminar and turbulent skin-friction coefficients used in calculating B are evaluated from the previously
     derived expressions, equations (86) and (63), by setting R = R_crit instead of R_ℓ:". The references are set with
     `\eqref{ch3:eq:86}` and `\eqref{ch3:eq:63}`, and both labels exist (ch3-sec3b line 294, ch3-sec3a line 604).
3. **Item 8, equations symbol by symbol (PDF 688-689).**
   - (97): ΔD = -(ρ/2) U_∞² b x_crit [(C_f)_turb - (C_f)_lam].
   - (98): ΔC_f = -(x_crit/ℓ)[...].
   - (99): ΔC_f = -(R_crit/R_ℓ)[...].
   - (100): B = R_crit[...].
   - (101): C_f = 0.074/R_ℓ^{1/5} - B/R_ℓ. The power is not in parentheses, as printed.
   - (102a): (C_f)_turb = 0.074/(R_crit)^{1/5}.
   - (102b): (C_f)_lam = 1.328/(R_crit)^{1/2}.
   - All seven match the unit. (97)-(101) are identical in the 1973 print (PDF 388), in HEAD and in the supplement.
     Only (102a) and (102b) changed, from R_ℓ to R_crit.
4. **Item 8, the \ednote (E2).** It sits in the prose after the first sentence of the replaced paragraph. It is not in a
   display or a caption, so it is legal under section 9. Chapter 2 places notes on replaced passages the same way, and
   its wording ("the supplement's replacement page ...") matches ch3-sec6b.
   - "Equations (97)-(101) are unchanged": true (point 3).
   - The 1973 (102a) and (102b) are quoted in full and correctly: 0.074/(R_ℓ)^{1/5} and 1.328/(R_ℓ)^{1/2} (PDF 389).
   - The explanation "with the plate Reynolds number R_ℓ where the coefficients at the transition point, R = R_crit, are
     meant" is supported by the supplement's own new sentence. It is also supported by the arithmetic: with R_crit,
     (100) gives B = 1055, 1743, 3341 and 8944 at R_crit = 3e5, 5e5, 1e6 and 3e6. I recomputed these values. With R_ℓ,
     B would not be a constant of R_crit.
   - Every 1973 sentence that changes is quoted, and each quotation matches PDF 388 and HEAD exactly: the two "where"
     sentences, the "Since the laminar region introduces a reduction..." sentence, "The incremental decrease in drag
     force is then", "Letting", and the missing "of length = ℓ".
   - This satisfies the Decisions: the passage is longer than a paragraph, so the note quotes the sentences whose
     content changes, and it quotes every replaced equation that differs. The note calls the non-"where" changes "only
     reworded", although "from the leading edge to" and "due to the laminar region" are small clarifications. The note
     quotes all of them, so the reader loses nothing.
5. **D14.** PDF 367 prints (69) as D = ρb∫_0^h (U_∞² - u² - U_∞² - uU_∞) dy, and HEAD keeps it as printed. The note
   sits in "surface, or", the sentence that introduces the display, which is legal.
   - The note's premise is correct. Table 2 (PDF 368) gives the A_1B_1 momentum flux as -ρb∫_0^h U_∞(U_∞ - u) dy.
   - The note's claim is correct. The sum of the AA_1, BB_1 and A_1B_1 fluxes is U_∞² - u² - U_∞² + uU_∞ =
     u(U_∞ - u), which is the integrand of (70). With the printed "- uU_∞" the integrand is -u(u + U_∞), which does not
     reduce to (70).
   - The closing sentence has the prescribed form: "Neither the errata nor the supplements correct this; the equation
     is kept as printed."
6. **Item 3.** Line 352 reads "forces due to rotation of the body, and whether or not heat", word for word the errata
   sheet on both typings. It is unchanged from HEAD (line 347).
7. **Scope.** The whole diff contains only the D14 note and the item 8 hunks. No other line of the unit changed.
8. **Labels.**
   - `ch3:eq:97` to `ch3:eq:101` are kept.
   - `ch3:eq:102`, `ch3:eq:102a` and `ch3:eq:102b` are kept, in a `subequations` group, as for the 1973 lettered pair.
   - Item 8 has no new equations, so no n-label is needed.
   - `ch3:ref:15` and `ch3:tab:2` are referenced correctly.
9. **Section 14 notation.** `R_{\mathrm{crit}}`, `R_\ell`, `(R_\ell)^{1/5}`, `(C_f)_{\mathrm{turb}}`,
   `(C_f)_{\mathrm{lam}}`, `x_{\mathrm{crit}}`, `\ell` and `U_\infty` are all in the listed forms, in both the corrected
   passage and the notes.
10. **Rendering.**
    - `ch3-sec3b-04.png`: (69) with the E1 marker after "or". The E1 footnote is complete and its math renders.
    - `ch3-sec3b-12.png`: 3.5.3 with the new first paragraph, the italic underlined phrase, the E2 marker after "edge.",
      (97)-(99), and the E2 footnote in full.
    - `ch3-sec3b-13.png`: "Then, letting", (100), (101), the new "where" sentence, (102a)-(102b) with (R_crit), and the
      unchanged tabulation and paragraph.
    - The only "??" are cross-unit references (ch3:ref:15, ch3:eq:63, figures and sections in other units), which the
      standalone unit build tolerates. The log has no overfull boxes and no errors.

## Observations (not discrepancies)

- The unit has no header comment of the form "% Corrections applied (corrections/ch3.md): ...". ch3-sec3a,
  ch3-sec3c-sec4a, ch3-sec4b and ch3-symbols have one, but the other corrected units do not either. STYLE.md does not
  require it.
- The status column of corrections/ch3.md still reads "todo" for item 8 and "note" for D14. The same is true of the
  other items applied in this step, so the status is presumably updated at the end of the step.
- The tabulation of B that follows (102b) is unchanged, as the supplement says. It is cited from Reference 15 and
  called "approximate". The 3e6 entry, 8700, is about 3% below the 8944 that (100) with (102a)-(102b) gives. The other
  three entries agree to rounding. This is not an item, and a note is not warranted.

## Discrepancies

none

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| none | | | |
