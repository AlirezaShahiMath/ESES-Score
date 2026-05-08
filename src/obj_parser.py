import numpy as np


def load_obj(path):
    vertices = []
    faces = []

    with open(path, "r", errors="ignore") as f:
        for line in f:
            if line.startswith("v "):
                p = line.strip().split()
                vertices.append([float(p[1]), float(p[2]), float(p[3])])

            elif line.startswith("f "):
                p = line.strip().split()[1:]
                idx = []

                for x in p[:3]:
                    idx.append(int(x.split("/")[0]) - 1)

                faces.append(idx)

    return (
        np.asarray(vertices, dtype=np.float64),
        np.asarray(faces, dtype=np.int64),
    )
