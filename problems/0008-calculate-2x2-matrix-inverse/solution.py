def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    det = a * d - b * c

    if det == 0:
        return None
    matrix_adj = [
        [d, -b],
        [-c, a]
    ]

    matrix_inv = [[(1 / det) * val for val in row] for row in matrix_adj]

    return matrix_inv
