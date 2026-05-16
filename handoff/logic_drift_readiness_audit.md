# Logic Drift arXiv Readiness Audit

Date: 2026-05-16

Project root:

`C:\Users\atsak\Downloads\ad-worktree\foi-projects-roots\foi-outreach-app`

Primary manuscript audited:

`C:\Users\atsak\Downloads\0412logic drift paper v18 .md`

Note: `C:\Users\atsak\Downloads\0412logic drift paper v18 .md` and `C:\Users\atsak\Downloads\1217logic drift paper v18 .md` have the same SHA-256 hash, so they appear to be identical copies.

## Executive Judgment

The paper is promising enough for an arXiv-style preprint, but not yet ready for low-friction submission. The core idea is viable if the submission is framed as an LLM evaluation/protocol paper: frontier models can separately report consensus and deductive validity, while their inductive logic scores appear sensitive to semantic/domain framing.

The fastest credible path is not to make this a definitive paper on consciousness or alignment. The fastest path is to make it a clean, modest, reproducible benchmark note with disciplined implications.

Recommended target:

**Short arXiv preprint / technical report on an LLM evaluation protocol, with consciousness as one illustrative stress test.**

Avoid target:

**Broad manifesto about alignment, consciousness, scientific authority, or the future of inquiry.**

## Readiness Rating

Current readiness: **60-65%**

Minimum-friction arXiv readiness after focused edits: **80-85%**

Remaining gap:

- Tone and claims discipline: medium-high risk.
- Methods/reproducibility: high risk.
- References: medium-high risk until verified.
- Figures/tables: high risk because placeholders remain.
- arXiv category/moderation fit: medium risk, reducible by reframing.

## Strategic Position

I agree with the working strategy: this paper should be treated with respect, but not overbuilt. It is a placeholder and proof object for the broader FOI project, not the final intellectual home of the idea.

The right standard is:

1. Clear enough that AI/NLP readers can understand and cite it.
2. Neutral enough that arXiv moderation is unlikely to reject it as polemical.
3. Reproducible enough that a contractor can package the data and figures.
4. Modest enough that the claims are not easy to dismiss.
5. Useful enough to support later FOI outreach, X/Substack/podcast material, and future protocol work.

## Highest-Risk Issues

### 1. The paper currently overclaims alignment causality

Risk level: **High**

The manuscript repeatedly implies that RLHF/alignment causes the observed behavior. The data can support a behavioral finding, but not a causal mechanism.

Examples to revise:

- Abstract: "current alignment approaches may inadvertently train models to mirror consensus rather than evaluate it"
- Introduction: "If an AI system is trained primarily to minimize the difference between its outputs and human consensus..."
- Section 5.2: claims about "alignment intensity" and model ranking
- Section 5.7: process supervision and consistency training may fail
- Conclusion: "We have built systems that can reason correctly and trained them to defer instead"

Minimum fix:

Recast all alignment/RLHF language as hypothesis:

> These results are consistent with, but do not establish, the possibility that alignment or post-training procedures can amplify deference to consensus in high-prestige domains.

Best contractor instruction:

Search for every occurrence of `alignment`, `RLHF`, `trained`, `suppress`, `default`, `defer`, and `consensus compliance`. Convert causal language into behavioral observation unless the paper directly tests the mechanism.

### 2. The paper risks sounding like a consciousness polemic

Risk level: **High**

The NMC test case is useful, but it creates moderation/reception risk if it appears that the paper's real purpose is to litigate materialism, consciousness, or the biological robot model.

Problematic patterns:

- "The biological robot model" is strategically useful for FOI outreach, but not for the arXiv paper.
- The "Hard Problem" framing can stay, but it should not dominate.
- The radio analogy should be presented as a structural control, not as evidence for transmission theory.
- Moral/value implications in Section 5.3 are a distraction and should likely be removed or shortened.

Minimum fix:

Frame NMC as a **stress-test domain** selected because it combines high consensus, philosophically recognized underdetermination, and simple formal structure. Do not frame the paper as arguing that NMC is false.

