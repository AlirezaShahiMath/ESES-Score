#!/bin/bash

PDB_DIR=./pdbbind_v2016_general-set/general-set
OUT_DIR=./features/eses_out

mkdir -p $OUT_DIR

for d in $PDB_DIR/*; do
    pdbid=$(basename $d)

    eses \
        --input $d/${pdbid}_protein.pdb \
        --output $OUT_DIR/$pdbid
done
