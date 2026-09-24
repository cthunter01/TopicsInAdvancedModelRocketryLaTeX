# Audit: ch3-sec3c-sec4a, corrections step, round 3

Unit: `chapters/ch3-sec3c-sec4a.tex` (PDF 389-408, printed pp. 357-376). Baseline: git HEAD (commit 7e2087d, the
faithful 1973 transcription). Items: 4 (errata, page 364), F1 (Figure 22 caption), D15 (check, PDF 392).

## Sources read

- STYLE.md sections 4, 8, 9, 10, 11 and 14, and corrections/ch3.md, including its uncommitted "Decisions" block.
- `git diff HEAD -- chapters/ch3-sec3c-sec4a.tex` (23 lines added, 3 removed) has three hunks: the header comment
  (lines 4-8), the Figure 22 caption with its new `\edcap`, and the Bernoulli sentence with its `\ednote`. The diff
  changes nothing else, and the unit has not changed since round 2 (it was saved at 09:39:15).
- Authors and dates. None of the documents shows an author or a date:
  - The errata sheet, PDF 664. Its heading is "ERRATA / TOPICS IN ADVANCED MODEL ROCKETRY by Gordon K. Mandell,
    George J. Caporaso, and William P. Bengen (Cambridge, Massachusetts: The MIT Press, 1973)".
  - PDF 665, the second typing, headed "TOPICS IN ADVANCED MODEL ROCKETRY / Errata".
  - The supplement pages PDF 688-689, 690, 691, 693, 694, 695, 696 and 698, which I checked in a thumbnail montage
    at build/zoom/audit_ch3-sec3c-sec4a_r3-montage.png.
- PDF 689 ends "[REMAINDER OF TEXT ON PAGE 357 IS UNCHANGED]", so the tabulation's B = 1700 stands in the corrected
  text.
- 1973 pages read: PDF 389 (the tabulation, and the text giving B = 1700 and function C), PDF 390 (the Figure 22
  caption, B = 1740), PDF 392 ((104)-(105) and the turbulent example) and PDF 396 (page 364).
- Rendered pages build/unit/ch3-sec3c-sec4a-1.png and -3.png, built at 09:41:50, after the .tex was saved, so they
  are current. The unit log shows only cross-unit undefined references, which is expected in a unit build.

## Earlier findings, re-verified

- **Round 1: the doubled "((" in the `\edcap`.** Still fixed. The note reads "Equation (100), with ... from
  equations (102a) and (102b) at R_crit, gives B = 1743, ...", and the page 1 render confirms it.
- **Rounds 1-2: the D15 row of corrections/ch3.md.** The fixer disputed this one as outside its scope. I agree with
  the fixer: the unit itself needs no change. The row is still unchanged in the working tree:
  - it gives "about 6.15 x 10^-5" and "the .00459 the formula gives", and both figures are wrong;
  - its status is still "note (check first)".

  My recomputation below agrees with the fixer and with the unit's header comment. The row stays in the table as a
  checklist item for the orchestrator.

## Item 4 (errata, page 364 = PDF 396)

- **Extent.** Page 364 opens with "23." (the end of the page 363 sentence). The first complete sentence is "In the
  inviscid flow ... from point B to point C." The second is the Bernoulli sentence, and it is the only text that
  changed. The prose before and after it is identical to HEAD.
- **New sentence.** I compared it word by word with PDF 664 and PDF 665, and it matches: "In accordance with
  Bernoulli's equation, there is a decrease in static pressure between A and B and a corresponding increase along
  the downstream surface from B to C." The "down-/stream" on PDF 664 is a line-break hyphen, and PDF 665 prints
  "downstream".
- **Note.**
  - The `\ednote` follows the sentence's final period in running prose, which is legal (section 9).
  - It quotes the 1973 sentence exactly as PDF 396 and HEAD have it: "... there is an increase in static pressure
    between A and B and a corresponding decrease along the downstream surface from B to C."
  - "Increase and decrease reversed" and "the pressure falls where the fluid is accelerated and rises where it is
    decelerated" are both correct, since Bernoulli's equation and the curve C_p = 1 - 4 sin^2(phi) give minimum
    pressure at B.
  - Its style matches the sibling note for item 5 in ch3-sec4b.
