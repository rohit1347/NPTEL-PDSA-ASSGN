def orangecap(d):
	players=[]
	matches=list(sorted(d.keys()))
	playertotal={}
	flag=0
	score=[]
	for s in matches:
		if d[s] not in players:
			players.extend(d[s])
			players=list(sorted(set(players)))
	for s in matches:
		if flag==0:
			for k in players:
				playertotal[k]=0
				flag=1				
		for k in players and d[s].keys():
			playertotal[k]=playertotal[k]+d[s][k]
	for i in playertotal.keys():
		score.append(playertotal[i])
		op=max(score)
	for z in playertotal.keys():
		if playertotal[z]==op:
			return(z,op)
		
	#({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
	#Output{'player1': 42, 'player2': 41, 'player3': 91, 'player4': 63}
	#([(4,3),(3,0)],[(-4,3),(2,1)])[(2, 1),(3, 0)]
	
	
def addpoly(p1,p2):
	tollen=len(p1)+len(p2)
	p3=[[0]*2 for i in range(tollen)]
	for i in range(len(p1)):
		p3[i][1]=p1[i][1]
	for j in range(len(p2)):
		p3[len(p1)+j][1]=p2[j][1]
	for i in range(len(p1)): 	
		for j in range(len(p3)):
			if p1[i][1]==p3[j][1]:
				p3[j][0]=p1[i][0]	
	for i in range(len(p2)):
		for j in range(len(p3)):
			if p2[i][1]==p3[j][1]:
				p3[j][0]=p3[j][0]+p2[i][0]			
	for z in range(len(p3)):
		try:
			if p3[z][0]==0:
				p3.remove(p3[z])
		except IndexError:
			pass
	p3=[tuple(l) for l in p3]
	#List to tuple conversion
	pr=sorted(list(set(p3)), reverse=True, key=lambda x:x[1])
	#Removing duplicates command	
	return(pr)
#addpoly Ans=[(1,2),(2,1)]
#([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])	
#Multpoly Ans=[(1, 3),(-1, 0)]
def multpoly(p1,p2):
	tollen=len(p1)+len(p2)
	p3=[[0]*2 for i in range(tollen)]
	#Make length of result equal to length of largest input
	if len(p1)>len(p2):
		(p3,a)=(p1,p2)
	elif len(p2)>len(p1):
		(p3,a)=(p2,p1)
	else:
		(p3,a)=(p1,p2)
	p3=[list(l) for l in p3]
	pk=[[[0]*2 for i in range(len(p3))]for i in range(len(a))]
	#Multiplication algorithm begins here
	for i in range(len(a)):
		for j in range(len(p3)):
			pk[i][j][0]=p3[j][0]*a[i][0]
			pk[i][j][1]=p3[j][1]+a[i][1]	
	while len(pk)>=2:
		pk[-2]=addpoly(pk[-2],pk[-1])
		pk.remove(pk[-1])
	pk=pk[0]
	#Mult Algo ends Here
	for z in range(len(pk)): #Remove entries with zero coefficients
		try:
			if pk[z][0]==0:
				pk.remove(pk[z])
		except IndexError:
			pass
	return(pk)	