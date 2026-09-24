# Audit: Chapter 3 prose check (tools/prose_diff.py)

Every page that tools/prose_diff.py did not pass was checked against the scan by the assembly step; its conclusions are recorded here because build/prose-ch3.md is regenerated on every build.

Chapter 3 (PDF 291-528), from build/prose-ch3.md: 204 pages checked. 140 pass, 64 inspect, 0 missing. 34 pages skipped (fewer than 30 tokens). 121 windows flagged. No page is flagged as likely dropped, so I added no artwork_pages entry for ch3.

Method: for every inspect page, I listed each pair of adjacent OCR words that are real words (both appear somewhere in the compiled text) but do not appear side by side in build/main.pdf. A dropped or garbled passage would show up as a run of such pairs. I checked each hit against the .tex, and against the scan where it was not obvious (full page or zoom: 302, 305, 309, 310, 368, 373, 383, 384, 385, 374, 408). Result: no prose is dropped, garbled or duplicated. Every flag comes from OCR noise, hand-lettered maths, lettering inside figures, math or \ref tokens, or pdftotext reordering floats and running heads.

Per page:
- 294, 296, 298: Symbols list. Subscripts such as cant, turb, stag and tot are set as math; the rest is OCR noise (oross, seoond, ilig). OK.
- 302: very noisy OCR (muximum, oonta, duta, soociation, ueasurd). Checked line by line against the scan; text complete.
- 305: OCR noise (tsel, stron, sooe). Scan checked; complete.
- 308: Figure 1 page. The OCR is the lettering inside fig01 (size, shape, airspeed, finish, angle of attack, density, viscosity, speed of sound); the caption is transcribed.
- 309, 310, 311, 313: OCR noise (lfhich, anderstanding, thnt, lcinecatio, M1deal1zed, r~:'lge = range, 1111near) plus the hand-lettered gas-law display. Scans 309 and 310 checked; complete.
- 326: caption page for Figures 9 and 10, plus artwork lettering ("they coordinate" is "the $y$ coordinate"). Captions complete.
- 329: "turn moon" = Saturn V; "types ot !low problems"; launch-site hyphen. Complete.
- 334: OCR lost the underlined "can be less". Complete.
- 345: "~late 1" = Plate 1; "!light". Complete.
- 347: OCR noise and the hyphen in three-dimensional. Complete.
- 352, 354, 358, 359, 366: hand-lettered displays (Blasius, eqs 35-68) and OCR noise (ncnr, asYID.ptot1cally). Complete.
- 368: Table 2. Compared cell by cell with the scan; complete.
- 373: Table 3 page (Table 3 has no caption in the book). Complete.
- 380: k_crit maths plus OCR noise (enollgh, 1:n.fluence). Complete.
- 384: "given in Reference 15" confirmed on the scan. Complete.
- 385: OCR noise plus eqs 94-96. Scan checked (no comma after eta); complete.
- 388: OCR garbled the underlined phrase "as if it had been turbulent all the way from". Complete.
- 391, 395, 399, 402, 404: OCR noise (effeots, boundatz, thla, mdary, lqer, renee, preasure, pigure, suboritical, emblee). Complete.
- 408: "design:" confirmed on a zoom. Complete.
- 418, 422, 426, 427, 430, 431, 433, 434, 435, 439, 441: OCR noise (oenturi, MaleW1ck1, Sk;ychute, boerner, boatta, fioiently, vetted, ooeff, "aide :force" = side force, acqllire) plus displays 119-125, 142-144 and the worked arithmetic. Complete.
- 442, 448, 469: caption pages for Figures 38/39, 40/41 and 44/45 ("tip sha pes", "light" = flight, irobee ocket). Captions complete.
- 445, 447, 449, 451: OCR noise (planfonn, interfe~ence, and bodz liftfininlift, which is the K_F(B)/K_B(F) definition set as math; oefhc iellt). Complete.
- 460, 461, 463, 467: OCR noise ("give n", heading "Simple ~ Rockets", J\1st, plan.form, trai1ing). Complete.
- 477, 479, 489, 491, 498, 500: displays 181-210 and fin-area arithmetic; OCR noise (Pollow1ng, fwiotion, rarel1, fore!). Complete.
- 516, 519: OCR noise ("light" = flight; "t h e ~" is the underlined "cube"). Complete.
- 527, 528: References. OCR noise (Ori ti cal, Og1ve, Rydro, Aeroruechanics, Fublications). All 20 references present.

Repeated 8-grams involving Chapter 3: every one is legitimate.
- Table of contents entries against their headings (3.1, 3.5.1, 3.6, 6/6.1, 6.3.2, 6.3.3, 7).
- Symbols entries against text: the two "... based on maximum frontal cross-sectional area" entries; C_Dc and eta against the p439 definitions.
- Gregorek's paper title: quoted on p303 (Introduction) and p462 (6.1), and again in Reference 1.
- The Figure 19 and 20 captions, which are identical in the book except "flat plate" vs "cone" (scan p383).
- The Figure 13-15, Table 1 and Figure 17 captions, which share "boundary layer over a flat plate at zero angle of attack".
- The Table 4 and Figure 41 captions, which share their opening in the book.
- "Step 1: Forebody drag coefficient", printed twice in the Javelin recalculations.
- Running-head artifacts.
- References 12 and 13 (Prandtl and Tietjens).
- Barrowman TIR-33 and Davis, Follin and Blitzer, which also appear in Chapter 2's reference list.
No duplicated transcription.
