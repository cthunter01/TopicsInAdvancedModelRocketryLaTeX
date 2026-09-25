# M5 audit: supplement, "Corrections to Pages 251 Through 254 and 259" (Mandell, 15 February 2022), round 1

Scan pages: PDF 683-687 (figures/pages/p683.png ... p687.png, one Read each).
**Note on p684.png:** figures/pages/p684.png is only the chart image embedded in PDF page 684 (1418 x 1020 px,
landscape). It does not show the page's text. PDF 684 is a letter-size portrait page that also carries
"[Add Figure 52 to Page 252 below Figure 51:]" above the chart, and the "Values of βc ..." paragraph and the
"Note: ..." paragraph below it. I rendered the whole page (build/zoom/audit_supp-ch2-2022_r1-full-684.png, 150 dpi)
and checked that text against the render. PDF 687 was also rendered in full (build/zoom/audit_supp-ch2-2022_r1-full-687.png).
It holds only the larger chart and no text.
Zoomed scan crops at 300 dpi: build/zoom/audit_supp-ch2-2022_r1-eq115-683.png, ...-eq116-685.png, ...-eq117-685.png,
...-ybar-685.png. PDF 280 (book page 250) was rendered to check the first editorial note (build/zoom/audit_supp-ch2-2022_r1-p-280.png).
Render: build/unit/s-ch2-2022-1.png ... -3.png, plus crops of build/unit/s-ch2-2022.pdf at 250 dpi
(build/zoom/audit_supp-ch2-2022_r1-c1eq.png, -c2txt.png, -c3eq.png). No .tex file was opened.
Other checks: I ran a word-level diff of the PDF's embedded text layer for 683-686 (drafts/p68x.txt) against
pdftotext of the unit PDF. The only differences are the expected ones: title case in the heading, "??" for
references, the two editorial notes, math-font glyphs, rejoined line breaks, and running heads and page numbers.
I also checked the label targets in the unit log, the unit .aux, and build/main.pdf for the claim in the first editorial note.

## Items checked (79)

- Heading: typescript "CORRECTIONS TO PAGES 251 THROUGH 254 AND 259" is set as the unnumbered chapter
  "Corrections to Pages 251 Through 254 and 259", which is the form the task specifies. The .aux has newlabel{supp:ch2-2022} and a TOC chapter entry.
  That is the only label in the unit, so there are no \label on the tagged equations. This is correct.
- Italic introductory paragraph, every word: "These corrections include corrections to Equations (115) and (116) to
  remove the errors reported by Alan V. Jones on February 18, 1986, the addition of Figure 52 to correct the omission
  reported by Tom on the Rocketry Forum website in 2021 and relayed to me by Dave Fitch on August 3, 2021,
  generalization of the equilibrium roll rate equation to include all fin-induced roll, the addition of Reference 12
  to Page 259, and improvements to the text." It matches and is all italic. The references go to ch2:eq:115, ch2:eq:116, ch2:fig:52 and ch2:ref:12,
  which is correct. "Page 259" is kept as printed. The upright parentheses from \eqref are not a discrepancy.
- Five centred bracketed instructions, all matching word for word and in punctuation:
  "[Replace the text on Page 251 with the following:]"; "[Add Figure 52 to Page 252 below Figure 51:]" (refs to
  ch2:fig:52 and ch2:fig:51); "[Replace the text on Page 253 / and the portion of the paragraph at the top of page 254 with
  the following:]" (two lines, lowercase "page 254" as printed); "[The remainder of the text on Page 254 is unchanged]"
  (no final punctuation, as printed); "[Add Reference 12 to the List of References on Page 259:]" (ref to ch2:ref:12).
