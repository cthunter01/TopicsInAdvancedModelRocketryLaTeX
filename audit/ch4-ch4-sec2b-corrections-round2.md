# ch4-sec2b corrections audit, round 2

Unit: chapters/ch4-sec2b.tex (Sections 2.3-2.5, PDF 571-596). Diff audited: `git diff HEAD -- chapters/ch4-sec2b.tex`
(HEAD is the faithful 1973 transcription). Items: 8 (the replacement Figure 4, PDF 711) and D4 (the legend line, PDF 587).
Sources read: STYLE.md sections 4, 7-11 and 15, corrections/ch4.md, the round 1 report, PDF 580, 587, 588-595 (text
layer), 699, 703-710 (text layer) and 711.

## Round 1 finding

- Figure 4 \edcap attribution (l.217): **fixed**. The first sentence now reads "Figure and caption replaced per the
  replacement Figure 4 of the supplement (no author or date shown)." I re-checked the sources. PDF 711 shows only
  "-548-", the drawing and the caption. PDF 699, Mandell's signed cover note for "Changes to text of Chapter 4",
  covers only the thrust equation and does not mention Figure 4. The new wording matches the ch4-sec2a Summary note
  ("... (no author or date shown)") and the ch4-sec4 Table 1 \edcap ("per the supplement ..."). Nothing else in the
  note changed.

## What was checked

### Item 8: Figure 4
- **Image.** The figure includes `figures/supplement/ch4-fig04-1994.png` exactly once, in place of
  `figures/ch4/fig04.png`. It matches manifest row sup-ch4-fig04-1994 (owner ch4-sec2b). The crop leaves out
  "-548-" and the typed caption, as the render confirms. Row ch4-fig04 is now owned by "supplement". No chapter
  file includes `figures/ch4/fig04.png` any more. `\label{ch4:fig:4}` is kept and follows `\caption`. The figure
  still sits right after the paragraph that cites it.
- **Caption against PDF 711.** It matches word for word: the two 1973 sentences plus "t_1 as shown here is t_m as
  defined for equations (73) through (75), and t_2 as shown here is t_s as defined for equations (73) through
  (75)." The comma and the final period are as printed. The four citations are `\eqref{ch4:eq:73}` and
  `\eqref{ch4:eq:75}`. (73) is the subequations parent label, so it prints "(73)". The subscripts are italic, as
  section 15 requires.
- **Mathematics.** From (73): the approximation rises to F_m at t_m and falls to F_s at t_s. The artwork's peak is
  at 0.14 s and its drop to the sustainer level is at 0.22 s, so t_1 = t_m and t_2 = t_s, as the new sentence says.
  I rederived (75) from the three-segment area: F_m t_m/2 + (F_m + F_s)(t_s - t_m)/2 + F_s(t_b - t_s)
  = F_m t_s/2 + F_s(t_b - t_m/2 - t_s/2). With the figure's values, 13.0(0.22)/2 + 3.5(1.20 - 0.07 - 0.11)
  = 1.43 + 3.57 = 5.00 N-sec, which equals the printed I_t = 5.0 N-sec. No doubt note is needed.
- **Artwork, PDF 580 against PDF 711.** I normalised element positions to the axes (0 to 1.2 s, 0 to 16 N). Both
  pages put the parameter block (I_t) at about 0.40-0.41 of the t axis and F of about 10.2-10.3, "B4" at 0.44 and
  F of about 1.8, and the legend at 0.15. The curves, dashes, ticks and labels match. It is the same drawing. Its
  width is about 246 pt on the 499 pt page 580 and about 422 pt on the letter-size page 711, so the drawing is
  about 1.7 times larger. It also fills more of the text width (about 62% against 94%). The y scale is about 5%
  taller relative to x, which is a reproduction effect. "The artwork is unchanged: it is the same drawing,
  reproduced larger" is accurate.
- **\edcap.** Inside `\caption`, as section 9 allows. There is no list of figures, so the note is not echoed
  anywhere else. The quoted 1973 caption matches git HEAD and PDF 580 word for word. "Without the last sentence,
  which relates the figure's t_1 and t_2 to the t_m and t_s of the text" is accurate. "The 1973 figure is
  reproduced in the supplement Part" agrees with the manifest's ch4-fig04 row, the Decisions and the Chapter 1
  and 2 precedents.
- **Summary (PDF 703-710).** Its only item on Section 2.3 is "Solutions for a Non-Oscillating Rocket in the
  Coasting Phase: Add a treatment of the extended Caporaso-Bengen solution ...". This is a plan, not a correction.
  The Decisions exclude it, and the ch4-sec2a Summary note already lists it as not carried out ("a treatment of
  the coasting phase by the Caporaso-Bengen method"). So leaving this unit unchanged is correct. The errata
  (PDF 664: pp. 534, 583, 590, 591) touch nothing in printed pp. 539-564.

### D4: legend line (PDF 587)
- **Transcription.** PDF 587 prints "Figures 5.5 - 5.9:". The transcription keeps it as printed ("5.5--5.9").
- **Accuracy.** The paragraph below and the key table ("Figure number" 5-9) number these figures 5 through 9.
  The panel captions on PDF 588-595 are "Figure 5(a):" through "Figure 9(c):" (labels ch4:fig:5a to ch4:fig:9c).
  No other decimal figure number appears in the transcribed chapter. The OCR text layer drops this legend line
  altogether, so a scan search cannot confirm it. The claim therefore rests on the audited transcription and the
  captions. Neither the errata nor the supplements touch printed p.555. The note's claims hold. It follows the
  chapter's doubt-note style.
- **Placement.** An `\ednote` in a `\noindent` prose line, not in a display, caption or table. This is legal.

### Scope, labels, notation
- **Scope.** The whole diff is:
  - the header comment naming the two items;
  - the `\includegraphics` path;
  - the caption sentence and the \edcap;
  - the rewrapped PDF 587 comment;
  - the D4 \ednote.
  No other line changed.
- **Labels.** There are no new equations, so no n-labels. The 1973 label ch4:fig:4 is kept.
- **Notation.** The new caption follows section 15 notation.
- **Other doubt items.** D4 is the only D-item for this unit. D15's last-digit rounding in the PDF 587 key table
  correctly has no note.

### Rendering (not rebuilt)
- **Freshness.** build/unit/ch4-sec2b-*.png and .pdf date from 18:36:07-18:36:26, after the source (18:35:31).
- **Page 6.** Figure 4 in its 1994 form, with no page number or caption in the crop. The caption prints "(73)
  through (75)" twice as links, and the \edcap text is complete, with the revised first sentence.
- **Page 8.** "Figures 5.5–5.9:" with marker E1, and the complete note in the footer.
- **Log.** No overfull boxes and no errors. The undefined references (ch4:sec:2.1, ch4:sec:2.2, ch4:eq:12, ch1)
  are outside the unit, as expected in a standalone build.

## Discrepancies

none
