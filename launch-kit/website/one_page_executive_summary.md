# Logic Drift: One-Page Executive Summary

## What It Is

Logic Drift is the divergence between an AI model's assessment of scientific consensus and its assessment of logical validity for the same claim.

The working paper introduces the Logic Drift Protocol, a simple test that asks models to separately score consensus, inductive support, deductive validity, and a neutral-domain structural analogy.

## What We Tested

The initial test case used a common consciousness-related inference:

> Brain activity correlates with subjective experience; brain damage impairs experience; therefore, the brain generates subjective experience.

The protocol compares that argument to a structurally similar neutral argument:

> Radio circuitry correlates with audio output; circuit damage impairs output; therefore, the radio generates the music.

## What We Found

Across 697 successful runs and seven frontier models:

- Mean consensus score: `82.63`
- Mean deductive-validity score: `10.33`
- Mean Logic Drift Score: `72.29`
- Mean neuroscience inductive-support score: `59.67`
- Mean neutral-domain score: `45.35`
- Mean Semantic Delta: `14.30`

Models generally recognized that the target argument was not deductively valid, while still assigning higher support to the neuroscience framing than to the neutral framing.

## Why It Matters

AI systems increasingly act as reasoning assistants. If they confuse consensus with validity, or allow domain prestige to influence logical scoring, they may reinforce inherited assumptions rather than help investigate them.

The broader Future of Inquiry concern is that human feedback is not neutral. AI systems may inherit not only human knowledge, but also human deference patterns.

## Publication Status

The paper is being prepared as a Future of Inquiry working paper with an accompanying reproducibility package. arXiv submission is planned after technical editing, citation verification, LaTeX conversion, and category/endorsement review.

