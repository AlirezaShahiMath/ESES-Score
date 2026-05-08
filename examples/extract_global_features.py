import os
import csv
from src.global_features import extract_global_features

INPUT_DIR = "./features/eses_out"
OUT_CSV = "./features/global_features.csv"

rows = []

for pdbid in os.listdir(INPUT_DIR):
    obj = os.path.join(INPUT_DIR, pdbid, "marching_cubes.obj")

    if not os.path.exists(obj):
        continue

    feats = extract_global_features(obj)
    feats["pdbid"] = pdbid
    rows.append(feats)

with open(OUT_CSV, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