Best contractor instruction:

Move consciousness-specific implications into a short "Test Case Rationale" subsection and keep the discussion focused on model evaluation.

### 3. The methods are not yet replication-grade

Risk level: **High**

The manuscript says the protocol is reproducible, but the current paper does not yet provide enough operational detail to make that fully true.

Missing or under-specified:

- Exact model IDs and providers.
- Exact run dates.
- API/platform used for each model.
- Temperature and sampling settings, including what "default" meant per provider.
- Whether runs were independent conversations or repeated calls in one context.
- Whether system prompts were used.
- Exact JSON schema.
- Parser used.
- Retry/exclusion rules.
- Whether failures, refusals, malformed JSON, or timeouts occurred.
- Whether scores were extracted automatically or manually checked.
- Where raw outputs live.

Minimum fix:

Add a compact Methods Details table:

| Field | Required value |
|---|---|
| Model/provider | Exact names |
| Date range | Collection dates |
| Runs | 100 per model |
| Prompting | Fresh context or not |
| Temperature | Provider default or exact value |
| Output format | JSON schema |
| Exclusions | Rules and count |
| Parser | Script/location |
| Data availability | URL or "to be released" |

Best contractor instruction:

Before editing prose, reconstruct a reproducibility packet. If raw data is missing, mark the paper as "protocol/preliminary" and reduce empirical certainty.

### 4. The figures are placeholders

Risk level: **High**

Section 4.3 still says "Figure 1 would show..." This alone makes the paper look unfinished.

Minimum required figures:

1. Consensus vs. deductive validity by model.
2. Brain/NMC inductive score vs. neutral/radio score by model.
3. Semantic Delta by model.

Optional but useful:

- Compact table heatmap of `S_C`, `S_L`, `S_D`, neutral score, compatibility, LDS, and Semantic Delta.

Best contractor instruction:

Generate publication-ready PNG/PDF figures from a single processed CSV. Use restrained academic styling, not marketing graphics.

### 5. The results need confidence/variance reporting

Risk level: **Medium-high**

The manuscript mentions standard deviation but the visible results mostly report means and ranges. If N=100 runs per model is the empirical backbone, the paper should show variance.

Minimum fix:

Add per-model mean and standard deviation for:

- Consensus score.
- Inductive logic score.
- Deductive validity score.
- Neutral/radio score.
- Compatibility score.
- Semantic Delta.

If standard deviation is unavailable, say so and avoid overstating stability.

### 6. The "universal drift" phrase is too strong

Risk level: **Medium-high**

The abstract says "universal drift" and all seven models had positive Semantic Delta. But elsewhere the manuscript says "most models" and notes Grok 4.1 Fast had near-zero delta.

Minimum fix:

Replace "universal drift" with:

> Across seven tested models, all separated consensus from deductive validity when prompted directly, and most showed positive semantic sensitivity in inductive scoring.

If all seven really had positive deltas, the paper can say that, but should avoid making "universal" sound like a general law.

### 7. The related work section is too thin

Risk level: **Medium**

The current related work appears as a short subsection in the theoretical framework. For arXiv, it should be its own section or a clearly expanded subsection.

Needed buckets:

- LLM sycophancy and social deference.
- LLM-as-judge and rubric scoring.
- Calibration and uncertainty.
- Prompt sensitivity / framing effects.
- Shortcut learning / spurious correlations.
- Reasoning faithfulness and latent capability vs. elicited behavior.
- Scientific consensus, epistemic authority, and philosophy of science.

Minimum fix:

Add 1-2 paragraphs per bucket. Keep it lean.

### 8. References need verification

Risk level: **Medium-high**

Several references are recent 2025 items and may be incorrect, incomplete, or too weak to carry the claims. The contractor must verify every citation.

Specific flags:

