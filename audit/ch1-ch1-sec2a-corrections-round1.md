# Audit: corrections applied to chapters/ch1-sec2a.tex (round 1)

Unit: `chapters/ch1-sec2a.tex` (1973 pp. 12-31, PDF 42-61). Diff audited: `git diff HEAD -- chapters/ch1-sec2a.tex`
(five hunks: header comment, Figure 2, pp. 16-19, the F1 display, pp. 30-31) plus `git diff HEAD -- figures/manifest.csv`.
Build audited: `build/unit/ch1-sec2a-{01..12}.png`, built 18:51:31 from the .tex saved 18:51:30 (current, so no
rebuild was needed). Sources consulted: PDF 666 (pressure-term notation, 1 June 1994), 668-674 (replacement pages and
new Figure 2), 664 (errata: nothing for this unit), 1973 pages PDF 44, 46, 48, 49, 56, 60, 61, and the crop
`figures/supplement/ch1-fig02-1994.png`.

## What was checked

1. **Item 3, manifest.** New row `sup-ch1-fig02-1994,674,12.0,18.0,558.0,455.0,line,ch1-sec2a,figures/supplement/ch1-fig02-1994.png,...`:
   box is in MediaBox points (page 612.48 x 792.48 per `pdftotext -bbox-layout`); the caption block starts at
   y = 471.1, the artwork's equation row ends at y = 432.3, so y1 = 455 keeps the drawing with its
   `-c(dm_e/dt) + (P_e - P_a)A_e = F` row and excludes the caption. `ch1-fig02` owner changed to `supplement`,
   file `figures/ch1/fig02.png` not deleted. `check_numbering.py` rule 4 (every manifest output owned by a unit
   of the chapter is included) is satisfied statically; the checker itself needs a full build and was not run.
2. **Item 3, crop.** Viewed: three rockets, axes, `P_a`/`P_e`/`A_e`/`F` labels and the equation row; no caption,
   no specks. (The equation row inside the bitmap necessarily keeps the long arrow drawn by Mandell; item 10 can
   only apply to typeset text.)
3. **Item 3, include.** `\includegraphics{figures/supplement/ch1-fig02-1994.png}` replaces `figures/ch1/fig02.png`;
   `\label{ch1:fig:2}` kept; renders as a float page (unit p. 2) with the drawing and the full caption.
4. **Item 3, caption text** (PDF 674/668) sentence by sentence: "Origin of Rocket Thrust." ... "The sum of the two
   force components is the rocket's *thrust* F:" matches word for word; underlined terms (*nozzle exit plane*,
   *ambient*, *thrust*, *NOTE*) are `\emph`.
5. **Item 3, caption equation** `\vec{F} = -\vec{c}(dm_e/dt) + (P_e - P_a)\vec{A}_e`: matches, arrow over `A_e` only.
6. **Item 3, NOTE paragraph**: matches word for word.
7. **Item 3, `\edcap`**: inside the caption (STYLE 9); its statement of the 1973 reading ("single rocket"; caption
   ended "The thrust F is given by the equation F = -c(dm_e/dt) and thus acts in the (+y) direction."; no pressure
   term) is exact against PDF 44.
8. **Item 4** (PDF 668, insert after line 3 of p. 16): new paragraph "As the exhaust gases leave the nozzle ...
   also called the *ambient* pressure." matches word for word; placed after "...obtaining derivatives from graphs
   and tables." (the Figure 3 float sits between in the source, which is float placement only). E1 accurate.
9. **Item 5, paragraph "Now the thrust of a rocket engine ..."** (PDF 668): matches the typed page except that the
   supplement types "momemtum" (a typewriter slip; the 1973 text and the italic phrase have "momentum") and the
   transcription silently has "momentum" -- see table. E2 quotes the 1973 first sentence and the end of the
   1973 second sentence ("...depends upon two quantities: ...") exactly (PDF 46).
10. **Item 5, equation (1)** `\vec{F} = -\vec{c}\,(dm_e/dt) + (P_e - P_a)\vec{A}_e`, label `ch1:eq:1` kept: matches
    PDF 669 symbol by symbol with the arrow moved to `A_e` (item 10). E3 in the introducing sentence; its 1973
    reading (`\vec{F} = -\vec{c}\,dm_e/dt` and the "where F denotes ..." sentence) is exact.