- Prose paragraphs, every word (13): "spin in model rockets. ... direction of flight." (no indent, as printed; it continues the book's sentence);
  "A roll rate may be induced ... roll rate as" (indented, "Figure 51" is a ref to ch2:fig:51, "dispersion-reduction" and
  "aerodynamically-induced" keep their hyphens; "dispersion-reduction" is also printed mid-line on p686);
  "Values of βc ... any value of βc." ; "Note: A larger ... correction pages." (ref to ch2:fig:52); "where:"; "θ = the angle ... canted fins";
  "θ = - (α0) when roll ..."; "α0 = the angle ... presented in Reference 12." (ref to ch2:ref:12); "V = the rocket's airspeed";
  "kr, the roll forcing interference coefficient, is given by"; "and kd, the roll damping interference coefficient, is given by";
  "Ȳt is given by equation (90), ... equations (115) through (117)." (refs to ch2:eq:90, ch2:fig:36, ch2:sec:4.1, ch2:eq:115 and ch2:eq:117,
  which are Figure 36 and Section 4.1 as printed); "Given the ability ... but not over 2.0ωnc." (indented; it runs over p685-686; both
  "Figure 52" are refs to ch2:fig:52). Paragraph breaks and indents match the scan.
- Emphasis (5): the whole introductory paragraph is italic; underlined "other", "deleterious", "Note" and "Theory of Wing Sections" are set with \emph.
- Display (115), zoomed: ω_z = 6θVȲ_T(1 + λ)k_r / [(1 + 3λ)s² + 4(1 + 2λ)sr_t + 6(1 + λ)r_t²]k_d. The fraction bar spans the whole
  denominator. The subscript of Ȳ is uppercase T here, as printed. The tag (115) is at the right. Matches symbol by symbol.
- Display (116), zoomed, four lines: (1/π²){(π²/4)[(τ + 1)/τ]² + (π/τ²)[(τ² + 1)/(τ − 1)]² arcsin[(τ² − 1)/(τ² + 1)]
  − (2π/τ)(τ + 1)/(τ − 1) + [8/(τ − 1)²] ln[(τ² + 1)/(2τ)] + {(τ² + 1)/[τ(τ − 1)]}²{arcsin[(τ² − 1)/(τ² + 1)]}²
  − {4(τ + 1)/[τ(τ − 1)]} arcsin[(τ² − 1)/(τ² + 1)]}. The large outer braces open after (1/π²) and close at the end of line 4. Every
  exponent, bracket, sign and the tag (116) match. The typescript's italic "ln" is set as upright \ln, which STYLE.md section 4 requires.
- Display (117), zoomed: k_d = 1 + {[(τ − λ)/τ] − [(1 − λ)/(τ − 1)] ln(τ)} / {[(τ + 1)(τ − λ)/2] − (1 − λ)(τ³ − 1)/[3(τ − 1)]}.
  Matches, including the tag (117). The en dash in "(1 – λ)" is a minus.
- Inline math (27): I_Rω_z; β_c = ω_z/ω_nc; ζ_c ≥ 0.4472; β_c; θ (twice); θ = −(α_0); α_0; V; k_r; k_d; Ȳ_t (lowercase t as printed, zoomed; it differs
  from Ȳ_T in (115) in the typescript itself); λ; c_t/c_r; τ; (s + r_t)/r_t; ω_z (twice); ω_cres (twice, upright "cres" per STYLE.md section 13);
  β_c = ω_z/ω_nc; I_L; ζ_c; 0.44ω_nc; 1.35ω_nc; 2.0ω_nc; and in the caption AR_c and 1.25/C_1. All match. The typed lowercase roll-rate
  subscript z is kept as printed. Chapter 2's ω_Z comes from its hand-lettered form (STYLE.md section 13: typewritten subscripts keep their case).
- Figure 52: the image is figures/supplement/ch2-fig52-2022.png (1278 x 875, from PDF 687 per figures/manifest.csv; the
  pdfimages listing confirms 687 has the larger image). All of the plot is kept: y axis 0.000-0.500 with "Coupled Damping Ratio ζc",
  x axis 0.000-2.500 with "Coupled Frequency Ratio βc = (ωz/ωnc)", and the curve from about 0.45 to 1.35 with its peak near 0.445 at βc ≈ 0.78.
  The printed title inside the chart is excluded from the crop and typed below as the caption
  "Figure 52: Roll Rates to Avoid to Keep AR_c from Exceeding 1.25/C_1". It matches the printed "Figure 52: Roll Rates to Avoid to Keep ARc
  from Exceeding 1.25/C1", with AR_c as \mathit{AR}_c per STYLE.md section 13.
- Editorial note 1, after "spin in model rockets.": "Page 251 of the 1973 edition begins in mid-sentence; page 250 ends 'Stabilization is not,
  however, the only motive for inducing'. The corrected text is in Section ??" (ref ch2:sec:6.3). **True.** PDF 280, book page 250, ends with exactly that
  sentence fragment, and PDF 281 begins "-251- spin in model rockets." build/main.pdf shows the corrected text in Chapter 2 section 6.3, "Rolling Rockets".
- Editorial note 2, after the "Note:" paragraph: "The image above is taken from that larger copy, which follows these pages in the source scan
  (its page 687); it is not repeated here." **True.** The crop is from PDF 687, and 687 follows 683-686.
- PDF 687 (the larger copy of Figure 52) is not set again, as the task requires.
- Reference 12: "12. Abbott, Ira H., and Von Doenhoff, Albert E., Theory of Wing Sections, Dover Publications, Inc., New York, 1959." Matches,
  with the title in \emph. The hanging indent of the enumerate is layout only.
- Signature and date: "Gordon K. Mandell" / "February 15, 2022" on two lines, flush left. Matches.
- Cross-references (18 in the unit log), all to the correct chapter 2 targets: eq:115 (twice), eq:116, eq:117, eq:90, fig:51 (twice),
  fig:52 (six times), fig:36, sec:4.1, sec:6.3 and ref:12 (three times). All of these labels exist in chapters/*.tex (grep of \label only).
- The "%" in "25%" was checked with pdftotext. It is a plain percent sign; at low resolution the Termes glyph only looks like "‰".

Not discrepancies: the running heads and page numbers of the standalone class; "??" for chapter references; the caption set below the
image instead of above it (project convention); rejoined line breaks; the wider spacing around "=" on a justified line in "Values of βc = ωz/ωnc".

## Discrepancies

none

| where | scan reading | compiled reading | severity |
|-------|--------------|------------------|----------|
| none  |              |                  |          |
