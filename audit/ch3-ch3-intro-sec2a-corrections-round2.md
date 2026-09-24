# Audit: corrections applied to chapters/ch3-intro-sec2a.tex (round 2)

Unit: `chapters/ch3-intro-sec2a.tex` (Chapter 3 introduction to 2.1.2). Diff audited:
`git diff HEAD -- chapters/ch3-intro-sec2a.tex` against HEAD 7e2087d (the faithful transcription): two hunks,
22 lines added, 2 removed. Each hunk inserts one `\ednote` into an existing sentence. Rendering audited from
`build/unit/ch3-intro-sec2a-01.png` to `-11.png`. The PDF was built at 09:40:16, after the .tex was saved at
09:40:11, so the build is current. I did not rebuild. Rules read: STYLE.md sections 4, 8, 9, 10, 11 and 14, and
corrections/ch3.md, including "Decisions for the corrections step (2026-09-24)".

Items: **D9** (PDF 314-315), a note on E taken as the sea-level (isothermal) pressure, and **D10** (PDF 315), a note
on "Laplace's equation". Both are type "note", with no text replacement.

## Sources, authors and dates

- 1973 pages read: PDF 314 (p. 284), 315 (p. 285) and 316 (p. 286). I also read the figure crops
  `figures/ch3/fig02.png` (rho_o = 1.225014 kg/m^3) and `fig04.png` (c = 340 m/sec at 0 m, about 330 at 2500 m).
- Errata sheet PDF 664 ("ERRATA", with the book's citation) and PDF 665 (a second typing, "Errata"). **Neither
  shows an author or a date.** Their Chapter 3 entries are pp. 268, 270, 342, 364, 382, 401 and 480. Neither has an
  entry for pp. 284-286.
- Supplement pages PDF 688-698, all read. **None shows an author or a date.** Each page's heading or page number
  is as follows:
  - 688-689: replacement pp. 356 and 357, with "calculated" inserted by caret.
  - 690: "Corrections and additions to Section 5.2.2".
  - 691-693: "Corrections to drag due to fin cant ... Section 5.3".
  - 694: the symbol-table additions. None of them is E, c or rho_o.
  - 695: p. 445. 696: p. 449. 697-698: pp. 451-452.
- None of these pages touches pp. 284-286. Both notes are right to say "Neither the errata nor the supplements
  correct this".

## Round-1 findings (verification)

1. **E2 wording ("governs steady potential flow") is fixed.** Line 352 of the source now reads "Laplace's equation,
   which governs incompressible potential flow, has no time derivative and so no speed of propagation". This is
   correct. The velocity potential of incompressible flow satisfies Laplace's equation, steady or unsteady, and the
   equation has no time derivative.
2. **The E1 parenthetical is dropped.** The note now ends its physics sentence at "... are adiabatic." without the
   historical aside. Laplace is now named only in E2, where the text names it.

## What was checked

1. **Application.** Neither item replaces text or equations. The two hunks only insert notes. With both `\ednote{...}`
   bodies stripped, the current file and HEAD have the same token sequence (4571 = 4571 tokens). No 1973 word,
   equation or label changed. Only the source line breaks after each note moved. The retained sentences match PDF
   314-315:
   - "... E is just equal to the sea-level pressure of 101,325 nt/m^2."
   - "... by solving a calculus problem known as Laplace's equation, given the density and elasticity of the air.
     The result of the calculation is"
2. **Statement of the 1973 reading.**
   - E1 says "The text sets E equal to the sea-level pressure, its value for isothermal changes". This matches PDF
     314.
   - E2's quotation, "a calculus problem known as Laplace's equation", is exact (PDF 314 last line to PDF 315
     line 1). Crediting "equation (5)" to it is accurate: the next sentence reads "The result of the calculation
     is (5)".
3. **Arithmetic (redone).**
   - sqrt(101325/1.225) = 287.60, or 287.60 with 1.225014. This gives "≅ 288 meters/second".
   - 1.4 x 101325 = 141,855, or "about 141,900" to four figures.
   - sqrt(141855/1.225) = 340.29. This gives "340 meters/second".
   - Check: 340^2 x 1.225/101325 = 1.398, which is gamma.
   - Figure 4 falls from 340 to about 330.3 m/s at 2500 m. The adiabatic 20.05 sqrt(T) gives 340.3 at 288.15 K and
     330.6 at 271.9 K. So the figure is the adiabatic value, as E1 implies.
   - "Used below" (PDF 316: "about 340 meters/second"), "in Section 7" (ch3-sec7.tex line 43) and "plotted in
     Figure 4" are all true.
   - "The argument that follows is unchanged" is true. (1)-(9) keep their form, and E = c^2 rho_o with c = 340 is
     consistent only with the adiabatic E.
4. **E2 derivation (redone).**
   - Linearized continuity: ∂ρ'/∂t + ρ_o ∂u/∂x = 0.
   - Momentum: ρ_o ∂u/∂t = −∂p'/∂x.
   - Equation (4): p' = E ρ'/ρ_o.
   - Together these give ∂²p/∂t² = (E/ρ_o) ∂²p/∂x². The waves travel at sqrt(E/ρ_o).
   - The note's display and wording are correct.
5. **Style and placement** (section 9).
   - Both notes close with the Decisions template: "Neither the errata nor the supplements correct this; the text is
     kept as printed." This matches the Chapter 2 notes.
   - E1 follows "101,325 nt/m$^{2}$."
   - E2 follows "elasticity of the air.", the sentence that names Laplace's equation, before the sentence that
     introduces (5).
   - Neither note is inside a display, caption or table.
   - Both notes stay short and factual (about 95 and 75 words).
6. **Scope.** The whole diff is these two insertions. Nothing else in the unit changed.
7. **Labels.** There are no new equations and no label changed. `\eqref{ch3:eq:4}`, `\eqref{ch3:eq:5}`,
   `\ref{ch3:fig:2}` and `\ref{ch3:fig:4}` resolve. `\ref{ch3:sec:7}` is defined in ch3-sec7.tex, so the "??" in
   the unit build is expected. The log's only undefined references are cross-unit ones.
8. **Notation** (section 14).
   - `\rho_o` uses the letter o.
   - Pressure is lowercase p, and `\partial` is used where a partial derivative is meant.
   - `\cong` sets "≅" and `101{,}325` spaces the number correctly.
   - Units are text ("meters/second", "nt/m$^{2}$"), as the book has them.
9. **Rendering.**
   - `-05.png`: the E1 marker follows "101,325 nt/m²." The note begins at the foot of the page.
   - `-06.png`: E1 continues from "c = √(101,325/1.225) ≅ 288 meters/second" through "kept as printed." It no longer
     has the Newton/Laplace parenthetical.
   - The E2 marker follows "air." The note is complete, with ∂²p/∂t² = (E/ρ_o) ∂²p/∂x², √(E/ρ_o) and "which governs
     incompressible potential flow".
   - Nothing is clipped, and the log reports no overfull boxes.

Side observation, not a discrepancy in the unit: the D9 and D10 rows of corrections/ch3.md still read "note". When
the checklist is updated they should read:
- D9: "applied (\ednote after '101,325 nt/m^2.', PDF 314)"
- D10: "applied (\ednote after 'elasticity of the air.', PDF 315)"

## Discrepancies

none
