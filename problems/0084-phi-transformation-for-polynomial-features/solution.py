import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	"""
	Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	Args:
		data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.

	"""
	result = []
	if degree < 0 or data == []:
		return result
	
	result = [[vector ** i for i in range(degree + 1)] for vector in data]


	return result 