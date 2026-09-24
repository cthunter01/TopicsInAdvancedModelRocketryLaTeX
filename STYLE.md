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
  mechanically). All macros live in `preamble.tex`.
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
