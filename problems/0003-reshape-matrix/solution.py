
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

	old_shape = (len(a), len(a[0]))
	reshaped_matrix = []
	if (new_shape[0] * new_shape[1] == old_shape[0] * old_shape[1]):
		
		n = new_shape[0] * new_shape[1] 
		elems = []
		for i in range (old_shape[0]):
			for j in range(old_shape[1]):
				elems.append(a[i][j])
		

		reshaped_matrix = [elems[i:i + new_shape[1]] for i in range(0, n, new_shape[1])]



	return reshaped_matrix