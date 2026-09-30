N ?= 1
U ?= chapters/ch1-sec1
PRE ?=
UNIT := $(notdir $(U))
PDFLATEX_UNIT = pdflatex -interaction=nonstopmode -file-line-error -halt-on-error -jobname=$(UNIT) -output-directory=build/unit '\def\unitfile{$(U)}$(PRE)\input{tools/unit}'

.PHONY: all check chapter final unit dirs pages figures figs fig figdata clean

all: dirs figs
	latexmk main.tex
	$(MAKE) check

check:
	python3 tools/check_numbering.py
	python3 tools/prose_diff.py

chapter: dirs figs
	latexmk -usepretex -pretex='\def\INCLUDEONLY{chapters/ch$(N)}' main.tex

final: dirs figs
	latexmk -g -usepretex -pretex='\def\FINAL{}' main.tex

# standalone compile of one unit file; renders its pages to build/unit/<unit>-N.png
unit: dirs figs
	@$(PDFLATEX_UNIT) >/dev/null || (grep -E -A4 '^(\./|!|.*:[0-9]+:)' build/unit/$(UNIT).log | head -60; exit 1)
	@$(PDFLATEX_UNIT) >/dev/null
	@rm -f build/unit/$(UNIT)-*.png
	@pdftoppm -r 150 -png build/unit/$(UNIT).pdf build/unit/$(UNIT)
	@grep -E 'Overfull \\hbox \([0-9.]+pt' build/unit/$(UNIT).log | awk -F'[()]' '$$2+0 > 20 {print "  " $$0}' | head -20
	@echo "unit ok: build/unit/$(UNIT).pdf ; pages: build/unit/$(UNIT)-*.png"

dirs:
	@mkdir -p build/chapters build/unit

pages:
	python3 tools/extract_pages.py

figures:
	python3 tools/crop_figures.py

# ---- version 2 figures -------------------------------------------------------------------------
# figures/v2/<dir>/<name>.tex is a standalone document (\usepackage{tamrfig}) compiled from the
# repository root; its PDF sits beside it (gitignored). It is rebuilt when the source, its data files
# (<name>.csv, <name>-*.csv), the style or the notation macros change.
FIG_SRC := $(wildcard figures/v2/*/*.tex)
FIG_PDF := $(FIG_SRC:.tex=.pdf)
F ?= ch1/fig01

figs: $(FIG_PDF)

.SECONDEXPANSION:
figures/v2/%.pdf: figures/v2/%.tex $$(wildcard figures/v2/$$*.csv figures/v2/$$*-*.csv) figures/v2/tamrfig.sty macros.tex
	@mkdir -p build/v2/$(dir $*)
	@TEXINPUTS=.:figures/v2: pdflatex -interaction=nonstopmode -file-line-error -halt-on-error \
	  -output-directory=build/v2/$(dir $*) $< >/dev/null \
	  || (grep -E -A4 '^(\./|!|.*:[0-9]+:)' build/v2/$*.log | head -40; exit 1)
	@cp build/v2/$*.pdf $@
	@echo "fig ok: $@"

# one figure: build it, render it at the scan's 150 dpi and set it beside the v1 crop
fig: figures/v2/$(F).pdf
	@python3 tools/v2/compare.py $(F)

# rerun the scripts that compute or digitize curve data
figdata:
	@for s in $(wildcard figures/v2/*/*.py); do echo "$$s"; python3 $$s || exit 1; done

clean:
	rm -rf build
