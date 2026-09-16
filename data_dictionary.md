# Data Dictionary

Covers `data/raw/REE_Stage1_MASTER_All_Claude_Datasets_Unique.xlsx`, sheet `MASTER_Unique_Data` (413 rows, 56 columns) — the current primary evidence pool. Only columns that actually exist in this sheet are documented. Null counts are out of 413 rows. "NR" appearing as a cell value (rather than a true blank) means the source paper's non-reporting was recorded explicitly, as opposed to the field never having been extracted.

For the alternate 277-row snapshot's own schema, see the `Feature_Dictionary` sheet inside `REE_Stage1_MASTER_All_Unique_Datasets_For_Professor.xlsx` directly (not duplicated here, since its column set differs — notably it has no pH field).

## Identifiers / Provenance

| Column | Meaning | Unit | Type | Example | Role | Missing values |
|---|---|---|---|---|---|---|
| `Final Row ID` | Unique record identifier assigned during extraction | – | string | `F-001` | Metadata | 60 null — rows added in later merge batches were not all assigned this ID; `Source_Row_IDs` partially covers the gap |
| `Paper` | Free-text source paper label (author + year) | – | string | `Rabatho 2013` | Metadata | 0 null. Not fully normalised — 119 distinct values vs. 74 distinct DOIs, indicating some duplicate/variant labels for the same paper |
| `group_paper_id` | Integer/text ID grouping rows by source paper | – | string/int | `0` | Metadata (grouping key) | 119 null |
| `DOI` | Digital Object Identifier of the source paper | – | string | `10.1007/s10163-012-0105-6` | Metadata (provenance) | 0 null |
| `source_dataset` | Which of the 6 merge-batch source files this row's kept version came from | – | string | `v4` | Metadata | 0 null |
| `Source_Datasets` | All source batches this row appeared in before merge | – | string | `v4` | Metadata | 0 null |
| `Source_Row_IDs` | Original row ID(s) in the source batch(es) | – | string | `F-001` | Metadata | 60 null |
| `Merged_Duplicate_Count` | Number of duplicate reports of the same experiment merged into this row | count | int | `1` | Metadata | 0 null |

## Feedstock / Composition Features

| Column | Meaning | Unit | Type | Example | Role | Missing values |
|---|---|---|---|---|---|---|
| `Feedstock` | Free-text feedstock description as extracted from the paper | – | string | `NdFeB` | Feature (raw) | 0 null |
| `feat_feedstock_group` | Feedstock bucketed into a coarse category (e.g. `NdFeB_magnet`, `NiMH_battery`) | – | string | `NdFeB_magnet` | Feature (engineered) | 129 null — bucketing not applied to all rows, notably later merge batches |
| `Raw Material Source (composition)` | Free-text feedstock elemental composition as reported | – | string | `NdFeB(-Dy) magnetic waste sludge... Nd 35.1, Fe 29.5, Dy 1.1, B 0.5 wt%` | Feature (raw) | 8 null |
| `feat_total_REE_wt%` | Sum of parsed Nd/Pr/Dy/Tb/Y wt% from the composition text | wt% | float | `1.04` | Feature (engineered) | 272 null — only parsed where composition text matched an `Element ##.##%` pattern |
| `feat_Fe_to_REE_ratio` | Fe wt% ÷ total REE wt% | ratio | float | `0.003` | Feature (engineered) | 225 null |

## Leaching Condition Features

