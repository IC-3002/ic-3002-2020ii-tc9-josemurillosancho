def maximizar(As, D):
	As.sort(key = lambda x: x[1])
	M = []
	suma = 0
	for i in range(len(As)):
		temp += As[i][1]
		if suma < D:
			M += [As[i]]
		else:
			break
	return M
