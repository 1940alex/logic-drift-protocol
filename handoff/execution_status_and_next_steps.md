# Execution Status and Next Steps

Date: 2026-05-16

## What Is Done

Created lean paper/demo package:

`C:\Users\atsak\Downloads\ad-worktree\foi-projects-roots\foi-outreach-app\logic-drift-protocol`

Included:

- Canonical v18 manuscript source.
- arXiv-oriented working draft.
- Prompt files.
- Cleaned 697-run dataset.
- Supporting raw JSON files.
- Dependency-free analysis script.
- Optional live API runner using `OPENROUTER_API_KEY`.
- Processed model summary and overall summary.
- Three SVG figures.
- BibTeX starter file.
- Readiness audit, related-work notes, and contractor brief.

## Reproduced Dataset Result

The analysis script reports:

- 697 successful runs.
- 7 models.
- Mean consensus score: 82.63.
- Mean inductive logic score: 59.67.
- Mean deductive validity score: 10.33.
- Mean LDS: 72.29.
- Mean neutral-domain score: 45.35.
- Mean Semantic Delta: 14.30.

Run command:

```powershell
python .\scripts\analyze_logic_drift.py
```

## Key Paper Correction

The old draft says or implies 700 runs. The clean dataset currently supports:

> 697 successful protocol runs across seven models.

If the final paper says "700 attempted runs," it needs the attempted-run source file and a short exclusions sentence. The current cleaned analysis package supports "697 successful runs."

## What Needs Human Review

1. Confirm whether the 697-run cleaned dataset is the intended final empirical dataset.
2. Confirm whether `gpt-4` should remain in the model list or be removed/reframed as an older baseline.
3. Confirm whether model names/slugs are acceptable as aggregator names or need provider-native version verification.
4. Decide whether to publish raw model rationales or only the cleaned score table.
5. Choose public archive target: GitHub, OSF, Zenodo, or private contractor handoff first.
6. Decide whether to submit to arXiv directly or post to OSF/Zenodo first.

## What A Contractor Should Do Next

1. Convert `paper/source/logic_drift_arxiv_working_draft.md` to LaTeX.
2. Verify every citation and complete `paper/refs/references.bib`.
3. Convert SVG figures to arXiv-friendly PDF/PNG as needed.
4. Add formal figure captions.
5. Tighten the working draft into final paper prose.
6. Verify model metadata and run dates.
7. Add final data/code availability URL.
8. Compile PDF and run an arXiv package check.

## Recommended Publication Path

1. Finish the arXiv-oriented paper draft.
2. Publish or privately stage the reproducibility package.
3. Submit to arXiv as `cs.CL` or `cs.AI`, depending on final framing.
4. If endorsement or moderation friction appears, publish via OSF/Zenodo first and resubmit after cleanup.
5. Use the accepted/preprint link as the anchor for FOI messaging, SignalBeyond tie-ins, and public explanation.

## Boundary For This First Paper

Keep in:

- Logic Drift Protocol.
- Consensus-validity separation.
- Semantic Delta.
- Domain-prestige sensitivity.
- Sycophancy/RLHF literature as context.
- Minimal reproducibility demo.

Keep out:

- Full app/platform.
- Dossier engine.
- Gaslighting probes.
- Ten-probe benchmark.
- Kuhn/Lakatos deconstruction as central frame.
- Strong causal claims about RLHF.
- Broad consciousness/metaphysics advocacy.
