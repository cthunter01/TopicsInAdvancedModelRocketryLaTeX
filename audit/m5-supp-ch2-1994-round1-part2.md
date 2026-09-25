# M5 audit: supplement, 1994 Chapter 2 documents, round 1, part 2

Scan pages: PDF 680, 681, 682 (plus PDF 224 for the 1973 Figure 36 and its caption; PDF 683-686
consulted only to check the statements of the editorial note). Render: build/unit/s-ch2-1994-4.png
to -8.png (render page 4 is the neighbour page, the end of the fin-equations document; pages 5-8 carry
this part's content). Zoomed crops: build/zoom/audit_supp-ch2-1994_r1_p2-*.png (scan at 300 and 600
dpi; render at 250 dpi).

## Items checked

New Figure 36 (PDF 680 -> render p. 5)
- Heading "New Figure 36" (editorial heading; the scan has none).
- Image figures/supplement/ch2-fig36-1994.png present and complete: s, Z_T, C_r/2, Z-bar_T(B),
  C.P._T(B), Gamma_c, C.P._T, C_r, Y-bar_T, l (script), C_t/2, C_t, "Rocket centerline", r_t,
  AR = 4s/(C_r + C_t).
- Caption, word by word: "Figure 36: Notation used in determining the normal force curve slope and
  center of pressure location of single fins and symmetrical fin assemblies. Z_T is the distance from
  the tip of the rocket's nose to the intersection of the fin root and the fin leading edge.
  Z-bar_T(B) is the distance from the nose tip to the center of pressure of the fin assembly. l is the
  distance from the midpoint of the fin root chord to the midpoint of the fin tip chord. The definition
  of AR, the aspect ratio of a pair of fins joined at the root to create a "wing" of span 2s, is also
  given." Underlined "aspect ratio" -> emphasis; AR ligature; script l -> \ell; bar over Z only;
  subscript T(B). The typist's stray underscore in "rocket's_nose" silently dropped (typing slip).
  All match.

1973 Figure 36 (render p. 6, checked against PDF 224)
- \edcap line "[Editor's note: The 1973 Figure 36, which this figure replaces:]" present; statement true.
- Image figures/ch2/fig36.png present and complete (AR = 2s/(C_r + C_t), no l marked).
- Caption: "Figure 36: Notation used in determining the normal force coefficient and center of pressure
  location of single fins and symmetrical fin assemblies. Z_T is the distance from the tip of the nose to
  the intersection of the fin root and leading edge; Z-bar_T(B) is the distance from the nose tip to the
  center of pressure of the fin assembly. The definition of AR, the aspect ratio of a single fin, is also
  given." Matches PDF 224 word for word, including the semicolon and the emphasis.

Handwritten correction of (115)-(117) (PDF 681-682 -> render pp. 7-8)
- Heading "Handwritten Corrections to Equations (115) Through (117)" (editorial; the scan has none).
- Head \edcap: superseded by Mandell's corrections of 15 February 2022, which come next; not applied in
  Chapter 2, which uses the 2022 text; corrected equations agree with the 2022 ones. Verified: PDF 686
  is signed "Gordon K. Mandell / February 15, 2022"; the 2022 (115) on PDF 683 is
  6 theta V Y-bar_T (1+lambda) k_r / {[(1+3lambda)s^2 + 4(1+2lambda)s r_t + 6(1+lambda)r_t^2] k_d},
  the 2022 (116) and (117) on PDF 685 match the 1994 forms; Chapter 2 (build/main.pdf) prints the 2022
  (115) with an editorial note naming the 2022 correction. Statement true.
