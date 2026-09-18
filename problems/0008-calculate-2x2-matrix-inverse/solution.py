import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a = np.array(matrix)

    det = np.linalg.det(a)

    if det == 0:
        return None

    return np.linalg.inv(a).tolist()