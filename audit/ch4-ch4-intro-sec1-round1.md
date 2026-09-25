# Audit: ch4-intro-sec1, round 1

## (1) Pages and items checked

- Scan pages: PDF 537-552 (figures/pages/p537.png ... p552.png), each read in full; zoomed crops (300 dpi) of
  p542 eq (2), p545 eqs (6)-(7), p550 eqs (12)-(15), p552 line 1 (the typed x-double-dot) and eqs (16)-(17).
- Render: build/unit/ch4-intro-sec1-1.png ... -7.png (7 pages), plus 250 dpi crops of the compiled PDF's pages 2 and 4-6
  for the displays. I also ran a word-level diff of the compiled text against the OCR layer of PDF 537-552. Every
  difference it found was OCR noise, math or page and equation numbers.
- Headings (4): Introduction (unnumbered, 537), 1. (541), 1.1 (546), 1.2 (549, two lines). The running title
  on 537 is not transcribed, as intended.
- Numbered equations (17): (1)-(17). Each was checked symbol by symbol (arrows, subscripts e/E, signs, brackets,
  fractions, dots), along with its number and its place in the sequence. (9)-(11) are typed; the rest are hand-lettered. The survey's
  page list is right: (1) 541, (2)-(3) 542, (4)-(5) 544, (6)-(8) 545, (9)-(10) 547, (11) 548, (12)-(15) 550,
  (16)-(17) 552, above the "2." heading.
- Unnumbered displays (2): dp = m(t)dv - v dm_e - dm_e dv (542) and dp = dp_E - dp_e (545), plus the connective
  "or" before (6).
- Figure captions (2): Figure 1 (543, with the panel (a)/(b) wording) and Figure 2 (551, with the italic trajectory/range/altitude).
- Inline math: (F = ma) with arrows, v, E, dv, v + dv, dm_e, m(t) - dm_e, dp, dp_e, dp_E, (c + v), E dt,
  -c(dm_e/dt), m-dot, F(t), plain E on 546, F(t), alpha, m(t)g, kv^2, k, epsilon, f(alpha), x-dot, y-dot,
  dx/dt, x-double-dot, d^2x/dt^2, theta, v.
- Prose: every sentence on 537-552. I checked wording, the paragraph breaks (including the flush-left continuations after
  displays and at page tops on 539 and 542, and the sentences joined across the short page 546/547), and every underlined emphasis (vanishingly,
  size, number, increases, thousands, closed-form, differential x2, linearization, change of variable,
  estimation, truncation of integrals, results, conserved, system, flux, exhaust velocity, rocket, from, to,
  added x2, subtracted x2, impulse, thrust, backward, negative, positive x2, increase, flight forces, weight,
  drag, external, net forces acting on the rocket's center of mass, coupled to, and the long phrase on 552).
  "Handbook of Model Rocketry" is italic both times. Chapter cross-references print "??" (standalone build), which is intended.
- Tables: none in this unit. There are no draft notes or editorial notes in the render.
- Numbering offset: none. The equations run 1-17 and the figures 1-2, as in the book.
- Survey (build/ch4-notes/ch4-intro-sec1.md): confirmed. One small inaccuracy: the line-end hyphen "rigid-/body"
  also occurs on 547 (and "repre-/sentation" on 549), not only on 548. The compiled text handles both correctly.

## (2) Discrepancies

none
