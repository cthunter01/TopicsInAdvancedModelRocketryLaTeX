# Audit: corrections applied to chapters/ch1-sec2a.tex (round 2)

Unit: `chapters/ch1-sec2a.tex` (1973 pp. 12-31, PDF 42-61). Diff audited: `git diff HEAD -- chapters/ch1-sec2a.tex`
(five hunks: header comment, Figure 2, pp. 16-19, the F1 display, pp. 30-31; 236 insertions, 77 deletions) and
`git diff HEAD -- figures/manifest.csv` (owner of `ch1-fig02` changed, one row added). Build audited:
`build/unit/ch1-sec2a-{01..12}.png`, rendered 19:01:30 from the .tex saved 19:01:23 (current; no rebuild needed).
Sources consulted: PDF 666 (pressure-term notation, 1 June 1994), 668-674 (replacement pages, symbol list, new
Figure 2), 664 (errata: no item for this unit), 1973 pages PDF 44, 46, 48, 49, 56, 60, 61, and the crop
`figures/supplement/ch1-fig02-1994.png`.

## Round-1 finding

- Line 112 / E2 ("momemtum"): **fixed**. E2 now ends "The supplement types ``momemtum'' in the italicised sentence,
  a typewriter slip; it is read here as ``momentum'', the 1973 spelling." The body keeps "momentum" (the 1973
  spelling, PDF 46). Nothing else in the paragraph changed between rounds.

## What was checked (all pass)

1. **Item 3, manifest.** Row `sup-ch1-fig02-1994,674,12.0,18.0,558.0,455.0,line,ch1-sec2a,figures/supplement/ch1-fig02-1994.png,"replacement Figure 2, Mandell 1994; ..."`
   parses (`csv.DictReader`, 12 rows, 10 columns). Box is in MediaBox points (`pdftotext -bbox-layout`: page
   612.48 x 792.48); the caption block starts at y = 471.1 and the drawing's equation row ends at y = 432.3, so
   y1 = 455 keeps the whole drawing and excludes the caption (and the stray mark at y = 464-501). `ch1-fig02` owner
   is now `supplement`; `figures/ch1/fig02.png` still exists.
2. **Item 3, crop** (viewed): three rockets, axes, `P_a`, `P_e`, `A_e`, `F` labels, the equation row; no caption,
   no specks. The crop (18:46:50) is newer than the manifest (18:46:49).
3. **Item 3, include and caption.** `\includegraphics{figures/supplement/ch1-fig02-1994.png}`, `\label{ch1:fig:2}`
   kept. Caption compared sentence by sentence with PDF 674/668: "Origin of Rocket Thrust." ... "The sum of the two
   force components is the rocket's *thrust* F:" identical; display `\vec{F} = -\vec{c}(dm_e/dt) + (P_e - P_a)\vec{A}_e`
   (arrow over `A_e` only); NOTE paragraph identical; underlined terms as `\emph`. `\edcap` inside the caption
   (STYLE 9) states the 1973 reading exactly (single rocket; caption ended "The thrust F is given by the equation
   F = -c(dm_e/dt) and thus acts in the (+y) direction."; no pressure term; 1973 figure to be reproduced in the
   supplement Part) -- checked against PDF 44. Renders as a float page (unit p. 2) with drawing, caption, display
   and note; no `\listoffigures` anywhere in the repo, so the display in the caption is harmless.
4. **Item 4** (PDF 668): inserted paragraph "As the exhaust gases leave the nozzle ... also called the *ambient*
   pressure." word for word, after "...obtaining derivatives from graphs and tables." (the Figure 3 float sits between
   in the source only). E1 accurate (PDF 46).
5. **Item 5** (PDF 668-669): "Now the thrust of a rocket engine ..." paragraph word for word (see round-1 fix);
   E2 quotes the two 1973 sentences exactly. Equation (1) `\vec{F} = -\vec{c}\,(dm_e/dt) + (P_e - P_a)\vec{A}_e`,
   label `ch1:eq:1` kept; E3 in the introducing sentence, its 1973 reading (`\vec{F} = -\vec{c}\,dm_e/dt` and the
   "where F denotes ..." sentence) exact. "where" list: six entries identical, including the period after
   "...moving with the rocket." "Students of physics will note ... algebraic signs." identical; E4 quotes the 1973
   two sentences exactly. Page ends "...the exhaust stream" as in 1973.
