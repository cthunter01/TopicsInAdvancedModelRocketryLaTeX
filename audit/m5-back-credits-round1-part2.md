# M5 audit: Figure Credits, round 1, part 2 (scan PDF 660-663)

Compared: scan pages figures/pages/p660.png, p661.png, p662.png, p663.png (typescript pages -628- to -631-),
with zoomed crops at 300 dpi (build/zoom/audit_back-credits_r1_p2-*), against the unit render
build/unit/figure-credits-3.png, -4.png, -5.png (plus -3 as the page before; -5 is the last page).
No .tex file was opened. Because the standalone build prints "??" for every figure, plate and table
number, the numbers were checked from the undefined-reference lines of build/unit/figure-credits.log
(label names in input order), and each label was checked to exist in chapters/*.tex (label grep only).

## Placement

My content starts at render page 3 with the 4th Schlichting "Boundary Layer Theory" entry (Figure 16;
Figures 13-15 end scan p659) and ends at render page 5 with Table 8, the last entry of the section.
All of it falls under the Chapter 3 subheading, which is on p659 (the other auditor's range).
My pages have no headings.

## Items checked (37 paragraphs: 36 credit entries and 1 asterisk note)

| scan page | entries | link label (log) |
|---|---|---|
| p660 (-628-) | Figure 16, 17 (Schlichting, *Boundary Layer Theory*); 19, 20, 21 (NACA TN 4363); 23 (H. Schlichting); 24 (Hoerner, with "Hoerner\*"); asterisk note "\**Fluid Dynamic Drag* is distributed by Hoerner Fluid Dynamics, 2 King Lane, Greenbriar, Brick Town, New Jersey 08723."; 25 (Hoerner); 26 (Schlichting BLT); 27 (Prandtl and Tietjens) | ch3:fig:16, 17, 19, 20, 21, 23, 24, 25, 26, 27 |
| p661 (-629-) | Figure 28 (Prandtl and Tietjens); 29, 30 (Hoerner); 31 (Malewicki, "Model Rocket Altitude Performance", TIR-100); 32 (Stine, *Handbook of Model Rocketry*, copyright © 1970, 1967, 1965, Follett); 34 (Hoerner); 35, 36 (U.S.A.F. Stability and Control Datcom); 39 (Hoerner); 40 (Datcom); 41 (Aerobee experimental data after G.H. Stine); 42 (Hoerner) | ch3:fig:28, 29, 30, 31, 32, 34, 35, 36, 39, 40, 41, 42 |
| p662 (-630-) | Figure 44 (fin shapes after G.H. Stine); 46 (Datcom); 48 (Barrowman, "Calculating the Center of Pressure of a Model Rocket", Edited by Douglas J. Malewicki, TIR-33); 53, 54 (Hoerner); Plate 1 (*Shape and Flow*, Ascher Shapiro, © 1961, Educational Services, Doubleday); Plate 2 (*Applied Hydro- and Aeromechanics*, Dover); Plate 3 (*Boundary Layer Theory*, McGraw-Hill, "Used by permission"); Plate 4 (*Applied Hydro- and Aeromechanics*) | ch3:fig:44, 46, 48, 53, 54; ch3:plate:1, 2, 3, 4 |
| p663 (-631-) | Plate 5 (*Applied Hydro- and Aeromechanics*); Plate 6 (Photo by G. Mandell); Table 1 (*Boundary Layer Theory*); Table 5 (*Fluid Dynamic Drag*, "published by the author in 1965. Reprinted by permission"); Table 8 (Experimental data after Dr. S.F. Hoerner, "Used by permission") | ch3:plate:5, 6; ch3:tab:1, 5, 8 |

For each entry I checked: the word (Figure, Plate, Table) and its number (label order in the log is
exactly the scan order, with no gaps or extra entries); every word and punctuation mark of the credit
(including "published by the author 1965" in the figure entries vs "in 1965" in the table entries,
"by permission" vs "Reprinted by permission" vs "Used by permission", the full stop before the closing
parenthesis in the plate and table entries and its absence in the figure entries, the commas after the
closing quotes in Figures 31 and 48, lower-case "fin shapes" in Figure 44, "Edited" capitalised in
Figure 48); the © sign and years; the report numbers (NACA TN 4363, TIR-100, TIR-33, ZIP 08723);
the extent of the emphasis (all underlined title words, including "and" and "of", are italic and nothing
else is); the asterisk after "Hoerner" in Figure 24 and the asterisk note typed as its own paragraph;
one paragraph per entry. All 36 referenced labels exist in the chapter files. The log has no warnings
other than the expected undefined references.

Silent fixes verified (not discrepancies): "Prandl" to "Prandtl" (Figures 27, 28; Plates 2, 4, 5);
"Thebry" (a struck-over "o") to "Theory" (Table 1); "Publicat;ions" (stray strike) to "Publications"
(Plate 5). Not reported as layout: the scan has no space in "©1968" in Figures 16, 17 and 26 but has one
elsewhere; the render uses "© 1968" throughout, which is spacing only. Straight typewriter quotes are set
as curly quotes, per STYLE.md section 3. The space after "Dr." is an ordinary interword space (checked in
the PDF word boxes), not a sentence space.

## Discrepancies

| where | scan reading | compiled reading | severity |
|---|---|---|---|

none
