import numpy as np
from src.obj_parser import load_obj
from src.geometry_utils import tri_areas_normals, ensure_outward
from src.curvature_utils import mean_curvature_signed


def read_mol2_atoms(path):
    pts = []
    in_atoms = False

    with open(path, "r", errors="ignore") as f:
        for line in f:
            line = line.strip()

            if line.startswith("@<TRIPOS>ATOM"):
                in_atoms = True
                continue

            if line.startswith("@<TRIPOS>") and in_atoms:
                break

            if in_atoms:
                p = line.split()
                pts.append([float(p[2]), float(p[3]), float(p[4])])

    return np.asarray(pts)


def extract_pocket_features(obj_path, ligand_path, cutoff=6.0):
    V, F = load_obj(obj_path)
    ligand = read_mol2_atoms(ligand_path)

    F, vol = ensure_outward(V, F)

    face_area, _ = tri_areas_normals(V, F)
    Hs = mean_curvature_signed(V, F)

    face_H = (
        Hs[F[:, 0]] +
        Hs[F[:, 1]] +
        Hs[F[:, 2]]
    ) / 3.0

    centroids = (
        V[F[:, 0]] +
        V[F[:, 1]] +
        V[F[:, 2]]
    ) / 3.0

    d2 = np.sum(
        (centroids[:, None, :] - ligand[None, :, :]) ** 2,
        axis=2
    )

    dmin = np.sqrt(np.min(d2, axis=1))
    pocket_mask = dmin <= cutoff

    pocket_area = float(np.sum(face_area[pocket_mask]))

    concave_mask = face_H < 0
    pocket_concave = pocket_mask & concave_mask

    pocket_concave_area = float(
        np.sum(face_area[pocket_concave])
    )

    return {
        "volume_A3": vol,
        "pocket_area_A2": pocket_area,
        "pocket_concave_area_A2": pocket_concave_area,
        "pocket_concave_frac": pocket_concave_area / pocket_area
    }
