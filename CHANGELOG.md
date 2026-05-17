# Changelog

All notable changes to this working-paper package are recorded here.

## [v0.1.0] — 2026-05-17

Initial public release prepared for arXiv preprint and Zenodo archival.

### Added

- Working paper: `paper/source/logic_drift_arxiv_working_draft.md` and LaTeX source `paper/source/logic_drift.tex`.
- Built PDF: `paper/build/logic_drift.pdf` (and a stable snapshot at `paper/logic_drift.pdf`).
- Bibliography: `paper/refs/references.bib` with sycophancy and philosophy-of-mind citations.
- Protocol prompt: `prompts/logic_drift_protocol_v23_used_for_dataset.md`.
- Cleaned dataset: `data/raw/ldp_complete_dataset_100_runs_7llms.csv` (697 successful runs across seven models).
- Analysis script: `scripts/analyze_logic_drift.py` (Python stdlib only). Produces `data/processed/model_summary.csv`, `data/processed/overall_summary.csv`, `data/processed/inferential_summary.csv`, and three SVG figures.
- Operational methods document: `METHODS.md`.
- Provenance notes: `data/DATA_PROVENANCE.md`.
- Dual licensing: MIT for code (`LICENSE`), CC BY 4.0 for paper text, prompts, data, and figures (`DATA_AND_TEXT_LICENSE.md`).
- Citation metadata: `CITATION.cff`.

### Paper revisions in this release (relative to early internal drafts)

- Retitled to **"Logic Drift: An Initial Protocol for Probing Consensus–Validity Separation in Language Models"** to match the paper's actual scope.
- New §3.2 philosophy-of-mind grounding paragraph citing Crick & Koch, Chalmers, Tononi-Boly-Massimini-Koch, Doerig et al., and Aru et al.
- New §3.2 "Positionality" paragraph disclosing the author's research interests and how they bear on case selection.
- LDS demoted from "finding" to "measurement instrument" — both in the abstract and in §4 and §5.
- New §4.4 "The apologist response as logic drift" addressing the most predictable methodological critique.
- New "Author's note" paragraph in §1 in first person, stating the personal motivation for the work.
- New Acknowledgements section naming Christof Koch and Bernardo Kastrup as informal interlocutors, with an explicit non-endorsement disclaimer.
- §4.2 model-level table replaced with a paired-comparison table reporting mean difference, 95% CI, and Cohen's $d_z$.
- §6 limitations expanded to include rubric-anchoring, effect-size inflation, aggregator routing, and parsing-pipeline transparency.
- §7 future work reframed as an explicit v2 roadmap with named experiments (multi-stimulus design, truth-value controls, parser release, decoding-parameter sweep, authority perturbation, base vs. instruction-tuned comparison).

### Known limitations (carried forward to v2 work)

- Single test case and single prompt version — the largest open methodological gap.
- Score-extraction parsing code not yet public.
- Exact decoding parameters in `METHODS.md` are placeholders pending author confirmation.
- A small subset of bibliography entries (Shapira 2026, Turner 2026) carry `note = {Author to verify ...}` markers; final bibliographic details to be confirmed against published versions before formal arXiv submission.

### Acknowledgements for tooling

- MiKTeX for LaTeX, Inkscape for SVG-to-PDF conversion, GitHub for hosting.
- AI tools were used during drafting, editing, code generation, and red-team review of the working paper; the author is responsible for the final claims, analysis, and submitted text.
