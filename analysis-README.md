# Preliminary Analysis

This folder contains the current preliminary evidence plots (`recovery_plots/REE_Individual_Element_Recovery_Plots.pdf`), generated from the primary evidence pool (`data/raw/REE_Stage1_MASTER_All_Claude_Datasets_Unique.xlsx`). This is exploratory literature-data analysis, not a modelling result — no ML has been performed.

Each plot shows Stage-1 recovery (%) vs. acid concentration (mol/L) for one REE, coloured/marked by acid, with the observation count `n` per acid given in the legend.

## Dy — Dysprosium Recovery vs. Acid Concentration

Legend counts: HCl (n=4), HNO₃ (n=6), H₃PO₄ (n=1), Citric acid (n=81), Acetic acid (n=4), Malic acid (n=1), Ascorbic acid (n=4).

Reported Dy recovery spans roughly 12% to ~100% across the evidence pool. Citric acid, by far the most heavily represented acid for this element, shows recovery ranging from about 12% to 100% even within a narrow concentration band (e.g. multiple points clustered near 0.5–1.5 mol/L span roughly 20–95% recovery). HCl and HNO₃ observations sit mostly in the high-recovery region. The spread suggests element identity interacts with acid choice in a way that a single acid-concentration rule does not capture — a pattern, not a settled mechanism.

## Nd — Neodymium Recovery vs. Acid Concentration (primary target)

Legend counts: HCl (n=12), H₂SO₄ (n=11), HNO₃ (n=6), H₃PO₄ (n=1), Citric acid (n=78), Acetic acid (n=4), Malic acid (n=6), Ascorbic acid (n=4).

Nd recovery ranges from under 20% (dilute citric acid conditions) to ~100% (HCl and H₂SO₄ at various concentrations, and citric acid at some conditions). HCl trends high across most of its reported concentration range (0.2–6 mol/L), while citric acid — again the largest single group — shows recovery values spanning the full range at similar concentrations. No single acid or concentration threshold separates high- from low-recovery outcomes cleanly, which is the core observation motivating a multivariate modelling approach.

## Pr — Praseodymium Recovery vs. Acid Concentration

Legend counts: HCl (n=7), H₂SO₄ (n=3), Citric acid (n=81), Acetic acid (n=3), Malic acid (n=1), Ascorbic acid (n=4).

Similar overall pattern to Nd: HCl and H₂SO₄ points sit mostly in the higher-recovery region, while citric acid — the dominant group by count — spans roughly 18% to ~90% recovery across its concentration range.

## Tb — Terbium Recovery vs. Acid Concentration

Legend counts: H₂SO₄ (n=2), Citric acid (n=72).

Tb has the narrowest acid coverage of the five target REEs in the current evidence pool — almost all observations are from citric acid, with only two H₂SO₄ points. Reported recovery spans roughly 8% to 100%. Because acid diversity is so limited for Tb, cross-acid comparisons for this element should be treated with particular caution until more data are collected.

## Y — Yttrium Recovery vs. Acid Concentration

Legend counts: HCl (n=1), H₂SO₄ (n=10), Citric acid (n=53).

H₂SO₄ observations for Y are concentrated in the high-recovery region (mostly >85%). Citric acid again shows the widest scatter, from roughly 15% to ~100%. Only a single HCl observation is currently present for Y — too few to support an HCl-specific claim for this element.

## Cross-Cutting Observations

- **Citric acid** is the most heavily represented acid for every target REE (72–81 observations depending on element) and consistently shows the largest recovery scatter at similar concentrations — indicating that concentration alone is a poor predictor for this acid, and that other variables (pH — currently unreported, temperature, time, feedstock composition) likely matter.
- **HCl** shows comparatively tight, high recovery across most of its reported range, though some lower-recovery exceptions exist.
- **Element identity** (Dy vs. Nd vs. Pr vs. Tb vs. Y) changes the shape and spread of the recovery-vs-concentration relationship, not just the average — supporting the inclusion of REE identity as a model feature rather than modelling recovery as acid- or condition-only.
- Acid coverage is **uneven across REEs** — Tb and Y currently have data from only 2–3 acids each, while Nd and Dy have data from up to 7–8 acids. This imbalance should inform how per-REE vs. pooled modelling is approached.

## Important Interpretation Notes

These are preliminary, literature-derived observations from an unvalidated evidence pool (see [`../data/README.md`](../data/README.md)). They are **not** causal claims, they do not rank acids, and no acid is identified here as "the best" or "the one responsible" for high recovery. They motivate — but do not substitute for — the planned multivariate ML analysis.
