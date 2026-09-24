# Audit: ch3-symbols corrections, round 2

Unit: `chapters/ch3-symbols.tex` (Chapter 3 Symbols list, PDF 293-300, printed pp. 263-270).
Baseline: git HEAD 7e2087d (the faithful 1973 transcription). Diff: `git diff HEAD -- chapters/ch3-symbols.tex`.
Rendered pages: `build/unit/ch3-symbols-1.png` to `-5.png`, built at 09:42:58, after the last edit of the .tex at
09:42:56. I did not rebuild them. The build log has no overfull or underfull boxes. Its only warnings are
undefined references to other units (ch3:eq:146, ch3:sec:5.2.2, ch3:sec:5.3, ch3:eq:27, ch3:eq:33, ch3:fig:11,
ch4, ch3:ref:3); a standalone unit build always leaves these undefined. Each of these labels exists in its own unit
(grep of chapters/).

## Sources read, with author and date

- PDF 664, errata sheet headed "ERRATA / TOPICS IN ADVANCED MODEL ROCKETRY by Gordon K. Mandell, George J.
  Caporaso, and William P. Bengen (Cambridge, Massachusetts: The MIT Press, 1973)". The sheet itself shows no
  author and no date. PDF 665 is a second typing of the same list ("Errata"), also with no author or date. It
  gives the infinity entry as "page 270, line 14", which is the last line.
  - Zoomed crop `build/zoom/audit_ch3-symbols_r2-p664n.png`: the mark over the n on PDF 664 is a small arrow.
    PDF 665 draws a clear arrow. So the symbol is `\vec{n}`.
- PDF 694, "Corrections and additions to symbol table of Chapter 3": no author, no date.
- PDF 688-698: montage of the top and bottom strips in `build/zoom/audit_ch3-symbols_r2-strips.png`. These pages
  carry only page headers (-356-, -357-, -445-, -449-, -451-, -452-) and the page numbers 2 and 3 on PDF 692-693.
  None shows an author, date or signature.
- PDF 690 (e = 0.863, (144A)-(144B)) and PDF 692 ((154)-(156), Δα, the twist and cant coefficients), read to check
  what the notes say about them.
- 1973 pages:
  - PDF 293-294: the C_D block and the 1973 meaning of (C_Di')_cant.
  - PDF 297: d_r is followed by f( ); there is no e.
  - PDF 298: n and t, both printed without an arrow.
  - PDF 299: the Greek block; there is no Δα.
  - PDF 300: the last line, "infinity", has an empty Symbol cell.
  - PDF 336, 337 and 340: (27), the Figure 11 caption and (33), each with an arrowed t.

## Round 1 finding (order of the C_D additions): verified fixed

The C_D block now reads C_Di, **ΔC_Di**, C_Di', (C_Di')_cant, **(ΔC_Di)_cant**, **(C_Di)_twist**,
**(C_Di')_twist**, **(ΔC_D)_cant**, (C_D)_lug. This is the order round 1 asked for. It follows the two patterns the
1973 list shows:

1. A Δ form stands next to its base: C_Df, ΔC_Df, C_Df' (PDF 293).
2. Entries are grouped by outer subscript, with the Δ form after the primed one: (C_f)_lam, (C_f')_lam,
   (ΔC_f)_lam, then the turb group (PDF 294).

(ΔC_D)_cant comes before (C_D)_lug, since cant sorts before lug. The 1973 list is not fully consistent (ΔC_f sits
between (C_f)_B and (C_f)_F), so the order chosen is defensible, and the header comment (lines 2-9) describes it
accurately.

The one note for the additions has moved to the new first added row, ΔC_Di. It is now an hbox-cell `\ednote`
(`\multicolumn{1}{l@{}}{...}`, the chapters/ch1-symbols.tex form, legal under STYLE.md section 9). It renders as E1
on page 1, and its text reaches the footnote.

## What was checked

1. **Item 1** (errata, p. 268 line 3). Counting the Symbol/Meaning head as line 1, line 3 is the "unit normal
   vector" row. That row is now `$\vec{n}$`, applied silently as decided, and page 3 renders the arrow.
2. **Item 2** (errata, p. 270, last line). The row is now `$\infty$ & infinity`, and the comment that said the cell
   is empty as printed has been removed. Applied silently; page 5 renders it.
3. **Item 11** (PDF 694). All eight meanings match the supplement word for word, including "cross-sectional" and the
   quoted ``lift''.
   - (C_Di')_cant is the only entry that exists in 1973. Its meaning is replaced, and note E2 quotes the 1973 meaning
     exactly ("increase in drag coefficient due to canting of fins", PDF 294).
   - E2 also says (ΔC_D)_cant = (C_Di')_cant + (C_Di')_twist + (ΔC_Di)_cant. This is (156) on PDF 692, and the
     arithmetic checks: 2(8.38) = 16.76, and 13.02 + 16.76 = 29.78.
   - ΔC_Di is not in the 1973 list, so it is added, not replaced. The other six are also absent in 1973.
   - E1 names all seven additions. Each of its statements holds:
     - ΔC_Di is defined in the 1973 text by (146) (HEAD ch3-sec5b.tex, line 18).
     - e is in the corrected Section 5.2.2 (PDF 690).
     - The twist coefficients, (ΔC_Di)_cant, (ΔC_D)_cant and Δα are in the corrected Section 5.3 (PDF 691-692).
       Section 5.3 is labelled ch3:sec:5.3, "Drag Due to Rotation", and contains (152)-(156).
     - A grep of every HEAD ch3 unit finds none of these symbols in the 1973 text, apart from (C_Di')_cant.
   - Placement:
     - e comes after d_r, before f( ) (PDF 297).
     - Δα comes after ᾱ, as ΔV follows the decorated V-vector in the 1973 list (PDF 297) and Δρ follows ρ (PDF 299).
   - All eight symbols use the section 14 forms the item specifies. `(\Delta C_D)_{\mathrm{cant}}` renders the same
     as the `(\Delta\CD)_{\mathrm{cant}}` of ch3-sec5b.
4. **D2** (unit tangent vector t). The note E3 is an hbox cell and renders on page 4. Each of its statements is
   supported by the scan:
   - PDF 298 prints t without an arrow, the same as the "time; also fin thickness" row above it.
   - (27) (PDF 336), (33) (PDF 340) and the Figure 11 caption (PDF 337) all draw the arrow over t.
   - The errata marks only the n, and PDF 694 has no t entry.

   The closing sentence follows the Chapter 2 style decided in corrections/ch3.md.
5. **Scope.** The whole diff consists of:
   - the header comment;
   - the added row ΔC_Di (with E1);
   - the corrected (C_Di')_cant row (with E2);
   - the four added rows after it;
   - e and Δα;
   - the n row, the t row (with E3) and the infinity row, with the old comment removed.

   Nothing else changed.
6. **Labels.** The unit adds no equations. ch3:sec:symbols is unchanged.
7. **Renders.** Pages 1, 3, 4 and 5 show every corrected passage correctly. The hbox cells stay on one line
   within the column.

## Discrepancies

none
