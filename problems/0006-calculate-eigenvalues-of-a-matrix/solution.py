def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import numpy as np

	eigenvalues = np.linalg.eigvals(matrix)
	return eigenvalues