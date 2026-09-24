# Audit: corrections step, chapters/ch3-sec3a.tex, round 1

Unit: 3. Viscous (Skin-Friction) Drag, Sections 3.1-3.3 up to heading 3.4 (PDF 340-362, printed pp. 308-330).
Items: D11, D12, D13 (doubt notes only; no errata or supplement item falls in this unit).
Diff: `git diff HEAD -- chapters/ch3-sec3a.tex` (HEAD = 7e2087d, faithful 1973 transcription).

## Sources and their authors and dates

- 1973 errata sheet, PDF 664 (headed "ERRATA", then the book's title, authors and imprint). It shows no author of
  the sheet and no date. Its Chapter 3 entries are pp. 268, 270, 342, 364, 382, 401 and 480. None falls in
  printed pp. 308-330, so none applies to this unit (the unit header comment says so correctly).
- Chapter 3 supplement pages, PDF 688-698 (replacement pp. 356-357; Section 5.2.2; Section 5.3; symbol table;
  pp. 445, 449, 451-452). I read the top and bottom of every page and searched the PDF text layer of 688-698 for
  a name or year: none shows an author or a date. None of them touches printed pp. 308-330.
- "Neither the errata nor the supplements correct this" is therefore true for all three notes.

## What I checked

1. Scope of the diff (whole diff inspected, word diff too). The only changes are: three header comment lines;
   the `\edcap` appended inside the Plate 2 caption (the printed caption text "... $R_\ell$ of 3." is unchanged);
   an `\ednote` after "we obtain" before (55a)-(55b); an `\ednote` after "From equations (34) and (48)" before
   (60). No printed word, number or equation is altered. Labels and tags are identical to HEAD (scripted diff of
   all `\label`/`\tag`). No new equations, so no n-labels needed.
2. Placement (STYLE.md section 9). Both `\ednote`s sit in the sentence that introduces the display, outside any
   math environment. The Plate 2 note is an `\edcap` inside `\caption`, in the same form as the F1 note of the
   Figure 22 caption (ch3-sec3c-sec4a) and the Chapter 1/2 caption notes. Wording follows the Chapter 2 style
   ("... is evidently meant ... Neither the errata nor the supplements correct this; the ... is kept as printed.").
3. D11 (PDF 358-359). Scan read: (55a) "3.10 x 10^-3 sqrt(x)", (55b) "3.10 x 10^-2 sqrt(x)", (57)
   "3.22x10^-2 / sqrt(x) meters/second"; text "U = 60 meters/second (6000 centimeters/second) and nu = 1.495 x
   10^-5 meter^2/second (0.1495 cm^2/second)"; thicknesses .031, .098, .310 cm; Reynolds numbers 4.02 x 10^4,
   10^5, 10^6; "v is 0.322 meter/second". Arithmetic redone:
   - (54): 5 sqrt(1.495e-5/60) = 2.4958e-3 (m); 5 sqrt(0.1495/6000) = 2.4958e-2 (cm): note's 2.50e-3 and 2.50e-2 correct.
   - (56): 0.865 sqrt(1.495e-5 x 60) = 2.5907e-2: note's 2.59e-2 correct.
   - nu implied by 3.10e-3: 60 (3.10e-3/5)^2 = 2.306e-5; by 3.22e-2: (3.22e-2/0.865)^2/60 = 2.310e-5: note's 2.31e-5 correct.
   - thicknesses with 2.4958e-2: .0250, .0789, .2496 cm: note's ".025, .079 and .250" correct; printed .031, .098,
     .310 follow 3.10e-2 (.0310, .0980, .3100): correct.
   - v at x = 0.01 m: 0.2591 (formula) vs 0.322 (printed coefficient): note's "for 0.259" correct.
   - Reynolds numbers with the stated nu: 4.013e4, 4.013e5, 4.013e6 (printed 4.02, last digit already in D35);
     with nu = 2.31e-5 they would be 2.60e4. So "computed with it [the stated nu]" is supported.
   The note's 1973 readings of the coefficients (3.10e-3, 3.10e-2, 3.22e-2) match the scan and HEAD.
4. D12 (PDF 361). Zoomed crop of (60): the last member is "alpha U_inf sqrt(U_inf/nu x)" with no mu; the middle
   member is "mu U_inf sqrt(U_inf/nu x) . f''(0)". The next sentence says f''(0) is represented by alpha, and (61)
   begins ".332 mu b U_inf sqrt(U_inf/nu) ...". Check of (61): .332 mu b U sqrt(U/nu) x 2 sqrt(l) = .664 b U
   sqrt(mu rho l U), consistent. The note's statement of the printed form and of the intended form is accurate.
5. D13 (PDF 349). Scan read: "Plate 2: Flow about a thin plate of length l at a Reynolds number R_l of 3." The
   `\edcap` arithmetic: 5/sqrt(3) = 2.887, so delta = 5 l/sqrt(R_l) = 2.9 l ("nearly three times as thick as the
   plate is long") is correct. "the text describes a thin layer": PDF 348-349 text ("Very near the surface of the
   plate, the traces are much shorter ... this region of reduced velocity is the boundary layer"); "which
   Section 3.1 attributes to large Reynolds numbers": ch3:sec:3.1 says the influence of viscosity "in situations
   where the Reynolds number is large" is confined to a thin region near the surface. Both supported. The
   photograph shows a band of short traces next to the plate, roughly a tenth of the plate length thick at the
   trailing edge, not a region larger than the plate. "A far larger value is evidently meant" is supported and
   rightly does not guess a value.
   Patched type (item text: "check the scan before writing"). At 600 dpi (build/zoom/audit_ch3-sec3a_corr_r1-p349capC-349.png)
   "at a Reynolds number" and "R_l of 3." print lighter, and their baseline sits about 8 px (0.3 mm) lower than
   "Flow about a thin plate of length". Measured on the crop, the character pitch (~48 px) and the ascender
   height (~55 px) are the same as in the rest of the caption, so "smaller type" is not confirmed and a patch
   is not certain. Leaving the patch out of the `\edcap` is sound, since the note states only what the scan
   and the arithmetic support.
6. Section 14 notation in the notes: `\nu`, `U_\infty`, `\delta`, `v_\infty`, `R_\ell`, `\ell`, `\mu`, `\alpha`,
   `f''(0)`, `\cong`; units in prose as text ("meters/second", "meter$^{2}$/second", "cm."), leading-dot decimals
   as printed. All conform.
7. Cross-references in the notes (ch3:eq:54, 55a, 55b, 56, 57, 61, ch3:sec:3.1) are all defined within the unit.
   The build log's undefined references are all cross-unit (ch3:ref:12, ch3:ref:15, ch3:sec:2, 3.4, 3.5, etc.),
   which the standalone build tolerates. None comes from the new notes.
8. Rendered pages (build/unit/ch3-sec3a-*.png, newer than the .tex): page 5, the Plate 2 caption with the
   bracketed editor's note, typeset correctly (sqrt and cong render). Page 8, E1 mark after "we obtain", with the
   footnote starting under (55a). Page 9, Table 1 float page. Page 10, the E1 continuation, the E2 mark after
   "From equations (34) and (48)", display (60) as printed, and the E2 footnote. All render correctly. The
   E1 footnote runs across the float page, which is ordinary LaTeX behaviour and not a defect.

Side remark (outside this unit, not a discrepancy): the Status column of corrections/ch3.md still reads "note"
for D11-D13. Record the note locations there when the checklist is updated (Plate 2 caption \edcap; \ednote
before (55a); \ednote before (60)).

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| none | | | |
