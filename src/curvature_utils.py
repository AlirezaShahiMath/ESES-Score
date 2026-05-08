import numpy as np
from src.geometry_utils import tri_areas_normals


def vertex_normals(V, F):
    face_area, fn = tri_areas_normals(V, F)

    N = np.zeros_like(V)

    for t in range(F.shape[0]):
        i, j, k = F[t]
        w = face_area[t]

        N[i] += fn[t] * w
        N[j] += fn[t] * w
        N[k] += fn[t] * w

    nrm = np.linalg.norm(N, axis=1)
    return N / np.maximum(nrm[:, None], 1e-30)


def cotangent(a, b):
    cross = np.linalg.norm(np.cross(a, b))
    if cross < 1e-30:
        return 0.0
    return float(np.dot(a, b) / cross)


def mean_curvature_signed(V, F):
    nV = V.shape[0]
    VN = vertex_normals(V, F)

    face_area, _ = tri_areas_normals(V, F)

    A = np.zeros(nV)

    for t in range(F.shape[0]):
        i, j, k = F[t]
        a = face_area[t] / 3.0
        A[i] += a
        A[j] += a
        A[k] += a

    A = np.maximum(A, 1e-30)

    Hn = np.zeros((nV, 3))

    for t in range(F.shape[0]):
        i, j, k = F[t]
        vi, vj, vk = V[i], V[j], V[k]

        cot_i = cotangent(vj - vi, vk - vi)
        cot_j = cotangent(vi - vj, vk - vj)
        cot_k = cotangent(vi - vk, vj - vk)

        w_ij = 0.5 * cot_k
        w_jk = 0.5 * cot_i
        w_ki = 0.5 * cot_j

        Hn[i] += w_ij * (vj - vi)
        Hn[j] += w_ij * (vi - vj)

        Hn[j] += w_jk * (vk - vj)
        Hn[k] += w_jk * (vj - vk)

        Hn[k] += w_ki * (vi - vk)
        Hn[i] += w_ki * (vk - vi)

    Hn = Hn / (2.0 * A[:, None])

    H = 0.5 * np.linalg.norm(Hn, axis=1)
    sign = np.sign(np.einsum("ij,ij->i", Hn, VN))

    return H * sign
