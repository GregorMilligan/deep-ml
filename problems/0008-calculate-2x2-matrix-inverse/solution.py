def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    import numpy as np
    # Your code here
    matrix = np.array(matrix)
    det = np.linalg.det(matrix)

    if det != 0:
        a = matrix[0, 0] 
        b = matrix[0, 1] #getting each element in the 2x2
        c = matrix[1, 0]
        d =  matrix[1, 1]

        adj = np.array([[d, -b],
                        [-c, a]])

        inv_manual = (1/det) * adj
        return inv_manual
    pass