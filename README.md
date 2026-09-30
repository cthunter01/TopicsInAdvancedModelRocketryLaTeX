# Topics in Advanced Model Rocketry — LaTeX edition

A newly typeset LaTeX edition of *Topics in Advanced Model Rocketry* (Gordon K. Mandell, George J. Caporaso,
William P. Bengen; The MIT Press, 1973), made from the 712-page scan that the authors released in 2025,
when they dedicated the work to the public domain. It contains the 2025 front matter (title pages, public-domain
notice, "Historical Perspective", author photographs), the 1973 front matter (title pages, dedication,
Publisher's Foreword, Preface), an editorial note "About This Edition", Chapters 1-4, Appendixes A-D, the
figure credits, and a final Part, "Errata and Supplement", that reproduces the 1973 errata sheet and the
authors' later corrections (Mandell's of June 1994 and 15 February 2022, and the undated ones). The output is
`build/main.pdf`.

## Status

Version 1.0: the complete book (front matter, Chapters 1-4, appendixes, figure credits, and the Errata and
Supplement Part) with the corrections applied. The corrections of the errata sheet and of the later documents
are made in the chapters, each with an editor's note that quotes what the 1973 edition read (purely
typographical ones without a note); the few instructions not carried out are named in the notes and in
"About This Edition". The text, mathematics, tables and Symbols lists are typeset; the figures and
photographs are cropped from the scan (`figures/manifest.csv`), and version 2 will vectorize the figures.
The text was transcribed from the page images and checked against the scan in separate audit passes, one
report per unit and round in `audit/`; the per-chapter correction lists, with the decision taken on each
item and on each doubt, are in `corrections/`. `make all` also runs `tools/check_numbering.py` (every
equation, figure, table and plate of `inventory/` labelled and displayed with its printed number, anchors,
log warnings, figure files) and `tools/prose_diff.py` (text coverage against the OCR of the scan; the
supplement pages are checked with `python3 tools/prose_diff.py --chapter supplement`).

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
    make figs           # version 2: compile the redrawn figures figures/v2/**/*.tex to PDF (all, chapter, final, unit do this first)
    make fig F=ch1/fig06    # one redrawn figure, rendered beside its scan crop in build/v2/png/
    make figdata        # rerun the scripts that compute or digitize curve data (figures/v2/**/*.py)

Toolchain used: TeX Live 2026 (pdflatex, newtx, manyfoot, newfloat, placeins; TikZ and pgfplots 1.18 for
version 2), latexmk 4.87, poppler 26.08 (pdfimages, pdftotext, pdftoppm, pdfinfo, pdffonts), Python 3 with
Pillow 12.3, numpy and (version 2 tools) scipy.

## Version 2 (in progress)

Version 2 redraws the line figures as vector artwork (TikZ and pgfplots, in a modern style; photographs and
plates stay scanned). The sources are `figures/v2/<dir>/<name>.tex`, one standalone document per figure in
the house style `figures/v2/tamrfig.sty`; `figures/v2/inventory.csv` lists every figure with what it holds,
where its curve data come from and its status. A figure replaces its crop in the book once it is audited.
Curve data are computed from the book's equations where they determine the curve, otherwise traced from
the scan with `tools/v2/digitize.py`, which also overlays any curve on the scan to check it.

## Layout

See `STYLE.md` for the transcription conventions, `inventory/` for the expected equation/figure lists,
`corrections/` for the per-chapter correction checklists and `audit/` for the audit reports.
