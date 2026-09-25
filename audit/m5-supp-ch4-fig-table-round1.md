# M5 audit: supplement, replacement Figure 4 and Table I corrections of Chapter 4 (round 1)

I compared the scan images with the unit render `build/unit/s-ch4-fig-table-{1,2,3}.png`. I did not open any .tex file.

## Pages and items checked

- **PDF 711 (replacement Figure 4, typed page "-548-")**
  - Heading `[Replacement Figure 4 of Chapter 4]` (editorial, bracketed): present.
  - Figure image `ch4-fig04-1994.png`: the full plot is present. It has the legend "Actual curve / Approximation", the axes F (N) 0-16 and t (sec) 0-1.2, the label B4, and the parameter block I_t = 5.0 N-sec, F_m = 13.0 N, F_s = 3.5 N, t_1 = 0.14 sec, t_2 = 0.22 sec, t_b = 1.20 sec (zoomed). It has no page number.
  - Caption: I checked it word by word against the zoomed scan, including "Figure 4:", "piecewise-linear", "NAR Type B4" and the added 1994 sentence "t_1 as shown here is t_m as defined for equations (73) through (75), and t_2 as shown here is t_s as defined for equations (73) through (75)." The subscripts are 1, m, 2 and s; the s of t_s is lowercase, zoomed. The compiled caption matches.
    - The equation references print "(??)" in the standalone build. The unit log shows they point to `ch4:eq:73` and `ch4:eq:75`, which `build/chapters/ch4.aux` resolves to 73 and 75. That is correct.
- **PDF 580 (1973 Figure 4)**
  - The \edcap line "[Editor's note: The 1973 Figure 4, which this figure replaces:]" is true: PDF 580 is the 1973 Figure 4 (book page 548).
  - Image `figures/ch4/fig04.png`: it matches the plot on PDF 580.
  - The 1973 caption matches PDF 580 word by word (zoomed; the typewriter "4:" is a colon).
- **PDF 712 (Table I corrections)**
  - Heading: "CORRECTIONS TO ROCKET CHARACTERISTICS IN TABLE I OF CHAPTER 4, ON PAGE 595 OF ORIGINAL BOOK" (zoomed; "TABLE I" is a Roman I). The compiled heading has the same wording in title case.
  - Table header: Characteristic | Value.
  - Rows:
    - "Fin cant angle for ω_c = ω_cres" | "0.00993 radian = 0.569°"
    - "Fin cant angle for ω_c = 10ω_cres" | "0.0993 radian = 5.69°"
    - "k" | "0.92 x 10^-4 kg/m without fin cant / 0.921 x 10^-4 kg/m with 0.569° cant / 1.016 x 10^-4 kg/m with 5.69° cant"
    - All digits, exponents, degree signs and wording were zoomed and match.
    - The subscript c of ω_c is lowercase and set in italic. cres is set upright, following the Chapter 4 convention in STYLE.md section 15.
  - Bracketed note: "[NOTE: There will be consequential corrections to altitudes attained by rockets with canted fins]" (zoomed). It matches, including the missing final period.
  - The \edcap "Table ?? of Chapter ?? labels these two rows with ω_z, the roll rate, where this page has ω_c." is true:
    - PDF 627 (book page 595, Table 1) prints "ω_z = ω_cres" and "ω_z = 10ω_cres".
    - STYLE.md section 15 defines ω_z as the roll rate.
    - The refs `ch4:tab:1` and `ch4` resolve to 1 and 4 in `build/chapters/ch4.aux`.

## Discrepancies

none
