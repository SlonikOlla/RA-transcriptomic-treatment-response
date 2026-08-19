#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
p=Path(__file__).resolve().parents[1]/"data"/"derived"/"GSE68215_lineage_composition_sensitivity.csv"
print(pd.read_csv(p).to_string(index=False))
