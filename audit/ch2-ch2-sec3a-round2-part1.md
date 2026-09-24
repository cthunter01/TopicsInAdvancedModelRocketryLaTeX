# Audit ch2-sec3a, round 2, part 1 (scan PDF 122-135)

## 1. Scope and item counts

Scan pages: figures/pages/p122.png through p135.png, one page per Read. On p122 I checked only the
part from the heading "3. Solutions to the Dynamical Equations for Particular Cases of Interest"
down.
Render pages: build/unit/ch2-sec3a-01.png through -08.png. Page 08 is the seam: it opens with
"where tau_1 and tau_2 are called the time constants" (p136, part 2), so nothing from p134-p135 is
lost there.

Zoomed crops (build/zoom/audit_ch2-sec3a_r2_p1-*): p126 eqs. (16)-(17) (the "=" sign in (16)), and
the "5%" of render page 5.

Round 1 item re-checked:
- PDF 129, "For values of C_1, C_2, and I_L such that ...": now indented as a new paragraph in
  render page 3, as in the scan. Fixed.

Items checked:
- Headings: 3 ("3." p122, "3.1" and "3.1.1" p123). All match.
- Numbered equations: 10, (15) p124, (16) (17) (18) p126, (19) p127, (20) p129, (21) p131,
  (22) p132, (23) and (24) p134. In sequence, no offset. All match symbol by symbol.
- Unnumbered display lines: 31. p124: 1. p125: 11 (two derivatives, the three-line substitution,
  the two clipped lines, the sine/cosine pair, the divided pair). p126: 6. p127: 1. p132: 4.
  p133: 7 (including alpha_X0 = A_1). p134: 1 (Omega_X0 = A_2 - DA_1). All match.
- Unnumbered table "Present Treatment | Gurkin Report" (p129): 2 header cells, 2 rows x 3 cells.
  All match.
- Inline formulas: about 45. All match.
- Figure captions: 3 (Figure 10 p128, Figure 11 p130, Figure 12 p135). All match word for word.
- Prose: about 30 paragraphs and continuation blocks, checked sentence by sentence for wording,
  emphasis, quotation marks and paragraph breaks (indented versus flush-left continuation after
  every display).
- Editorial additions: E1 (p125, AomegaD factor), E2 (p133, "C_2/I_L" printed) and the draft note
  on the two clipped p125 lines. All three statements about the scan are true.

## 2. Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
