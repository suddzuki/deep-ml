
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:

	n = len(vectors)
	m = len(vectors[0])

	means = [sum(row) / len(row) for row in vectors]

	centr_matrix = [[feat - means[i] for feat in vectors[i]] for i in range(n)]

	df = 1/(m-1)

	cov = [[df * sum(a * b for a,b in zip(centr_matrix[i],centr_matrix[j])) for j in range(n)] for i in range(n)]

	return cov