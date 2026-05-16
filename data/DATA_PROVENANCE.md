# Data Provenance

## Included Dataset

`data/raw/ldp_complete_dataset_100_runs_7llms.csv`

Source file found at:

`C:\Users\atsak\Downloads\1216ldp_complete_dataset_100_runs_7llms.csv`

Observed source timestamp:

`2025-12-16 05:16:26`

This is currently treated as the best cleaned dataset for the v18 paper. It contains 697 successful rows across seven models.

## Related Source Files Found But Not Used As Primary

- `C:\Users\atsak\Downloads\combined_runs_700.csv` - 700 rows, but only 459 marked successful and 241 marked failed.
- `C:\Users\atsak\Downloads\final_combined_runs.csv` - 940 rows, 699 successful and 241 failed, apparently combining multiple passes.
- `C:\Users\atsak\Downloads\clean_completed_runs.csv` - 597 successful rows.
- `C:\Users\atsak\Downloads\ldp_raw_data_80_runs_3llms_20251215_184417.json` - found as supporting raw data but excluded from the shareable package because its embedded run config contained an old API key.
- `C:\Users\atsak\Downloads\1214ldp_raw_data_7_llm_20_runs.json` - found as supporting raw data but excluded from the shareable package because its embedded run config contained an old API key.

## Paper Implication

The paper should avoid saying simply "700 runs" unless the failed/missing runs are explained. The safer phrasing is:

> We analyzed 697 successful protocol runs across seven models.

If the author wants to retain "700 attempted runs," the methods section should explain that three runs were excluded from the cleaned analysis dataset and provide exclusion criteria.
