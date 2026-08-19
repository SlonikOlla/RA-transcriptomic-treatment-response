# Methods and reproducibility notes

## Evidence hierarchy

Analyses are labelled as discovery/hypothesis generation, internal transfer, frozen external validation, or longitudinal mechanistic/remodeling evidence. Discovery performance is never presented as external validation.

## Baseline response state

Programme scores are computed from predefined gene sets using within-dataset standardized expression. Binary response analyses retain the observed high-score AUC direction. Direction-free AUC = max(AUC, 1-AUC) is reported only as a secondary discrimination statistic.

## Longitudinal remodeling

Signed programme change is post-treatment minus baseline. Global DRI is the root-mean-square standardized transcriptomic displacement across expressed features. Clinical coupling is assessed separately using DAS28 improvement.

## GSE198520 sensitivity analysis

Patient-level age, sex, anti-TNF drug, synovial pathotype, baseline DAS28 and DAS28 change were reconstructed from public GEO sample metadata and matched to baseline ETC/OXPHOS scores. Logistic and linear sensitivity models assess whether the ETC/OXPHOS effect persists after adjustment.

## GSE68215 lineage sensitivity

Because measured differential blood counts were not publicly linked to the expression samples, myeloid, B-cell/CXCL13 and Th1/T-cell programme scores were used as expression-derived lineage proxies. This is explicitly a sensitivity analysis and is not described as measured cell-count adjustment.

## Important limitation

The most informative future validation would use prospectively collected or sample-linked measured leukocyte differentials in an independent whole-blood cohort and harmonized treatment/tissue sampling.
