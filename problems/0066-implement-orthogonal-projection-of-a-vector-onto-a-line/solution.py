
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	
	v_dot_l = [a * b for a, b in zip(v,L)]

	l_sqrt = [a * b for a, b in zip(L,L)]


	proj = [(sum(v_dot_l) / sum(l_sqrt)) * a for a in L] 
	return proj