| Column | Meaning | Unit | Type | Example | Role | Missing values |
|---|---|---|---|---|---|---|
| `Leaching acid` | Free-text acid identity as extracted | – | string | `HCl` | Feature (raw) | 0 null |
| `feat_acid_type` | Acid bucketed into a coarse category | – | string | `HCl` | Feature (engineered) | 129 null |
| `feat_acid_is_mineral_strong` | 1 if acid is HCl/H₂SO₄/HNO₃ (strong mineral acid), else 0 | binary | float | `1.0` | Feature (engineered) | 129 null |
| `Acid conc.` | Free-text acid concentration as extracted | – | string | `3 M` | Feature (raw) | 18 null |
| `feat_acid_conc_molL` | Acid concentration normalised to mol/L | mol/L | float/str | `3` | Feature (engineered) | 108 null |
| `feat_leach_pH` | Leaching pH as reported | pH units | string | `NR` | Feature (engineered) | 123 true-null (in addition, ~277 rows hold the literal string `NR`) — pH is essentially unreported across this evidence pool; **never inferred from acid concentration** |
| `flag_pH_reported` | 1 if pH was explicitly reported, else 0 | binary | float | `0.0` | Feature (indicator) | 193 null; of non-null rows, 0 rows have value 1 — i.e. pH is not currently captured for any row |
| `Leach temp (extracted)` | Free-text leaching temperature | – | string | `25 C` | Feature (raw) | 60 null |
| `feat_leach_temp_C` | Leaching temperature normalised to °C | °C | float | `25.0` | Feature (engineered) | 149 null |
| `Leach time (extracted)` | Free-text leaching time | – | string | `180 min` | Feature (raw) | 0 null |
| `feat_leach_time_h` | Leaching time normalised to hours | h | float/str | `3` | Feature (engineered) | 101 null |
| `S:L or L:S ratio (extracted)` | Free-text solid:liquid or liquid:solid ratio | – | string | `NR` | Feature (raw) | 60 null |
| `feat_SL_gL` | Solid:liquid ratio normalised to an approximate g solid / L liquid basis | g/L | float | `50.0` | Feature (engineered) | 224 null — approximate; source formats highly heterogeneous |
| `Agitation/stirring (extracted)` | Free-text agitation/stirring description | – | string | `NR` | Feature (raw) | 60 null |
| `feat_agitation_rpm` | Stirring speed where explicitly reported in rpm | rpm | float/str | `120` | Feature (engineered) | 233 null |
| `Feedstock particle size (extracted)` | Free-text particle size description | – | string | `NR` | Feature (raw) | 60 null |
| `feat_particle_size_bucket` | Particle size bucketed into a coarse category | – | string | `Not_reported` | Feature (engineered) | 129 null |
| `Leach stages/cycles (extracted)` | Free-text number/description of leaching stages | – | string | `1 (single stage, NR if unstated)` | Feature (raw) | 62 null |
| `feat_leach_stages_n` | Number of leaching stages/cycles as an integer | count | float | `1.0` | Feature (engineered) | 147 null |

## Reporting-Completeness Indicator Flags

| Column | Meaning | Unit | Type | Example | Role | Missing values |
|---|---|---|---|---|---|---|
| `flag_SL_reported` | 1 if S:L ratio was explicitly reported, else 0 | binary | float | `0.0` | Feature (indicator) | 129 null |
| `flag_agitation_reported` | 1 if agitation was explicitly reported, else 0 | binary | float | `0.0` | Feature (indicator) | 129 null |
| `flag_particle_reported` | 1 if particle size was explicitly reported, else 0 | binary | float | `0.0` | Feature (indicator) | 129 null |
| `flag_acidconc_reported` | 1 if acid concentration was explicitly reported, else 0 | binary | float | `1.0` | Feature (indicator) | 129 null |
| `flag_temp_reported` | 1 if leach temperature was explicitly reported, else 0 | binary | float | `1.0` | Feature (indicator) | 129 null |
| `flag_time_reported` | 1 if leach time was explicitly reported, else 0 | binary | float | `1.0` | Feature (indicator) | 129 null |
| `flag_target_needs_manual_review` | 1 if the Stage-1 text contains numeric leaching info the automated parser could not confidently extract | binary | float | `0.0` | Metadata / QC | 129 null; 114 rows flagged 1 |

## Target Variables

