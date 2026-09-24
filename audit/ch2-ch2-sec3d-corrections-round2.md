# Audit: ch2-sec3d corrections, round 2

Item audited: D10 (PDF 204, printed p.174). The issue is the sign of the left-hand side of the display
after "This can readily be transformed into". This round re-checks the round-1 finding on the second
sentence of the D10 \ednote.

## What was checked

- `git diff HEAD -- chapters/ch2-sec3d.tex`: one hunk only. It adds an `\ednote` to the sentence
  "This can readily be transformed into" (l.356-365). No display, label, tag or other text changed.
  The display after the note is unchanged from HEAD and matches p204.png:
  `A_r{[w_Z^2(I_L+I_R) - C_1]^2 + C_2^2 w_Z^2} = A_f sqrt([...]^2 + C_2^2 w_Z^2)`.
- Round-1 finding, now fixed. The second sentence now reads "When w_Z^2(I_L+I_R) > C_1,
  multiplying it through by w_Z^2(I_L+I_R) - C_1 gives -A_r{...} = A_f sqrt(...), so that A_r is
  negative". It states the whole K > 0 result, with the right-hand side, as the round-1 audit
  proposed. It no longer suggests that the minus sign on the left appears only for K > 0.
- Algebra, redone independently. Let K = w_Z^2(I_L+I_R) - C_1. The preceding display is
  A_r[-K - C_2^2 w_Z^2/K] = A_f sqrt(C_2^2 w_Z^2/K^2 + 1), that is,
  -A_r(K^2 + C_2^2 w_Z^2)/K = A_f sqrt(K^2 + C_2^2 w_Z^2)/|K|.
  - K < 0: this gives A_r{K^2 + C_2^2 w_Z^2} = A_f sqrt(...), the printed display, with A_r > 0.
    The note's first sentence ("only when w_Z^2(I_L+I_R) < C_1") is right.
  - K > 0: this gives -A_r{...} = A_f sqrt(...), so A_r < 0. The note's second sentence is right.
  - Numerical cross-check from the first pair above (68a), with principal phi and A_f = 1,
    C_1 = 2, C_2 = 0.3, I_L + I_R = 1:
    - w_Z = 0.5 (K = -1.75): A_r = +0.5693 = 1/sqrt(K^2 + C_2^2 w_Z^2).
    - w_Z = 3 (K = 7): A_r = -0.1417 = -1/sqrt(...).
  - The step that loses the sign is sec(phi) = +sqrt(tan^2 phi + 1). It holds only for
    cos(phi) > 0. If phi is shifted by pi above the frequency where K = 0, cos(phi) < 0 and A_r
    is positive. So the note is right that "the lost sign belongs in phi, which above that
    frequency differs by pi from the principal value of equation (68a)".
- "The derivation of equation (45b) takes the same step". Checked against ch2-sec3b.tex l.385-423
  (the HEAD transcription of p163-p164). The display before "Some algebraic manipulation transforms
  this expression to" has the same structure with I_L w_f^2 - C_1. It is followed by the positive
  A_r[(I_L w_f^2 - C_1)^2 + C_2^2 w_f^2] = A_f sqrt(...). The claim is accurate. ch2-sec3b has no
  duplicate note on this step: its only corrections hunk is the D8 note.
- "Neither the errata nor the supplements correct this": the errata sheet (p664) has Chapter 2
  entries for pp.108, 113 and 144-145 only. The Chapter 2 supplements cover pp.186-196 and
  251-254/259. Nothing touches p.174. The claim is accurate.
- Placement (STYLE.md section 9): the note is in the sentence that introduces the display. It is
  outside any amsmath display, inside the `subequations` wrapper of (68), which is not typeset twice.
- Labels: none added or changed. The note cites ch2:eq:68a and ch2:eq:68b, both in this unit, and
  ch2:eq:45b in ch2-sec3b.
- Notation (STYLE.md section 13): `\omega_Z`, `\varphi`, `A_r`, `I_L`, `I_R`, `C_1` are as settled.
- Build: build/unit/ch2-sec3d-*.png and the log date from 05:29:09-12, after the .tex edit at
  05:29:07. On page 7 the note renders as E1, fully wrapped in the footnote, with
  -A_r{...} = A_f sqrt... legible. (68b) and (68a) are links. The only `??` is (45b), from another
  unit. Page 8 continues (68b), (69)-(75) in sequence. The log has no undefined reference to a label
  defined in this unit and no overfull boxes.
- Nothing outside D10 changed in this unit.

Observations, not discrepancies:
- "above that frequency" has no named antecedent. It means the frequency at which
  w_Z^2(I_L+I_R) = C_1, which the preceding sentences imply. This is readable as it stands.
- The D10 row in corrections/ch2.md still says "todo". That is checklist bookkeeping outside this unit.

## Discrepancies

none
