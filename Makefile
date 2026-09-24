N ?= 1
U ?= chapters/ch1-sec1
PRE ?=
UNIT := $(notdir $(U))
PDFLATEX_UNIT = pdflatex -interaction=nonstopmode -file-line-error -halt-on-error -jobname=$(UNIT) -output-directory=build/unit '\def\unitfile{$(U)}$(PRE)\input{tools/unit}'

.PHONY: all check chapter final unit dirs pages figures clean

all: dirs
	latexmk main.tex
	$(MAKE) check

check:
	python3 tools/check_numbering.py
	python3 tools/prose_diff.py

chapter: dirs
	latexmk -usepretex -pretex='\def\INCLUDEONLY{chapters/ch$(N)}' main.tex

final: dirs
	latexmk -g -usepretex -pretex='\def\FINAL{}' main.tex

# standalone compile of one unit file; renders its pages to build/unit/<unit>-N.png
unit: dirs
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

clean:
	rm -rf build
