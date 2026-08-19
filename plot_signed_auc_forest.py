#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"data"/"derived"/"RA_response_signed_AUC_CI_matrix.csv"
df=pd.read_csv(p)
print(df.columns.tolist())
# This script intentionally leaves column mapping explicit because the evidence matrix may evolve.
# Use observed-direction AUC and its CI columns to build the final forest plot.