- "Chaudhury, 2025. Alignment is Localized..." needs exact author/title/arXiv verification.
- "Huang et al. 2025. Safety Tax..." needs verification and careful use.
- "Irpan et al. 2025. Consistency Training..." needs verification.
- "Sun and Wang 2025" and "Posner and Saran 2025" may be peripheral; keep only if they serve the narrowed paper.
- "Patil et al. Li et al." appears in prose without complete references.
- Formatting is not BibTeX-ready.

Minimum fix:

Create `references.bib`; remove unverified citations; prefer robust, well-known citations over fragile recent ones.

### 9. Some language reads as advocacy rather than scholarship

Risk level: **Medium-high**

Examples to soften or remove:

- "This is not a capability failure. It is a disclosure failure."
- "The contribution is not the discovery of a subtle phenomenon. The contribution is the documentation of an obvious one."
- "The true test of an AI's reasoning capability..."
- "effectively cementing the AI as an agent of scientific conservatism"
- "prestige stops masquerading as proof" belongs in outreach, not arXiv.
- "We have built systems that can reason correctly and trained them to defer instead."

Minimum fix:

Keep one or two memorable phrases at most. Make the body dry, precise, and refereeable.

### 10. The current conclusion should be rewritten

Risk level: **Medium-high**

The conclusion is rhetorically strong but too sweeping. The arXiv version should close with a bounded contribution:

1. The paper proposes a protocol.
2. The protocol distinguishes consensus estimation, deductive validity, inductive support, and semantic sensitivity.
3. An initial seven-model study shows evidence of semantic sensitivity in a consciousness-related test case.
4. Further domains and controlled model comparisons are needed.

Recommended conclusion tone:

> These results do not establish a general mechanism or prove that alignment training causes semantic-logic coupling. They show that, in this test setting, model evaluations of an argument's logical strength can vary with domain framing despite preservation of formal structure. This makes Logic Drift a useful target for further benchmark development.

## Recommended Paper Reframe

Current implicit frame:

**AI has been aligned into consensus obedience, and consciousness exposes the problem.**

Recommended arXiv frame:

**We introduce a simple protocol for measuring whether LLM logical scoring remains invariant across semantically different but structurally similar arguments. An initial seven-model test suggests that semantic framing can affect inductive validity estimates even when models separately recognize low deductive validity.**

This keeps the FOI payload alive, but packages it in a way that is harder to reject.

## Suggested Revised Title

Current:

**Logic Drift: Quantifying Semantic-Logic Coupling in Frontier LLMs**

Recommended:

**Logic Drift: Measuring Semantic Sensitivity in LLM Evaluations of Consensus and Validity**

Alternative:

**Logic Drift: A Protocol for Testing Consensus-Validity Separation in Language Models**

Best low-friction title:

**Logic Drift: A Protocol for Measuring Consensus-Validity Separation in Language Models**

## Suggested Revised Abstract

Draft replacement:

> Language models are increasingly used to evaluate scientific and philosophical arguments, but it remains unclear whether their assessments of logical support are invariant across domains with different levels of social or scientific prestige. We introduce the Logic Drift Protocol, a simple evaluation method that asks models to separately estimate scientific consensus, inductive support, deductive validity, and compatibility with alternative explanations. In an initial study of seven frontier models using a consciousness-related test case, models generally assigned high consensus scores to the neurological model of consciousness while assigning low deductive-validity scores to a specific correlation/damage-to-generation inference. Several models also assigned higher inductive-support scores to the neuroscience version of the argument than to a structurally similar neutral radio/circuit version, producing a positive Semantic Delta. These results suggest that semantic framing can influence model evaluations of logical strength, even when models can explicitly distinguish consensus from deductive validity. We present the protocol, prompts, and analysis structure as a reproducible starting point for broader tests across domains. The results should be interpreted as initial behavioral evidence, not as proof of a causal alignment mechanism.

## Minimum-Friction Revision Plan

### Pass 1: Make the paper safe for arXiv moderation

Goal: Remove the most rejectable material.

Tasks:

