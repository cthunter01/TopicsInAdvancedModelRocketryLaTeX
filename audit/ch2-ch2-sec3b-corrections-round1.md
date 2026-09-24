# Audit: corrections applied to chapters/ch2-sec3b.tex (round 1)

Unit: `chapters/ch2-sec3b.tex` (3.1.3-3.1.4, PDF 149-168). Diff audited: `git diff HEAD -- chapters/ch2-sec3b.tex`
(one hunk, 6 insertions, 1 deletion). Build audited: `build/unit/ch2-sec3b-{01..10}.png` and `ch2-sec3b.pdf`,
built 05:24:56 from the .tex saved 05:24:51, so the build is current. Sources consulted: PDF 158 (printed p. 128, the display),
PDF 156 (printed p. 126, equation (40)), the 1973 errata sheets PDF 664 and PDF 665, and corrections/ch2.md (D8).

Item to apply: **D8.** The unnumbered zero-angular-velocity display before (43a) prints a factor $t$ in both numerators.

## What was checked

1. **The doubt itself, derived independently.** Equation (40), confirmed against PDF 156, is
   $\alpha_X = \frac{H\tau_1\tau_2}{I_L(\tau_1-\tau_2)}\left[e^{-t/\tau_1} - e^{-t/\tau_2}\right]$. Differentiating it gives
   $d\alpha_X/dt = -\frac{H\tau_2}{I_L(\tau_1-\tau_2)}e^{-t/\tau_1} + \frac{H\tau_1}{I_L(\tau_1-\tau_2)}e^{-t/\tau_2}$.
   The numerators are $H\tau_2$ and $H\tau_1$ with no factor $t$, and the signs match the printed display.
   A sympy check confirms the derivative (the difference simplifies to 0). A numerical check shows that
   (43a) $t_m = \tau_1\tau_2\ln(\tau_1/\tau_2)/(\tau_1-\tau_2)$ makes this derivative zero (residual 5.6e-17). Setting
   the printed display to zero is the same equation for $t \neq 0$, because $t$ is a common factor of both terms. So
   (43a) is unaffected. The doubt is confirmed.
2. **1973 reading quoted in the note, checked against PDF 158.** The display prints "$tH\tau_2$" over
   $I_L(\tau_1-\tau_2)$ and "$tH\tau_1$" over $I_L(\tau_1-\tau_2)$, with the leading minus and the plus exactly as
   transcribed. The note's quotations ``$tH\tau_2$'' and ``$tH\tau_1$'' are accurate.
3. **Accuracy of the claim "Neither the errata nor the supplements correct this".** Neither errata sheet (PDF 664,
   PDF 665) has an entry for page 128. The Chapter 2 supplements (PDF 676-687) cover pp. 186-196, 251-254 and 259
   only. The claim is correct.
4. **The display is kept as printed** (STYLE.md section 11). The `equation*` body is unchanged from HEAD. Only the
   introducing sentence gained the note.
5. **Placement** (STYLE.md section 9). The `\ednote` sits in the sentence that introduces the display ("the applicable
   equation is\ednote{...}"), outside the `equation*`. This is as D8 specifies.
6. **Wording and consistency.** The note follows the pattern of the other Chapter 2 doubt notes (ch2-sec3a,
   ch2-sec3c): it states the printed reading, says what the derivation gives, and ends with "Neither the errata nor
   the supplements correct this; the display is kept as printed." It says only what the scan and the derivation support.
7. **Scope** (whole diff). The only change is the note, plus a source line break that moves "is" to the next line.
   It has no effect on the output. Nothing else in the unit changed.
8. **Labels.** No labels were added, removed or retagged. The note's `\eqref{ch2:eq:40}` and `\eqref{ch2:eq:43a}`
   are labels in this unit and resolve to (40) and (43a) in the build. The log's undefined references are all
   labels in other units: `ch2:sec:3.1.1`, `ch2:sec:3.1.2`, `ch2:fig:5`, `ch2:eq:13`, and `ch2:eq:15`-`26`. These are expected.
9. **Notation** (STYLE.md section 13). $H$, $\tau_1$, $\tau_2$, $t$ and $I_L$ are consistent with the unit and the Symbols list.
10. **Rendering.** On `build/unit/ch2-sec3b-05.png`, the marker E1 follows "is". The display is unchanged, with (43a)
    following it, and (41b), (42a), (42b) and (43a) are in sequence. The footnote text is complete, both
    cross-references resolve, and the layout is not broken.

Side observation, not a discrepancy in the unit: the D8 row in corrections/ch2.md still reads "todo". Its status
should be updated to "applied (\ednote in the sentence introducing the overdamped zero-velocity display before
(43a))" when the checklist is updated.

## Discrepancies

none
