# Paper

This directory contains the working paper, its LaTeX source, the bibliography, and the build infrastructure.

## Files

- `source/logic_drift_arxiv_working_draft.md` — Canonical Markdown version of the paper. Read this if you just want the text.
- `source/logic_drift.tex` — LaTeX source, used to build the PDF for arXiv and Zenodo.
- `refs/references.bib` — Bibliography.
- `Makefile` — Build driver.
- `logic_drift.pdf` — Most recent built PDF (copied here on every successful build).
- `build/` — Build artifacts (gitignored except for the final PDF).

## Build

From this directory:

```bash
make
```

Requirements:

- A LaTeX distribution with `pdflatex` and `bibtex` on PATH. Tested with MiKTeX 25.x. On Windows, after installing MiKTeX, you may need to open a new shell so PATH picks up `C:\Users\<you>\AppData\Local\Programs\MiKTeX\miktex\bin\x64`.
- Python 3.10+ with `svglib` and `reportlab` for the SVG-to-PDF conversion of the figures:
  ```
  pip install svglib reportlab
  ```

The build will (in order):

1. Run `scripts/convert_figures_to_pdf.py` to populate `../figures/pdf/`.
2. Run `pdflatex` twice plus `bibtex` once to resolve references.
3. Copy the resulting PDF to `paper/logic_drift.pdf`.

## Clean

```bash
make clean      # remove build/
make distclean  # remove build/ and the in-place PDF
```
