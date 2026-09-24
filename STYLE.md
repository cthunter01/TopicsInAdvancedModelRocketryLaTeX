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
  (e.g. a lone "(102b)" with no "(102a)"). Uppercase letters (144A): see preamble note.
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
```
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
