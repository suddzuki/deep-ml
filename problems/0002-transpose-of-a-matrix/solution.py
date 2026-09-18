import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    an = np.array(a)
    
    return an.T.tolist()