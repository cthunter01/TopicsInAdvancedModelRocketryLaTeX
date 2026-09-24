# Audit: ch1-sec2a ("2. Description of the Flight Forces" + "2.1 Thrust") — round 2

## Scope checked

- Scan pages: figures/pages/p042.png – p060.png (19 pages, one Read each), plus p061.png to
  confirm the unit ends with "...and a knowledge of the engine's thrust-time curve." immediately
  before "2.2 Weight" (nothing from 2.2 has leaked into the unit).
- Render pages: build/unit/ch1-sec2a-01.png – ch1-sec2a-10.png (10 pages; the unit now paginates
  to 10 pages, the earlier round's "render page 5" is now render page 6).
- Headings: 2 ("2. Description of the Flight Forces", "2.1 Thrust") — numbers and wording correct.
- Numbered equations: 7 — (1) F⃗ = −c⃗ dm_e/dt (arrows on F and c); (2) F = c dm_e/dt (no arrows);
  (3) I_t ≡ ∫_0^{t_b} F(t)dt (≡, limits 0 and t_b); (4) F_av = I_t/t_b; (5) I_sp = I_t/m_f;
  (6) I_sp = I_t/w_f; (7) c = gI_sp. Each checked symbol by symbol; numbering sequence 1–7 and
  placement in the text correct.
- Unnumbered displays: 9 — "rate of mass change = −dm_e/dt = derivative of mass with respect to
  time" (two lines); c⃗ ≡ −c; F(t) = At^n; ∫F(t)dt = A/(n+1) t^(n+1) + C (parenthesised exponent
  kept); F(t) = At^0 / = A; ∫F(t)dt = At + C; ∫_0^{t_b}F(t)dt = At]_{t=t_b} − At]_{t=0} / = At_b − A·0
  / = At_b; I_t ≅ F_1Δt_1 + … + F_6Δt_6 + / F_7Δt_7 + F_8Δt_8 (line break after F_6Δt_6 + as printed);
  lim_{m→∞} Σ_1^m F_1Δt_1 = ∫_0^t F(t)dt (typewriter "1" subscripts and upper limit "t" reproduced
  as printed; verified on a 5× enlargement of the scan). All faithful.
- Inline formulas: ~40 (c, y, Δt, Δm_e, Δm_r = −Δm_e, dt, −dm_e, t′, dm_e/dt, ṁ, I_t, F(t), t_b,
  0 and t_b, ∫F(t)dt, A, n, C, n = 0, ¼A, I_sp, m_f, w_f, g, meters/sec.², kilogram-meter/(second²),
  Δm, dm/dt, F⃗ = −c⃗(dm_e/dt), (−y), (+y), etc.) — faithful.
- Figure captions: 4 (Figures 2, 3, 4, 5) — compared word for word, emphasis preserved
  (integral, decreases, increases).
- Prose: every sentence of every paragraph compared (~24 paragraphs/continuation blocks);
  wording, emphasis (underline → italics), dashes, quotes, book titles, paragraph breaks and
  run-on "where"/"so that"/"Then"/"It will be found"/"So you can see"/"You can also see"/
  "A similar numerical method" lines at the left margin all faithful.
- Punctuation spot-check on a 4× enlargement: scan "According to this convention," (PDF 48) is a
  comma, matching the render.
- Accepted normalisations not counted: "x" typed as multiplication sign in "(force x time)"
  rendered as "×"; "Then" + display on one typewritten line rendered as text line + centred
  display; "Chapter 4" → "Chapter ??"; placeholder/provisional figure crops; different line and
  page breaks; equation numbers at the right.

## Round-1 discrepancy re-verified

- PDF 53, "It is evident that more than eight rectangles can be used" after the display
  I_t ≅ F_1Δt_1 + … + F_8Δt_8: now rendered at the left margin with no paragraph indent
  (render page 6), continuing the paragraph "The total impulse according to this method is given
  approximately by" exactly as in the scan. Fixed.

## Discrepancies

none
