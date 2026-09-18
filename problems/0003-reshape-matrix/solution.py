import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	an = np.array(a)
	old_shape = an.shape
	reshaped_matrix = []
	if (new_shape[0] * new_shape[1] == old_shape[0] * old_shape[1]):
		reshaped_matrix = an.reshape(new_shape).tolist()
	return reshaped_matrix