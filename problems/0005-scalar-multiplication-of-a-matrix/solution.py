
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	

	a_scalar = [list(map(lambda x: x * scalar, row)) for row in matrix]

	return a_scalar