- **Render (page 3).** The sentence and footnote E1 are complete and correct.

## F1 (Figure 22 caption, PDF 390)

- **Caption.** The 1973 caption is kept exactly as printed: "... R_crit = 5 x 10^5 (corresponding to B = 1740 in
  equation (101))." The `\edcap` inside `\caption` is legal (section 9).
- **Claims checked against PDF 389 and ch3-sec3b.tex.**
  - The tabulation ("listed below (15)") gives 1700 for 5 x 10^5, and (15) is `ch3:ref:15` (Schlichting).
  - The text says "a B of about 1700" and that the curve "for B = 1700 is plotted as function C in Figure 22".
  - The labels `ch3:sec:3.5.3` (the tabulation's subsection), `ch3:ref:15`, `ch3:eq:100`, `ch3:eq:101`,
    `ch3:eq:102a` and `ch3:eq:102b` all exist.
  - (100) and (102a)-(102b) in the edition have the supplement's R_crit form, and the note relies on that form.
- **Arithmetic, redone.**
  - .074/(5 x 10^5)^{1/5} = .0053634.
  - 1.328/(5 x 10^5)^{1/2} = .0018781.
  - B = 5 x 10^5 x .0034853 = 1742.6, which rounds to 1743.
  - The note's .005363, .001878 and 1743 are correct, and so is "the caption's 1740 matches to three figures".
  - The checklist's "about 1742" is the same value truncated.
- **Closing sentence.** "Neither the errata nor the supplements reconcile the two values; both are kept as printed"
  is correct. There is no errata entry for page 357 or 358, and the supplement leaves the tabulation unchanged.
- **Render (page 1).** The note typesets correctly. The `??` marks are cross-unit references in the unit build.

## D15 (check, PDF 392): no note, which is sound

- **(105).** 1.6 x 10^-3 x 10 / (1.206 x 10^6)^{2/5} = .016/270.73 = 5.910 x 10^-5. The printed 5.93 x 10^-5 equals
  .016/270, that is, R_l^{2/5} rounded to 270.
- **Flat-plate value.** .074/(1.206 x 10^6)^{1/5} = .0044974, which the text states as 0.0045.
- **(C_f')_turb.** By the printed formula, (C_f')_turb = .0044974 + .0000591 = .0045565. The printed .0045593 is
  exactly .0045 + .0000593, which is 0.06% high.
- **The percentages.** The increase is 1.314% by the formula and 1.318% with the printed figures, so the text's
  "1.3%" holds. So does "a bit less than 1/3" of the laminar case's 4.4%: 1.3/4.4 = 0.30.
- **Conclusion.** This is last-digit rounding that changes no conclusion, which is D35 practice. The header comment
  (lines 5-8) records the figures and the reason accurately.

## Other checks

- **Scope.** Only the three hunks changed. The header comment accurately describes items 4 and F1 and the D15 check.
- **Labels.** No equation was added, removed or relabelled, and all 1973 labels are intact.
- **Section 14 notation.** The new text uses the specified forms: `R_{\mathrm{crit}}`, `(C_f)_{\mathrm{turb}}` and
  `(C_f)_{\mathrm{lam}}`, leading-dot decimals, capital B, and the point labels A, B, C.
- **Bookkeeping.** In corrections/ch3.md, item 4 and F1 are still marked "todo". That bookkeeping belongs to the
  orchestrator, as for the other units, so it is not listed as a discrepancy.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| corrections/ch3.md, row D15 (checklist, for the orchestrator; no change to the unit) | (105) gives 5.91 x 10^-5 (printed 5.93 x 10^-5 = .016/270); formula (C_f')_turb = .0044974 + .0000591 = .004557; printed .0045593 = .0045 + .0000593; 1.3% holds; status "no note (last-digit rounding; reason in the unit header)" | row still reads "about 6.15 x 10^-5" and "the .00459 the formula gives" (both wrong) with status "note (check first)" | note |
