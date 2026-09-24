# Audit: ch3-sec3c-sec4a, corrections step, round 2

Unit: `chapters/ch3-sec3c-sec4a.tex` (PDF 389-408, printed pp. 357-376). Baseline: git HEAD (commit 7e2087d, the
faithful 1973 transcription). Items: 4 (errata, page 364), F1 (Figure 22 caption), D15 (check, PDF 392).

## Sources read

- STYLE.md sections 4, 8, 9, 10, 11 and 14, and corrections/ch3.md (with its uncommitted "Decisions" block).
- `git diff HEAD -- chapters/ch3-sec3c-sec4a.tex` has three hunks: the header comment (lines 4-8), the Figure 22
  caption with its new `\edcap`, and the Bernoulli sentence with its `\ednote`. The diff changes nothing else.
- The errata sheet, PDF 664, shows no author or date. Its heading is "ERRATA / TOPICS IN ADVANCED MODEL ROCKETRY by
  Gordon K. Mandell, George J. Caporaso, and William P. Bengen (Cambridge, Massachusetts: The MIT Press, 1973)".
  PDF 665 is the second typing ("TOPICS IN ADVANCED MODEL ROCKETRY / Errata"). It also shows no author or date, and
  its page 364 entry is word for word the same.
- Supplement PDF 688-689 (replacement page 356 and the top of page 357) shows no author or date. It gives
  (100) B = R_crit[(C_f)_turb - (C_f)_lam] and (102a)-(102b) with R_crit, and ends "[REMAINDER OF TEXT ON PAGE 357
  IS UNCHANGED]", so the tabulation's 1700 stands.
- 1973 pages read: PDF 389 (tabulation and text, B = 1700), PDF 390 (Figure 22 caption, B = 1740), PDF 392
  ((104)-(105) and the turbulent example) and PDF 396 (page 364).
- Rendered pages build/unit/ch3-sec3c-sec4a-1.png and -3.png. They were built at 09:39:21, after the .tex was saved
  at 09:39:15, so they include the round-1 fix. The unit log shows only cross-unit undefined references, which is
  expected in a unit build.

## Round-1 findings, re-verified

1. **Figure 22 `\edcap`, the doubled "((": fixed.** The note now reads "Equation (100), with
   $(C_f)_{\mathrm{turb}} = .005363$ and $(C_f)_{\mathrm{lam}} = .001878$ from equations (102a) and (102b) at
   $R_{\mathrm{crit}}$, gives $B = 1743$, which the caption's 1740 matches to three figures." The render on page 1
   confirms it, with no nested parentheses.
