import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	# \(\theta = (X^T X)^{-1} X^T y\), 

	theta = np.linalg.inv(np.transpose(X) @ X) @ np.transpose(X) @ y
	return theta