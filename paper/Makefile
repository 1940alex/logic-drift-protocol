# Build the Logic Drift paper PDF.
# Requires: a LaTeX distribution (tested with MiKTeX) and a working `latexmk`
# OR `pdflatex` + `bibtex`. Also requires Python with svglib + reportlab for
# the SVG-to-PDF conversion step:
#     pip install svglib reportlab

PAPER  := logic_drift
SRCDIR := source
REFDIR := refs
BUILD  := build
FIGSRC := ../figures
FIGPDF := ../figures/pdf

TEXFILE := $(SRCDIR)/$(PAPER).tex
BIBFILE := $(REFDIR)/references.bib

PDFLATEX := pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD)
BIBTEX   := bibtex

.PHONY: all figures clean distclean

all: $(BUILD)/$(PAPER).pdf

figures:
	cd .. && python scripts/convert_figures_to_pdf.py

$(BUILD)/$(PAPER).pdf: $(TEXFILE) $(BIBFILE) figures | $(BUILD)
	cp $(BIBFILE) $(BUILD)/references.bib
	$(PDFLATEX) $(TEXFILE)
	cd $(BUILD) && $(BIBTEX) $(PAPER)
	$(PDFLATEX) $(TEXFILE)
	$(PDFLATEX) $(TEXFILE)
	cp $(BUILD)/$(PAPER).pdf ./$(PAPER).pdf

$(BUILD):
	mkdir -p $(BUILD)

clean:
	rm -rf $(BUILD)

distclean: clean
	rm -f $(PAPER).pdf
