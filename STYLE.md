# Transcription style guide

Read this whole file before transcribing or auditing any unit. It is the contract that lets many
people (and agents) work on the book in parallel and end with one consistent document.

## 1. Source of truth

- The **page image** is the source of truth: `figures/pages/pNNN.png` (native 1040×1476 px scan,
  NNN = PDF page number, zero-padded). Read one page per `Read` call. Never rely on a downsampled
  multi-page render: at 150 ppi the difference between ω_n and ω_m, or b and ℓ, is a few pixels.
- `drafts/pNNN.txt` is the OCR text layer of that page. Use it only as a typing aid for prose,
  captions, symbol lists and references, then correct it against the image. OCR confuses typewriter
  C with O ("O.G." is C.G.), 1 with l, and inserts stray punctuation. It is worthless for math.
- Displayed and inline mathematics in the 1973 book is hand-lettered. Transcribe every equation,
  subscript, Greek letter, vector arrow and overbar from the image. Hand-lettering look-alikes:
  script e vs ℓ, ω_n vs ω_m, b vs ℓ, cursive "sin/cos/t", ζ drawn as a curly glyph. Decide from
  context and the chapter's Symbols list; when still unsure use `\draftnote{...}` (rule 10).

## 2. Units of work

- A unit is one file `chapters/chN-<unit>.tex`, bounded by **headings, not pages**: it runs from
  its first heading up to but not including the next unit's heading. Where a page holds the end of
  one unit and the start of the next, the boundary paragraph belongs to the unit whose heading
  precedes it.
- A unit file starts with its own heading (`\section{...}`, `\subsection{...}` or `\unnumberedsection{...}`) and
  contains **no** `\newcommand`, `\def`, `\let`, `\usepackage`, `\renewcommand` (checked
  mechanically). All macros live in `preamble.tex` (the notation macros in `macros.tex`, which the redrawn
  figures share).
- Self-check before hand-off: `make unit U=chapters/chN-<unit> PRE='\def\chapstart{N}\def\eqstart{K}\def\figstart{J}'`
  must succeed (K, J = the numbers of the last equation/figure before the unit). Pages render to
  `build/unit/<unit>-*.png`; look at them.

## 3. Prose

- Reproduce wording, sentence order, paragraphing, lists and emphasis exactly. Rejoin words
  hyphenated at line ends. Keep the authors' spelling, units and punctuation; do not modernize.
- Fix obvious typographical slips and OCR errors silently ("Wlfortunately" → "unfortunately",
  "toal" → "total"). If a *statement or formula* looks wrong, keep it and flag it (rule 10/11).
- Underlining in the typescript means emphasis or a title: use `\emph{...}` for both, including
  whole underlined sentences.
- `--` in the typescript is a dash: write `---` (no spaces). Quotes: ``like this''.
- Section headings: `\section{Definition of the Problem}` (book "1. Definition of the Problem"),
  `\subsection{Thrust}` ("2.1"), `\subsubsection{...}` ("3.1.2"). Unnumbered headings
  (Introduction, Symbols, References): `\unnumberedsection{Introduction}`.
  Every heading gets a label (rule 5). Headings containing math use `\texorpdfstring{$...$}{...}`.
- Author's ink insertions (words added by caret on the printed page) are part of the text:
  transcribe them as intended, without a note.
- The running chapter title repeated at the top of the first text page is not transcribed.
  Page numbers are not transcribed.

## 4. Mathematics

- Numbered equation: `\begin{equation}\label{chN:eq:K} ... \end{equation}` where K is the number
  printed in the 1973 book (e.g. `ch1:eq:7`). That label never changes, even if a later correction
  rewrites or renumbers the equation. Equations that exist only in the corrected edition use
  `chN:eq:nK` (e.g. `ch1:eq:n21`).
- Lettered groups (27a, 27b): `\begin{subequations}\label{chN:eq:27} \begin{equation}\label{chN:eq:27a}...`.
  Use `\tag{102b}` only when the printed lettering cannot be produced by `subequations`
  (e.g. a lone "(102b)" with no "(102a)"). Uppercase letters such as (144A), which occur only in the
  corrected text: `\begin{equation*}\tag{144A}\label{chN:eq:n144A}`.
  A `\tag` always goes in a starred environment (`\begin{equation*}\tag{2a}\label{...}`): inside
  a numbered `equation` it re-uses the next equation's PDF link target, so links to that equation
  land on the tagged one (tools/check_numbering.py check 8 fails on it).
- Unnumbered displays: `equation*`, `align*` (align on `=`), `gather*`. Multi-line derivations:
  `align*` with `&=` on each line. Side conditions printed at the right ("(t < 0)"): `\qquad (t<0)`
  inside the display, or `cases` when the display is piecewise.
- Connective words the typescript prints beside or between displays ("and", "or", "from which",
  "or, since") are set as short prose lines between the displays; conditions such as "(t < 0)",
  labels such as "(conical nose)" and units printed at the right stay inside the display after `\qquad`.
- Unnumbered side-by-side comparisons (e.g. "Present Treatment | Gurkin Report") are a `tabular` inside
  `center`, without caption or number, so they do not consume table numbers.
- For an unclear hand-lettered glyph, render a zoomed crop of the scan and look at it:
  `pdftoppm -r 300 -f P -l P -x X -y Y -W W -H H -png Topics_in_Advanced_Model_Rocketry.pdf build/zoom`
  (X, Y, W, H in pixels at 300 dpi; the page is about 2080 x 2950 px).
- Text between displays stays as prose paragraphs. Short "where" lists after an equation:
  `\begin{itemize}[nosep,leftmargin=*]` or a `where $x$ = ...` paragraph, matching the book.
