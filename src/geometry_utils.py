import numpy as np


def tri_areas_normals(V, F):
    v0 = V[F[:, 0]]
    v1 = V[F[:, 1]]
    v2 = V[F[:, 2]]

    normals = np.cross(v1 - v0, v2 - v0)
    area = 0.5 * np.linalg.norm(normals, axis=1)

    unit_normals = normals / np.maximum(
        np.linalg.norm(normals, axis=1, keepdims=True),
        1e-30
    )

    return area, unit_normals


def mesh_volume(V, F):
    v0 = V[F[:, 0]]
    v1 = V[F[:, 1]]
    v2 = V[F[:, 2]]

    vol = np.sum(
        np.einsum("ij,ij->i", v0, np.cross(v1, v2))
    ) / 6.0

    return float(vol)


def ensure_outward(V, F):
    vol = mesh_volume(V, F)

    if vol < 0:
        F = F[:, [0, 2, 1]].copy()
        vol = -vol

    return F, vol
