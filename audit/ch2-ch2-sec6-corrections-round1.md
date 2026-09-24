# Audit: ch2-sec6 corrections, round 1

Items audited: 7 (new text of p.251 and new (115)), 8 (new Figure 52), 9 (new text of p.253 and the
top of p.254, (116), (117)), D13 (the 1973 "Figure 52" citation). D12 stays. D14 is superseded.

Sources read: p683, p684, p685, p686 (2022 correction); p281, p282, p283, p284 (1973 pages); git HEAD
of chapters/ch2-sec6.tex. Zoomed renders: build/zoom/audit_ch2-sec6_r1-p683eq-683.png (2022 (115)),
build/zoom/audit_ch2-sec6_r1-p685a-685.png (2022 (116)), build/zoom/audit_ch2-sec6_r1-p685b-685.png
(2022 (117)). An earlier auditor's crops of the 1973 (116) and (117) on p283 were also read.

## What was checked

### Scope of the diff
`git diff HEAD -- chapters/ch2-sec6.tex` has two hunks.
- Hunk 1 runs from "rockets." (end of the first line of p.251) through the paragraph after (117).
- Hunk 2 inserts the Figure 52 float and replaces the "Given the ability..." paragraph.

Nothing else changed. The Figure 51 float, the D12 note (l.48) and the paragraph "In cases where it
is desired..." are identical to HEAD.

### Item 7 (p683 against p281 and HEAD)
- **Extent.** 1973 p.251 begins "spin in model rockets." and ends with (115), as does the 2022 page.
  The whole page is replaced. Nothing from p.251 is left behind.
- **Prose.** Both paragraphs were compared with p683 sentence by sentence and match:
  - "horizontal distance of the rocket from its launch site"
  - "intended direction of flight"
  - the order "airfoiled fins, canted fins, and ``spinnerons''"
  - "flywheel-like devices have been installed"
  - `$I_R\omega_Z$ \emph{other}` (underlined in the source)
  - "aerodynamically-induced roll", "the equilibrium roll rate as"

  The hyphens in "dispersion-reduction" and "aerodynamically-induced" are real. Mandell hyphenates
  -ly compounds throughout ("statically-stable").
- **(115)** matches the zoomed p683 symbol by symbol:
  `6\theta V\bar{Y}_T(1+\lambda)k_r / {[(1+3\lambda)s^2 + 4(1+2\lambda)s r_t + 6(1+\lambda)r_t^2]k_d}`.
  `\label{ch2:eq:115}` is kept.
- **Mathematics check.** Strip theory gives
  omega = V theta ∫c xi dxi / ∫c xi^2 dxi.
  - ∫c xi dxi = s c_r(1+lambda)/2 · Ybar_T, with Ybar_T measured from the axis, as in (90).
  - ∫c xi^2 dxi = (s c_r/12)[(1+3lambda)s^2 + 4(1+2lambda)s r_t + 6(1+lambda)r_t^2].

  The ratio is exactly the new (115) before the k_r/k_d factor.
- **\ednote E2.** It is placed at the start of the replaced text, after "rockets.", outside any
  display. Each statement was checked against HEAD and p281:
  - The 1973 "dispersion" definition is quoted exactly.
  - The 1973 sentence introducing (115) is quoted in full and exactly.
  - The 1973 (115) is quoted in full: `12\theta V A_r\bar{Y}_T k_r/\{s c_r k_d[...]\}`.
  - The rewordings listed are right: axis/direction, the order of the techniques, and "from time to
    time ... have appeared".
  - The Alan V. Jones / 18 Feb 1986 statement and "all fin-induced roll" agree with the p683 header.

### Item 8 (p684, p687)
- **Placement.** The float comes immediately after the Figure 51 float.
- **Float.** It follows STYLE.md section 7: the width/height/keepaspectratio options, and
  `figures/supplement/ch2-fig52-2022.png`, included once.
- **Manifest.** The manifest row sup-ch2-fig52-2022 (PDF 687) names that file. The crop excludes the
  printed title line, so the caption is not duplicated in the artwork.
- **Caption.** "Roll Rates to Avoid to Keep $\mathit{AR}_c$ from Exceeding $1.25/C_1$" matches the
  p684 title "ARc ... 1.25/C1", with section 13 notation.
- **\edcap.** Its content is as specified.
- **Label.** `\label{ch2:fig:52}`.
- **List of figures.** There is no \listoffigures, so the \edcap cannot leak into one.

### Item 9 (p685-p686 against p283-p284 and HEAD)
- **Extent.** The replaced text runs from "where" (the top of p.253) to "...the low spin rate needed
  for resonance." (the end of the first paragraph of p.254). This matches the 2022 text and its
  bracket "[The remainder of the text on Page 254 is unchanged]". The next paragraph, "In cases where
  it is desired...", is untouched.
