# Logic Drift Preprint Contractor Brief

## Project

Prepare the manuscript **"Logic Drift: Quantifying Semantic-Logic Coupling in Frontier LLMs"** for low-friction arXiv submission.

This is a focused AI/LLM evaluation preprint, not a ghostwriting project and not a broad consciousness manifesto. The goal is to make the existing paper academically legible, reproducible, and clean enough to submit as a stable citable preprint.

## Source Files

Primary manuscript:

`C:\Users\atsak\Downloads\0412logic drift paper v18 .md`

Project docs:

`C:\Users\atsak\Downloads\ad-worktree\foi-projects-roots\foi-outreach-app\docs\arxiv_logic_drift_handoff.md`

`C:\Users\atsak\Downloads\ad-worktree\foi-projects-roots\foi-outreach-app\docs\logic_drift_readiness_audit.md`

## Working Frame

Preferred framing:

> We introduce a protocol for measuring whether language models distinguish scientific consensus from logical validity, and whether semantically different but structurally similar arguments receive different logical-strength scores.

Avoid framing:

> AI alignment has proven that models are trained to defend materialist consensus about consciousness.

The consciousness/NMC case should be treated as an initial stress test, not as the paper's primary philosophical claim.

## Core Tasks

### 1. Tone and Claims Revision

Revise the manuscript so it reads as a neutral LLM evaluation paper.

Required changes:

- Soften causal claims about RLHF/alignment.
- Replace "universal drift" with more precise language.
- Remove or compress rhetorical passages.
- Move FOI/outreach-style language out of the arXiv paper.
- Keep the paper's thesis intact: models can separate consensus from validity when asked directly, but logical-strength scoring may vary by semantic framing.

### 2. Methods and Reproducibility

Make the methods section replication-grade.

Add or verify:

- Exact model names and providers.
- Run dates.
- Number of runs per model.
- Sampling settings or provider defaults.
- Whether each run used a fresh context.
- Exact prompts.
- JSON schema or output format.
- Parsing method.
- Exclusion/retry rules.
- Data/code availability statement.

### 3. Results and Figures

Replace all figure placeholders.

Minimum figures:

- Consensus vs. deductive validity by model.
- Brain/NMC inductive score vs. neutral/radio score by model.
- Semantic Delta by model.

Minimum tables:

- Per-model summary table.
- Mean and standard deviation where available.
- Control suite vs. NMC summary.

All numbers in prose must match the tables/figures.

### 4. Related Work

Expand and clean the related work enough for arXiv.

Required areas:

- LLM sycophancy/deference.
- LLM-as-judge and rubric scoring.
- Calibration/uncertainty.
- Prompt sensitivity/framing effects.
- Shortcut learning/spurious correlations.
- Reasoning faithfulness or elicitation.
- Consensus and epistemic authority.

Keep this concise. The paper does not need a dissertation-length literature review.

### 5. References

Verify every citation.

Required:

- Confirm author names, years, titles, venues/arXiv IDs.
- Remove unverified or weak references.
- Add missing standard citations if needed.
- Convert references to BibTeX.

Known issues:

- Some 2025 citations may be fragile or incorrect.
- "Patil et al. Li et al." appears in prose without complete references.

### 6. arXiv Packaging

Prepare an arXiv-ready package.

Required:

- LaTeX source.
- BibTeX file.
- Figures in accepted formats.
- Clean compiled PDF.
- No placeholder URLs.
- No spaces or unsafe characters in packaged filenames.
- Metadata draft: title, authors, abstract, comments, category, license.

Likely category:

- `cs.CL` if framed as language model evaluation.
- `cs.AI` if framed as general reasoning/evaluation.

Do not submit without author review.

## Suggested Revised Title

Best option:

**Logic Drift: A Protocol for Measuring Consensus-Validity Separation in Language Models**

Alternative:

**Logic Drift: Measuring Semantic Sensitivity in LLM Evaluations of Consensus and Validity**

## Suggested Revised Abstract

> Language models are increasingly used to evaluate scientific and philosophical arguments, but it remains unclear whether their assessments of logical support are invariant across domains with different levels of social or scientific prestige. We introduce the Logic Drift Protocol, a simple evaluation method that asks models to separately estimate scientific consensus, inductive support, deductive validity, and compatibility with alternative explanations. In an initial study of seven frontier models using a consciousness-related test case, models generally assigned high consensus scores to the neurological model of consciousness while assigning low deductive-validity scores to a specific correlation/damage-to-generation inference. Several models also assigned higher inductive-support scores to the neuroscience version of the argument than to a structurally similar neutral radio/circuit version, producing a positive Semantic Delta. These results suggest that semantic framing can influence model evaluations of logical strength, even when models can explicitly distinguish consensus from deductive validity. We present the protocol, prompts, and analysis structure as a reproducible starting point for broader tests across domains. The results should be interpreted as initial behavioral evidence, not as proof of a causal alignment mechanism.

## Deliverables

1. Revised manuscript in LaTeX.
2. Compiled PDF.
3. BibTeX references file.
4. Figures and source data.
5. Prompt appendix.
6. Short changelog explaining major edits.
7. arXiv metadata recommendation.
8. List of remaining author decisions before submission.

## Success Criteria

- The paper reads as a scholarly LLM evaluation preprint.
- The NMC/consciousness case is clearly framed as a test case.
- The empirical claims are traceable to data, prompts, tables, or figures.
- Alignment/RLHF claims are clearly labeled as hypotheses.
- The PDF has no unfinished placeholders.
- A reader can reproduce or at least inspect the protocol.
- The package is ready for author review before arXiv submission.

