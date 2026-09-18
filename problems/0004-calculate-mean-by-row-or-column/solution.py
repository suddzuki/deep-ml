import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	intsructions = {'column': 0, 'row': 1}

	a = np.array(matrix)

	means = a.mean(axis = intsructions[mode])

	return means