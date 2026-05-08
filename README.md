# ESES-Score

Implementation of ESES-based geometric descriptors for:

- Protein-ligand binding affinity prediction
- Binding site similarity analysis

---

## Features

This repository extracts:

### Global descriptors
- Surface area
- Volume
- Concave area
- Convex area
- Concave fraction
- Convex fraction

### Pocket descriptors
- Pocket area
- Pocket concave area
- Pocket concave fraction

---

## Repository Structure

```bash
examples/
src/
utils/
features/
```

---

## Usage

### 1. Generate ESES surfaces

```bash
bash examples/run_eses_surface_generation.sh
```

### 2. Extract global descriptors

```bash
python examples/extract_global_features.py
```

### 3. Extract pocket descriptors

```bash
python examples/extract_pocket_features.py
```

### 4. Regression

```bash
python examples/run_regression.py
```

### 5. Similarity

```bash
python examples/compute_similarity.py
```

### 6. AUC evaluation

```bash
python examples/run_auc_evaluation.py
```

---

## Dataset

Uses:

- PDBbind v2016 Refined Set
- CASF-2016 Core Set

Expected structure:

```bash
pdbbind_v2016_general-set/
└── general-set/
```

---

## Output

Generated files saved in:

```bash
features/
```

including:

- global_features.csv
- pocket_features.csv

---

## Citation

If using this repository, please cite our work.
