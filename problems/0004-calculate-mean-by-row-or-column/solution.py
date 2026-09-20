
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	a = matrix
	if mode == "column":
		a = [list(e) for e in list(zip(*matrix))]

	means = [sum(row) / len(row) for row in a]
	

	return means