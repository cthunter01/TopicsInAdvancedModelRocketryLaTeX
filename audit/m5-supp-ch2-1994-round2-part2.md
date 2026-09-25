# M5 audit: supplement, 1994 Chapter 2 documents, round 2, part 2 (PDF 680-682)

Scan pages checked: figures/pages/p680.png, p681.png and p682.png, with zoomed 300 dpi crops of the
p680 caption, every p681 display and every p682 display (build/zoom/audit_supp-ch2-1994_r2_p2-*).
I also checked PDF 224, the 1973 Figure 36 and its caption, against the edcap block on render p. 6.
To check the edcap statements I compared the 2022 corrections (PDF 683, 685 and the 15 February 2022 signature on 686).

Render pages checked: build/unit/s-ch2-1994-4.png through -8.png. These PNGs are newer than the
current .tex file (19:27:45 against 19:27:37). I also made 250 dpi crops of pages 7 and 8 of
build/unit/s-ch2-1994.pdf.

## Round-1 item

- PDF 681, "Note that A_f, the planform area ...": this now starts a new indented paragraph after
  the display of (115), matching the other sentences that begin after a display. **Fixed; verified.**

## Items checked

- PDF 680, render pp. 5-6 (supp:ch2-fig36): the heading "New Figure 36" is editorial because the
  scan prints no heading. The 1994 figure image (figures/supplement/ch2-fig36-1994.png) is present
  and complete: AR = 4s/(c_r+c_t), the ℓ dimension line, C.P.T(B) and C.P.T, Ȳ_T, r_t, c_r/2 and c_t/2.
  The caption matches word for word: "Figure 36: Notation used in ... normal force curve slope ...
  Z_T ... rocket's nose ... fin root and the fin leading edge. Z̄_T(B) ... ℓ is the distance ... tip
  chord. The definition of AR, the *aspect ratio* (underlined in the scan) of a pair of fins joined at
  the root to create a "wing" of span 2s, is also given." The stray underscore in "rocket's_nose" is a
  typing mark and is correctly not transcribed.
- The edcap "The 1973 Figure 36, which this figure replaces:" is true. It is followed by the 1973
  image (2s/(c_r+c_t), no ℓ) and the 1973 caption, which matches PDF 224 word for word ("normal force
  coefficient ... tip of the nose ... fin root and leading edge; Z̄_T(B) ... *aspect ratio* of a single
  fin, is also given.").
- PDF 681-682, render pp. 7-8 (supp:ch2-115-1994), head edcap. "Superseded by Mandell's corrections of
  15 February 2022" is true: PDF 686 is signed February 15, 2022. "Its corrected equations agree with
  the 2022 ones" is also true: the final (115) form, (116) and (117) are the same as the 2022 (115),
  (116) and (117) on PDF 683 and 685.
- The prose matches every word of the scan: "Equation (115) on page 251 should read"; "Note that ...
  (ref. pg. 187). Ȳ_T, s, c_r, and r_t are illustrated in Figure 36 on page 194, along with the fin
  chord c_t at the fin tip. The value of Ȳ_T is given by equation (90) on page 196 as"; "and λ is given
  on page 253 as"; "Aside from ... ω_Z on c_r. Noting that"; "one can write equation (115) as";
  "Equation (116) on page 253, which defines the roll forcing interference coefficient k_r, also
  contains an error. Equation (116) should read"; "The error in the book consisted of omitting a
  superscript 2 in the second term. The term given as"; "on page 253 should read"; "where"; "The roll
  damping interference coefficient k_d is given correctly by equation (117) on page 253 as". The
  equation and figure references show "??" in the standalone build, which is expected. The scan's
  printed page numbers are kept.
- I checked the displays symbol by symbol:
  - ω_Z = 12θVA_fȲ_Tk_r / (s c_r k_d[(1+3λ)s² + 4(1+2λ)s r_t + 6(1+λ)r_t²])
  - Ȳ_T = r_t + (s/3)[(c_r+2c_t)/(c_r+c_t)]
  - λ = c_t/c_r., with the period as printed
  - A_f = s((c_r+c_t)/2) = (s c_r/2)(1+λ)
  - ω_Z = 6θVȲ_T(1+λ)k_r / ([(1+3λ)s² + 4(1+2λ)s r_t + 6(1+λ)r_t²]k_d)
  - k_r = (1/π²){(π²/4)((τ+1)/τ)² + (π/τ²)((τ²+1)/(τ−1))² arcsin((τ²−1)/(τ²+1))
    − (2π/τ)((τ+1)/(τ−1)) + (8/(τ−1)²) ln((τ²+1)/(2τ)) + [(τ²+1)/(τ(τ−1))]²[arcsin((τ²−1)/(τ²+1))]²
    − (4(τ+1)/(τ(τ−1))) arcsin((τ²−1)/(τ²+1))}
  - the old term (π/τ²)((τ+1)/(τ−1))² arcsin(...) and the corrected term (π/τ²)((τ²+1)/(τ−1))² arcsin(...)
  - τ = (s+r_t)/r_t., with the period as printed
  - k_d = 1 + [(τ−λ)/τ − ((1−λ)/(τ−1)) ln τ] / [(τ+1)(τ−λ)/2 − (1−λ)(τ³−1)/(3(τ−1))]

  All are correct. ω_Z uses an uppercase subscript, as STYLE.md section 13 sets.
- Paragraphs: new sentences after displays ("Note that", "Aside from", "Equation (116)", "The error",
  "The roll damping") are indented paragraphs. Continuations ("and λ ...", "one can write ...", "on
  page 253 should read", "where") are unindented. This matches the scan.
- The "-2-" page number on PDF 682 is correctly not transcribed.

## Discrepancies

none
