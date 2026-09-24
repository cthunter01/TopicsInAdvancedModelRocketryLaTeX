# Audit: ch3-symbols corrections, round 1

Unit: `chapters/ch3-symbols.tex` (Chapter 3 Symbols list, PDF 293-300, printed pp. 263-270).
Baseline: git HEAD 7e2087d (faithful 1973 transcription). Diff: `git diff HEAD -- chapters/ch3-symbols.tex`.
Rendered pages checked: `build/unit/ch3-symbols-1.png` to `-5.png` (built 09:36:15, after the last edit of the
.tex at 09:36:06; not rebuilt). The build log has no overfull or underfull boxes; the only warnings are the
cross-unit references (ch3:sec:5.3, ch3:sec:5.2.2, ch3:eq:146, ch3:eq:27, ch3:eq:33, ch3:fig:11, ch4,
ch3:ref:3), which the standalone unit build is expected to leave undefined. All of these labels exist in
the other units.

## Sources read, with author and date

- PDF 664, errata sheet ("ERRATA / TOPICS IN ADVANCED MODEL ROCKETRY by Gordon K. Mandell, George J.
  Caporaso, and William P. Bengen (Cambridge, Massachusetts: The MIT Press, 1973)"). The sheet has no author
  and no date of its own; the heading names the book and its authors. PDF 665 is a second typing of the same
  list, also without author or date. The mark over the n on both is an arrow (on PDF 665 it is a clear
  arrow; on PDF 664 a harpoon-like arrow, checked in a zoomed crop). That makes it `\vec{n}`, not a hat.
- PDF 694, "Corrections and additions to symbol table of Chapter 3": no author, no date.
- PDF 690 (Section 5.2.2, e = 0.863) and PDF 691-693 (Section 5.3, (152)-(156)) were read to check what
  the notes say about them. Neither shows an author or a date (PDF 692-693 carry only the page numbers 2 and 3).
  The top and bottom strips of PDF 688-698 show no author, date or signature, only page headers
  (-356-, -357-, -445-, -449-, -451-, -452-).
- 1973 pages: PDF 293 and 294 (the C_D block; the 1973 (C_Di')_cant meaning), 297 (d_r is followed directly
  by f( ), so there is no e), 298 (n and t, both printed plain), 299 (Greek block: no Δα), 300 (last line
  "infinity" with an empty Symbol cell); PDF 336 ((26)-(27)), 337 (Figure 11 caption), 340 ((33)).

## What was checked

1. **Item 1 (errata, p. 268 line 3).** Line 3 of PDF 298 counts the "Symbol / Meaning" head as line 1,
   so it is the "unit normal vector" row. That row is now `$\vec{n}$ & unit normal vector`, applied
   silently as decided. The rendered page 3 shows the arrowed n. Correct.
2. **Item 2 (errata, p. 270 last line).** The row is now `$\infty$ & infinity`, and the comment saying the
   cell is empty as printed is removed. Rendered on page 5. Correct and silent.
3. **Item 11 (PDF 694).** The file matches the supplement's eight meanings word for word (including
   "cross-sectional" and the quoted ``lift''). Each was compared with the 1973 list (PDF 293-300):
   - `(C_{Di}')_{\mathrm{cant}}` is the only entry that already exists. Its meaning is replaced with "increase in
     induced drag coefficient due to canting of fins". The `\ednote` quotes the 1973 meaning exactly
     ("increase in drag coefficient due to canting of fins", PDF 294). Its added sentence, that
     (ΔC_D)_cant = (C_Di')_cant + (C_Di')_twist + (ΔC_Di)_cant, is exactly (156) on PDF 692. The note uses the
     legal hbox cell `\multicolumn{1}{l@{}}{...}`, and its text reaches the footnote (E1) on the rendered page 1.
   - ΔC_Di is not in the 1973 list (PDF 293-294 have C_Di, C_Di', (C_Di')_cant and no ΔC_Di). It is therefore
     added, correctly, not replaced. The other six are also absent in 1973 and are added.
   - There is ONE note for the additions: an `\edcap` on the first added row, (C_Di)_twist. It is legal in a
     `p{}` cell (STYLE.md section 9) and names all seven added symbols. Its statements check out. They are
     absent from the 1973 list. ΔC_Di is defined in the 1973 text by (146), as HEAD sec5b shows. e is in the
     corrected Section 5.2.2 ((144A)-(144B) and the constant, PDF 690). (C_Di)_twist, (C_Di')_twist,
     (ΔC_Di)_cant, (ΔC_D)_cant and Δα are in the corrected Section 5.3 (PDF 691-692). None of the twist, Δα
     or (ΔC_D)_cant symbols occurs anywhere in the 1973 Chapter 3 text (grep of all HEAD ch3 units).
   - Blocks: e is in the lowercase block after d_r, where alphabetical order puts it. Δα is in the Greek
     block after ᾱ, consistent with the book's placing of Δ forms after their base (ΔV, Δρ). The C_D
     additions are in the C_D block, but their order inside it is the supplement's order, not the list's
     (see the table).
   - Section 14 forms: all eight symbols are set as the item specifies. `(\Delta C_D)_{\mathrm{cant}}` renders
     the same as the `(\Delta\CD)_{\mathrm{cant}}` of ch3-sec5b.
4. **D2 note (unit tangent vector t).** The hbox-cell `\ednote` (E2) renders in the footnote on page 4.
   Checked against the scan: PDF 298 prints t plain, the same as the "time; also fin thickness" row above.
   (27) on PDF 336, (33) on PDF 340 and the Figure 11 caption on PDF 337 all draw the arrow over t. The
   errata marks only the n. The closing "Neither the errata nor the supplements correct this; the symbol is
   kept as printed" matches the Chapter 2 style decided in corrections/ch3.md. The note is accurate.
5. **Scope.** The whole diff changes only the header comment (new lines 2-7), the (C_Di')_cant row, the
   seven added rows, the n row, the t row and the last row (plus the removed comment). Nothing outside the
   items changed.
6. **Labels.** None are involved: the unit adds no equations, and ch3:sec:symbols is unchanged.
7. **Arithmetic.** No figures are asserted in this unit's notes. (156) was checked as a sum of three
   terms: 13.02 + 16.76 = 29.78 for the ᾱ² coefficient, which agrees with PDF 692.
8. **Checklist.** corrections/ch3.md still shows items 1, 2 and 11 and D2 as "todo". The other units
   already corrected are also still "todo" there, so status is apparently updated at assembly. This is not
   counted as a discrepancy for this unit.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| ch3-symbols.tex lines 33-37 (order of the C_D additions) and the header comment line 4 | Item 11 asks for the additions in the list's (alphabetical) order, and the checklist says "in the book's order". The 1973 list puts a Δ form next to its base (ΔC_Df between C_Df and C_Df', PDF 293) and groups entries by outer subscript ((C_f)_lam, (C_f')_lam, (ΔC_f)_lam, then the turb group, PDF 294). That gives C_Di, **ΔC_Di**, C_Di', (C_Di')_cant, **(ΔC_Di)_cant**, **(C_Di)_twist**, **(C_Di')_twist**, **(ΔC_D)_cant**, (C_D)_lug. The one `\edcap` for the additions then moves to the new first added row, ΔC_Di (or becomes an hbox `\ednote` there, since that meaning is short). | The supplement's order is copied as one block after (C_Di')_cant: (C_Di)_twist, (C_Di')_twist, ΔC_Di, (ΔC_Di)_cant, (ΔC_D)_cant. ΔC_Di sits after the twist entries, away from its base C_Di, and (ΔC_Di)_cant is split from (C_Di')_cant by the twist rows. | layout (minor) |

No other discrepancies. Items 1 and 2 are correct and silent. All eight item-11 meanings and the 1973 quote
are exact. The D2 note is accurate and legally placed, and the renders are correct.
