import numpy as np

def cross_product(a, b):

    plus = [a[(i) % 3] * b[(i + 1) % 3] for i in range(1,4)]
    minus = [a[(i + 1) % 3] * b[(i) % 3] for i in range(1,4)]
    return [(p - m) for p,m in zip(plus,minus)]