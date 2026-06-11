# arXiv Publication Action Memo

For: Alex and Vivianna  
Project: Logic Drift Protocol  
Date: 2026-05-28

## Purpose

This memo is a simple checklist for getting the Logic Drift paper onto arXiv and then archived with a DOI.

Vivianna is helping Alex manage the publication process. She is not responsible for the substance of the Logic Drift paper, the scientific argument, the analysis, or the paper's claims. Alex owns all final content decisions.

## Where the files are

The repository is public:

```text
https://github.com/1940alex/logic-drift-protocol
```

Use this branch:

```text
feature/publication-revisions
```

The current PDF is here:

```text
paper/logic_drift.pdf
```

The current arXiv upload zip is on Alex's local machine here:

```text
paper/arxiv_submission/logic_drift_arxiv_source.zip
```

That zip is not committed to GitHub because it is a generated upload package. If Vivianna needs it, Alex can send it directly or ask Codex to regenerate it.

## Roles

### Alex owns

- Final approval of the paper.
- Final approval of the arXiv category, title, abstract, and submission text.
- Choosing who to ask for endorsement.
- Sending any emails that should come personally from Alex.
- Responding to substantive questions about the paper.
- Deciding when the paper is ready to submit.

### Vivianna owns

- Keeping the publication checklist moving.
- Helping identify and track possible endorsers.
- Drafting endorsement emails for Alex to approve/send.
- Tracking who has been contacted and who has responded.
- Helping with arXiv account/submission logistics.
- Helping create the GitHub release after arXiv submission.
- Helping mint the Zenodo DOI after the GitHub release.
- Making sure README/CITATION/paper links get updated after the DOI exists.

### Codex can help with

- Regenerating the arXiv source zip.
- Checking that the PDF/source compile.
- Drafting emails.
- Updating repository files after Alex approves changes.
- Preparing GitHub release/Zenodo metadata text.
- Updating README/CITATION/paper DOI references after the DOI is minted.

## Step-by-step plan

### 1. Confirm final PDF

Status: Done.

Alex has reviewed the current PDF and approved it for moving forward.

### 2. Decide arXiv category

Recommended:

```text
Primary: cs.CL
Secondary: cs.AI, if appropriate
```

Alex should make the final call.

### 3. Get arXiv endorsement if needed

Vivianna should help Alex make a short list of possible endorsers in NLP, LLM evaluation, AI safety, or machine learning.

Important: lead with the AI-evaluation angle, not the consciousness angle.

Suggested positioning:

```text
This is a short LLM evaluation preprint about whether models separate consensus, inductive support, and deductive validity under framing shifts. It is a pilot study with public data, deterministic analysis code, and a reproducibility package.
```

Vivianna can draft emails. Alex should approve and likely send them.

### 4. Submit to arXiv

Alex should submit or directly supervise submission.

Use the arXiv source zip, not only the PDF.

Suggested arXiv comment:

```text
13 pages, 3 figures, reproducibility package available at GitHub
```

Suggested framing during submission:

- AI evaluation / LLM behavior paper.
- Initial protocol / pilot study.
- Not a consciousness theory paper.
- Not a claim that the paper proves anything about consciousness.

### 5. Wait for arXiv processing

Possible outcomes:

- Accepted and posted.
- Held briefly for moderation.
- Reclassified to another category.
- Asked for endorsement.
- Asked for minor source/metadata fixes.

Vivianna should track the status and keep Alex updated.

Alex should answer any substantive paper questions.

### 6. Create GitHub release

After the arXiv version is accepted or posted, create a GitHub release from the final publication branch.

Recommended tag:

```text
v0.1.0
```

Release title:

```text
Logic Drift Protocol v0.1.0
```

### 7. Mint Zenodo DOI

After the GitHub release exists, archive the release on Zenodo and mint the DOI.

Vivianna can manage this logistics step with Alex's account/access as needed.

### 8. Update links after DOI exists

After the Zenodo DOI is minted, update:

- `README.md`
- `CITATION.cff`
- `paper/source/logic_drift.tex`
- `paper/source/logic_drift_arxiv_working_draft.md`
- `paper/logic_drift.pdf`

Codex can make these updates and rebuild the PDF.

### 9. Optional arXiv replacement

If the DOI is minted after the first arXiv submission, Alex can submit a small arXiv replacement that adds the Zenodo DOI to the data/code availability section.

This is optional but recommended.

## Endorsement email template

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

## Current bottom line

The paper itself is ready for the publication workflow.

The next practical task is endorsement/submission logistics, not more paper drafting.
