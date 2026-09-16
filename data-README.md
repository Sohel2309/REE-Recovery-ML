# Data

This folder contains the literature-derived Stage-1 (acid-leaching) evidence pool for the project, in `raw/`, and its column-level documentation in `metadata/data_dictionary.md`.

## What the dataset contains

Each row represents one usable experimental record (or reported condition within a paper) describing acid leaching of NdFeB magnet waste or spent NiMH battery material, extracted from a published study. Columns capture the operating conditions (acid, concentration, pH, temperature, time, solid:liquid ratio, agitation, particle size, number of stages), feedstock/REE composition, and the reported Stage-1 recovery/extraction result, along with DOI, source paper, and provenance fields. Full column-by-column documentation is in [`metadata/data_dictionary.md`](metadata/data_dictionary.md).

## Two snapshots exist — which one is authoritative

Two dataset files are provided in `raw/`, reflecting two different points in the project's data-collection history:

### 1. `REE_Stage1_MASTER_All_Claude_Datasets_Unique.xlsx` — current evidence pool (primary)

- Sheet `MASTER_Unique_Data`: **413 unique rows**, mechanically merged and deduplicated from **453 raw rows** contributed by 6 source datasets (`v4 cleaned`: 228, `Claude Batch1`: 51, `Claude Batch2`: 70, `Claude Batch10`: 30, `Romano 2023 file`: 60, `This-session Liu/Das`: 14). Merge and dedup logic is recorded in the accompanying `Merge_Summary` and `Dedup_Audit` sheets.
- Includes a `feat_leach_pH` field (currently "NR"/not-reported for effectively all rows — see [Known Data Gaps](#known-data-gaps)).
- Includes `Quality_Tier`, `Data_Type`, and `Downstream_Oxalate_Step_Confirmed` / `Oxalate_Step_Evidence` columns in its schema, but **these columns are currently empty for all 413 rows** — they are placeholders from the merge schema, not yet populated.
- **This file was determined to be the current, actively-used evidence pool** because: (a) all 7 literature sources explicitly verified in the project brief (Das 2026, Romano 2024, Romano 2023, Korkmaz 2018, Yang 2014, Otron 2024, Li 2025) are present by DOI in this file; and (b) per-acid, per-REE observation counts in this file match the counts shown in the legends of the current preliminary-analysis plots (`analysis/recovery_plots/`) and the current project presentation almost exactly (e.g. citric acid: Nd n=78, Dy n=81, Pr n=81, Tb n=72 — all reproduced exactly from this file's per-element target columns).

### 2. `REE_Stage1_MASTER_All_Unique_Datasets_For_Professor.xlsx` — earlier/parallel curated snapshot

- Sheet `Master_All_Unique_Rows`: 277 unique rows across all feedstocks encountered (including out-of-scope ones).
- Sheet `ML_Scope_NdFeB_NiMH`: 241 rows, pre-filtered to the two locked feedstocks (NdFeB magnet: 183, NdFeB swarf: 19, NiMH battery: 39).
- Sheet `Excluded_OutOfScope`: 36 rows explicitly identified and separated as out of scope (fluorescent-lamp phosphor: 16 rows, red-mud/bauxite residue: 20 rows).
- Sheet `Manual_Review`: 94 rows flagged for manual completion of the Stage-1 recovery target.
- Sheet `Feature_Dictionary`: column-level documentation for this snapshot's schema.
- **Does not include a pH field**, and its per-acid/per-REE row counts do not match the current plots/presentation — indicating it reflects an earlier or parallel branch of data collection rather than the dataset currently in active use.

**Both files are retained in this repository for transparency and auditability.** The 277-row snapshot's explicit scope-filtering (`ML_Scope_NdFeB_NiMH`) and `Manual_Review` structure are useful references for the QC work still to be done on the primary 413-row evidence pool (see [Future Work](../README.md#future-work)).

**Current literature evidence pool; final ML-ready dataset is under validation.** Neither file should be read as "the final dataset." Row counts reported anywhere in this repository (README, plots, presentation) refer to the underlying literature evidence pool at the time of writing, not a finalised training set.

## Inclusion Criteria

See [`../docs/scope.md`](../docs/scope.md) for the full locked scope (feedstocks, REEs, acids) and inclusion logic (real feedstock → Stage-1 leaching → downstream oxalate pathway).

## What "Stage 1" and "Recovery" Mean

**Stage 1** = the acid-leaching step only, i.e. the process by which REEs are dissolved out of the solid waste feedstock into the acid leachate. It does not include downstream separation/purification or oxalate-precipitation yields.

**Recovery** (Stage-1 recovery/extraction, %) = the reported percentage of a given REE (or, for aggregate records, of total REE content) dissolved from the feedstock into the leachate under the stated conditions, as directly reported by the source paper. Recovery is never derived by this project from retention or from concentration data unless the source study itself provides a complete, explicit mass balance supporting that derivation.

## CORE vs. REVIEW Data (Primary Evidence Pool)

Within the 413-row primary evidence pool:

| Category | Rows | Definition |
|---|---|---|
| Has at least one specific per-element Stage-1 recovery value (Nd/Pr/Dy/Tb/Y) | 188 | Closest to "CORE" — a directly reported, element-specific numerical recovery |
| Has only an aggregate/total-REE Stage-1 recovery value (no per-element breakdown at all) | 55 | REVIEW-type / coarser — mixes different REE baskets across papers; treat as lower precision than per-element rows |
| Neither a per-element nor an aggregate numeric value currently parsed (narrative/text-only Stage-1 description, or genuinely not reported) | 170 | Needs manual review before use as a modelling target |
| Flagged `flag_target_needs_manual_review = 1` (numeric information present in source text but not confidently auto-parsed) | 114 | Overlaps with the categories above; recommended next step is manual completion, following the same approach as the `Manual_Review` sheet in the 277-row snapshot |

(188 + 55 + 170 = 413, the full evidence pool; the manual-review flag count overlaps these categories rather than adding a fourth disjoint bucket.)

**Note on internal labelling inconsistency:** the raw `target_recovery_class` column in the primary file mixes at least two different labelling conventions inherited from its 6 merged source batches (e.g. `High_>=90%` / `Medium_70-90%` / `Low_<70%` alongside literal `CORE`, `EXTENDED`, `high`, `medium`, `low`, and various `NR` variants). This has **not yet been standardised** and is tracked as a QC item — do not treat this column as a clean categorical feature until harmonised.

## Why Missing Values Are Not Automatically Imputed

Per the project's data-quality philosophy, a missing operating condition (e.g. `NR` for pH, particle size, or agitation) is left as "not reported" rather than imputed, estimated, or inferred from a correlated field (e.g. pH is never inferred from acid concentration). Silent imputation would misrepresent what the source literature actually reported and could bias any downstream model. Handling of missing values (e.g. via explicit `flag_*_reported` indicator columns, which are already present in the schema) is left to the Preprocessing & Feature Engineering stage.

## Known Data Gaps

- **pH:** `flag_pH_reported` is 0 (not reported) for effectively all 413 rows in the primary evidence pool. pH was added as an important Stage-1 variable, but the current literature evidence essentially does not capture it. This is a priority gap for future literature collection.
- **Downstream oxalate confirmation:** `Downstream_Oxalate_Step_Confirmed` / `Oxalate_Step_Evidence` are empty for all rows in the primary file. Pathway-consistency was applied during literature selection but is not currently machine-verifiable per row.
- **Data-quality tier:** `Quality_Tier` and `Data_Type` columns exist in the schema but are empty. CORE/REVIEW distinction currently has to be approximated from target-column completeness (see table above) rather than read directly from a populated tier column.
- **Glycolic acid and maleic acid:** zero rows currently represented, despite being locked in acid scope.

## Provenance

Every row retains: `Final Row ID`, `Paper` (source paper label), `group_paper_id`, and `DOI`. The primary file additionally retains `source_dataset` / `Source_Datasets` / `Source_Row_IDs` / `Merged_Duplicate_Count`, documenting exactly which of the 6 merged source files each row came from and how many duplicate reports were merged into it (379 of 413 rows are unique with no merge; 34 rows represent 2–5 merged duplicate reports of the same underlying experiment).

## Evidence Pool vs. Final ML-Ready Dataset

The current files are **evidence pools**: every row that met the literature-inclusion criteria at extraction time, regardless of whether its Stage-1 recovery value ended up as a clean per-element number, an aggregate number, or an unparsed narrative description. A **final ML-ready dataset** — the next planned stage (see [Future Work](../README.md#future-work)) — will involve: reconciling the two existing snapshots, populating/standardising the QC fields described above, resolving the `target_recovery_class` labelling inconsistency, and deciding how aggregate-only and manual-review rows are handled (used with a provenance flag, downweighted, or excluded). None of that reconciliation has been performed yet.