2. **corrections/ch3.md row D15 (disputed as outside the fixer's scope).** I agree with the fixer. The unit is
   correct: it has no note, and the header comment records the recomputed figures and the reason. My recomputation
   (below) agrees with the fixer's figures. The checklist row still has the wrong recomputed values "about
   6.15 x 10^-5" and "the .00459 the formula gives", and still has the status "note (check first)". Only the
   orchestrator can correct it, so it stays in the table as a checklist item. It needs no change to the unit.

## Item 4 (errata, page 364 = PDF 396)

- **Extent.** Page 364 begins with "23." (the end of the page 363 sentence). The first complete sentence is "In the
  inviscid flow ... to point C.", and the second is the Bernoulli sentence. The edition replaces only that sentence.
  The text before and after it matches HEAD.
- **New text.** Compared word by word with PDF 664 and PDF 665, it matches: "In accordance with Bernoulli's
  equation, there is a decrease in static pressure between A and B and a corresponding increase along the
  downstream surface from B to C." PDF 664 prints "down-/stream" hyphenated at a line break, and PDF 665 prints
  "downstream", which the edition follows.
- **Note.** The `\ednote` follows the sentence's final period, in prose, which is legal (section 9). Its quotation
  of the 1973 sentence matches PDF 396 and HEAD word for word. The explanations "increase and decrease reversed"
  and "the pressure falls where the fluid is accelerated and rises where it is decelerated" are physically correct.
  The note's style matches the sibling note for item 5 in ch3-sec4b.
- **Render (page 3).** The sentence reads correctly, and footnote E1 is complete.

## F1 (Figure 22 caption, PDF 390)

- **Caption.** The 1973 caption is kept exactly as printed: "... $R_{\mathrm{crit}} = 5 \times 10^{5}$
  (corresponding to $B = 1740$ in equation (101))." The `\edcap` inside `\caption` is legal (section 9). `\edcap`
  is a plain bracketed macro, and the edition has no list of figures.
- **Claims checked against PDF 389 and ch3-sec3b.tex.**
  - The tabulation gives 1700 for R_crit = 5 x 10^5 and cites "(15)", which is `ch3:ref:15` (Schlichting).
  - The text says "a B of about 1700" and "for B = 1700 is plotted as function C". The note's "curve C" is fair.
  - The labels `ch3:sec:3.5.3`, `ch3:ref:15`, `ch3:eq:100`, `ch3:eq:102a` and `ch3:eq:102b` all exist.
  - (100) and (102a)-(102b) in the edition are the supplement's forms, which the note uses.
- **Arithmetic, redone.**
  - (C_f)_turb = 0.074/(5 x 10^5)^{1/5} = .0053634.
  - (C_f)_lam = 1.328/(5 x 10^5)^{1/2} = .0018781.
  - B = 5 x 10^5 x .0034853 = 1742.6, which rounds to 1743. The note's figures are correct, and so is "matches to
    three figures". The checklist's "about 1742" is the same value truncated.
- **Closing sentence.** "Neither the errata nor the supplements reconcile the two values; both are kept as printed"
  is correct. The errata have no entry for page 357 or 358, and the supplement leaves the tabulation unchanged.
- **Render (page 1).** The caption and note typeset correctly. The `??` marks are cross-unit references in the
  unit build.

## D15 (check, PDF 392): no note, which is sound

- (105): 1.6 x 10^-3 x 10 / (1.206 x 10^6)^{2/5} = .016/270.73 = 5.910 x 10^-5. The page prints 5.93 x 10^-5, which
  equals .016/270, that is, R_l^{2/5} rounded to 270.
- The flat plate: .074/(1.206 x 10^6)^{1/5} = .0044974, which the text calls 0.0045.
- By the printed formula, (C_f')_turb = .0044974 + .0000591 = .004557. The printed .0045593 is exactly
  .0045 + .0000593, a difference of 0.06%.
- The increase is 1.31% by the formula and 1.32% with the printed figures, so the text's "1.3%" holds, and so does
  "a bit less than 1/3" of the laminar 4.4%.
- This is last-digit rounding that changes no conclusion. Leaving it without a note follows D35 practice, and the
  header comment (lines 5-8) records the figures and the reason accurately.

## Other checks

- **Scope.** The diff contains only the three hunks above, and the header comment accurately lists the items
  applied and the D15 check.
- **Labels.** No equation is added, removed or relabelled, and all 1973 labels are untouched.
- **Section 14 notation.** In the new text, `R_{\mathrm{crit}}`, `(C_f)_{\mathrm{turb}}` and
  `(C_f)_{\mathrm{lam}}`, the leading-dot decimals and capital B are all as specified.
- **Bookkeeping.** corrections/ch3.md still marks item 4 and F1 "todo". That bookkeeping belongs to the
  orchestrator, as for the other units, and is not listed as a discrepancy.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| corrections/ch3.md, row D15 (checklist, for the orchestrator; no change to the unit) | (105) gives 5.91 x 10^-5 (printed 5.93 x 10^-5, = .016/270); formula (C_f')_turb = .0044974 + .0000591 = .004557; printed .0045593 = .0045 + .0000593; 1.3% holds; status "no note (last-digit rounding; reason in the unit header)" | row still reads "about 6.15 x 10^-5" and "the .00459 the formula gives" (both wrong) with status "note (check first)" | note |
