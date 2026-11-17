# Screening agreement data and code

Screening agreement records for the manuscript *"A systematic review of validity evidence for artificial intelligence assessing clinician empathy"* (71 studies, 74 reports).

Authors: N. Kunnath, P. Gurram, M. Elgendi (corresponding author).

## Contents

| File | What it contains |
|---|---|
| [`data/Supplementary_Data_2_title_abstract_screening_agreement.xlsx`](data/Supplementary_Data_2_title_abstract_screening_agreement.xlsx) | Both reviewers' independent title and abstract screening decisions for 3,158 journal-article records, consensus decisions, the agreement record and the full-text cross-check (Supplementary Data 2) |
| [`code/screening_agreement_kappa.py`](code/screening_agreement_kappa.py) | Calculates observed agreement, Cohen's kappa and its 95% bootstrap confidence interval from the reviewers' decisions |

## Running the analysis

Requirements: Python 3.10 or later, `numpy`, `openpyxl`.

```bash
python code/screening_agreement_kappa.py
```

Expected output: 3,115 of 3,158 records agreed (98.6%), Cohen's kappa 0.92 (95% bootstrap CI 0.90-0.94; 100,000 resamples, seed 20261116).

## Licence

Code: MIT licence ([`LICENSE`](LICENSE)). Data: CC BY 4.0 ([`LICENSE-DATA.md`](LICENSE-DATA.md)).

## Citation

Kunnath N, Gurram P, Elgendi M. A systematic review of validity evidence for artificial intelligence assessing clinician empathy. Manuscript submitted for publication.
