import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	v1_norm, v2_norm = np.sum(v1 * v1) ** (1/2), np.sum(v2 * v2) ** (1/2)

	cosine = np.dot(v1, v2) / (v1_norm * v2_norm)
	return cosine