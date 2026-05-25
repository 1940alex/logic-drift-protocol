# Changelog

All notable changes to this working-paper package are recorded here.

## [Unreleased] — publication-readiness revisions

- Reframed the manuscript around the consciousness case as a deliberately narrow, high-leverage stress test rather than a generic cross-domain demonstration.
- Replaced the more combative §4.4 framing with a narrower section, renamed in the latest pass to "The truth-asymmetry objection." The section now treats the predictable critique seriously, surfaces its circular structure when it appeals to the very inference under test, and notes that the move itself is a small instance of the pattern the paper is measuring — while explicitly carving out legitimate methodological objections.
- Rewrote the §1 paragraph on why the consciousness case is high-leverage. Replaced the unmodified "consciousness sits upstream of observation" assertion with a literature-grounded framing around the distinction between neural correlates and explanatory sufficiency.
- Reintroduced the Planck 1931 reference only as a non-load-bearing historical footnote with a specific Observer citation.
- Added a Discussion subsection explaining why consciousness is a high-leverage AI-evaluation case.
- Fixed the prompt heading to match the analyzed `LDP-v23` dataset.
- Updated paired-difference summary logic so model and overall Semantic Delta values are row-paired when fields are missing.
- Clarified Table 1 sample sizes and pooled all-model statistics, renamed the Figure 2 "NMC" label to science-framed inductive score, and added parser/routing disclosure notes.
- Corrected bibliography metadata for Shapira 2026 and Turner 2026.
- Added `LOGIC_DRIFT_HANDOFF_FOR_VIVIANNA.md` for preprint/release coordination.

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
- New §4.4 addressing the most predictable methodological critique.
- New "Author's note" paragraph in §1 in first person, stating the personal motivation for the work.
- New Acknowledgements section naming Christof Koch and Bernardo Kastrup as informal interlocutors, with an explicit non-endorsement disclaimer.
- §4.2 model-level table replaced with a paired-comparison table reporting mean difference, 95% CI, and Cohen's $d_z$.
- §6 limitations expanded to include rubric-anchoring, effect-size inflation, aggregator routing, and parsing-pipeline transparency.
- §7 future work reframed as an explicit v2 roadmap with named experiments (multi-stimulus design, truth-value controls, parser release, decoding-parameter sweep, authority perturbation, base vs. instruction-tuned comparison).

### Known limitations (carried forward to v2 work)

- Single test case and single prompt version — the largest open methodological gap.
- Score-extraction parsing code not yet public.
- Exact decoding parameters in `METHODS.md` are placeholders pending author confirmation.
- Exact decoding parameters remain unrecovered in the public package and should be confirmed from original run configuration if possible.

### Acknowledgements for tooling

- MiKTeX for LaTeX, Inkscape for SVG-to-PDF conversion, GitHub for hosting.
- AI tools were used during drafting, editing, code generation, and red-team review of the working paper; the author is responsible for the final claims, analysis, and submitted text.
