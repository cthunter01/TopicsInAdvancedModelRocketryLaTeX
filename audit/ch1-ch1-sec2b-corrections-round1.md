# Audit: corrections applied to chapters/ch1-sec2b.tex (round 1)

Unit: `chapters/ch1-sec2b.tex` (1973 pp. 36-43, PDF 66-73). Diff audited: `git diff HEAD -- chapters/ch1-sec2b.tex`
(three hunks). Build audited: `build/unit/ch1-sec2b-{1..7}.png`, built 18:44:19 from the .tex saved 18:44:11
(current). Sources consulted: PDF 675 (replacement of p. 40), PDF 666 (pressure-term notation), PDF 664 (errata),
1973 pages PDF 68, 69, 70, 72.

## What was checked

1. **Item 9, replacement paragraph (PDF 675) sentence by sentence.** The first sentence ("According to the method
   ... whose magnitude is given by") is identical in 1973 and 1994 and is an unchanged context line. The four new
   or reworded sentences ("where $C_N$ is the normal force coefficient whose computation ... Chapter 2." /
   "For angles of attack that are not too large ..." / "The variation of $C_N$ with $\alpha$ can then be expressed
   as" / "where $\CNa$ is the slope of the curve ... normal force curve slope. Then") and the closing two sentences
   ("The component of force $N\sin\alpha$ ... component of force $N\cos\alpha$ ... Figure 7.") match the typed page
   word for word, including the 1994 wording "component of force $N\cos\alpha$" (1973: "component $N\cos\alpha$")
   and the absence of the 1973 comma after "coefficient". Underlined terms are `\emph`.
2. **Equation (20)** $N = \tfrac{1}{2}\rho C_N A_r v^{2}$: matches PDF 675 symbol by symbol ($C_N$, not $C_{n\alpha}$).
3. **Equation (21)** $C_N = \CNa \cdot \alpha$: matches, including the raised dot.
4. **Equation (22)** $N = \tfrac{1}{2}\rho \CNa A_r v^{2}\alpha$: matches.
5. **E2 ednote, statement of the 1973 reading** compared with PDF 70: the 1973 equation (20)
   $N = \tfrac{1}{2}\rho C_{n\alpha} A_r v^{2}$ and the quoted 1973 sentences ("where $C_{n\alpha}$ is the normal
   force coefficient, whose computation ... Chapter 2. The component of force $N\sin\alpha$ ... while the component
   $N\cos\alpha$ is a side force ...") are quoted exactly; the note correctly says the 1973 text had no equations
   corresponding to (21)/(22) and correctly reports the "+2" instruction.
6. **E2 placement** (STYLE.md section 9): in the sentence that introduces display (20), outside the `equation`
   environment.
7. **Labels** (STYLE.md section 4): `ch1:eq:20` kept on the rewritten (20); new equations labelled `ch1:eq:n21`,
   `ch1:eq:n22`; the 1973 (21) and (22) keep `ch1:eq:21`/`ch1:eq:22` in the `align`; `grep '\\tag'` finds nothing
   in the unit. The .aux confirms `ch1:eq:21` -> 23 and `ch1:eq:22` -> 24.
8. **inventory/ch1-renumber.json**: contains exactly `{"21": "23", "22": "24"}`.
9. **PDF 72 citation.** 1973 "(19), (20), and (21)" now targets `ch1:eq:19`, `ch1:eq:n22`, `ch1:eq:21`, rendering
   "(19), (22), and (23)". With (19) $D = \{k + \epsilon f(\alpha)\}v^{2}$, new (22) $N = \tfrac{1}{2}\rho\CNa A_r
   v^{2}\alpha$ and (23) $N\sin\alpha \cong N\alpha$, the deduction $\epsilon = \tfrac{1}{2}\rho\CNa A_r$,
   $f(\alpha) = \alpha^{2}$ follows; these are the equations the authors evidently meant.
10. **$\epsilon$ display**: 1973 $C_{n\alpha}$ written `\CNa`, as the item requires (the 1973 quantity is what
    the 1994 text calls the normal force curve slope). No other $C_{n\alpha}$/$C_n$ remains in the unit outside
    the ednote quotations.
11. **E3 ednote**: the 1973 citation and the 1973 form of the $\epsilon$ relation are quoted accurately against
    PDF 72; it explains both the retargeted citation and the $C_{n\alpha} \to \CNa$ change; placed in the sentence
    introducing the `equation*` display.
12. **Item 10 (pressure term)**: `grep 'P_e\|P_a\|A_e'` finds no occurrence in this unit; not applicable.
13. **Flag F2**: the two thresholds "less than $5 \times 10^{5}$" (PDF 68) and "greater than $5 \times 10^{6}$"
    (PDF 69) are kept as printed; the E1 ednote quotes both correctly; the errata sheet (PDF 664) has no entry for
    pp. 38-39, so the note's statement that neither source corrects them is accurate. Placed at the end of the
    sentence containing the second threshold, in running prose (no display involved).
14. **Scope**: the whole diff consists of the F2 ednote, the item 9 paragraph replacement, and the PDF 72
    citation/ednote/$\epsilon$ change. Nothing else in the unit changed.
15. **Rendered pages** 4-7: equations run (18), (19), (20), (21), (22), (23), (24) in sequence; footnotes E1-E3
    typeset at the foot of pages 4 and 5; every `??` is a cross-unit label (`ch2`, `ch3`, `ch4`, `ch1:fig:8`,
    `ch1:sec:2.1`, `ch1:eq:2`); the log has 0 errors, 0 multiply defined labels, 0 overfull boxes > 20 pt.
    Figure 7 now floats to a page of its own in the standalone build (page 6); not a defect.
16. **tools/check_numbering.py** (`--aux build/unit/ch1-sec2b.aux --tolerate-undefined`): check 2 "displayed
    numbers" OK, 17 labels compared, 0 mismatches, with `n21`/`n22` reported as corrected-edition equations. Its
    failing checks [1] and [4] concern labels and the 1994 Figure 2 file belonging to other units.

## Discrepancies

| where | expected (supplement/1973) | found | severity |
|---|---|---|---|
| none | | | |

## Observations (non-blocking)

- E1 (flag F2) goes slightly beyond "noting the inconsistency": the parenthetical "(a single transition value is
  evidently intended; $5 \times 10^{5}$ is the usual flat-plate figure)" is an editorial inference. It misstates
  nothing and is left to the editor's judgment.
- The Status column of `corrections/ch1.md` still reads "todo" for items 9, 10 and F2; updating it was not part of
  this unit's brief.
