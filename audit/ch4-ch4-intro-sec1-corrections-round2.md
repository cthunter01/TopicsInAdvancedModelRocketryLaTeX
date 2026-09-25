# Audit: ch4-intro-sec1 corrections, round 2

Unit: chapters/ch4-intro-sec1.tex (Introduction, Section 1, 1.1 and 1.2; PDF 537-552, printed pp. 505-520).
Items for this unit:
- Item 5 (PDF 700-702, pressure term per PDF 666): the June 1994 thrust text after (7) and at the top of p.514.
- D9 (PDF 552): note on $F_p$ of (10).

Read: STYLE.md sections 4, 7, 8, 9, 10, 11 and 15; corrections/ch4.md; the round 1 report;
`git diff HEAD -- chapters/ch4-intro-sec1.tex`.

Source pages read: p545, p546, p551, p552 (1973); p666, p699, p700, p701 (1994); p703 (the Summary's first page).

Zoomed crops (300 dpi, prefix build/zoom/audit_ch4-intro-sec1_r2-):
- p700-7ab-700.png: (7a)-(7b);
- p700-where-700.png: the "Where $\vec{A}_e$" line;
- p700-7cd-700.png: the "Equation (7) above ..." paragraph through (7d);
- p701-8-701.png: (8) and its "Where" line.

## Round 1 finding

The round 1 finding (E1, the extent of the item 5 note) is **fixed**.
- The \ednote marker now follows the first replaced sentence, "... as it would be measured in a static test stand." (l.187).
- The note now opens "From the sentence after equation (7) ("If the nozzle ...") to the end of the paragraph before
  Section 1.1". This names the full extent of the 1994 replacement: from PDF 700's first sentence to "... or drag." on
  PDF 701.
- The placement is legal under section 9: in prose, before "That is," and the (7a) display, not inside a display.

## What was checked

1. **Item 5 applied as the source specifies.**
   - **Extent.** The change replaces the 1973 text from "The term $-\vec{c}(dm_e/dt)$ is just ..." (PDF 545) to "... or
     drag." (PDF 546). Section 1.1 and the rest of p.514 are unchanged. The 1973 sentence "The thrust can be denoted by the
     single symbol $\vec{F}(t)$ ..." is gone, as in the source.
   - **Prose.** Compared sentence by sentence with PDF 700-701, every sentence matches:
     - the "optimum expansion" paragraph;
     - "That is,";
     - the "not equal" sentence;
     - the Where/and list;
     - the convergent/divergent paragraph;
     - the pressure-component paragraph;
     - "and to write the equation for thrust in the form";
     - the "Since the effective exhaust velocity ..." paragraph;
     - the (8) Where line;
     - "Both the engine thrust ...", with no comma after "flight forces", as printed;
     - the new top of p.514.

     All underlines are \emph: exit plane, ambient, thrust, not, backward, negative, positive (twice), increase, other than,
     flight forces, weight and drag. The quotation marks and their punctuation match the source.
   - **Equations (zoomed).** Each equation matches the source symbol by symbol:
     - (7a) is $F(t) = -\vec{c}(dm_e/dt)$. PDF 700 prints F without an arrow; it is kept plain and the note says so.
     - (7b) is $\vec{F}(t) = -\vec{c}(dm_e/dt) + (P_e - P_a)\vec{A}_e$.
     - (7c) is $\vec{c}_{\mathrm{eff}} = \vec{c} - (P_e - P_a)\vec{A}_e/(dm_e/dt)$.
     - (7d) is $\vec{F}(t) = -\vec{c}_{\mathrm{eff}}(dm_e/dt)$.
     - (8) is $m(t)(d\vec{v}/dt) = \vec{F}(t) + \vec{E}_o$.

     The pressure term follows PDF 666, with the arrow over $A_e$ only, in (7b), (7c) and twice in the prose.
   - **Mathematics.** $-\vec{c}\,\dot m + (P_e-P_a)\vec{A}_e = -[\vec{c} - (P_e-P_a)\vec{A}_e/\dot m]\,\dot m$, so (7b),
     (7c) and (7d) are consistent. With $\vec{A}_e$ pointing forward, the signs agree with the over- and underexpansion
     prose.
2. **Item 5 \ednote (E1).**
   - It names Mandell's June 1994 "Changes to text of Chapter 4" and their purpose (PDF 699), and the 1 June 1994 arrow note
     (PDF 666).
   - It says that the changes draw the arrow over the whole term, and it records the unarrowed F(t) of (7a).
   - It quotes the 1973 text, which I checked by script against git HEAD (whitespace-normalized): the paragraph from "The
     term ..." to "so we can write" is identical, and so is "Both the engine thrust ... \emph{drag}.".
   - The 1973 (8), $m(t)\frac{d\vec{v}}{dt} = \vec{F}(t) + \vec{E}$, matches PDF 545.
   - The unarrowed 1973 $E$ on PDF 546 and the unarrowed $E_o$ on PDF 701 are both stated correctly.
3. **D9 \ednote (E2).**
   - It is placed in "in the form", before (16)-(17), which is legal.
   - I redid the mathematics. (12)-(13) contain only $F_t\cos\theta$ and $F_t\sin\theta$. Substituting (9), (14) and (15)
     gives exactly the $F(t)\cos\alpha\,(\dot y/v)$ and $F(t)\cos\alpha\,(\dot x/v)$ of (16)-(17) (PDF 552). A term from
     $F_p = F(t)\sin\alpha$ would enter as $\pm F_p\sin\theta$ and $\mp F_p\cos\theta$, and no such term appears.
   - The note's "normal to the trajectory" matches the text's "perpendicular to the trajectory". The side-force argument on
     PDF 549 concerns aerodynamic force, so "without comment" holds.
   - "Neither the errata nor the supplements correct this" is accurate. The errata's Chapter 4 entries are pp. 534, 583,
     590 and 591; the 1994 changes cover pp. 513-514 and the Symbols list; the Summary covers the multistage equations.
   - The wording follows the chapter's doubt-note style.
4. **Scope.** The whole diff has three parts: header comment lines, the item 5 block and the D9 note. The 1973
   $\vec{E}$ before (7) (lines 107, 161-181) is untouched, as instructed.
5. **Labels.**
   - (7a)-(7d) are `equation*` with `\tag` and the labels `ch4:eq:n7a` to `n7d`. The aux file gives them the distinct
     anchors AMS.4-AMS.7.
   - (8) keeps `\label{ch4:eq:8}` in a numbered `equation` (equation.4.8).
6. **Section 15 notation.** These match section 15:
   - $\vec{A}_e$, $P_e$ and $P_a$ (italic letter subscripts);
   - $\vec{c}_{\mathrm{eff}}$ (upright word subscript, arrow over the letter only);
   - $\vec{E}_o$ (letter o);
   - $dm_e/dt$ and $\mdot$;
   - the plain $E_o$ on the p.514 line.
7. **Render.** The PDF was built at 18:38:13, after the last edit of the source at 18:38:08; I did not rebuild.
   - Page 5 shows (7a)-(7d), the Where/and list, the three paragraphs, (8) and note E1 in full, with the marker after
     "static test stand.".
   - Page 6 shows the (8) Where line, the new p.514 sentence and Section 1.1.
   - Page 9 shows (16)-(17) and note E2.

   There are no overfull boxes. The "Chapter ??" references are expected in a unit build. The tight spacing after the Where
   lists comes from `nosep` (STYLE.md section 4) and is not a discrepancy.

## Discrepancies

none
