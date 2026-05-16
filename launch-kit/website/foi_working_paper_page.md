# Logic Drift

## A Working Paper From Future of Inquiry

**Logic Drift: A Protocol for Measuring Consensus-Validity Separation in Language Models**

Future of Inquiry is preparing a working paper on a measurable failure mode in frontier AI reasoning: language models can often distinguish scientific consensus from logical validity when asked directly, yet their evaluations of logical support may shift when the same argument appears in a high-prestige domain.

The paper introduces the **Logic Drift Protocol**, a compact test for separating:

- what a model thinks the scientific consensus is,
- what the stated argument inductively supports,
- what follows deductively from the stated premises,
- and whether the same logical structure receives a different score in a neutral domain.

## The Core Finding

In an initial analysis of **697 successful runs across seven frontier models**, models assigned high consensus scores to a neuroscience/consciousness claim while assigning low deductive-validity scores to the specific argument used to support it.

The same models also showed, to varying degrees, a **Semantic Delta**: a difference between the logical-support score assigned to the neuroscience version of an argument and the score assigned to a structurally similar neutral radio/circuit version.

The point is not that AI has solved consciousness. It has not.

The point is more precise:

> AI systems may inherit not only human knowledge, but human patterns of epistemic deference.

## Why It Matters

Future AI systems will not only answer questions. They will evaluate arguments, summarize research, advise scientists, and help define what counts as plausible inquiry.

If these systems treat consensus as a substitute for validity, they may become engines of paradigm preservation rather than tools of discovery.

Logic Drift gives that risk a name and a measurement protocol.

## Current Status

This is a **Future of Inquiry working paper** and reproducibility package.

Status:

- Working paper drafted.
- Reproducibility/demo package assembled.
- Figures generated from the cleaned dataset.
- arXiv submission package in preparation.
- External technical editor / arXiv packaging consultant being sought.

## Materials

Working paper:

- `Logic Drift: A Protocol for Measuring Consensus-Validity Separation in Language Models`

Reproducibility package:

- protocol prompt,
- cleaned dataset,
- model summary table,
- figure-generation script,
- generated figures,
- optional live runner for selected models.

Generated results:

- Mean consensus score: `82.63`
- Mean deductive-validity score: `10.33`
- Mean Logic Drift Score: `72.29`
- Mean Semantic Delta: `14.30`

## What This Does Not Claim

This paper does not claim:

- that AI is an unbiased truth machine,
- that the neurological model of consciousness is false,
- that RLHF has been proven to cause the observed effect,
- or that one test case proves a universal law.

It claims something narrower:

> In this test setting, model evaluations of logical support vary in ways that suggest sensitivity to consensus and domain prestige. That behavior can be measured, reproduced, and tested in other domains.

## Future of Inquiry Frame

Human feedback is not neutral. It carries the assumptions, incentives, authority structures, and unresolved metaphysics of the humans providing it.

Logic Drift is one early measurement of that problem.

For Future of Inquiry, the deeper question is not only whether AI can reason. It is whether AI systems can help us examine the human feedback loops that taught them what to defer to.

