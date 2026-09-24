# Audit ch2-sec3b, round 2, part 1 (scan PDF 149-158)

## (1) Scope and item counts

Scan pages checked: figures/pages/p149.png (only from the 3.1.3 heading at the foot of the page) through
figures/pages/p158.png, one page per Read. Zoomed crops (build/zoom/audit_ch2-sec3b_r2_p1-*) were rendered
of the impulse-definition display on PDF 150 (scan at 300, 600 and 1200 dpi, and the compiled PDF at 600 dpi)
to confirm the condition glyph: the scan prints ">" over "<" (\gtrless), and so does the render.

Render pages compared: build/unit/ch2-sec3b-01.png to -06.png. Page 1 opens with the 3.1.3 heading (nothing
from the previous unit), page 5 carries the end of PDF 158 ("which gives us") and the start of PDF 159, and
page 6 holds only PDF 159+ material (seam check; nothing from my pages spills onto it).

Round-1 item re-checked:
- PDF 150, "While there are more rigorous definitions of impulse inputs ...": now set flush left, continuing
  the paragraph that ends "may be defined as follows:" (render page 1). Fixed, correct.

Full re-check:
- Headings: 1 (3.1.3 Complete Response to Impulse Input); matches.
- Numbered equations: 9, in sequence with no offset: (37a), (37b) PDF 154; (38) PDF 154; (39), (40) PDF 156;
  (41a), (41b), (42a), (42b) PDF 158. Checked symbol by symbol (signs, subscripts X0/L/Xm/m, tau1/tau2
  placement, exponents -Dt, -t/tau1, -t/tau2, -(D/omega) arctan(omega/D), fractions, square brackets, "e"
  in I_L D e).
- Unnumbered displays: 13 (three-line impulse definition with (t gtrless 0), (t = 0), (t = 0); omega = Mt/I;
  alpha = (1/2)(M/I)t^2; omega = H/I; alpha = (H/2I)t; Omega_X = H/I_L; phi = arctan(0) = 0;
  A = H/(I_L omega); critically damped A_1 = 0, A_2 = H/I_L; overdamped A_1, A_2 (minus sign on A_2 only);
  the underdamped, critically damped and overdamped zero-velocity equations, including the "t" in the
  overdamped numerators tH tau_2 and tH tau_1). All match.
- Connective lines ("from which we obtain", "so that", "from which", "and", "which gives us"): 5; match.
- Figure captions: 4 (Figures 20, 21, 22, 23), compared word by word; all match.
- Prose: about 28 paragraphs and continuation blocks compared sentence by sentence (wording, italics for
  underlining including "impulse of strength H", "in such a way that ... remains constant", "limiting
  arguments", "singularity functions", "strong", "short", "not", "finite", "homogeneous"; quotes; em dashes
  in the Figure 20 caption; "??" for Section 3.1.2, Figure 5 and equations (15)-(19), (16), (17), (22),
  (23), (24)-(26), (25), all in other units; "occured" silently corrected). About 35 inline formulas checked.
  Paragraph indents and flush continuations after displays all match the scan.

## (2) Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