- Prose (all-caps hand lettering set in sentence case): every word of "Equation (115) on page 251 should
  read", "Note that A_f, the planform area of one fin, ... (ref. pg. 187). Y-bar_T, s, c_r, and r_t are
  illustrated in Figure 36 on page 194, along with the fin chord c_t at the fin tip. The value of
  Y-bar_T is given by equation (90) on page 196 as", "and lambda is given on page 253 as", "Aside from
  the error it contains, equation (115) could have (and should have) been written in a more convenient
  form that does not give the impression of an inverse dependence of omega_Z on c_r. Noting that", "one
  can write equation (115) as", "Equation (116) on page 253, which defines the roll forcing interference
  coefficient k_r, also contains an error. Equation (116) should read", "The error in the book consisted
  of omitting a superscript 2 in the second term. The term given as", "on page 253 should read",
  "where", "The roll damping interference coefficient k_d is given correctly by equation (117) on page
  253 as". Quotation marks around "reference area", parentheses, commas and full stops all match.
- References: the "??" in the standalone build resolve (per the log) to ch2:eq:115 (x3), ch2:fig:36,
  ch2:eq:90, ch2:eq:116 (x2), ch2:eq:117 and ch2. ch2:eq:90 is the 1973 Y-bar_T equation (main.pdf
  prints it as (90)), matching "equation (90) on page 196". Printed page citations kept.
- Displays, symbol by symbol (scan zoomed at 300/600 dpi):
  - omega_Z = 12 theta V A_f Y-bar_T k_r / (s c_r k_d [(1+3lambda)s^2 + 4(1+2lambda)s r_t
    + 6(1+lambda)r_t^2]): subscript of Y-bar confirmed T at 600 dpi; the crossed z is set Z per STYLE.md
    section 13. Match.
  - Y-bar_T = r_t + (s/3)[(c_r + 2c_t)/(c_r + c_t)]: match (no end punctuation in scan or render).
  - lambda = c_t/c_r. (with full stop): match.
  - A_f = s((c_r + c_t)/2) = (s c_r/2)(1+lambda): match.
  - omega_Z = 6 theta V Y-bar_T (1+lambda) k_r / ([(1+3lambda)s^2 + 4(1+2lambda)s r_t + 6(1+lambda)r_t^2]
    k_d): match.
  - k_r = (1/pi^2){(pi^2/4)((tau+1)/tau)^2 + (pi/tau^2)((tau^2+1)/(tau-1))^2 arcsin((tau^2-1)/(tau^2+1))
    - (2pi/tau)((tau+1)/(tau-1)) + (8/(tau-1)^2) ln((tau^2+1)/(2tau)) + [(tau^2+1)/(tau(tau-1))]^2
    [arcsin((tau^2-1)/(tau^2+1))]^2 - (4(tau+1)/(tau(tau-1))) arcsin((tau^2-1)/(tau^2+1))}: all signs,
    exponents, bracket types and the brace extent match; two-line break as in the scan.
  - term "given as" (pi/tau^2)((tau+1)/(tau-1))^2 arcsin((tau^2-1)/(tau^2+1)) and "should read"
    (pi/tau^2)((tau^2+1)/(tau-1))^2 arcsin((tau^2-1)/(tau^2+1)): match.
  - tau = (s + r_t)/r_t. (with full stop): match.
  - k_d = 1 + [(tau-lambda)/tau - ((1-lambda)/(tau-1)) ln tau] / [(tau+1)(tau-lambda)/2
    - (1-lambda)(tau^3-1)/(3(tau-1))]: match (no end punctuation in scan or render).
- Page number "-2-" on PDF 682 not transcribed (correct).

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 681, sentence after the first display (render p. 7, "Note that A_f, the planform area ...") | "NOTE THAT Af, ..." begins a new sentence at the left margin after the display of (115), set off by the same blank space as the other new sentences after displays ("ASIDE FROM ...", "EQUATION (116) ...", "THE ERROR IN THE BOOK ...", "THE ROLL DAMPING ..."), which the render all starts as new indented paragraphs | "Note that ..." is set as an unindented continuation of the paragraph ending in "should read" (no paragraph break), unlike every other sentence-initial line after a display in this document | layout |
