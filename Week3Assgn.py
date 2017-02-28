def descending(list):
	for i in range(len(list)-1):
		if list[i]<list[i+1]:
			return(False)
	return(True)
	
def alternating(list):
	if len(list)==0:
		return(True)
	for i in range(len(list)-2):
		if list[i]>list[i+1]:
			if list[i+1]<list[i+2]:
				return(True)
			return(False)	
		if list[i]<list[i+1]:	
			if list[i+1]>list[i+2]:
				return(True)
			return(False)	
	return(False)
	
def matmult(m1,m2):
	m3=[],[]
	for i in range(len(m1)):
		for j in range(len(m1[0])):
			m3[i][j]+=m1[i][j]*m2[j][i]
	return(m3)

	