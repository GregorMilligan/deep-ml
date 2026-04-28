def matrixmul(a:list[list[int|float]],b:list[list[int|float]])-> list[list[int|float]]:
    import numpy as np
    a = np.array(a)
    b = np.array(b)
    if a.shape[1] != b.shape[1]:
        c = -1
    else:
        c = np.matmul(a, b)
    return c