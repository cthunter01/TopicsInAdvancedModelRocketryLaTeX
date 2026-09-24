# Audit: ch2-sec3d corrections, round 1

Item audited: D10 (PDF 204, printed p.174), the sign of the left-hand side of the display after
"This can readily be transformed into".

## What was checked

- `git diff HEAD -- chapters/ch2-sec3d.tex`: one hunk only. It adds an `\ednote` to the sentence
  "This can readily be transformed into". No display, label, tag or other text changed. The display
  after the note is unchanged from HEAD and matches the 1973 page (p204.png):
  `A_r{[w_Z^2(I_L+I_R) - C_1]^2 + C_2^2 w_Z^2} = A_f sqrt([...]^2 + C_2^2 w_Z^2)`.
- The algebra, redone independently. Let K = w_Z^2(I_L+I_R) - C_1. The preceding display is
  A_r[-K - C_2^2 w_Z^2/K] = A_f sqrt(C_2^2 w_Z^2/K^2 + 1). Multiplying through by K gives
  -A_r{K^2 + C_2^2 w_Z^2} = A_f (K/|K|) sqrt(K^2 + C_2^2 w_Z^2).
  - K < 0: the result is the printed display, with A_r > 0.
  - K > 0: -A_r{...} = +A_f sqrt(...), so A_r = -A_f/sqrt(...) < 0.
  Cross-check from the pair above (68a). With principal phi = arctan(C_2 w_Z/K) and K > 0, cos phi > 0
  and sin phi > 0. So A_r[-K cos phi - C_2 w_Z sin phi] = A_f makes A_r negative. The alternative,
  A_r > 0 with phi shifted by pi, satisfies both equations of the pair.
  D10 is therefore confirmed, but only above the frequency where K = 0. The note correctly limits
  it to that case. It also correctly says that the book's positive (68b) holds if the pi goes into
  phi. That matches the book's own convention in Section 3.1.4, where Figure 24 extends phi from 0
  to -pi. Figure 30 is "identical" to Figure 24.
- Note claim "The derivation of equation (45b) takes the same step": checked against p163-p164.
  The display before "Some algebraic manipulation transforms this expression to" has the same
  structure, A_r[(C_1 - I_L w_f^2) - C_2^2 w_f^2/(I_L w_f^2 - C_1)] = A_f sqrt(...), and it is followed by
  the positive A_r[(I_L w_f^2 - C_1)^2 + C_2^2 w_f^2] = A_f sqrt(...). The claim is accurate.
- Note claim "Neither the errata nor the supplements correct this": the errata sheet (p664) has
  no entry for p.174. The Chapter 2 supplements cover pp.186-196 and 251-254/259 only. The claim
  is accurate.
- Placement (STYLE.md section 9): the note is in the sentence that introduces the display. It is
  outside any amsmath display. It sits inside the `subequations` wrapper of (68), which is not a
  display, so it is not typeset twice. Correct.
- Labels: no labels added or changed. The note cites ch2:eq:68a and ch2:eq:68b, both in this unit,
  and ch2:eq:45b in ch2-sec3b, which is expected to show `??` in the unit build.
- Notation (STYLE.md section 13): `\omega_Z`, `\varphi`, `A_r`, `I_L`, `I_R`, `C_1` are as settled.
- Rendered page build/unit/ch2-sec3d-07.png (built 05:25:44, after the .tex edit at 05:25:43).
  The note renders as E1 at the foot of the page, and (68a)/(68b) render as links. The only `??` is
  (45b), from another unit. The log has no undefined reference to a label defined in this unit and
  no overfull boxes. The layout is fine.
- Nothing outside D10 changed in this unit.

## Discrepancies

| where | expected (source/1973) | found | severity |
|---|---|---|---|
| ch2-sec3d.tex l.356-360, D10 \ednote, second sentence | Multiplying the preceding display by K = w_Z^2(I_L+I_R) - C_1 gives -A_r{...} on the left for either sign of K. What depends on the sign is the right side, A_f(K/\|K\|)sqrt(...). The sentence should state the whole K > 0 result, e.g. "When w_Z^2(I_L+I_R) > C_1, multiplying it through by w_Z^2(I_L+I_R) - C_1 gives -A_r{...} = A_f sqrt(...), so that A_r is negative" | "When w_Z^2(I_L+I_R) > C_1, multiplying it through by w_Z^2(I_L+I_R) - C_1 gives the left-hand side with a minus sign, -A_r{...}, so that A_r is negative". This implies the minus sign on the left arises only for K > 0. The conclusion is right but the reason given is imprecise (minor) | note |

Optional, not a discrepancy: "above that frequency" has no named antecedent. "above the frequency
at which w_Z^2(I_L+I_R) = C_1" would be clearer. The note could also point to the book's own
extended arctangent (Section 3.1.4, Figures 24 and 30), which already puts the pi into phi. The
D10 row in corrections/ch2.md still says "todo" (checklist bookkeeping, outside this unit).