- **Where-list.** "where:" and the list (theta twice, `\theta = -(\alpha_0)`, alpha_0, V) match p685
  word for word. `Reference~\ref{ch2:ref:12}` is used, and that label exists in ch2-refs.tex. The
  list environment `[nosep,leftmargin=*,label={}]` matches the chapter's other where-lists.
- **(116)** matches the zoomed p685 symbol by symbol:
  - The four lines break where the 2022 page breaks them.
  - The outer braces are `\Bigl\{ ... \Bigr\}`, larger as printed.
  - The second term has `[(\tau^2+1)/(\tau-1)]^2`.
  - The label is kept.

  Against Barrowman's roll forcing interference factor, the corrected second term
  pi(tau^2+1)^2/(tau^2(tau-1)^2) is right. The 1973 term (tau+1) was the error.
- **(117)** matches the zoomed p685. The label is kept.
- **Paragraph after (117).** It matches p685:
  - `$\bar{Y}_t$` is set with a lowercase t, as the 2022 page prints it.
  - `equation~\eqref{ch2:eq:90}` points to the 1973 (90), the radial position Ybar_T of the fin C.P.
    This is consistent with the recorded numbering decision and with the new (115).
  - `Figure~\ref{ch2:fig:36} in Section~\ref{ch2:sec:4.1}` and
    `equations~\eqref{ch2:eq:115} through~\eqref{ch2:eq:117}` are used.
- **"Given the ability..." paragraph.** It matches p685-p686 sentence by sentence:
  - "of a proposed rocket", \emph{deleterious}, "by the fins"
  - `\omega_{\mathrm{cres}}` twice
  - `\beta_c = \omega_Z/\omega_{nc}`, 25\%, `Figure~\ref{ch2:fig:52}` twice
  - "roll-coupled resonant frequency", "low roll rate"
  - the rule-of-thumb sentence with `\zeta_c`, 0.44, 1.35 and 2.0 `\omega_{nc}`
- **\ednote E3.** It is placed at "where:", where the replaced text starts, outside any display.
  - The 1973 (116) is quoted in full. It was verified against p283, zoomed: the same six terms in the
    same order, with (tau+1)/(tau-1) in the second term. The claim "(tau+1) where the corrected second
    term has (tau^2+1)" is the only difference, and it is right.
  - The 1973 (117) is quoted in full, and the claim that it is the same expression as the corrected
    one was verified.
  - The 1973 "where k_r ... is given by", the "fin canting" sentence, the omega_nc sentence and the
    "Figure 52" sentence are quoted exactly as in HEAD.
  - The listed rewordings ("is given by" for "is", "a proposed rocket"/"his rocket",
    "roll-coupled resonant frequency", "roll rate"/"spin rate") are right.
  - The closing-sentence statement is right.

### D13
The 1973 sentence "The selection of available relations ... is illustrated in Figure~52." spans
pp.253-254 and lies inside the text that item 9 replaces. It is correctly removed, together with its
faithful-pass \ednote. The Figure 52 \edcap now says that the figure is cited but missing in 1973.

### Labels and notation
- Labels ch2:eq:115, 116 and 117 are kept. There are no new equation labels, since no new equations
  were added. The one new label is ch2:fig:52.
- The notation in the corrected passages follows STYLE.md section 13: `\omega_Z`,
  `\omega_{\mathrm{cres}}`, `\omega_{nc}`, `\beta_c`, `\zeta_c`, `\alpha_0`, `\mathit{AR}_c`,
  `\bar{Y}_T` in (115), `\arcsin`, `\ln`.

### Rendered pages
build/unit/ch2-sec6-08.png to -11.png were built at 05:30:48, after the last edit to the .tex at
05:30:47.
- Equations are numbered (115), (116), (117) in sequence, and Figures 51 and 52 are in sequence.
- (116) sets cleanly on four aligned lines with large outer braces.
- The where-list renders without bullets.
- The E2 and E3 footnotes render in full.
- The ?? are only for labels in other units: ch2:ref:12, ch2:eq:90, ch2:fig:36, ch2:sec:4.1 and
  ch2:sec:3.2.5, all of which exist in their own units.
- The log has no overfull boxes and no multiply-defined labels.

### Observations, not discrepancies
- The E3 note writes the 1973 (116) in linear form with the 2022 bracket style: outer {}, inner []. The
  1973 display has outer square brackets and parentheses. The content is identical. The E2 note
  linearizes the 1973 (115) the same way.
- The E3 note lists "the added reference to Figure 36" under "only reworded". Strictly this is an
  addition, but the note states it, so it is not hidden.
- "The 1973 equation (115)/(116)/(117)" is written with bare numbers inside the notes. This follows the
  convention of the Chapter 1 correction notes ("the 1973 equation (5) read").

## Discrepancies

none
