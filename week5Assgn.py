tennis={}
flag=0
tdata_list=[]
while flag==0:
	try:
		tdata=input()
		tdata_list.append(tdata)
		if not tdata:
			raise ValueError('empty string')
	except ValueError:
		flag=1
play=[[0]*2 for i in range(len(tdata_list))]
for i in range(len(tdata_list)):
	play[i]=tdata_list[i].split(':')
	play[i].remove(play[i][-1])
play=play[0:-1]
players=[]
for i in range(len(play)):
	for j in range(len(play[i])):
		if play[i][j] not in players:
			players.append(play[i][j])

tdata_f=[[0]*2 for i in range(len(play))]
setscore=[[0]*2 for i in range(len(tdata_list))]
for i in range(len(tdata_list)-1):
	setscore[i]=tdata_list[i].split(',')
	setscore[i][0]=setscore[i][0].split(':')[2]
setscore=setscore[0:-1]
for i in range(len(play)):
	tdata_f[i][0]=play[i]
	tdata_f[i][1]=setscore[i]
best5t=[]
best3t=[]
best5=[[0]*2 for i in range(len(players))]
best3=[[0]*2 for i in range(len(players))]
setwon=[[0]*2 for i in range(len(players))]
setlost=[[0]*2 for i in range(len(players))]
gamewon=[[0]*2 for i in range(len(players))]
gamelost=[[0]*2 for i in range(len(players))]
setf=[[0,[]] for i in range(len(tdata_f))]
for i in range(len(tdata_f)):
		if len(tdata_f[i][1])>3:
			best5t.append(tdata_f[i][0][0])
		elif len(tdata_f[i][1])<=3:
			best3t.append(tdata_f[i][0][0])

ind=0
for s in players:
	best5[ind][0]=s
	best5[ind][1]=best5t.count(s)
	best3[ind][0]=s
	best3[ind][1]=best3t.count(s)
	ind=ind+1

set_f=[[0]*2 for i in range(len(setscore))]
for k in range(len(setscore)):
	p1sc=[]
	p2sc=[]
	#game=[]
	for j in range(len(setscore[k])):
		game=setscore[k][j].split('-')
		p1sc.append(game[0])
		p2sc.append(game[1])
		set_f[k][1]=[p1sc,p2sc]
		set_f[k][0]=[play[k][0],play[k][1]]
	(set_f[k][0][1],set_f[k][1][0])=(set_f[k][1][0],set_f[k][0][1])

ind2=0
for s in players:
	setwon[ind2][0]=s
	setlost[ind2][0]=s
	for i in range(len(set_f)):
		for j in range(len(set_f[i])):
			if s == set_f[i][j][0]:
				for k in range(len(set_f[i][j][1])):
					if j==0:
						if int(set_f[i][j][1][k])>int(set_f[i][j+1][1][k]):
							setwon[ind2][1]=setwon[ind2][1]+1
						else:
							setlost[ind2][1]=setlost[ind2][1]+1
					else:
						if int(set_f[i][j][1][k])>int(set_f[i][j-1][1][k]):
							setwon[ind2][1]=setwon[ind2][1]+1
						else:
							setlost[ind2][1]=setlost[ind2][1]+1
	ind2=ind2+1
ind3=0
for s in players:
	gamewon[ind3][0]=s
	gamelost[ind3][0]=s
	for i in range(len(set_f)):
		for j in range(len(set_f[i])):
			if s == set_f[i][j][0]:
				for k in range(len(set_f[i][j][1])):
					if j==0:
						gamewon[ind3][1]=gamewon[ind3][1]+int(set_f[i][j][1][k])
						gamelost[ind3][1]=gamelost[ind3][1]+int(set_f[i][j+1][1][k])
					else:
						gamewon[ind3][1]=gamewon[ind3][1]+int(set_f[i][j][1][k])
						gamelost[ind3][1]=gamelost[ind3][1]+int(set_f[i][j-1][1][k])
	ind3=ind3+1
winner=[[0,0,0,0,0,0] for i in range(len(players))]
for i in range(len(players)):
	winner[i]=[players[i],best5[i][1],best3[i][1],setwon[i][1],gamewon[i][1],setlost[i][1],gamelost[i][1]]
	#print(players[i],best5[i][1],best3[i][1],setwon[i][1],gamewon[i][1],setlost[i][1],gamelost[i][1])
#list(winner)
final=[[None,None,None,None,None,None] for i in range(len(players))]
repeated=[[None,None] for i in range(len(players))]
seen=[[None,None] for i in range(len(players))]

winner.sort(key=lambda x:x[1],reverse=True)
class BreakIt(Exception): pass
try:
	for i in range(len(players)):
		for j in range(1,len(winner[i])):
			if i<len(players)-1	:
				if winner[i][j]==winner[i+1][j]:
					temp=winner[i:i+2]
					temp.sort(key=lambda x:x[j+1])
					winner[i:i+2]=temp
				else:
					raise BreakIt
except:
	pass
for i in range(len(players)):
	#winner[i]=[players[i],best5[i][1],best3[i][1],setwon[i][1],gamewon[i][1],setlost[i][1],gamelost[i][1]]
	print(winner[i][0],winner[i][1],winner[i][2],winner[i][3],winner[i][4],winner[i][5],winner[i][6])
#print(winner)
