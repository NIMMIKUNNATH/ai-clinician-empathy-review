"""Title and abstract screening agreement between the two reviewers.

Reads the independent decisions in Supplementary Data 2 (sheet 'TA Independent
Comparison') and reports observed agreement, Cohen's kappa and a percentile
bootstrap 95% confidence interval (records resampled with replacement).

Usage:
    python code/screening_agreement_kappa.py [path_to_Supplementary_Data_2.xlsx]
"""
import sys
from pathlib import Path

import numpy as np
import openpyxl

ROOT = Path(__file__).resolve().parent.parent
XLSX = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data" / "Supplementary_Data_2_title_abstract_screening_agreement.xlsx"
N_BOOT = 100_000
SEED = 20261116


def kappa(a, b):
    """Cohen's kappa for two binary raters (1 = Include, 0 = Exclude)."""
    po = np.mean(a == b, axis=-1)
    pa, pb = a.mean(axis=-1), b.mean(axis=-1)
    pe = pa * pb + (1 - pa) * (1 - pb)
    return (po - pe) / (1 - pe)


ws = openpyxl.load_workbook(XLSX, read_only=True)["TA Independent Comparison"]
rows = list(ws.iter_rows(values_only=True))
col = {name: i for i, name in enumerate(rows[0])}
r1 = np.array([r[col["Reviewer 1"]] == "Include" for r in rows[1:] if r[0]], dtype=float)
r2 = np.array([r[col["Reviewer 2"]] == "Include" for r in rows[1:] if r[0]], dtype=float)

n = len(r1)
agree = int((r1 == r2).sum())
k = float(kappa(r1, r2))

rng = np.random.default_rng(SEED)
boot = np.empty(N_BOOT)
for start in range(0, N_BOOT, 10_000):
    idx = rng.integers(0, n, size=(min(10_000, N_BOOT - start), n))
    boot[start:start + len(idx)] = kappa(r1[idx], r2[idx])
lo, hi = np.percentile(boot, [2.5, 97.5])

print(f"Records compared: {n}")
print(f"Both include: {int(((r1 == 1) & (r2 == 1)).sum())}, both exclude: {int(((r1 == 0) & (r2 == 0)).sum())}, disagreements: {n - agree}")
print(f"Observed agreement: {agree}/{n} ({100 * agree / n:.1f}%)")
print(f"Cohen's kappa: {k:.3f} (95% bootstrap CI {lo:.3f}-{hi:.3f}; {N_BOOT:,} resamples, seed {SEED})")
