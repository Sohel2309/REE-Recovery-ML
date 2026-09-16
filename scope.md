# Locked Scientific Scope

This document records the scope locked for the current phase of the project. Changes to any of these boundaries should be treated as a scope change, not silently absorbed into the dataset or README.

## Feedstocks (locked: 2)

1. **NdFeB magnet waste** (including magnet swarf / hydrogen-decrepitation-stage material, and end-of-life magnets from disassembled electronics)
2. **Spent NiMH batteries**

These two feedstocks are real waste streams containing valuable REEs but with substantially different feedstock compositions and chemical environments (e.g. Fe-rich magnetic alloy vs. Ni/Co-rich battery electrode material). The contrast is used to test whether a predictive model can learn recovery behaviour across different real waste systems, rather than being specific to one feedstock. **This is not currently claimed as experimentally proven generalisation** — it is the reason both feedstocks were selected, not a demonstrated result.

Other feedstocks encountered during literature collection (e.g. fluorescent-lamp phosphor, red-mud/bauxite residue) are explicitly **out of scope** and are excluded from the modelling dataset where identified (see [`data/README.md`](../data/README.md) for how each current dataset snapshot handles this).

## Target REEs (locked: 5)

- **Nd** — Neodymium (preferred primary target, due to its importance in NdFeB magnet systems)
- **Pr** — Praseodymium
- **Dy** — Dysprosium
- **Tb** — Terbium
- **Y** — Yttrium

Pr, Dy, Tb, and Y are retained when directly reported by a source study. Total/aggregate REE values are retained as a secondary, coarser observation when a study reports only a combined figure — these are **never** silently converted into an individual-element recovery value.

## Acid Scope (locked: 10)

| # | Acid |
|---|---|
| 1 | HCl |
| 2 | H₂SO₄ |
| 3 | HNO₃ |
| 4 | H₃PO₄ |
| 5 | Citric acid |
| 6 | Acetic acid |
| 7 | Malic acid |
| 8 | Glycolic acid |
| 9 | Maleic acid |
| 10 | Ascorbic acid |

DES (deep eutectic solvent) and ionic-liquid leaching routes are excluded from the main dataset. No additional acids are added without an explicit scope decision.

**Current representation status:** as of the primary evidence-pool snapshot, 8 of the 10 locked acids have at least one represented observation (HCl, H₂SO₄, HNO₃, H₃PO₄, citric acid, acetic acid, malic acid, ascorbic acid). **Glycolic acid and maleic acid currently have zero represented rows** — they remain locked in scope for future literature collection.

## Literature Inclusion Logic

The dataset is not intended to contain every paper on REE leaching. A record is included only if it fits:

```
Real waste feedstock → Stage-1 acid leaching → downstream recovery pathway involving oxalic-acid/oxalate precipitation
```

- Synthetic REE solution experiments (no real waste feedstock) do not satisfy the real-feedstock requirement on their own.
- Studies using an alternative downstream route without the required oxalate stage are not treated as equivalent to in-scope studies.
- Stage-2/Stage-3 (downstream) results are never leaked into the Stage-1 recovery target.

See [`methodology.md`](methodology.md) for the current data-quality caveat regarding per-row verification of this criterion.

## Stage-1 Variables Captured

For each usable experimental record, the dataset attempts to capture: feedstock, acid, acid concentration, pH, leaching temperature, leaching time, solid:liquid / liquid:solid ratio, agitation/stirring speed, particle size, number of leaching stages/cycles, feedstock composition, REE composition, Fe/Ni/Co/B impurity information (where directly reported), Fe:REE ratio (where directly supported), REE identity, Stage-1 recovery/extraction, DOI/paper source, paper/group identifier, and provenance information.

Rules applied during extraction:
- pH is **never** inferred from acid concentration.
- Values are **never** estimated from a graph unless the source explicitly supports that extraction, and the record is marked accordingly.
- Missing operating conditions are **never** fabricated.
- Retention is **never** converted into recovery.
- Recovery is **never** derived from concentration unless a complete, explicit mass balance supports it.

## Current Stage-1 Boundary

The current modelling target is **Stage-1 (acid leaching) recovery/extraction only**. Downstream separation/purification and oxalate-precipitation results are used only as an inclusion filter at the literature-selection stage (a study must plausibly belong to a pathway that includes them) — their own recovery/yield numbers are not part of the Stage-1 target and are not present as target columns in the current dataset.
