# Repository Package Notes

## Recommended Sharing Shape

Use this folder as the base of a Git repository:

`logic-drift-protocol`

Recommended first public/private repo name:

`logic-drift-protocol`

## What This Repo Demonstrates

This repository supports the Future of Inquiry working paper:

**Logic Drift: A Protocol for Measuring Consensus-Validity Separation in Language Models**

It contains:

- a working paper draft,
- the canonical v18 source manuscript,
- protocol prompts,
- a cleaned 697-run dataset,
- standard-library analysis scripts,
- generated figures,
- related-work and publication handoff notes,
- Monday launch copy.

## What To Share With Researchers

For direct outreach, share:

- `README.md`
- `paper/source/logic_drift_arxiv_working_draft.md`
- `data/processed/model_summary.csv`
- `data/processed/overall_summary.csv`
- `figures/`
- `prompts/logic_drift_protocol_v24.md`
- `scripts/analyze_logic_drift.py`
- `data/DATA_PROVENANCE.md`

The `launch-kit/` and `handoff/` folders are useful internally, but may be too inside-baseball for first-contact academic outreach. For a public repo, consider either:

1. keeping them in a `project-notes/` folder, or
2. excluding them from the first public release and sharing them privately with hired collaborators.

## Secret Scan Status

The package was scanned for common secret patterns. Two supporting raw JSON files were removed because they contained old hard-coded OpenRouter API keys in embedded config sections.

The remaining references to API keys are generic environment-variable instructions for `OPENROUTER_API_KEY`.

Before publishing publicly, run:

```powershell
rg -n "sk-|api_key|AIza|BEGIN .*PRIVATE|token|secret" .
```

Review any matches manually.

## License Recommendation

Suggested split:

- Code: MIT License.
- Paper/text/data: CC BY 4.0.

If unsure, leave the repository private until the license choice is finalized.