- Notation: vectors `\vec{F}`; overbars `\bar{Z}_T`; time derivatives `\dot{m}`, `\ddot{x}`;
  multi-letter or grouped subscripts `\bar{Z}_{T(B)}`, `C_{N\alpha}` (use `\CNa`); functions
  `\sin`, `\cos`, `\tan`, `\arctan`, `\arcsin`, `\sinh`, `\cosh`, `\tanh`, `\ln`, `\exp`;
  `\Delta t`, `\partial`; integrals `\int_{0}^{t}`; sums `\sum`; script letters `\mathscr{F}`;
  infinity `\infty`; "≅" `\cong`; "≈" `\approx`; "≡" `\equiv`; "≥" `\ge`; "≶" `\lessgtr`.
  Units inside math: `5\un{cm}`, `\un{dyn\,cm\,s}`; degrees `\dg`.
- Macros available (all in `preamble.tex`; use these and no others):

  | macro   | meaning                          | expands to                |
  |---------|----------------------------------|---------------------------|
  | `\AR`   | aspect-ratio ligature            | italic AR, tightened      |
  | `\CNa`  | normal force curve slope         | `C_{N\alpha}`             |
  | `\mdot` | mass flow rate                   | `\dot{m}`                 |
  | `\Isp`  | specific impulse                 | `I_{\mathrm{sp}}`         |
  | `\CD`   | drag coefficient                 | `C_{D}`                   |
  | `\CDo`  | zero-lift drag coefficient       | `C_{D_0}`                 |
  | `\un{}` | unit in math                     | `\,\mathrm{...}`          |
  | `\dg`   | degree sign                      | `^{\circ}`                |
  | `\CG`, `\CP` | centre of gravity/pressure (text) | `C.G.`, `C.P.`      |

- Typewritten inline symbols such as "m_e" or "C_n" are typed as math: `$m_e$`, `$C_n$`.

## 5. Labels

`chN` (chapter), `chN:sec:2.1` (section, the book's number), `chN:eq:53`, `chN:eq:53a`,
`chN:fig:20`, `chN:plate:1`, `chN:tab:4`, `chN:ref:3`. Every heading, equation, figure, plate, table
and reference item gets exactly one label.

## 6. Cross-references

`equation~\eqref{chN:eq:53}`, `equations~\eqref{...} and~\eqref{...}`, `Figure~\ref{chN:fig:20}`,
`Figure~\ref{chN:fig:4}a` (panel letters follow the ref), `Section~\ref{chN:sec:2.4}`,
`Chapter~\ref{ch2}`, `Table~\ref{chN:tab:1}`, `Plate~\ref{chN:plate:1}`, `Reference~\ref{chN:ref:3}`.
Never type a bare number for anything that has a label. A reference to another chapter's
equation is `equation~\eqref{ch2:eq:30} of Chapter~\ref{ch2}` (the label may not exist yet; that is
expected until that chapter is transcribed and is tolerated by the standalone unit build only).
A cited equation that does not exist in the book (stale reference) is typed literally as printed
and flagged with `\ednote{...}` naming the probable target.

## 7. Figures and plates

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth,height=0.85\textheight,keepaspectratio]{figures/ch1/fig02.png}
  \caption{Origin of rocket thrust. In a time interval $\Delta t$ the rocket expels ...}
  \label{ch1:fig:2}
\end{figure}
```
- Place the figure environment right after the paragraph that first refers to it.
- Caption text is transcribed in full (they are often long). The label word and number are added
  by LaTeX; do not type "Figure 2:" in the caption.
- Panel letters (a), (b) stay inside the artwork. A figure printed over two pages is one figure
  with two `\includegraphics` stacked. Photographs use `\begin{plate}...\end{plate}` with the same
  structure and `\label{chN:plate:1}`.
- The image file is the one named in `figures/manifest.csv` for that figure; include it exactly
  once. Figures whose artwork contains formulas stay as images in version 1.
- A figure printed as separately captioned panels ("Figure 5(a):", "Figure 5(b):" ...) is one figure environment
  per panel with `\figurepanel{a}` (then `{b}`, `{c}`) before `\caption` and the label `chN:fig:5a`, `chN:fig:5b` ...;
  cite a panel as `Figure~\ref{ch4:fig:5a}` (it prints 5(a)); cite the whole set as `Figure~\hyperref[ch4:fig:5a]{5}`
  ("Figures 5 through 9": `\hyperref[ch4:fig:5a]{5} through~\hyperref[ch4:fig:9a]{9}`).

## 8. Tables

`booktabs` (`\toprule`, `\midrule`, `\bottomrule`), `\caption` **above** the table,
`\label{chN:tab:N}`. Numeric columns with `siunitx` `S` columns when the data are plain numbers.
Symbols lists:
```latex
\unnumberedsection{Symbols}\label{ch1:sec:symbols}
\begin{longtable}{@{}l p{0.78\linewidth}@{}}
\toprule \textbf{Symbol} & \textbf{Meaning} \\ \midrule \endfirsthead
\toprule \textbf{Symbol} & \textbf{Meaning} \\ \midrule \endhead
\bottomrule \endlastfoot
$A_r$ & reference area of a rocket \\
...
\end{longtable}
\addtocounter{table}{-1}% a caption-less longtable still steps the table counter (STYLE.md section 8)
```
The `\addtocounter` line is required: longtable steps the table counter even without a caption, so without it
the chapter's Table 1 would print as Table 2.
Keep the book's order of entries.

## 9. Footnotes and editorial notes

- The authors' own footnotes: `\footnote{...}`.
- Editorial notes: `\ednote{...}` (numbered E1, E2, … per chapter). Put it in the sentence that
  introduces a display, never inside `align`/`gather`/`equation` (amsmath typesets the body twice),
  never inside `\caption` or a `longtable` head. Inside captions use `\edcap{...}`. Inside a `longtable`
  a `p{}` cell silently drops the text of an `\ednote` (longtable re-routes only kernel footnotes), so in
  table rows either use `\edcap{...}` or, for a short cell, make it an hbox cell:
  `\multicolumn{1}{l@{}}{short meaning\ednote{...}}` (see chapters/ch1-symbols.tex).

## 10. Uncertain readings

`\draftnote{clipped at margin; reconstructed from eq. (52)}` right where the doubt is. Never guess
silently. A unit is not finished until every `\draftnote` is resolved or converted to `\ednote`.

## 11. Corrections

The 1973 errata and the 1994/2022 supplement are applied in a separate corrections step, never
during the faithful transcription pass. Transcribe what is printed, including known errors.

## 12. References

```latex
\unnumberedsection{References}\label{ch1:sec:refs}
\begin{enumerate}[label=\arabic*.,ref=\arabic*,leftmargin=*]
  \item\label{ch1:ref:1} Mandell, G. K., \emph{Model Rocketry}, Oct. 1968. ...
