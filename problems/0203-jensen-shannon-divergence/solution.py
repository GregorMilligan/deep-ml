import numpy as np

def jensen_shannon_divergence(P: list[float], Q: list[float]) -> float:
	"""
	Compute the Jensen-Shannon Divergence between two probability distributions.
	
	Args:
		P: First probability distribution
		Q: Second probability distribution
	
	Returns:
		Jensen-Shannon Divergence value
	"""
	# this is buggged I rekon
	P = np.array(P)
	Q = np.array(Q)
	M = (P+Q)/2

	JSD = 0.5*P*np.log((P+1e-12)/(M+1e-12)) + 0.5*Q*np.log((Q+1e-12)/(M+1e-12))
	return  np.sum(JSD)

