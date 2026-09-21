def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	
	val, row, col_sum = [], [], [0]

	n, m = len(dense_matrix), len(dense_matrix[0])
	s = 0
	for j in range(m):
		c = 0
		for i in range(n):
			if dense_matrix[i][j] != 0:
				val.append(dense_matrix[i][j])
				row.append(i)
				c += 1
		s += c
		col_sum.append(s)
	return val,row,col_sum