\end{enumerate}
```
Underlined titles become `\emph{}`; keep the authors' citation wording.

## 13. Chapter 2 notation (settled at assembly)

The hand-lettering does not distinguish the case of x/X, y/Y, z/Z or of o/0 in subscripts, so
Chapter 2 uses one form throughout, taken from its Symbols list. Auditors: these forms are intended.

- Axis subscripts on angles and angular velocities are uppercase: `\alpha_X`, `\alpha_Y`,
  `\Omega_X`, `\Omega_Y`, `\omega_Z` (roll rate), `\alpha_{Xm}`; hand-lettered moment subscripts
  likewise `M_X`, `M_Y`, `M_Z` (the typed prose prints them so). Initial values carry a digit zero:
  `\alpha_{X0}`, `\Omega_{Y0}`, `\alpha_0`.
- Typewritten subscripts keep their printed case: the forcing functions `f_x(t)`, `f_y(t)` and the
  Symbols list's `M_x`, `M_y`, `M_z`; the letter o in `I_{Lo}`, `M_o`, `\bar{W}_o`, `R_o`.
- Amplitude ratio (two separate letters in the book) is `\mathit{AR}`, `\mathit{AR}_c`,
  `\mathit{AR}_{\mathrm{res}}`, `\mathit{AR}_{\mathrm{cres}}`; `\AR` is only the aspect-ratio ligature.
- Word-like subscripts are upright: `\beta_{\mathrm{res}}`, `\beta_{\mathrm{cres}}`,
  `\omega_{\mathrm{cres}}`, `t_{\max}`; letter subscripts stay italic: `\omega_n`, `\omega_{nc}`,
  `\zeta_c`, `\beta_c`, `I_{Lch}`. The natural-frequency subscript that looks like m is n.
- Phase angle `\varphi`; damping ratio `\zeta`; angular acceleration `\gamma`; the Symbols list's
  script F is `\mathscr{F}`.

## 14. Chapter 3 notation (settled before transcription)

Chapter 3 mixes typed symbols in the prose with hand-lettered displays, and the two often differ in case and in
how far a subscript drops. The Chapter 3 Symbols list (`chapters/ch3-symbols.tex`) fixes the form of each symbol.
Where a hand-lettered glyph does not show its case or level (x/X, s/S, c/C, v/V, p/P, k/K, z/Z, o/0, subscript vs
sub-subscript), set the listed form without a note. Where the print is unambiguous but differs from the list for
what is evidently the same quantity, transcribe it as printed and report it (the corrections step decides).
Auditors: the forms below are intended.

- **Drag coefficients: one subscript level.** `\CD`, `(\CD)_{\mathrm{lug}}`, `(\Delta\CD)_{\mathrm{lug}}`,
  `C_{Db}`, `(C_{Db})_m`, `C_{Dc}`, `C_{Df}`, `\Delta C_{Df}`, `C_{Df}'`, `(C_{Df})_b`, `C_{Di}`, `C_{Di}'`,
  `\Delta C_{Di}`, `(C_{Di}')_{\mathrm{cant}}`, `C_{DI}`, `C_{Ds}`, `C_{Dv}`, `C_{D\alpha}`. The second letter
  often drops in the hand-lettering and sometimes in the typing (PDF 429, 439): that is placement, not a
  sub-subscript. The one true sub-subscript is `C_{D_B}(\alpha)`. Capital I (`C_{DI}`, interference) and lowercase
  i (`C_{Di}`, induced) follow the printed case even where the meaning suggests the other (ΔC_Di in (146)); the
  hooked, λ-like hand glyph with a dot is i.
- **Zero-lift drag coefficient** is `\CDo` (as in Chapter 1): `\CDo`, `(\CDo)_B`, `(\CDo)_F`, `(\CDo)_{FB}`,
  typed or lettered. It is the only o subscript set as a digit zero.
- **Every other o subscript is the letter o**: `S_o`, `x_o`, `V_o`, `p_o`, `\rho_o`, `\mu_o`, `\nu_o`, `\tau_o`,
  `\tau_{ok}`. A value is a digit: `f''(0)`, `y=0`, `\int_{0}`.
- **Skin friction**: `C_f`, `C_{fb}`, `C_{fx}`, `C_f'`, `\Delta C_f`, `(C_f)_B`, `(C_f)_F`, `(C_f)_{\mathrm{lam}}`,
  `(C_f)_{\mathrm{turb}}`, `(C_f')_{\mathrm{lam}}`, `(C_f')_{\mathrm{turb}}`, `(\Delta C_f)_{\mathrm{lam}}`,
  `(\Delta C_f)_{\mathrm{turb}}`. The crossed hand f that looks like t or + is f. Outer capitals B (body) and F (fins)
  are italic and distinct from the lowercase b of `(C_{Df})_b`.
- **Upright subscripts** (`\mathrm`, spelling and periods as printed at that place): `lug`, `cant`, `lam`, `turb`,
  `tot`, `adm`, `crit`, `root`, `tip`, `model`, `full\text{-}scale`, `forebody`, `std.`/`std`, `stag.`/`stag`,
  `equiv.` (the Symbols list's "eqiv." is a typing slip, fixed silently). Shape descriptors keep their printed
  capitals: `ELLIP.`, `OGIVE`, `CONE`, `BOATTAIL`, `NOSE`, `CYL`, `GCR`, `LAM.`; the "cyL." of (169)-(170) is set
  `\mathrm{cyl.}` (this hand has no upright lowercase l). Letter and digit subscripts stay italic: `S_b`, `S_e`,
  `S_E`, `S_F`, `S_m`, `S_s`, `S_x`, `d_b`, `d_m`, `d_n`, `d_r`, `\ell_b`, `\ell_N`, `\ell_T`, `\ell_s`, `D_a`,
  `D_b`, `D_e`, `D_f`, `D_p`, `D_v`, `D_\alpha`, `p_b`, `p_s`, `p_{s1}`, `p_{s2}`, `A_r`, `A_c`, `R_a`, `k_t`,
  `u_k`, `\eta_k`, `\eta_B`, `\eta_3`, `K_{F(B)}`, `K_{B(F)}`, `p_1`, `p_2`, `u_1`, `u_2`, `A_1`, `A_2`.
- **Pressure is lowercase p** (`p`, `\Delta p`, `p_b`, `p_o`, `p_s`, `p_\infty`, `p_{\mathrm{tot}}`, `C_p`, `D_p`),
  including hand p's without a descender. Capital `P` is only the perimeter `P(x)`.
- **Surfaces and areas**: `A`, `A_c`, `A_r`, `A_{\mathrm{lug}}`; the surface of integration `\iint_{S}` with `dS`
  (and `S_b`, `dS_b`), even where the hand S looks like s; lowercase `s` is the distance along a surface. `S_s`
  has a lowercase s. `S_E` and `S_e`, and `\sigma_F` and `\sigma_E`, are different symbols.
- **Script ell** `\ell` everywhere, hand or typed: `\ell`, `\ell_b`, `\ell_T`, `\ell_N`, `\ell_s`, `R_\ell`,
  `\ell/d_m`. The script "ℓn" in (229)-(230) is `\ln`.
- **Reynolds number is R**: `R`, `R_\ell`, `R_x`, `R_c`, `R_d`, `R_k`, `(R_k)_t`, `R_{\mathrm{crit}}`, exponents as
  printed (`R_\ell^{1/5}`, `(R_\ell)^{1/5}`). `R_a` is the area ratio. The R of Figure 33 and the A, B, C of
  Figures 23-24 are point labels.
- **Velocities**: `U_\infty` wherever an infinity sign is drawn (even degraded); plain `U` where printed plain;
  lowercase `u`, `u_k` for flow velocity; `v` the transverse velocity (lowercase even when drawn large); `V` where
  the prose types V.
- **ν and look-alikes**: decide ν by context, not by the tail: a curled v-like glyph in viscosity and Reynolds
  expressions (`U/\nu x`, `UL/\nu`, `ku_k/\nu`, `\sqrt{\nu x/U_\infty}`) is `\nu` even with a descender; `y` is the
  coordinate normal to the surface (`\partial/\partial y`, `y=0`) with a straight descender; the looped one is
  `\gamma` (shear strain). `\rho` has its loop at the top, `\delta` at the bottom. The hand q and g that look like 9
  are `q` and `g`.
- **x and times**: coordinates `x`, `y`, `z` are lowercase (the cap-height hand x is x). An X-shaped glyph is
  `\times` only between numbers or before a power of ten; between symbols it is the variable (`2x\eta_k` in (93)).
- **Thicknesses**: `\delta`, `\delta^{*}`, `\theta` (lowercase; θ also names the deformation and fin-cant angles,
  including the Θ-shaped hand and typed forms of (152)-(153)).
- **Greek**: `\epsilon`; `\eta`; `\phi` (surface deviation angle, PDF 360-361, and the typed slashed ø) vs
  `\varphi` (central angle on a cylinder, PDF 377, 396-402, 414); `\psi`; `\pi`; `\alpha`, `\bar{\alpha}`,
  `\alpha_i`; `\omega_Z` (roll rate); `\tau`; `\mu`; `\sigma_E`, `\sigma_F`.
- **Derivatives**: italic `d` (also the curled hand d); `\partial` only where a partial sign is drawn.
- **Vectors**: `\vec{}` wherever an arrow is drawn (`\vec{n}`, `\vec{t}`, `\vec{V}`, `\vec{F}`, `\vec{D}_i`); a
  letter printed without an arrow stays plain.
- **Primes** follow the whole subscript: `C_{Df}'`, `(C_f')_{\mathrm{lam}}`; Blasius `f`, `f'`, `f''`, `f'''`.
- **Functions and relations**: `\sin^{-1}` in (171a) as printed; `\tanh`, `\tanh^{-1}`, `\ln`, `\log`; `\cong`
  (tilde over two bars); `\sim` in (35)-(37); `\propto`; `\equiv` (three bars: (24), (25), PDF 353); `\le`, `\gg`,
  `<`, `>` (side conditions); words inside formulas in `\text{}` ("constant", "cross-sectional area").
- **Numbers**: leading-dot decimals as printed (`.0617`); `3 \times 10^{6}` in math; the typed ½ and the small hand
  ½ are `\tfrac{1}{2}`; slashed fractional exponents as printed (`^{1/5}`); degrees `90\dg`, including the typed
  raised o after a number.
- **Units**: in prose after a number, units stay as text ("60 meters/second"); units attached to a number inside a
  formula use `\un{}` with the printed period (`5.67 \times 10^{-3}\un{cm.}`); a unit word printed at the right of
  a display goes after `\qquad` as `\text{...}` (Chapter 2 practice).
- **Other symbols**: `\AR`, `\Delta\AR` (aspect ratio); lowercase `c` for chord and for the speed of sound (even
  when drawn large, e.g. `c = c_{\mathrm{std}}\sqrt{T/T_{\mathrm{std}}}`); `b` lowercase (span), `B` capital
  (transition constant); `M` (Mach number); `n` (rotation rate, unit normal, and the number of fins on PDF 465,
  as printed); `d` (body diameter, PDF 447-448, 392); `m` (mass, PDF 521-523); `\Delta` typed or drawn.
- **Tables** follow section 8 (booktabs, caption above, no vertical rules or boxes, whatever the typescript draws);
  stacked sub-tables (Tables 4 and 8) are two tabulars in one table float with their sub-titles; an unnumbered
  tabulation is a `tabular` in `center` or an aligned display, per section 4. Tables drawn inside a figure's artwork
  (Figures 29, 31, 39b, 44, 45) stay in the image.

## 15. Chapter 4 notation (settled before transcription)

Chapter 4's prose, Symbols list, equations (9)-(11), "where" lists and Tables 1-2 are typewritten. Every other display is hand-lettered, and hand-drawn Greek letters, arrows and Δ are also pasted into the typed prose. The lettering does not show case (v/V, x/X, y/Y, z/Z, c/C, k/K, s/S) or o/0, and it often draws a subscript at full size. The Chapter 4 Symbols list (`chapters/ch4-symbols.tex`) fixes the form of each symbol. A symbol gets the same LaTeX form whether it is typed or lettered. Where a lettered glyph does not show its case, its level or o/0, set the listed form without a note. Where the print is unambiguous but differs from the list for the same quantity, transcribe it as printed and report it. Auditors: the forms below are intended.

- **Axis subscripts are lowercase** (unlike Chapters 2 and 3): `\alpha_x`, `\alpha_y`, `\alpha_x(t)`, `\Delta\alpha_x`, `\omega_x`, `\omega_y`, `\Delta\omega_y`, `\omega_z` (roll rate), `M_x`, `M_y`, `H_x`, `H_y`, `f_x(t)`, `f_y(t)`, `v_x`, `v_y`. The list, the prose ("subscripts x and y", PDF 616) and Table 2 (typed ω_z) all print them lowercase. The crossed hand z (ƶ) is z, not 2, and the capital-looking Y of H_y in (160c) is y. These subscripts name the yaw and pitch axes, not the coordinates x and y.
- **Every o subscript is the letter o**, whether typed or lettered: `t_o`, `m_o`, `A_o`, `\theta_o`, `\omega_o`, `\alpha_{xo}`, `\alpha_{yo}`, `\omega_{xo}`, `\omega_{yo}`, `\omega_{zo}`. This includes the conditions (`t < t_o`, `t = t_o`, `t_o \le t \le t_1`) and Table 2. The typewriter makes a subscript by dropping a full-size character (the 1 of t_1 is digit height). Its o subscript is only x-height, shorter than its digit 0 (PDF 601, 620, 622). The rule also covers the large hand circles (ω_xo in (155c), ω_zo in (165b)), even though the text speaks of "zero-subscripted quantities" (PDF 619). It differs from Chapter 1's `m_0` and Chapter 2's `\alpha_{X0}`. Values are digits: `t = 0`, `\alpha_x = \alpha_y = 0`, `(0 \le t \le t_m)` (the x-height o of the (73a)-(74a) ranges is a digit), integral limits `0` (lower in (19b), (22)-(23), (41)-(43); upper in (63) and (66), `\int_{v_b}^{0}`), and the `0,0` of (23). The only digit-zero subscript is `(\CDo)_{FB}` (Table 1): its typed o is x-height, but the zero-lift coefficient follows the Chapters 1 and 3 `\CDo` convention.
- **Digit and index subscripts**: the typed 1 (the same glyph as l) and the lettered 1, which looks like a stroke, a comma or ı, are the digit 1. The z-like 2 is 2. So: `A_1`, `A_2`, `C_1`, `C_2`, `F_2`, `k_1`, `k_2`, `m_1`, `m_2`, `t_1`, `t_2`, `v_1`, `v_2`, `y_1`, `y_2`, `t_2^{2}`. The stage index is `F_n`, `k_n`, `m_n`, `t_n`, `v_n`, `y_n`, `v_{n-1}`, `y_{n-1}` (the lettered "n-ı" is n-1). Sums are set as lettered: `y_1 + \ldots + y_{n-1}`. In the prose, "nth" and "(n-1)th" are `$n$th` and `$(n-1)$th`.
- **Letter subscripts are italic** and lowercase, as the list gives them: `v_b`, `t_b`, `y_b`, `x_b`, `m_b` (the 6-like hand b is b), `t_c`, `y_c`, `m_f`, `F_m`, `t_m`, `F_s`, `t_s`, `F_t`, `F_p`, `I_t` (capital I), `A_f`, `A_r`, `\omega_f` (the crossed hand f), `\omega_n` (the m-like n), `\zeta_c`, `dm_e` (e even where it looks like ε), `v_t`, `\Delta v_t`, `\Delta v_a`, `\Delta\dot{x}_t`, `\Delta\dot{y}_a`. Capitals stay as printed: `I_L`, `I_R`, `C_{2A}`, `C_{2R}`. A subscript lettered at full size ("Va", "Fm" in (73b), "Δẋa") is still a subscript. The t of `v_t` and `\Delta v_t` (drag-free, "theoretical") and the t of `F_t` (tangent) are the same italic t. `d\vec{p}_E` (external forces) and `d\vec{p}_e` (exhaust) are different symbols.
- **Word subscripts are upright**: `\Isp` (also for the lettered "I_SP" of (69)), `\omega_{\mathrm{res}}`, `\omega_{\mathrm{cres}}`, `k_{\min}`, `k_{\max}`, `y_{\max}`, `\alpha_{\max}` (like Chapter 2's `t_{\max}`), `(\Delta\CD)_{\mathrm{lug}}`.
- **Velocity, altitude, range, time**: `v` is lowercase everywhere. That includes the cap-height lettered V in (12)-(13), (34), (80), (85), (94)-(128), (133)-(139) and (163)-(165), and the typed v of the tables. `x` (range) and `y` (altitude) are lowercase too, including the X-shaped x of (99), (101), (109), (114), (123) and (130) and the γ- or Y-like y. Time is `t`, `\Delta t`, `dt`. Dots go over the letter and the subscript follows: `\dot{x}`, `\dot{y}`, `\ddot{x}`, `\dot{u}`, `\ddot{u}`, `\Delta\dot{y}_t`, `\mdot`.
- **Thrust, mass and drag** (as in Chapters 1 and 3):
  - Thrust: `F` (average thrust), `F(t)`, `F_t`, `F_p`, `F_2`, `F_n`. (12)-(13) print `F_t` and (16)-(17) print `F(t)`; set both as printed.
  - Mass: `m` and `m(t)` are lowercase (the rn- or M-like hand m is m), with `m_b`, `m_f`, `m_o`, `dm_e/dt`. Capital M is only the moments `M_x`, `M_y` and the typed disturbing moment `M` of PDF 621 (`M/C_1`). `\gamma` is the mass-expulsion rate in (70)-(71), not y and not 8.
  - Drag: `D` (italic, as typed in (11)), and the typed or lettered word `\text{Drag}` in (77), (95), (117), (133). `k` is lowercase; `\epsilon`, `f(\alpha)`, `kv^{2}`, `(k + \epsilon\alpha^{2})v^{2}`, `\CD`, `(\Delta\CD)_{\mathrm{lug}}`, `A_r`, `\rho`, `\tfrac{1}{2}\rho\CD A_r`.
  - Other: `c = g\Isp`; `g` is always g, even when the hand g looks like 9 or q; `I_t`.
- **Greek**:
  - `\alpha` for every ∝-like glyph, typed, lettered or pasted into the prose. In (41)-(42), `\alpha` and `\beta` are generic limits (the κ-like smudge is α).
  - `\theta`, `\theta_o` for the Θ-like typed and lettered forms.
  - `\zeta`, `\zeta_c` for the curl that looks like ≤ or ʃ; `\rho` for the ʃ-like typed and lettered form.
  - `\epsilon` for the lunate, ∈-like form; also `\gamma` and `\omega`.
  - `\Delta`, typed or drawn, never A.
  - `\propto`, `\in`, `\Theta` and `\varepsilon` do not occur.
- **Vectors**: use `\vec{}` wherever an arrow is drawn, over the letter only: `\vec{F} = m\vec{a}`, `\vec{p}`, `d\vec{p}`, `d\vec{p}_E`, `d\vec{p}_e`, `\vec{v}`, `d\vec{v}`, `\vec{c}`, `\vec{E}`, and `\vec{F}(t)` in (8). A letter printed without an arrow stays plain (the E on PDF 546). The overbars of Figure 1 stay in the artwork.
- **Functions and calculus**:
  - Functions: `\ln` (for the script "ℓn"), `\tanh`, `\cosh`, `\sinh`, `\tanh^{-1}`, `\tan^{-1}` in (64) as printed (not `\arctan`), `\sin`, `\cos`, `\sqrt`. `e^{Ht}` has an italic e. The prose's "tanh( ), ln( ), cosh( )" are `$\tanh(\ )$`, `$\ln(\ )$`, `$\cosh(\ )$`.
  - The curled hand d is an italic `d`.
  - Integral limits go at the side, as in Chapters 1 and 3 (`\int_{t_1}^{t_1+t_2}`, `\int_{v_b}^{0}`), with no `\limits`, even where the typescript stacks them ((40), (43), (44), (52)): typographic, not a discrepancy. The evaluation bars are `kyv\Big]_{0,0}^{y_b,v_b}` in (23) and a full bracket pair `\biggl[\ldots\biggr]_{v_1}^{v_2}` in (53), as printed.
  - Relations: `\cong` in (135), `\Delta t \to 0` (PDF 585), `\le`, `\ge`, `<`.
  - Derivatives: `\dot{x}`, `\dot{y}`, `\ddot{x}`, `\dot{u}`, `\ddot{u}`; `dv_y/dt`, `dv_x/dt` with a lowercase v even where the lettering draws it large.
- **Riccati and Fehskens-Malewicki constants**: `u`, `A_1`, `A_2`, `H`, as in `u = A_1e^{Ht} + A_2e^{-Ht}`, `H = \frac{1}{m}\sqrt{k(F - mg)}` and `v = \frac{m}{k}\frac{\dot{u}}{u}`. `A` and `B` in the unnumbered cosh identity (PDF 568) are plain capitals. `C_1` and `C_2` are capitals even where (144)-(145) letter them small; the typed C that looks like O is C.
- **Brace-grouped conditions** ((154), (155), (157), (158), (160), (166)): each row keeps its printed number. One right brace spans the rows, and the condition follows it as printed (`t < t_o`, `t = t_o`, `t_o \le t \le t_1`, `t = 0`):
  ```latex
  \begin{subequations}\label{ch4:eq:155}
  \begin{empheq}[right={\empheqrbrace\quad t = t_o}]{align}
    \alpha_x &= \alpha_{xo} \label{ch4:eq:155a}\\
    \alpha_y &= \alpha_{yo} \label{ch4:eq:155b}\\
    ...
  \end{empheq}
  \end{subequations}
  ```
  The (154) group prints its third row as (156c). Use the Chapter 3 (203)-(204) pattern: first `\refstepcounter{equation}\label{ch4:eq:154}`, then `empheq` on `align*` with `\tag{154a}\label{ch4:eq:154a}`, `\tag{154b}\label{ch4:eq:154b}` and `\tag{156c}\label{ch4:eq:156c}`. Report the misnumber. A condition without a brace stays inside the display: `\qquad (t \ge t_o)` in (156) and `\qquad (t \ge t_1)` in (159). The `empheq` package is loaded in preamble.tex. The ranges of (73)-(74) form a column: `&& (0 \le t \le t_m)`.
- **Assignment lists** ((76)-(82), (83)-(87), (92)-(105), (106)-(115), (116)-(124), (125)-(131), (137)-(153)):
  - Use one numbered `align` per printed run, with one `\label` per row. A page break does not end a run; prose between the rows does.
  - Follow the typescript's layout: where a run's "=" signs are lined up ((92)-(97), (106)-(110), (116)-(120), (144)-(153)), align on "="; where they are not ((76)-(82), (138)-(143) ...), begin every row with `&` so the statements start at one column.
  - Keep "=" as printed (`y = y + \Delta y`, `t = t + \Delta t`). Never use `\gets`, `:=` or an arrow.
  - Stacked fractions stay stacked (`\frac{\Delta\dot{y}_a}{2}`) and slashed ones stay slashed (`\Delta v_a/2`, `[\ldots]/m(t)`).
  - The text steps are `&\text{calculate } C_1`, `&\text{calculate } C_2` and, in (143), `&\text{calculate or input } \omega_z`.
  - The typed "where" lists that follow use the Chapter 2 form: `\begin{itemize}[nosep,leftmargin=*,label={}]`, `\item $\Delta\dot{x}_t$ = drag-free ...`.
- **Wide displays** ((48)-(51), (56)-(60)):
  - Where the book breaks a display ((51), (58), (60)), break it at the same term with `split` inside `equation`. The continuation line starts with its +, set under the first term. The number stays centred between the lines, as printed.
  - Keep a one-line display on one line if it fits (`make unit` lists overfull boxes over 20pt).
  - If it does not fit, break it at an outermost + or − with `split`. Inside brackets, use `\biggl[`…`\biggr]`, not `\left`/`\right`.
  - A display that cannot be broken this way, because it is a single fraction ((48)-(50)), goes in `\begingroup\small … \endgroup` with no blank line around it. Use `\footnotesize` only if `\small` still overflows. Never use `\resizebox` or `\scalebox`.
  - Inside these brackets and radicals the letterer draws some stacked fractions small (t_2/2, t_2/m_2, t_n/m_n, (t−t_1)/m_2). Set them with `\tfrac`.
- **Repeated displays**: (16)-(17) are printed again on PDF 596 with their numbers. Set them as `\tag{16}` and `\tag{17}` in `equation*`/`align*`, with no `\label`; the labels stay on the first occurrence (PDF 552).
- **Stale citations**: several equation citations use numbers 35 higher than the printed equations: (175) on PDF 615, (189) on PDF 622, (195) on PDF 623, (200a) on PDF 625; and PDF 635 cites a "Figure 19" (Figure 16 is meant). Type them all literally, not as `\eqref`/`\ref`. The first three are corrected by the errata (corrections/ch4.md items 2-4) in the corrections step: no note in the faithful pass. (200a) and "Figure 19" get an `\ednote` naming the probable target ((165a), Figure~\ref{ch4:fig:16}) per section 6.
- **Connective words** printed at the right of a display ("and" after (16) on PDF 596 and after (163a) on PDF 624) are set as prose lines between the displays (section 4).
- **Unnumbered displays** such as `v = \frac{m}{k}\frac{\dot{u}}{u}` (PDF 557) and the identity `\cosh(A+B) = \cosh A\cosh B + \sinh A\sinh B` (PDF 568; A, B the Symbols list's dummy variables) stay unnumbered.
- **Numbers and units**:
  - A typed "x" between numbers is `\times` (`0.92 \times 10^{-4}`).
  - Leading-dot decimals stay as printed (`.001`, `.00833`).
  - Degrees are `\dg` (`1.11\dg`, `12\dg`, `\theta_o = 30\dg`).
  - The typed ½ is `\tfrac{1}{2}` (the engine class `$\tfrac{1}{2}$A`, and `\tfrac{1}{2}\rho\CD A_r`).
  - In prose and table cells, units stay as text: "0.04 kg", `396$v^{2}$ dyn-cm for $v$ in m/sec`, `(kg/m)/rad$^{2}$`, `g-cm$^{2}$`, and the header `$\omega_z$ (rad/sec)`. Use `\un{}` only for a unit attached to a number inside a formula.
  - Engine types stay plain text (B14, B4, D4, F100, F7).
- **Figures**: artwork labels stay in the images (Figure 2's ẏ = V_y, and the K/k, m_o and y_max of Figures 3-16). Symbols in typed captions follow this section: `$m_o$`, `$k_{\min}$`, `$x_b$`, `$y_b$`, `$\theta_o = 30\dg$`.
- **Table 2** (PDF 628-631, printed in two halves of about 5 columns) is one table of about 10 columns with its caption above: a `longtable` in `\small`, inside a `landscape` environment (pdflscape, loaded in the preamble) if it does not fit a portrait page. Table 1 is an ordinary table.
- **Macros**: no new macro is needed. The preamble's `\Isp`, `\CD`, `\CDo`, `\mdot`, `\dg` and `\un`, plus amsmath's `\tfrac`, `\text` and `\hat` (the last for the corrected (52)-(53)), cover the chapter. The brace groups use `empheq` and wide tables `pdflscape`, both loaded in preamble.tex.

## 16. Version 2 figures (settled at the pilot, 2026-09-30)

The line figures are redrawn as vector art in a modern style (the owner's decision): the same content, a
uniform modern look. Photographs and plates stay scanned. The plan is `~/.claude/plans/tamr-v2-figures.md`;
the per-figure record is `figures/v2/inventory.csv`; doubts and decisions are in `corrections/v2-figures.md`.

- **Files.** One standalone document per figure, `figures/v2/<dir>/<name>.tex` (the crop it replaces is
  `figures/<dir>/<name>.png`), `\documentclass[11pt]{standalone}` + `\usepackage{tamrfig}`, compiled from the
  repository root by `make figs` into `figures/v2/<dir>/<name>.pdf` (gitignored). Data files are named from the
  root. Curve data: `<name>.py` writes `<name>.csv` (or `<name>-*.csv`); curves shared by several figures live
  in `figures/v2/common/` (the B4, B14, E62 thrust curves). `make figdata` reruns the scripts.
- **Content invariants.** Keep every curve, printed label and value, axis quantity, unit and range, log scale,
  panel letter and circled reference letter, vector and its label, dimension and its value, the meaning of
  hatching, every formula and table in the artwork (typeset), and anything the caption or text relies on
  (a caption's "dashed" stays true). Figure lettering keeps the figure's own symbols (`corrections/v2-figures.md`,
  standing rules). Formulas and tables in the artwork are typeset in the book's notation (`\vec{V}`, `\cong`,
  `\CP`, `\CG`).
- **Size.** Drawn at final size, at most 6.5 in wide (the text block), included without scaling:
  `\includegraphics{figures/v2/<dir>/<name>.pdf}`.
- **Type.** newtx text and math (the book's); labels `\small`, tick labels `\footnotesize`; panel letters
  `(a)`, `(b)` in italic (`panel` style): at the upper right inside a plot's axes, at the lower right of a
  drawing's panel (where the 1973 drawings put their circled letters), on one baseline across a row.
- **Colour and ink** (`tamrfig.sty`). Ink `ink` (#0B0B0B) for outlines, vectors and text; `ink2` (#52514E) for
  axes (0.7pt), ticks (0.55pt), tick labels, centre lines, dimension and leader lines; gridlines `gridc`
  (#CFCEC6, 0.4pt major, 0.3pt minor, solid). The owner asked for the grid a step darker and the axes bolder
  and darker than the first cut: keep that contrast. Data curves 1pt in the categorical colours in fixed
  order: `s1` blue, `s2` orange, `s3` aqua (aqua only with a direct label); an ordered family of up to five
  curves takes `r1`-`r5` (light to dark); a larger family is one colour with a label on each curve. Two
  methods compared keep the printed solid/dashed as secondary encoding (`series1` solid, `series2` dashed).
  Text never takes a series colour.
- **Plots** (pgfplots): `tamr` (open left and bottom axes), `tamr grid` (a design chart read for values:
  hairline grid at the printed spacing), `tamr box`, `tamr sketch` (qualitative: arrowed axes, no numeric
  ticks). Tick labels with a leading zero (0.25, not .25); no thousands separator (2500). Curve labels
  directly on or beside the curve, set in a white knock-out only where no other curve passes; circled
  reference letters the text cites use `curve tag`. Reference levels and asymptotes: `guide`. True log axes
  (the 1973 "log" paper of Ch3 Figs 22, 26, 51, 52, 55 is not logarithmic between decades).
- **Drawings** (TikZ): outlines `outline` (0.6pt); force and velocity vectors `vec` (1.3pt, stealth head);
  lighter arrows `thin vec`; centre lines `centerline` (dash-dot); dimensions `\dimline` (label in a gap at the
  middle) with `extension` lines; callout leaders `leader`; hatching `hatch`/`hatch back` (45 and 135 degrees
  only); C.G. `cg mark` (quartered circle), C.P. `cp mark` (circle with centre dot); angles `angle arc`.
  Rockets: `\pic{rocket={model, ...}}` (the Chapter 1 model rocket; keys: length, diameter, nose, nose length,
  root chord, tip chord, span, sweep, fins, centerline, plume, lug), `\rocketoutline[<nose>]{<x/r stations>}`
  and `\rocketfins` for stepped bodies, `\plumeshape` for exhaust plumes. A pic takes its position but not its
  orientation from an enclosing rotation: give the rotation in the pic's own options. 3D drawings use a true
  orthographic view (Ch2 Fig 3: elevation 32 degrees, azimuth 45 degrees), right-handed axes as the book
  defines them.
- **Curve data.** Computed from the book's equations or tables when they determine the curve (the script
  names the equations); a qualitative sketch gets parameters matched to the scan; otherwise digitized with
  `tools/v2/digitize.py` (`lines`, `ticks`, `trace`, `overlay`; calibration `<name>.calib.json` against the
  crop). Every computed or digitized curve is overlaid on the scan: 95% of its points within 3 px (0.5 mm), or
  the mismatch goes to `corrections/v2-figures.md`.
- **Review.** `make fig F=<dir>/<name>` renders the figure beside its crop (`build/v2/png/`);
  `python3 tools/v2/review.py <keys>` builds a side-by-side review PDF; audits are
  `audit/v2-<dir>-<name>-roundN.md`; `check_numbering.py` check 10 accepts a switched figure only when its
  inventory status is audited.
