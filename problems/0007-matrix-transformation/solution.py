import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A = np.array(A)
	T = np.array(T)
	S = np.array(S)

	#T_is_square = T.ndim == 2 and T.shape[0] == T.shape[1]
	#S_is_square = S.ndim == 2 and S.shape[0] == S.shape[1]
	
	if T.shape[0] != T.shape[1] or S.shape[0] != S.shape[1]:
        transform_matrix = -1
	if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
		transform_matrix = -1
	else:
		T_inverse = np.linalg.inv(T)
		S_inverse = np.linalg.inv(S)
		transform_matrix = (T_inverse @ A) @ S
	return transform_matrix