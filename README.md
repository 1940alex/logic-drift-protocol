# Logic Drift Protocol

Working paper and reproducibility package for:

**Logic Drift: An Initial Protocol for Probing Consensus–Validity Separation in Language Models**
Alex Tsakiris, Future of Inquiry Institute, 2026.

📄 **Paper PDF:** [`paper/logic_drift.pdf`](paper/logic_drift.pdf)
📦 **Zenodo DOI:** *(forthcoming — will be linked here once the GitHub release is minted)*
🔗 **Repository:** https://github.com/1940alex/logic-drift-protocol

## What this paper does

The paper introduces a compact evaluation protocol that asks a language model to score the same inference from four angles: scientific consensus, inductive support, deductive validity, and inductive support for a structurally matched argument in a neutral domain. Across 697 successful runs on seven frontier models, the protocol surfaces two patterns: a near-deterministic gap between consensus and deductive-validity scores (treated as a measurement instrument, not a discovery), and a heterogeneous gap between science-framed and structurally matched neutral-framed inductive scores (the "Semantic Delta"), ranging from essentially null in `grok-4.1-fast` to large in `gemini-3-pro`.

The paper's scope is deliberately narrow: one test case, one prompt version, seven models, one API aggregator. It is initial behavioral evidence, not a causal account. See §6 of the paper for what it isn't.

## Repository contents

```
paper/
  logic_drift.pdf                    ← built PDF (read this)
  source/logic_drift_arxiv_working_draft.md   ← canonical Markdown
  source/logic_drift.tex             ← LaTeX source for arXiv submission
  refs/references.bib                ← bibliography
  Makefile                           ← build driver
  README.md                          ← build instructions
prompts/
  logic_drift_protocol_v23_used_for_dataset.md   ← exact prompt
data/
  raw/ldp_complete_dataset_100_runs_7llms.csv    ← 697 successful runs
  processed/model_summary.csv                    ← per-model means and SDs
  processed/overall_summary.csv                  ← cross-model means
  processed/inferential_summary.csv              ← paired CIs and Cohen's dz
  DATA_PROVENANCE.md                             ← cleanup history
scripts/
  analyze_logic_drift.py             ← stdlib-only analysis (run this to reproduce)
  convert_figures_to_pdf.py          ← SVG → PDF for the paper build
figures/
  *.svg                              ← bar charts produced by the analysis
  pdf/*.pdf                          ← same figures in PDF
METHODS.md                           ← operational details (API, decoding params, parsing)
CHANGELOG.md                         ← version history
CITATION.cff                         ← citation metadata
LICENSE                              ← MIT for code
DATA_AND_TEXT_LICENSE.md             ← CC BY 4.0 for text, prompts, data, figures
```

## Reproducing the analysis

From the repository root:

```powershell
python .\scripts\analyze_logic_drift.py
```

Python 3.10 or newer. No third-party dependencies. Outputs land in `data/processed/` and `figures/`.

## Reproducing the paper PDF

From `paper/`:

```powershell
make
```

Requires a LaTeX distribution (tested with MiKTeX) and `pip install svglib reportlab` for the SVG-to-PDF conversion step. See `paper/README.md` for details.

## Headline numbers

From the 697-run dataset:

| Metric | Mean |
|---|---:|
| Consensus score | 82.63 |
| Inductive logic score (science framing) | 59.67 |
| Deductive validity score | 10.33 |
| Logic Drift Score (consensus − deductive) | 72.29 |
| Neutral-domain inductive score | 45.35 |
| Semantic Delta (science − neutral) | 14.34 |

Per-model paired confidence intervals and Cohen's $d_z$ values are in `data/processed/inferential_summary.csv` and Table 1 of the paper.

## Citing

If you use this paper or any of its artifacts, please cite via `CITATION.cff`. A Zenodo DOI will be added once the v0.1.0 release is minted.

## Repository status

Working-paper release. The paper is being prepared for arXiv submission (cs.CL) and Zenodo archival. Endorsement and DOI minting are in progress. Author can be reached at alex.futureofinquiry@gmail.com.

## License

- Code (`scripts/`, `paper/Makefile`, etc.): MIT — see `LICENSE`.
- Paper text, prompts, data, and figures: Creative Commons Attribution 4.0 (CC BY 4.0) — see `DATA_AND_TEXT_LICENSE.md`.
