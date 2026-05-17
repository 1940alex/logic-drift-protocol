# Logic Drift Protocol

This repository contains the working paper and minimal reproducibility package for:

**Logic Drift: A Protocol for Measuring Consensus-Validity Separation in Language Models**

The paper tests whether language models distinguish scientific consensus from deductive validity, and whether logical-support scores shift when the same inference appears in a high-prestige domain versus a neutral domain.

## What Is Included

- Paper draft: `paper/source/logic_drift_arxiv_working_draft.md`
- Protocol prompt: `prompts/logic_drift_protocol_v23_used_for_dataset.md`
- Cleaned dataset: `data/raw/ldp_complete_dataset_100_runs_7llms.csv`
- Analysis script: `scripts/analyze_logic_drift.py`
- Generated tables: `data/processed/`
- Generated figures: `figures/`
- Citation metadata: `CITATION.cff`

## Reproduce The Results

From this repository root:

```powershell
python .\scripts\analyze_logic_drift.py
```

The script uses only the Python standard library.

## Current Results

The cleaned dataset contains **697 successful protocol runs across seven models**.

Generated overall means:

| Metric | Mean |
|---|---:|
| Consensus score | 82.63 |
| Inductive logic score | 59.67 |
| Deductive validity score | 10.33 |
| Logic Drift Score | 72.29 |
| Neutral-domain score | 45.35 |
| Semantic Delta | 14.30 |

## Repository Status

This is a working-paper package. The paper is being prepared for external technical review, archival release, and possible arXiv submission.
