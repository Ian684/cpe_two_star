def cal(n , l , aim):
	all = ['000','001','010','011','100','101','110','111']
	all1 = {'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
	check = {'0':[],'1':[]}
	n = bin(n)[2:]
	aim = aim + aim[0]
	if len(n) != 8:
		n = '0'*(8-len(n)) + n
	for i in range(8):
		if n[i] == '0':
			check['0'].append(all[7-i])
		else:
			check['1'].append(all[7-i])
	for s in range(len(check[aim[0]])):
		dp = [[False]*8 for _ in range(l+1)]
		dp[0][all1[check[aim[0]][s]]] = True
		for j in range(l):
			for k in range(8):
				if not dp[j][k]:continue
				for i in range(len(check[aim[j+1]])):
					if check[aim[j+1]][i][0:2] == all[k][1:3]:
						dp[j+1][all1[check[aim[j+1]][i]]] = True
		if dp[l][all1[check[aim[0]][s]]]:
			return True
	return False
while True:
	try:
		n , l , aim = input().split()
		n , l = int(n) , int(l)
		if cal(n , l , aim):
			print("REACHABLE")
		else:
			print("GARDEN OF EDEN")
	except EOFError:
		break
