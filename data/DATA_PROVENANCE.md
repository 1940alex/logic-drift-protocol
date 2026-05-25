# Data Provenance

## Included Dataset

`data/raw/ldp_complete_dataset_100_runs_7llms.csv`

This is the primary cleaned dataset for the arXiv-oriented working draft. It contains 697 successful rows across seven models.

## Protocol Prompt

The prompt used for the cleaned dataset is stored as:

`prompts/logic_drift_protocol_v23_used_for_dataset.md`

Earlier package versions named this prompt `logic_drift_protocol_v24.md`, but the prompt body and the raw dataset both record `LDP-v23`. The file was renamed to avoid implying that the analyzed data came from a later protocol version.

## Related Source Files Not Included

Several intermediate run files existed during project development but are not included in this streamlined release because they were either incomplete, superseded by the cleaned dataset, or contained embedded local configuration/secrets. The included CSV is the only dataset used by the analysis script and paper draft.

## Cleaning Notes

The archival CSV was cleaned to remove an unused trailing duplicate column (`summary_scores_system_B`). No analyzed score fields were changed.

One `gemini-3-pro` run is missing a complete science/neutral pair for the Semantic Delta comparison, so `data/processed/inferential_summary.csv` reports `n=99` for the `gemini-3-pro` `science_minus_neutral` comparison and `n=696` for the all-model `science_minus_neutral` comparison.

## Aggregator Caveat

Runs were collected through OpenRouter. Because aggregator endpoints can route through provider-hosted inference services with hidden server-side settings, the package should not be treated as a token-level reproduction record for provider-native endpoints. The pilot anchors its claims on macro-level behavioral score patterns in the recorded outputs rather than on exact token probabilities or provider-internal sampling details.

## Paper Implication

The paper should avoid saying simply "700 runs" unless the failed/missing runs are explained. The safer phrasing is:

> We analyzed 697 successful protocol runs across seven models.

If the author wants to retain "700 attempted runs," the methods section should first identify the source file that contains those attempted runs and provide explicit exclusion criteria. The included primary CSV contains only the 697 successful analyzed rows.
