# Audit: corrections applied to chapters/ch3-intro-sec2a.tex (round 1)

Unit: `chapters/ch3-intro-sec2a.tex` (Chapter 3 introduction to 2.1.2, PDF 298 on). Diff audited:
`git diff HEAD -- chapters/ch3-intro-sec2a.tex` against HEAD 7e2087d (the faithful transcription). It has two hunks
(24 lines added, 2 removed), each of which inserts one `\ednote` into an existing sentence. The build audited is
`build/unit/ch3-intro-sec2a-01.png` to `-11.png` with `ch3-intro-sec2a.pdf`. It was built at 09:34:29.75 from the
.tex saved at 09:34:28.33, so the build is current and was not rerun. Rules read: STYLE.md sections 4, 8, 9, 10, 11
and 14, and corrections/ch3.md, including the "Decisions for the corrections step (2026-09-24)" block.

Items to apply:
- **D9** (PDF 314-315): a note on $E$ being taken as the sea-level pressure (isothermal). With it, (5) gives about
  288 m/s, not the 340 m/s used on PDF 316 and in Figure 4.
- **D10** (PDF 315): a note on $c^2 = E/\rho_o$ being credited to "Laplace's equation" (the wave equation is meant).

## Sources and their authors and dates

- 1973 pages read in full: PDF 314 (p. 284: (1)-(4), "E is just equal to the sea-level pressure of 101,325
  nt/m^2"), PDF 315 (p. 285: "a calculus problem known as Laplace's equation", (5)-(9)), PDF 316 (p. 286: "about
  340 meters/second", 107 m/s) and PDF 506 (p. 474, Section 7.1: "about 340 meters/second"). I also read the figure
  crops `figures/ch3/fig02.png` (the artwork gives "rho_o = 1.225014 kg/m^3") and `figures/ch3/fig04.png` (c = 340
  m/sec at 0 m).
- 1973 errata sheet, PDF 664: headed "ERRATA" with the book's citation. It shows no author and no date. Its
  Chapter 3 entries are pp. 268, 270, 342, 364, 382, 401 and 480. None is for p. 284 or p. 285.
- Chapter 3 supplement pages, PDF 688-698, all read. None shows an author or a date.
  - PDF 688-689 are the replacement pp. 356 and 357 ((97)-(102b), "calculated" inserted by caret).
  - PDF 690 is Section 5.2.2 ((144A), (144B), e = 0.863).
  - PDF 691-693 are Section 5.3 ((152)-(156)).
  - PDF 694 is the eight symbol-table entries. None of them is E, c or rho_o.
  - PDF 695-698 are pp. 445, 449 and 451-452.
  - None of these pages touches pp. 284-286.
- So both notes are right to say "Neither the errata nor the supplements correct this".

## What was checked

1. **Faithful text kept.** Both hunks only insert `\ednote{...}`. The 1973 sentences are unchanged, word for word
   against PDF 314-315:
   - "... E is just equal to the sea-level pressure of 101,325 nt/m^2. The total mass ..."
   - "... can be found by solving a calculus problem known as Laplace's equation, given the density and elasticity
     of the air. The result of the calculation is"

   The only other change is the reflow of the line breaks after each note. No equation, label or other text in the
   unit changed.
2. **D9, statement of the 1973 reading.** The note says "The text sets E equal to the sea-level pressure, its value
   for isothermal changes". This matches PDF 314 ("assuming isothermal (constant-temperature) pressure changes, E
   is just equal to the sea-level pressure").
3. **D9, arithmetic (redone).**
   - sqrt(101325/1.225) = 287.60, and with rho_o = 1.225014 it is 287.60. So "≅ 288 meters/second" is correct.
   - 1.4 x 101325 = 141,855, which is "about 141,900" to four figures. This is correct.
   - sqrt(141855/1.225) = 340.29. So "gives 340 meters/second" is correct.
   - Check: 340^2 x 1.225 / 101325 = 1.398, which is gamma.
4. **D9, the other claims.**
   - The 340 m/s is "used below" (PDF 316), "in Section 7" (PDF 506, ch3-sec7.tex line 43) and "plotted in
     Figure 4" (the crop reads 340 at sea level). All three are true.
   - "The sea-level density of Figure 2" is true: the artwork prints 1.225014 kg/m^3.
   - "The adiabatic modulus, 1.4 times the pressure (1.4 being the ratio of the specific heats of air)" is correct:
     the isentropic bulk modulus is gamma p.
   - "The pressure changes of a sound wave, like those of the flow about a body, are adiabatic" is correct. The
     inviscid compression at a stagnation point is isentropic. This clause carries the next claim.
   - "The argument that follows is unchanged" is correct. (1)-(9) keep their form. With the adiabatic E,
     substituting E = c^2 rho_o with c = 340 m/s in (4) is self-consistent, which it is not with the isothermal E.
   - The closing formula matches the Decisions template.
5. **D10, statement of the 1973 reading.** The quoted words ``a calculus problem known as Laplace's equation'' are
   exact (PDF 315, line 1).
6. **D10, derivation (redone).**
   - Linearized continuity: d(rho')/dt + rho_o du/dx = 0.
   - Momentum: rho_o du/dt = -dp'/dx.
   - Equation (4): p' = E rho'/rho_o.
   - Together these give (rho_o/E) d2p'/dt2 = d2p'/dx2, that is d2p/dt2 = (E/rho_o) d2p/dx2. D'Alembert's
     solutions travel at sqrt(E/rho_o).
   - The note's display and its "waves traveling at the speed sqrt(E/rho_o)" are correct, and so is "contains no
     speed of propagation" (Laplace's equation has no time derivative). The one imprecision, "steady potential
     flow", is in the table.
7. **Placement** (section 9).
   - E1 follows "... 101,325 nt/m$^{2}$." In the build it is the note marker after that sentence.
   - E2 follows "... elasticity of the air.", the sentence that contains "Laplace's equation". It comes before
     the sentence that introduces (5).
   - Neither note is inside a display, a caption or a table.
8. **Labels.** There are no new equations, and no label was added, removed or retagged. `\eqref{ch3:eq:4}`,
   `\eqref{ch3:eq:5}`, `\ref{ch3:fig:2}` and `\ref{ch3:fig:4}` resolve in the unit build. `\ref{ch3:sec:7}` is
   defined in ch3-sec7.tex, so the "??" in the unit build is expected.
9. **Notation** (section 14).
   - $\rho_o$ uses the letter o.
   - Pressure is lowercase $p$ and derivatives use `\partial`.
   - "≅" is `\cong`.
   - Units after a number in prose stay as text ("meters/second"), and "nt/m$^{2}$" is spelled as the book spells
     it.
   - `101{,}325` gives the right spacing in math.
10. **Rendering.**
    - `build/unit/ch3-intro-sec2a-05.png`: the E1 marker follows "101,325 nt/m²." The footnote begins at the foot
      of the page ("E1 Editor's note: The text sets E equal to ...").
    - `-06.png`: E1 continues at the head of the footnotes with "c = √(101,325/1.225) ≅ 288 meters/second ...",
      complete through "kept as printed." The E2 marker follows "air." E2 is complete, with ∂²p/∂t² = (E/ρ_o)
      ∂²p/∂x² and √(E/ρ_o) typeset correctly.
    - E1 splitting across pp. 5-6 is ordinary footnote breaking in the unit build, and the chapter build will
      paginate differently.
    - Nothing is clipped or overfull.

Side observation, not a discrepancy in the unit: the D9 and D10 rows in corrections/ch3.md still read "note". When
the checklist is updated they should read "applied (\ednote after "101,325 nt/m^2.", PDF 314)" and "applied (\ednote
after "elasticity of the air.", PDF 315)".

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| ch3-intro-sec2a.tex line 352, D10 note (E2) | Laplace's equation governs *incompressible* potential flow, steady or unsteady. Steady compressible potential flow does not obey it. Say "governs incompressible potential flow", or just "Laplace's equation has no time derivative and so no speed of propagation" | "Laplace's equation governs steady potential flow and contains no speed of propagation" | note |
| ch3-intro-sec2a.tex lines 323-324, D9 note (E1) | The item asks for a short, factual note stating what the scan and the arithmetic support. The historical parenthetical is true but unneeded. Next to E2 it also names Laplace a second time, which blurs E2's point. Drop it (optional trim) | "are adiabatic (Laplace's correction of Newton's isothermal value)." | note |