11. **Item 5, "where" list**: six entries match PDF 669 including the period after "...moving with the rocket."
12. **Item 5, "Students of physics will note ... algebraic signs."**: matches; E4 quotes the 1973 two sentences exactly.
13. **Item 6, p. 18 prose** ("is directed dead astern ... forces and velocities ... algebraically *positive* ...
    algebraically *negative*. According to this convention,"): matches PDF 669. E5 quotes the 1973 sentence and
    `\vec{c} \equiv -c` "so that" exactly (PDF 48) and correctly says the `F = \vec{F}` and `A_e = \vec{A}_e`
    displays are new.
14. **Item 6, displays** `c = -\vec{c}`, `F = \vec{F}`, "and" `A_e = \vec{A}_e` so that
    `(P_e - P_a)A_e = (P_e - P_a)\vec{A}_e`: match PDF 669 (arrow over `A_e` only).
15. **Item 6, equation (2)** `F = c\,(dm_e/dt) + (P_e - P_a)A_e`, label kept: matches (scalar form, no arrow).
    E6 accurate ("F = c dm_e/dt, without the pressure term").
16. **Item 6, "Professional rocket engineers ... gains in overpressure."** (PDF 669-670): matches word for word,
    including "alternative", "convergent/divergent", "combustion-chamber", *throat area*, the four quoted terms.
    E7 quotes the 1973 "Note that, since positive quantities ..." sentence exactly and says the page ended there.
17. **Item 7, p. 19** (PDF 670-671): both paragraphs match word for word ("exhaust velocity, exhaust pressure, and
    mass flow rate ... and the ambient pressure ...", "propellant, combustion chamber, and nozzle", "In any given
    engine", "than to variations in the exhaust velocity and pressure", "assume that the exhaust velocity is
    constant and the exhaust is optimally expanded", "(now simplified by the absence of the pressure term, since
    optimum expansion assumes P_e = P_a) as"). E8's six quoted 1973 fragments are exact (PDF 49).
18. **Item 7, equation (2a)** `\mdot = (dm_e)/(dt) = F/c` with `\tag{2a}` and `\label{ch1:eq:n2a}`: matches PDF 671
    literally; .aux shows `{{2a}}` and (3) still follows as (3). E9 in the introducing sentence, accurate.
19. **Flag F1**: the display is unchanged (`F_1\Delta t_1`, upper limit `t`, as printed on PDF 56); E10 is in the
    sentence "for which the mathematical notation is" and says `F_i\,\Delta t_i` (and `t_b`) are evidently meant.
20. **Item 8, opening** ("The answer to this question ... unit weight of propellant. Specific impulse is thus a
    measure ... The definition of specific impulse is"): matches PDF 671. E11 (placed after the first replaced
    sentence) quotes the whole 1973 passage from "...unit mass of propellant." through "(9.8 meters/sec.2)." with
    the 1973 (5), (6), (7) inline, exactly as on PDF 60-61, states that the 1973 (5) I_sp = I_t/m_f disappears,
    and that the numbering is not shifted.
21. **Equation (5)** `\Isp = I_t/w_f = I_t/(m_f g)`, label `ch1:eq:5` kept: matches. E12 accurate.
22. **"where m_f is the *mass* ... numerically identical in all common systems of units. ... by the equation"**:
    matches, including "at mean sea level (9.806 meters/sec.2)".
23. **Equation (6)** `c + (P_e - P_a)A_e/\mdot = g\Isp`, label kept: matches. E13 accurate (1973 (6) = I_t/w_f).
24. **"where the quantity c + A_e[(P_e - P_a)/\mdot] ..."** and **equation (7)** as a two-line `split`
    (`c_eff = c + (P_e - P_a)A_e/\mdot` / `= g\Isp`), label kept: matches PDF 671. E14 accurate (1973 (7) c = gI_sp
    and the "where g is ..." sentence on PDF 61).
25. **"The specific impulse measured ... infinite exit plane area."** (PDF 671-672): matches word for word.
26. **Blackpowder paragraph** (PDF 672): matches; E15 lists exactly the four wording changes against PDF 61.
27. **Closing paragraph** (PDF 672): matches ("motor manufacturer", "average effective exhaust velocity using
    equation (7), assume optimum expansion so c_eff = c, ... from equation (2a)", new last sentence). E16 quotes
    the 1973 ending exactly and says the section ended there.
28. **Item 10**: all twelve `(P_e - P_a)` occurrences in the unit inspected: the vector form is always
    `(P_e - P_a)\vec{A}_e`; no `\overrightarrow`, no `\vec{(P...`, no `\vec{A_e}`.
29. **Labels (STYLE 4/5)**: `ch1:eq:1,2,3,4,5,6,7` kept; only `ch1:eq:n2a` carries `\tag`; `ch1:fig:2` kept.
30. **Scope**: every changed line in the five hunks belongs to items 3-8, 10 or F1 (plus the two source comments);
    the Figure 3 block, equations (3)-(4), the numerical-integration pages and the propellant-history paragraph
    are untouched.
31. **Build log**: no errors, no Overfull boxes; the only undefined reference is `ch4` (another unit, expected).
32. **Rendered pages** 2, 4, 5, 6, 7, 9, 10, 11, 12 viewed: equations numbered (1), (2), (2a), (3), (4), (5), (6),
    (7) in sequence; `\eqref{ch1:eq:n2a}` prints "(2a)"; footnotes E1-E16 in order; caption, where-list and the
    `split` render cleanly; no "??" inside the unit.

## Discrepancies

| where | expected (supplement/1973) | found | severity |
|---|---|---|---|
| p. 16 paragraph "Now the thrust of a rocket engine ..." (line 112) and its ednote E2 | PDF 668 types "transferring momemtum to the rocket" (a typewriter slip; the 1973 text reads "momentum"); STYLE 10 forbids a silent normalisation, so keep "momentum" but record in E2 that the supplement's "momemtum" is read as "momentum" | "momentum" with no mention of the supplement's spelling | note |

## Observations (not discrepancies)

- E11 is a long footnote that starts on unit p. 9 and continues on p. 11 because p. 10 is the Figure 5 float page;
  this is ordinary LaTeX behaviour and the pagination will differ in the chapter build.
- The artwork's own equation row (inside the 1994 bitmap) shows Mandell's long arrow over `(P_e - P_a)A_e`; the
  `\edcap` could mention that the typeset text follows his 1 June 1994 note instead, but the task does not require it.
- `corrections/ch1.md` still shows items 3-8, 10 and F1 as "todo"; the status column is outside this unit's file.
- `tools/check_numbering.py` requires `make all` and was not run.
