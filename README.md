# RA transcriptomic therapeutic-response framework

Reproducibility package for the manuscript:

**Therapeutic-response transcriptomes in rheumatoid arthritis depend on treatment and tissue context**

## Archived release

Version 1.0.0 is permanently archived on Zenodo.

**DOI:** 10.5281/zenodo.22019057

## Overview

This repository supports a cross-cohort re-analysis of publicly available rheumatoid arthritis (RA) transcriptomic datasets spanning abatacept, TNF inhibitors, methotrexate and tocilizumab. The analysis separates:

1. baseline response state (BRS),
2. longitudinal drug-response index (DRI), and
3. cross-cohort transferability.

The central design principle is that response-associated transcriptional programmes are interpreted jointly with treatment mechanism, tissue and evidence level rather than as universal signatures.

## Public source datasets

Core GEO accessions used in the manuscript include GSE68215, GSE33377, GSE15258, GSE129705, GSE176440, GSE45867 and GSE198520. GSE93272 is used only for the frozen partial external gene-signature transfer test described in the manuscript.

Primary expression data should be downloaded directly from NCBI GEO. No third-party raw expression matrices are redistributed in this repository.

## Repository structure

- `data/derived/` - derived patient-level or summary outputs used for sensitivity analyses and figures.
- `scripts/` - reproducibility scripts operating on public/derived inputs.
- `docs/` - editable figure package and supporting documentation.
- `DATA_SOURCES.md` - accession-level source map.
- `METHODS_REPRODUCIBILITY.md` - analysis conventions and evidence hierarchy.
- `CITATION.cff` - citation metadata.
- `requirements.txt` - Python package requirements.

## Key reproducibility conventions

- Discovery cohorts are not counted as external validation.
- Feature sets and directions are frozen before transfer tests whenever possible.
- Observed-direction AUC is retained; direction-free AUC is secondary descriptive information.
- Longitudinal molecular displacement is analysed separately from baseline prediction.
- Synovial and blood contexts are not assumed to be interchangeable.

## Re-running analyses

The included scripts reproduce the sensitivity analyses from the derived tables and provide templates for re-running public-data analyses after downloading the original GEO matrices. See `METHODS_REPRODUCIBILITY.md` for details.

## Data availability

All primary transcriptomic datasets are publicly available from NCBI GEO. Derived tables in this repository contain only non-identifying analysis variables and summary scores reconstructed from public records.

## Licence

Code is released under the MIT License. Derived tables are provided for scientific reproducibility; users should cite the originating GEO studies and the associated manuscript.
