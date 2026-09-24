# Audit: ch3-sec3c-sec4a, corrections step, round 1

Unit: `chapters/ch3-sec3c-sec4a.tex` (PDF 389-408, printed pp. 357-376). Baseline: git HEAD (commit 7e2087d, the
faithful 1973 transcription). Items: 4 (errata, page 364), F1 (Figure 22 caption), D15 (check, PDF 392).

## Sources read

- STYLE.md sections 4, 8, 9, 10, 11, 14; corrections/ch3.md (including its uncommitted "Decisions" block).
- `git diff HEAD -- chapters/ch3-sec3c-sec4a.tex`: three hunks. The header comment, the Figure 22 caption
  (`\edcap` added) and the Bernoulli sentence with its `\ednote`. Nothing else changed.
- Errata sheet PDF 664 and its second typing PDF 665. Neither shows an author or a date. PDF 664 is headed "ERRATA /
  TOPICS IN ADVANCED MODEL ROCKETRY by Gordon K. Mandell, George J. Caporaso, and William P. Bengen (Cambridge,
  Massachusetts: The MIT Press, 1973)". PDF 665 is headed "TOPICS IN ADVANCED MODEL ROCKETRY / Errata". Both give
  the same page 364 entry.
- Supplement PDF 688-689 (replacement page 356 and the top of page 357). These pages show no author or date. They
  end "[REMAINDER OF TEXT ON PAGE 357 IS UNCHANGED]", so the tabulation's 1700 stands.
- 1973 pages PDF 388, 389, 390, 391, 392, 396.
- Rendered pages build/unit/ch3-sec3c-sec4a-1.png and -3.png. They were built at 09:34:41, after the .tex was saved
  at 09:34:40, so they are current. The unit log shows only cross-unit undefined references, which is expected in a
  unit build.

## Item 4 (errata, page 364 = PDF 396)

- Extent: page 364 opens with "23." (the end of the page 363 sentence). The first complete sentence is "In the
  inviscid flow ... to point C." The second is the Bernoulli sentence, and it is the only sentence the edition
  replaced. The sentences before and after it match HEAD.
- New sentence, compared word by word with the errata: "In accordance with Bernoulli's equation, there is a decrease
  in static pressure between A and B and a corresponding increase along the downstream surface from B to C." It
  matches. The errata's "down-stream" is a hyphen at a line break, and the 1973 "downstream" is kept.
- Note: `\ednote` placed after the sentence's final period, in prose. That placement is legal. Its 1973 quotation
  "In accordance with Bernoulli's equation, there is an increase in static pressure between A and B and a
  corresponding decrease along the downstream surface from B to C." matches PDF 396 and HEAD word for word. The
  statements "increase and decrease reversed" and "the pressure falls where the fluid is accelerated and rises where
  it is decelerated" are correct. The wording matches the unit's sibling note in ch3-sec4b (item 5).
- Render (page 3): the sentence reads correctly, and footnote E1 is complete.

## F1 (Figure 22 caption, PDF 390)

- The 1973 caption is kept as printed ("corresponding to B = 1740 in equation (101)"). The `\edcap` is inside
  `\caption`, which is legal (section 9), and the edition has no list of figures that would pick it up.
- Claims checked against PDF 389 and ch3-sec3b.tex: the tabulation gives 1700 for R_crit = 5 x 10^5 and is cited to
  (15), which is `ch3:ref:15` (Schlichting). The text says "a B of about 1700" and plots "function C" for B = 1700.
  The labels `ch3:sec:3.5.3`, `ch3:ref:15`, `ch3:eq:100`, `ch3:eq:102a` and `ch3:eq:102b` all exist, in
  ch3-sec3b.tex and ch3-refs.tex.
- Arithmetic, redone:
  - (C_f)_turb = 0.074/(5 x 10^5)^{1/5} = .0053634
  - (C_f)_lam = 1.328/(5 x 10^5)^{1/2} = .0018781
  - B = 5 x 10^5 x .0034854 = 1742.6, which gives the note's 1743. The note's .005363 and .001878 are correct, and
    "1740 matches to three figures" is correct.
  - The checklist's "about 1742" is the same number truncated; the note's 1743 is the correct rounding.
  - For context, not a required note: the same formula gives 1055, 3341 and 8944 for the other three tabulated
    R_crit, against the printed 1050, 3300 and 8700. The note makes no claim about these values.
- "Neither the errata nor the supplements reconcile the two values; both are kept as printed": correct. The errata
  have no entry for page 358 or 357. The supplement's replacement stops at (102b) and leaves the tabulation
  unchanged.
- Render (page 1): the caption and the note typeset correctly. The `??` marks are cross-unit references in the unit
  build.

## D15 (check, PDF 392)

- (105): 1.6 x 10^-3 x 10 / (1.206 x 10^6)^{2/5} = .016/270.7 = 5.91 x 10^-5. The book prints 5.93 x 10^-5, a
  last-digit difference. R_l = 1.196 x 10^6 would give 5.93.
- (C_f)_turb = .074/(1.206 x 10^6)^{1/5} = .004497, which the book rounds to .0045.
- (C_f')_turb from the printed formula = .004497 + .0000591 = .004557. The printed .0045593 is exactly
  .0045 + .0000593, which is 0.06% high. The percentage increase is 1.31%, so the text's "1.3%" holds.
- Conclusion: the printed values differ only by rounding, and no conclusion changes. Leaving D15 without a note
  (D35 practice) is sound, and the unit's header comment records the reason.
- The checklist's D15 row states wrong recomputed values: "about 6.15 x 10^-5" and "the .00459 the formula gives".
  The correct values are 5.91 x 10^-5 and .004557. This should be corrected when D15's status is recorded.

## Other checks

- Scope: the diff has no other changes. The header comment accurately lists what was applied.
- Labels: no equations were added or changed, and the 1973 labels are untouched.
- Section 14 notation in the new text: `R_{\mathrm{crit}}`, `(C_f)_{\mathrm{turb}}`, `(C_f)_{\mathrm{lam}}`,
  leading-dot decimals and capital B are all correct.
- corrections/ch3.md still shows item 4 and F1 as "todo" and D15 as "note (check first)". This is presumably updated
  by the orchestrator, as for the other units.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| Figure 22 `\edcap`, "gives $B = 1743$ ($(C_f)_{\mathrm{turb}} = \ldots$" | parenthetical without doubled opening parentheses, e.g. "gives $B = 1743$, from $(C_f)_{\mathrm{turb}} = .005363$ and $(C_f)_{\mathrm{lam}} = .001878$ at $R_{\mathrm{crit}}$," | renders "B = 1743 ((C_f)_turb = .005363 and ...)", with "((" reading awkwardly (optional wording fix; content correct) | note |
| corrections/ch3.md, row D15 | recomputation: (105) gives 5.91 x 10^-5; the formula gives (C_f')_turb = .004557 (flat plate .004497); the printed .0045593 = .0045 + 5.93e-5; status "no note (rounding)" | row still says "about 6.15 x 10^-5" and "the .00459 the formula gives" (both wrong), status "note (check first)" | note |
