import os
import csv
from src.pocket_features import extract_pocket_features

INPUT_DIR = "./features/eses_out"
PDBBIND_DIR = "./pdbbind_v2016_general-set/general-set"
OUT_CSV = "./features/pocket_features.csv"

rows = []

for pdbid in os.listdir(INPUT_DIR):
    obj = os.path.join(INPUT_DIR, pdbid, "marching_cubes.obj")
    lig = os.path.join(PDBBIND_DIR, pdbid, f"{pdbid}_ligand.mol2")

    if not os.path.exists(obj):
        continue
    if not os.path.exists(lig):
        continue

    feats = extract_pocket_features(obj, lig)
    feats["pdbid"] = pdbid
    rows.append(feats)

with open(OUT_CSV, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
