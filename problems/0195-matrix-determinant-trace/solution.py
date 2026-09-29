def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    n = len(matrix)


    trace = sum(matrix[i][i] for i in range(n))


    def get_det(mat: list[list[float]]) -> float:
        size = len(mat)
        if size == 1:
            return mat[0][0]
        if size == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        det = 0.0
        for col in range(size):
            sub_matrix = [row[:col] + row[col + 1:] for row in mat[1:]]
            sign = 1 if col % 2 == 0 else -1
            det += sign * mat[0][col] * get_det(sub_matrix)

        return det

    determinant = get_det(matrix)

    return determinant, trace