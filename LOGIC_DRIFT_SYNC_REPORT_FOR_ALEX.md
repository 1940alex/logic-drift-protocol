# Logic Drift sync report for Alex

Compiled from the current `feature/publication-revisions` repository state and the Abacus/Claude proposed-change briefing.

## Current repository state checked

- Local repo path checked: `/Users/viviannasmith/logic-drift-protocol`
- Source branch checked: `feature/publication-revisions`
- Latest synced commit checked: `de24519 Address red-team preprint clarity fixes`
- GitHub status at time of check: local branch matched `origin/feature/publication-revisions` with `0 ahead / 0 behind`

Important local working-tree note: before this report was added, Vivianna's local copy already had uncommitted generated-output changes:

- `data/processed/inferential_summary.csv`
- `data/processed/model_summary.csv`
- `data/processed/overall_summary.csv`
- `paper/logic_drift.pdf` appeared deleted locally

Those pre-existing local changes were not reviewed as intentional paper edits and should not be committed until Alex decides whether they are expected build/analysis artifacts.

## Short answer

Abacus is partly out of date. The Codex/GitHub repository is now the source of truth.

Several red-team recommendations have already been addressed in the current paper, especially around scope, positionality, parser disclosure, and citation cleanup. Several important items remain open, especially parser examples/release, DOI minting, figure placement, and endorsement-email finalization.

## Already done in the current paper/repo

- The paper clearly frames the study as a narrow pilot, not a broad proof across science.
- The paper says the consciousness case is a high-leverage single test case, not a general-domain demonstration.
- The paper explicitly says the results are behavioral evidence, not a causal account.
- The paper discloses researcher positionality and the author's interest in consciousness/transmission-filter accounts.
- The paper states that the parser/extraction layer is not included in the current release.
- The paper treats the unreleased parser as a reproducibility limitation rather than hiding it.
- The future-work section includes parser release and input/output examples as a v2 item.
- The limitations section clearly states the single-stimulus/single-prompt limitation.
- The future-work section names multi-stimulus design as the highest-value extension.
- Shapira and Turner citation metadata appear corrected in `paper/refs/references.bib`.
- `CITATION.cff` exists and appears complete except for the future DOI.
- README and paper consistently indicate the Zenodo DOI is forthcoming.

## Not done yet

- Parser code has not been released.
- Worked examples showing raw model output mapped to parsed CSV rows are not present.
- A second stimulus pair has not been added.
- Zenodo DOI has not been minted.
- DOI has not been added to README, CITATION, or paper source.
- Figure float placement does not appear fixed in source; figures still use ordinary LaTeX float placement.
- Endorsement email drafts are not present in the repository, so the requested email edits cannot be verified from repo state.
- Mukherjee one-email vs. two-email strategy remains an Alex decision.

## Partially done / needs cleanup

### Table 1 and effect sizes

The current Table 1 already leads with paired mean differences and puts `d_z` in secondary columns. That addresses part of the Abacus recommendation.

However, the abstract still foregrounds very large effect sizes, including the `d_z = 42.7` value. The paper explains effect-size inflation in the results and limitations sections, but it does not include the exact warning recommended by Abacus:

> These effect sizes should not be compared to conventional benchmarks for small, medium, and large effects; they reflect near-deterministic decoding conditions.

Recommendation: add a sentence like this near the first discussion of effect sizes, and consider reducing the prominence of `d_z = 42.7` in the abstract.

### Section 4.4 truth-asymmetry objection

Section 4.4 has already been revised into a focused objection/response section, but it still contains a philosophical argument about truth-status and underdetermination.

Abacus recommended trimming this section to roughly 40% of its current length. That has not fully happened.

Recommendation: Alex should decide whether the current version is acceptable or whether to cut it down to:

- the objection,
- the narrow response,
- one sentence pointing to truth-value controls in v2.

### Koch/Kastrup mentions

Koch and Kastrup are still mentioned in:

- the author note / positionality framing,
- acknowledgements.

Abacus recommended cutting or footnoting these mentions because they may create unwanted association risk for an NLP/AI audience.

Recommendation: Alex decision needed. The current text is transparent and includes a non-endorsement disclaimer, but the reputational-risk concern remains.

## Email/outreach status

The repo contains a generic outreach note in `LOGIC_DRIFT_HANDOFF_FOR_VIVIANNA.md`, but it does not contain the three endorsement-email drafts referenced in Abacus.

Therefore, the following Abacus email edits cannot be verified from the repo:

- Add independent-researcher self-identification.
- Change "preprint" to "manuscript" until arXiv is live.
- Add Future of Inquiry explainer language.
- Add Mukherjee Skeptiko episode link.
- Remove "It's a quick process on your end."
- Change "Professor Mukherjee's team" wording.
- Add a result connected to Shapira.

Recommendation: put the current endorsement-email drafts into the repo, probably under a new `outreach/` or `emails/` folder, so they can be reviewed like paper changes.

## Recommended next actions

1. Decide what to do with the existing local generated-file changes and deleted PDF before committing anything else from Vivianna's machine.
2. Decide whether parser worked examples must be added before endorsement asks.
3. Decide whether to trim Section 4.4 further.
4. Decide whether to cut, footnote, or keep Koch/Kastrup mentions.
5. Decide whether the second stimulus pair is required for this release or explicitly v2.
6. Add or review the endorsement-email drafts in the repository so they stop living only in chat history.
7. Fix figure placement if the PDF still places figures after the wrong sections.
8. Mint Zenodo DOI after the GitHub release, then update README, CITATION, and paper source.

## Suggested collaboration workflow

Use GitHub/Codex as the source of truth.

- GitHub repository: canonical shared working folder.
- Branches: separate work lanes for reviewable changes.
- Pull requests: the place where Alex reviews diffs and decides what merges.
- Abacus/Claude/Codex chats: useful notes, but not canonical unless copied into the repo.

This workflow is reasonable. The main improvement is to stop letting important decisions live only in chat. Put decisions, drafts, and checklists into the repository so Alex can review actual files and diffs.
