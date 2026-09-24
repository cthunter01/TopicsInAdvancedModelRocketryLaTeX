# Audit ch2-sec3d, round 2, part 1

## Scope checked

- Scan pages: PDF 193 (from heading 3.2.2 on), 194, 195, 196, 197, 198, 199, 200, 201, 202, 203 (11 pages).
- Render pages read: build/unit/ch2-sec3d-01.png to -07.png (01 to 06 carry this content; 07 is the seam page).
- Headings: 3 (3.2.2, 3.2.3, 3.2.4, the last printed over two lines).
- Numbered equations: 12, namely (61), (62a), (62b), (63a), (63b), (64a), (64b), (65a), (65b), (66a), (66b), (67). All are in the right order and their numbers match the book, with no offset.
- Unnumbered displays: 20, checked symbol by symbol:
  - p194: 3
  - p195: 3
  - p196: 3
  - p197: 1
  - p199: 2
  - p202: 4
  - p203: 4
- Captions: 2 (Figure 28, Figure 29), checked word by word.
- Prose: every paragraph, inline formula, cross-reference ("??") and paragraph break on these pages.
- Zoomed scan crops were checked for:
  - p195: the leading minus in -M_s/C_1 and the Omega_X0 / Omega_Y0 lines
  - p199: A_1 sin/cos phi_1 with H/I_L
  - p203: the "we can obtain" pair and the pair after "from the first relation above"

## Round 1 items re-verified

- PDF 202, "The dynamical equations that must be solved become, in this case,": now indented as a new paragraph after the f_x(t), f_y(t) display, as in the scan. Fixed.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