- Rewrite abstract.
- Rewrite introduction to foreground LLM evaluation.
- Reduce "Alignment Paradox" to a hypothesis in Discussion.
- Delete or compress the moral/normative domain digression.
- Remove rhetorical closing reflection or move it to FOI outreach material.
- Replace "universal drift" with more precise claims.

### Pass 2: Make the methods credible

Goal: Ensure a reader can understand what was actually done.

Tasks:

- Add model/run/settings table.
- Add exact prompt appendix.
- Add JSON schema.
- Add parser/exclusion description.
- Add data/code availability statement.
- Clarify what "default temperature" means and why it was chosen.

### Pass 3: Make the results concrete

Goal: Replace assertions and placeholders with tables/figures.

Tasks:

- Generate three figures.
- Add per-model mean/SD table.
- Add short statistical/variance note.
- Ensure all numbers in prose match the table.

### Pass 4: Fix related work and citations

Goal: Make the paper look like it belongs in AI/NLP evaluation discourse.

Tasks:

- Verify all references.
- Remove weak or tangential references.
- Add missing standard references.
- Convert to BibTeX.
- Keep related work lean and targeted.

### Pass 5: Package for handoff/submission

Goal: Give contractor a nearly finished object.

Tasks:

- Convert to LaTeX.
- Create `paper/`, `figures/`, `data/`, `prompts/`, `scripts/`.
- Build PDF locally.
- Check arXiv filename constraints.
- Prepare metadata: title, authors, abstract, comments, license.
- Decide category.

## Proposed arXiv Category Strategy

Most likely:

- Primary: `cs.CL` if framed as language model evaluation and prompt sensitivity.
- Alternative primary: `cs.AI` if framed as general AI reasoning/evaluation.
- Possible cross-list: `cs.LG` only if the methods/results are made more benchmark-like.

Avoid:

- Over-framing as philosophy of consciousness.
- Over-framing as AI safety without enough safety evaluation machinery.

Rationale:

arXiv's current submission guidance says submissions should be topical, refereeable scientific contributions and may require endorsement for a first submission or new category. Its moderation guidance emphasizes self-contained scholarly value, neutral tone, figures/tables/references, and avoiding extraneous personal or political statements. This paper should therefore be packaged as a research/evaluation contribution, not as FOI outreach.

Official arXiv pages checked:

- Submission overview: https://info.arxiv.org/help/submit/index.html
- Preparation/metadata: https://info.arxiv.org/help/prep.html
- Moderation: https://info.arxiv.org/help/moderation/index.html
- Endorsement: https://info.arxiv.org/help/endorsement.html

## Contractor Handoff Instructions

Suggested role:

**AI/ML preprint editor and arXiv packaging consultant**

Scope:

Prepare the Logic Drift manuscript for low-friction arXiv submission as a concise LLM evaluation/protocol paper.

Do:

- Tighten tone.
- Verify and format citations.
- Strengthen methods.
- Prepare figures.
- Convert to LaTeX/BibTeX.
- Package data/prompts/scripts.
- Advise on arXiv category and endorsement.

Do not:

- Turn it into a broad consciousness argument.
- Dilute the core claim beyond recognition.
- Add speculative claims about proprietary model training.
- Make FOI outreach language part of the paper.
- Submit to arXiv without author review.

Success criteria:

- The paper compiles cleanly to PDF.
- No placeholder figures or URLs remain.
- All empirical claims trace to a table, figure, prompt, or raw output.
- Every citation is verified.
- Claims about alignment are explicitly labeled speculative.
- The paper reads as an LLM evaluation preprint, not a manifesto.

## Concrete Next Step

Before paying a contractor for polish, gather or reconstruct the empirical package:

1. Raw model outputs for all 700 runs.
2. Processed result table.
3. Prompt text for each protocol step.
4. Script or spreadsheet used to compute means, LDS, and Semantic Delta.
5. Any notes on failed/malformed runs.

If those exist, the contractor can finish the paper efficiently.

If they do not exist, the paper should be reframed as a preliminary protocol report, or the experiment should be rerun cleanly before submission.

