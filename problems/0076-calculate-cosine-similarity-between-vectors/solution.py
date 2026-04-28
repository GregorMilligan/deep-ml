import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	import numpy as np
	dot_product = np.dot(v1, v2)
	
	vec1_mag = np.sqrt(np.sum(v1**2))
	vec2_mag = np.sqrt(np.sum(v2**2))

	cos_sim = dot_product/(vec1_mag*vec2_mag)
	return cos_sim
	pass