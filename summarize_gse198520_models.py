#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
for name in ["GSE198520_multivariable_model_summary.csv","GSE198520_crossvalidated_model_comparison.csv"]:
    p=ROOT/"data"/"derived"/name
    if p.exists():
        print("\n",name)
        print(pd.read_csv(p).to_string(index=False))
