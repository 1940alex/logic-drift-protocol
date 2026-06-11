# Logic Drift Publication Handoff for Vivianna

Date: 2026-05-28

## Current source-of-truth branch

Use:

```text
feature/publication-revisions
```

Latest pushed publication commit:

```text
f3f2b53 Finalize arXiv figure layout
```

This branch contains the current approved paper PDF, LaTeX source, figures, data, methods notes, and reproducibility package.

## Current paper status

Alex reviewed and approved the rebuilt PDF after the figure-layout fix.

Current PDF:

```text
paper/logic_drift.pdf
```

The PDF now has a clean figure section:

- Table 1 appears before Section 4.3.
- Section 4.3 starts cleanly on its own page.
- Figure 1 appears under Section 4.3.
- Figures 2 and 3 appear together before Section 4.4.
- Section 4.4 starts after the figures, so the paper no longer looks like it has a figures heading with no figures.

## What was just changed

The final layout fix added two LaTeX page breaks in:

```text
paper/source/logic_drift.tex
```

One page break forces Section 4.3, "Figures," to start cleanly. The second prevents Section 4.4 from beginning before the figures have appeared.

The PDF was rebuilt from the LaTeX source and pushed.

## arXiv source bundle

A local arXiv upload bundle has been prepared and test-compiled:

```text
paper/arxiv_submission/logic_drift_arxiv_source.zip
```

This folder is intentionally ignored by Git so generated upload packages do not clutter the repository. The zip contains:

- `logic_drift.tex`
- `references.bib`
- `logic_drift.bbl`
- `figures/pdf/consensus_vs_deductive_validity.pdf`
- `figures/pdf/nmc_vs_neutral_inductive_score.pdf`
- `figures/pdf/semantic_delta_by_model.pdf`

The extracted zip was test-compiled successfully. The only remaining LaTeX warning observed was a harmless hyperref footnote destination warning. There were no unresolved citations or missing figures.

## Red-team issues now addressed

The recent Claude/Gemini red-team items that were still live have been handled:

- Planck quote is only a non-load-bearing historical footnote.
- "Non-materialist frameworks" style language was removed or softened.
- Figure 2 no longer uses the unexplained "NMC" label in the visible figure title/legend.
- Table note discloses `gemini-3-pro` Semantic Delta `n=99`.
- Table note clarifies the All-models row pools eligible runs and is not model-clustered.
- Question 5 explains why transmission/filter theory was chosen as the structural alternative, without endorsing it.
- Question 6 is disclosed as collected free text that is not quantitatively analyzed in this pilot.
- OpenRouter routing and request-level decoding limitations are disclosed.
- Parser release and multi-stimulus/synthetic controls are correctly framed as v2/future work.

## Remaining non-blockers

These should not delay the arXiv submission:

- Zenodo DOI is still forthcoming.
- Parser code is not included in v1; this is disclosed and placed on the v2 roadmap.
- The paper uses one stimulus pair; this is disclosed repeatedly as a pilot limitation.
- Exact request-level decoding parameters were not retained; this is disclosed.
- A 30-day longitudinal consistency study is not needed for this v1 pilot and should be treated as future work.

## Recommended arXiv plan

Primary category:

```text
cs.CL
```

Possible secondary category:

```text
cs.AI
```

Submission framing:

- Present this as an AI evaluation / language-model behavior paper.
- Avoid framing it as a consciousness theory paper.
- Use the phrase "pilot protocol" or "initial behavioral evidence."
- Do not claim the paper proves anything about consciousness itself.
- Emphasize reproducibility, deterministic analysis, and limitations.

Suggested short arXiv comment:

```text
13 pages, 3 figures, reproducibility package available at GitHub
```

## Endorsement strategy

The best endorser is someone with credibility in:

- NLP / computation and language
- AI evaluation
- LLM behavior
- AI safety / alignment
- machine learning methodology

Do not lead with the consciousness angle. Lead with:

- a compact LLM evaluation protocol,
- consensus-validity separation,
- deterministic analysis over 697 runs,
- seven model families,
- a clearly scoped pilot with public data/code.

## Suggested endorsement request

Subject:

```text
arXiv endorsement request for LLM evaluation preprint
```

Body:

```text
Hi [Name],

I am preparing to submit a short preprint to arXiv in cs.CL on an LLM evaluation protocol called the Logic Drift Protocol. The paper tests whether language models preserve the distinction between consensus, inductive support, and deductive validity when the same inference pattern is presented in different semantic domains.

The work is a pilot study: 697 successful runs across seven model families, with deterministic analysis code, public data, figures, and a reproducibility package. The paper is explicitly framed as initial behavioral evidence, not as a causal account or a claim about the underlying scientific test case.

Would you be willing to consider endorsing the arXiv submission in cs.CL if, after reviewing the PDF and repository, you think it meets the standard for a public preprint?

PDF:
https://github.com/1940alex/logic-drift-protocol/blob/feature/publication-revisions/paper/logic_drift.pdf

Repository:
https://github.com/1940alex/logic-drift-protocol/tree/feature/publication-revisions

Thank you,
Alex
```

## Git workflow for Vivianna

Before making edits:

```text
git fetch origin
git checkout feature/publication-revisions
git pull origin feature/publication-revisions
```

For any further edits, please use a new branch and a pull request against:

```text
feature/publication-revisions
```

Recommended PR style:

- One PR for paper text changes.
- One PR for release/Zenodo metadata.
- One PR for outreach or endorsement materials, if those are kept in the repo.

Avoid committing generated CSV/PDF deletions or local build artifacts unless they are intentional.

## Final pre-submission checklist

- Confirm Alex's name, affiliation, contact email, and title metadata.
- Confirm arXiv category: `cs.CL` primary.
- Confirm whether to add `cs.AI` as secondary.
- Confirm license choice during arXiv submission.
- Submit source zip, not only the PDF.
- After arXiv ID is live, create GitHub release.
- Mint Zenodo DOI from the GitHub release.
- Update README, CITATION.cff, and paper data-availability note with the Zenodo DOI in a follow-up revision.
