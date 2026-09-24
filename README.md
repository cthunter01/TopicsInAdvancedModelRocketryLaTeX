# Topics in Advanced Model Rocketry — LaTeX edition

A LaTeX transcription of *Topics in Advanced Model Rocketry* (Mandell, Caporaso, Bengen; MIT Press 1973),
dedicated to the public domain by the authors in 2025, including the 2025 front matter, the 1973 errata
and the authors' 1994/2022 corrections. Version 1: typeset text, mathematics, tables and symbol lists;
figures are cropped from the scan. Version 2 will vectorize the figures.

## Source

`Topics_in_Advanced_Model_Rocketry.pdf` (712 pages, 42 MB, not tracked in git).
sha256: `51b26ed677ca17e7db7638ecc3454bbf77c8eedf78b19b3415b49dd7430c60ae`

## Build

    make all            # full build -> build/main.pdf, then structural and prose checks
    make chapter N=1    # fast build of one chapter (\includeonly)
    make unit U=chapters/ch1-sec1 PRE='\def\chapstart{1}\def\eqstart{0}'   # standalone compile of one unit
    make final          # build with every \draftnote turned into a hard error
    make pages          # extract native page bitmaps to figures/pages/ (needs the source PDF)
    make figures        # crop figures listed in figures/manifest.csv

Toolchain used: TeX Live 2026 (pdflatex, newtx, manyfoot, newfloat, placeins), latexmk 4.87,
poppler 26.08 (pdfimages, pdftotext, pdftoppm), Python 3 with Pillow 12.3 and numpy.

## Layout

See `STYLE.md` for the transcription conventions, `inventory/` for the expected equation/figure lists,
`corrections/` for the per-chapter correction checklists and `audit/` for the equation audits.
