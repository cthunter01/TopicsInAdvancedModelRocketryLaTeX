# M5 audit: supplement, 1994 Chapter 2 documents (round 1, part 1)

Scan pages checked: PDF 676, 677, 678, 679 (figures/pages/p676.png to p679.png), with 300 dpi zooms of
the p676 bracketed instruction and first paragraph, all handwritten equations on p678 ((85) to (89) and
the tau definition) and p679 ((90) to (92)).
Render pages checked: build/unit/s-ch2-1994-1.png to -4.png (content), -5.png (neighbour; New Figure 36,
belongs to the other auditor).
Also read for the editorial note: scan PDF 225 and 226 (1973 book pages 195 and 196); the chapter
labels (grep of chapters/*.tex), and the \newlabel entries in build/*.aux and build/unit/s-ch2-1994.aux/.log.
No .tex file was opened.

## Items checked

### "Correction to Original Pages 186 Through 196 of Chapter 2" (p676-677, render 1-2)
- Heading: wording matches (title case of the typed capitals); label supp:ch2-186 present in the aux file.
- Paragraph 1 ("Barrowman's method ... accomplished is"): every word matches; "normal force coefficient" underlined -> italic; "angle of attack" quoted; alpha.
- Display N = (rho/2) C_N A_r V^2: matches.
- "where" list: N = normal force; rho = mass density of air; A_r = reference area ... "and I will follow his convention.": every word matches, aligned on "=".
- "For small angles of attack [typically 0.2 radian (about 11.5 degrees) or less] ... C_N can then be expressed as": matches (degree sign, brackets).
- Display C_N = C_{N alpha} . alpha: matches (centre dot).
- "where C_{N alpha} is the derivative (or "slope") ... (C_N = 0, alpha = 0). That is,": matches.
- Display C_{N alpha} = (dC_N/d alpha)|_{alpha=0}: matches (evaluation bar, subscript alpha = 0).
- Paragraph "The slope of the normal force coefficient curve ...": "normal force curve slope" and "lift curve slope" underlined -> italic; "1/radians or radians^-1": matches.
- Centred bracketed instruction "[Text beginning with "Throughout the rest of this treatment.... is unchanged ... at the bottom of page 187. That paragraph changes to the following:]": matches.
- Indented paragraph "Now the normal force curve slope ... center of pressure (C.P.) ... of the complete rocket.": matches; "center of pressure" underlined -> italic.
- Centred bracketed instruction on p677 "[In the rest of Section 4.1, from page 189 thorough page 196 and in the captions of Figures 34, 35, and 36, the phrase "normal force coefficient" is to be replaced with "normal force curve slope" wherever it appears except in the paragraph ... on page 193. That paragraph is to remain unchanged.]": matches; "except" underlined -> italic; the refs for Section 4.1 and Figures 34, 35, 36 point at ch2:sec:4.1 and ch2:fig:34/35/36, which exist ("??" in the standalone build, as expected).
- Page number "2" at top of p677: not transcribed (correct).

### "Corrections and Clarifications to Fin Normal Force Curve Slope Equations on Page 195 of Original Text" (p678-679, render 3-4)
- Heading: wording matches; label supp:ch2-fins present in the aux file.
- Bracketed instruction "[Starting with the sentence that begins at the bottom of page 193 of the original text, substitute the following text for the original]:": matches (flush left, colon after the bracket).
- "The normal force curve slope of a single fin is given by" (indented): matches.
- (85) (C_{N alpha})_1 = AR ((c_r + c_t)/r_r)(s/r_r) / (2 + sqrt(4 + (AR/cos Gamma_c)^2)): symbol by symbol match, including the radical's extent over the squared term and the tag (85).
- "where AR is the aspect ratio of the wing of span 2s that would be created if two fins were joined at the root:": matches.
- (86) AR = 4s/(c_r + c_t): matches.
- "If we define the distance ... as l, we have" and (87) l = s/cos Gamma_c: match (script l).
- "Equations (86) and (87) can be used to cast equation (85) into a simpler form. Substituting" / "4s/(c_r + c_t) for AR and l/s for 1/cos Gamma_c in equation (85), we obtain": matches.
- (88) (C_{N alpha})_1 = 2(s/r_r)^2 / (1 + sqrt(1 + (2l/(c_r + c_t))^2)): matches, including radical extent.
- "The normal force curve slope of a complete set of N fins, where N must be three, four, or six, is" and (89) (C_{N alpha})_T = (N/2)(C_{N alpha})_1: match.
- Paragraph "The airflow about the fins, however, ... "interference coefficient" K_{T(B)} by which (89) is to be multiplied ... If we let": matches.
- Unnumbered tau = (s + r_t)/r_t: matches.
- "then the value of the interference coefficient for three- and four-finned configurations is given by": matches (hyphens kept).
- (90) K_{T(B)} = 1 + 1/tau; "and its value for six-finned configurations is"; (91) K_{T(B)} = 1 + 1/(2 tau); "so that the applicable value of the normal force curve slope is"; (92) (C_{N alpha})_{T(B)} = K_{T(B)} (C_{N alpha})_T: all match, tags (90)-(92).
- Closing instruction "[continue with the original text on the bottom of page 195, as changed by the previous correction that substituted the phrase "normal force curve slope(s)" for "normal force coefficient(s)" everywhere it appears].": matches (lower-case "continue" kept).
- Case of the hand-lettered c_r, c_t and s follows the typed prose ("span 2s") and the chapter's notation: intended.

### Editorial note (render 3), statement checked
"[Editor's note: Chapter 2 numbers equations (85)-(88) of this document as printed and its (89)-(92) as (89')-(92'), because the 1973 equations (89)-(92), which follow them, keep their numbers.]"
True: build aux files print ch2:eq:85-88 as 85-88 and ch2:eq:n89-n92 as 89'-92'; the 1973 page 195
(PDF 225) holds (85)-(88), which the 1994 text replaces, and the text it continues with ("The longitudinal
position of the C.P. of any one fin ...", bottom of page 195) leads to the 1973 (89)-(92) on page 196 (PDF 226),
which keep labels ch2:eq:89-92.

## Typing slips fixed silently (not discrepancies)
- p676: the typescript has no closing quotation mark after "Throughout the rest of this treatment...."; the render adds it.
- p677: "thorough page 196" -> "through page 196".

## Observation outside the transcription
- The class's running head on render page 2 sets the digits of "CORRECTION TO ORIGINAL PAGES 186 THROUGH 196 OF CHAPTER 2" upright among italic capitals. This comes from the document class, not the transcription, and the scan has no running heads.

## Discrepancies

none