6. **Item 6** (PDF 669-670): p. 18 prose ("forces and velocities", "algebraically *positive*", "algebraically
   *negative*") identical; displays `c = -\vec{c}`, `F = \vec{F}`, "and" `A_e = \vec{A}_e` so that
   `(P_e - P_a)A_e = (P_e - P_a)\vec{A}_e` identical; equation (2) `F = c\,(dm_e/dt) + (P_e - P_a)A_e`, label kept;
   "Professional rocket engineers ... gains in overpressure." identical (alternative, convergent/divergent,
   combustion-chamber, *throat area*, the four quoted terms). E5 (1973 sentence and `\vec{c} \equiv -c` "so that",
   PDF 48), E6 (1973 (2) without pressure term) and E7 (1973 "Note that, since positive quantities ..." sentence,
   page ended there) all exact.
7. **Item 7** (PDF 670-671): both p. 19 paragraphs identical to the supplement; E8's six quoted 1973 fragments exact
   (PDF 49). Equation (2a) `\mdot = (dm_e)/(dt) = F/c` with `\tag{2a}\label{ch1:eq:n2a}`; the .aux shows `{{2a}}`,
   (3) still numbers as (3); E9 in the introducing sentence.
8. **Flag F1**: display unchanged (`F_1\Delta t_1`, upper limit `t`, as printed on PDF 56); E10 in "for which the
   mathematical notation is", saying `F_i\,\Delta t_i` (and `t_b`) are evidently meant.
9. **Item 8** (PDF 671-672): from "The answer to this question ..." to "...during the entire burning period."
   compared sentence by sentence: identical, including "unit weight", "(9.806 meters/sec.2)", "numerically identical
   in all common systems of units", the "ideal vacuum" passage, the blackpowder paragraph and the new closing
   sentence. Equations (5) `\Isp = I_t/w_f = I_t/(m_f g)`, (6) `c + (P_e - P_a)A_e/\mdot = g\Isp`, (7) two-line
   `split` `c_eff = c + (P_e - P_a)A_e/\mdot` / `= g\Isp`, labels `ch1:eq:5/6/7` kept, no `\tag`. E11 quotes the
   whole 1973 passage from "...unit mass of propellant." to "(9.8 meters/sec.2)." with the 1973 (5), (6), (7)
   exactly (PDF 60-61), states that the 1973 (5) disappears and that the numbering is not shifted. E12-E14 (1973 (5),
   (6), (7)), E15 (the four wording changes in the blackpowder paragraph) and E16 (1973 closing sentences, section
   ended there) all exact.
10. **Item 10**: every typeset pressure term in the unit inspected (lines 60, 64, 130, 135, 176, 181, 204, 472,
    474, 480): vector form always `(P_e - P_a)\vec{A}_e`; scalar form in (2), (6), (7) as the supplement has it;
    no `\overrightarrow`, `\vec{(P...` or `\vec{A_e}`.
11. **Labels** (STYLE 4/5): `ch1:eq:1,2,3,4,5,6,7` and `ch1:fig:2` kept; the only `\tag` is on `ch1:eq:n2a`;
    no `\draftnote` left.
12. **Scope**: every changed line belongs to items 3-8, 10 or F1 (plus the two source comments); Figure 3, (3),
    (4), the integration pages and the propellant-history paragraph are untouched; HEAD had no ednotes.
    Manifest: only the two Figure 2 rows differ.
13. **Build**: log has no errors and no Overfull boxes; the only undefined reference is `ch4` (another unit).
    All twelve rendered pages viewed: equations (1), (2), (2a), (3), (4), (5), (6), (7) in sequence; `\eqref` of
    `ch1:eq:n2a` prints "(2a)"; E1-E16 in order; caption, where-list, gather/equation* displays and the `split`
    render cleanly; the only "??" is "Chapter ??" (label `ch4`, expected).

## Discrepancies

none

## Observations (not discrepancies)

- On p. 18 the supplement also changes "alternate" (1973) to "alternative" in the mass-flow-rate sentence; the
  transcription follows the supplement. This is covered by E5's statement that the whole page is replaced, but no
  note quotes the 1973 word; E7 begins one sentence later. Harmless, could be folded into E5 if wanted.
- The 1994 bitmap's own equation row shows Mandell's long arrow over `(P_e - P_a)A_e`; item 10 can only apply to
  typeset text.
- `corrections/ch1.md` still lists items 3-8, 10 and F1 as "todo"; the status column is outside this unit.
- `tools/check_numbering.py` needs `make all` and was not run.
