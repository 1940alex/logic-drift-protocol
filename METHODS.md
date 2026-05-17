# Operational Methods

This document describes the operational details of how the Logic Drift Protocol dataset was collected and analyzed. It is the audit-trail companion to the paper.

## API aggregator

All seven models were accessed through a single aggregator: **OpenRouter** (`https://openrouter.ai/`). The aggregator routes requests to the named provider endpoint and returns the provider's response. The model slugs in `data/raw/ldp_complete_dataset_100_runs_7llms.csv` reflect OpenRouter's naming convention rather than the provider-native model identifiers.

| Display name | OpenRouter slug |
|---|---|
| claude-opus-4.5 | `anthropic/claude-opus-4.5` |
| deepseek-v3.2 | `deepseek/deepseek-chat-v3-0324` |
| gemini-3-pro | `google/gemini-3-pro-preview` |
| gpt-4-0314 | `openai/gpt-4-0314` |
| gpt-5.1 | `openai/gpt-5.1` |
| grok-4.1-fast | `x-ai/grok-4.1-fast` |
| o3 | `openai/o3` |

## Decoding parameters

> **AUTHOR ACTION ITEM.** The fields below need to be filled in from the run-pipeline configuration before public release. Defaults shown are best-current-knowledge placeholders inferred from the within-run variance in the dataset; replace with the exact values used.

- **Temperature.** Near-zero (likely `0` or `0.1`). The standard deviations on the consensus scores in `data/processed/model_summary.csv` are tight (between 1.76 and 4.74), which is consistent with near-deterministic sampling.
- **top_p.** [TODO: confirm — default is typically `1.0`]
- **max_tokens.** [TODO: confirm — protocol responses are long, so this needs to be ≥ ~3000]
- **System prompt.** [TODO: confirm whether a system prompt was used or whether the protocol prompt was sent as a single user turn]
- **Stop sequences.** [TODO: confirm — likely none]
- **Seed.** [TODO: confirm — likely none set, since OpenRouter does not guarantee deterministic seeding across providers]

## Run collection

- **Date range.** [TODO: confirm — dataset timestamps span the period the runs were collected]
- **Total attempted rows.** Not exhaustively logged outside the cleaned dataset. The cleaned dataset contains 697 successful rows.
- **Failed runs.** Three failures occurred for `gpt-4-0314` (97 successful out of 100 attempted). The failure mode was either an API error or a parser error; the original error messages are not retained in the cleaned dataset. Future versions should preserve `error` and `success=False` rows in the public CSV.
- **Run-per-model count.** 100 attempted per model, 100 successful for six models, 97 successful for `gpt-4-0314`.

## Response format and parsing

Each run prompts the model to emit a structured response consisting of:

1. A `run_header` JSON block.
2. Six `question_N` JSON blocks containing the scored fields and rationales.
3. A final `summary` JSON block restating the headline scores.

The full prompt is in `prompts/logic_drift_protocol_v23_used_for_dataset.md`.

**Parsing.** Model responses were parsed by a separate Python extraction layer that:

1. Located each JSON block by its leading key.
2. Repaired common JSON malformations (trailing commas, mixed quote styles, embedded code-fence markers).
3. Extracted numeric score fields and free-text rationale fields into the columns of the cleaned CSV.

The parser code is **not included in this release.** Public release of the parser is on the v2 roadmap. Until then, the cleaned CSV should be treated as the canonical record of model outputs, and the parsing layer should be treated as a documented but unverified link in the reproducibility chain. Anyone wishing to reproduce the parsing step from raw model responses can request the extraction code directly (see paper §3.4 and §6).

## Determinism, replication, and the dz inflation note

Within-model variance on the score fields is small (most standard deviations are between 1 and 5 on the 0–100 scale; gpt-4-0314 is an outlier with SDs up to 19.54 on the deductive-validity field). Two consequences:

1. **dz values are inflated relative to typical psychological-measurement reporting.** Within-condition standard deviations near zero produce paired effect sizes that look astronomical (the dz of 42.71 reported for gemini-3-pro on the consensus-minus-deductive contrast is mathematically real but reflects near-deterministic outputs rather than overwhelming evidential strength). The paper acknowledges this in §6.
2. **Re-running the protocol at the same decoding settings should reproduce these numbers within a few units.** Re-running at higher temperatures will produce wider within-condition distributions and smaller dz values; the mean differences should be similar.

## File layout

```
data/raw/ldp_complete_dataset_100_runs_7llms.csv     # canonical parsed dataset
data/processed/model_summary.csv                      # per-model means and SDs
data/processed/overall_summary.csv                    # cross-model means
data/processed/inferential_summary.csv                # paired CIs and Cohen's dz
figures/*.svg                                         # generated bar charts
figures/pdf/*.pdf                                     # PDF versions for paper embedding
scripts/analyze_logic_drift.py                        # stdlib-only analysis driver
prompts/logic_drift_protocol_v23_used_for_dataset.md  # the prompt sent to each model
paper/source/logic_drift_arxiv_working_draft.md       # paper source (markdown)
paper/source/logic_drift.tex                          # paper source (LaTeX)
paper/refs/references.bib                             # bibliography
```

## Reproducing the analysis

From the repository root:

```powershell
python .\scripts\analyze_logic_drift.py
```

Requires Python 3.10+. No third-party dependencies. Output lands in `data/processed/` and `figures/`.

## Reproducing the paper PDF

From `paper/`:

```powershell
make
```

Requires a LaTeX distribution (tested with MiKTeX) and Inkscape for SVG-to-PDF conversion. Output lands in `paper/build/logic_drift.pdf`.