| Column | Meaning | Unit | Type | Example | Role | Missing values |
|---|---|---|---|---|---|---|
| `STAGE 1: Leaching recovery` | Free-text Stage-1 recovery description as extracted from the paper | – | string | `Nd 90.3%, Dy 95.5% (Fe co-diss. 35.7%)` | Target (raw) | 79 null |
| `target_Nd_stage1_pct` | Nd Stage-1 recovery, parsed | % | float/str | `90.3` | **Target** | 232 null |
| `target_Pr_stage1_pct` | Pr Stage-1 recovery, parsed | % | float/str | `91.62` | **Target** | 260 null |
| `target_Dy_stage1_pct` | Dy Stage-1 recovery, parsed | % | float/str | `95.5` | **Target** | 274 null |
| `target_Tb_stage1_pct` | Tb Stage-1 recovery, parsed | % | float/str | (mostly `NR`) | **Target** | 301 null |
| `target_Y_stage1_pct` | Y Stage-1 recovery, parsed | % | float/str | (mostly `NR`) | **Target** | 293 null |
| `target_total_REE_stage1_pct` | Aggregate/total-REE Stage-1 recovery, used when a paper reports one combined figure instead of per-element values | % | float/str | `95` | Target (coarser, secondary) | 299 null. Mixes different REE baskets across papers (some Nd+Pr+Dy only, others all REEs including La/Ce) — treat as lower precision than per-element targets |
| `target_Fe_costripped_pct` | Fe co-dissolution % during Stage 1, where reported alongside REE recovery | % | float/str | `35.7` | Secondary target / selectivity feature | 327 null |
| `target_primary_REE_stage1_pct` | Recommended single ML target: Nd% if available, else mean of reported per-element REEs, else aggregate total-REE% | % | float/str | `90.3` | **Target (recommended primary)** | 134 null |
| `target_primary_REE_source` | Provenance tag for `target_primary_REE_stage1_pct` (`Nd_specific` / `other_element_mean` / `aggregate_total_REE` / free-text source notes / `unparsed`) | – | string | `Nd_specific` | Metadata / QC | 60 null. **Not fully standardised** — many values are free-text source notes (e.g. table/figure references) rather than the intended fixed category set; needs harmonisation before use as a clean feature |
| `target_stage1_note` | Free-text note on how the Stage-1 value was derived/interpreted | – | string | `complete_dissolution_narrative` | Metadata | 148 null |
| `target_recovery_class` | Intended as `target_primary_REE_stage1_pct` binned into Low/Medium/High | – | string | `High_>=90%` | Derived label (not yet standardised) | 127 null. **Mixed conventions** — contains at least two different labelling schemes inherited from merged source batches (`High_>=90%`/`Medium_70-90%`/`Low_<70%` alongside literal `CORE`, `EXTENDED`, `high`, `medium`, `low`, various `NR` variants); do not use as a clean categorical feature until harmonised |

## Downstream / QC Columns (Schema Present, Not Yet Populated)

| Column | Meaning | Unit | Type | Example | Role | Missing values |
|---|---|---|---|---|---|---|
| `Downstream_Oxalate_Step_Confirmed` | Intended to flag whether the source paper's downstream route was confirmed to include oxalate precipitation | binary | float | — | Metadata / QC | 413 null (100%) — not yet populated |
| `Oxalate_Step_Evidence` | Intended to hold the textual evidence supporting the above flag | – | float (placeholder) | — | Metadata / QC | 413 null (100%) — not yet populated |
| `Data_Type` | Intended to distinguish record types (e.g. experimental vs. review-derived) | – | float (placeholder) | — | Metadata / QC | 413 null (100%) — not yet populated |
| `Quality_Tier` | Intended to hold the CORE/REVIEW data-quality tier directly | – | float (placeholder) | — | Metadata / QC | 413 null (100%) — not yet populated; see `data/README.md` for an approximate CORE/REVIEW split derived from target-column completeness instead |
| `Notes` | Free-text analyst notes (e.g. flags for arithmetic inconsistencies found during extraction) | – | string | `FLAGGED for manual review: 2-stage cumulative...` | Metadata / QC | 396 null |
