# Audit: ch1-sec2a ("2. Description of the Flight Forces" + "2.1 Thrust") — round 1

## Scope checked

- Scan pages: figures/pages/p042.png – p060.png (19 pages, one Read each), plus p061.png
  for the boundary paragraphs that precede "2.2 Weight" (they belong to this unit).
- Render pages: build/unit/ch1-sec2a-1.png – ch1-sec2a-8.png (8 pages).
- Headings: 2 ("2. Description of the Flight Forces", "2.1 Thrust") — both correct.
- Numbered equations: 7 — (1) through (7), each checked symbol by symbol (vector arrows on
  F and c in (1), plain F and c in (2), integral limits 0 and t_b in (3), F_av = I_t/t_b in (4),
  I_sp = I_t/m_f (5), I_sp = I_t/w_f (6), c = g I_sp (7)); numbering sequence and placement correct.
- Unnumbered displays: 9 — "rate of mass change = −dm_e/dt = derivative of mass with respect
  to time"; c⃗ ≡ −c; F(t) = At^n; ∫F(t)dt = A/(n+1) t^(n+1) + C; F(t) = At^0 = A;
  ∫F(t)dt = At + C; the three-line definite integral with ]_{t=t_b} and ]_{t=0};
  I_t ≅ F_1Δt_1 + … + F_8Δt_8 (line break after F_6Δt_6 + kept); lim_{m→∞} Σ_1^m F_1Δt_1 = ∫_0^t F(t)dt
  (scan's typewriter subscript "1" and upper limit "t" reproduced as printed). All faithful.
- Inline formulas: ~40 (Δt, Δm_e, Δm_r = −Δm_e, dt, −dm_e, t′, dm_e/dt, ṁ, I_t, F(t), t_b,
  ∫F(t)dt, n = 0, C, ¼A, I_sp, m_f, w_f, g, meters/sec.², kilogram-meter/(second²), etc.) — faithful.
- Figure captions: 4 (Figures 2, 3, 4, 5) — word for word faithful, emphasis preserved.
- Prose: every sentence of every paragraph compared (~24 paragraphs/continuation blocks);
  wording, emphasis (underline → italics), dashes, quotes and list structure faithful.
- Accepted normalisations not counted: "x" typed as multiplication sign in "(force x time)"
  rendered as "×"; "Then" + display on one typewritten line rendered as text line + centred
  display; "Chapter 4" → "Chapter ??"; placeholder figures; Figure 4 split into two placeholders.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|
| PDF 53 (book p. 23), sentence "It is evident that more than eight rectangles can be used" after the display I_t ≅ F_1Δt_1 + … + F_8Δt_8 | Line starts at the left margin, i.e. it continues the same paragraph as "The total impulse according to this method is given approximately by" (no new paragraph) | Rendered as an indented new paragraph (render page 5) | layout |
