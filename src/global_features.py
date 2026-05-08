import numpy as np
from src.obj_parser import load_obj
from src.geometry_utils import tri_areas_normals, ensure_outward
from src.curvature_utils import mean_curvature_signed


def extract_global_features(obj_path):
    V, F = load_obj(obj_path)

    F, vol = ensure_outward(V, F)

    face_area, _ = tri_areas_normals(V, F)
    total_area = float(np.sum(face_area))

    Hs = mean_curvature_signed(V, F)

    face_H = (
        Hs[F[:, 0]] +
        Hs[F[:, 1]] +
        Hs[F[:, 2]]
    ) / 3.0

    concave_mask = face_H < 0
    convex_mask = face_H > 0

    concave_area = float(np.sum(face_area[concave_mask]))
    convex_area = float(np.sum(face_area[convex_mask]))

    return {
        "surface_area_A2": total_area,
        "volume_A3": vol,
        "concave_area_A2": concave_area,
        "convex_area_A2": convex_area,
        "concave_frac": concave_area / total_area,
        "convex_frac": convex_area / total_area,
    }
