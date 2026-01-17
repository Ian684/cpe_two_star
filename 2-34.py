def cal(crr):
	global n
	count = 1
	for a in range(len(crr[0])):
		for b in range(len(crr[1])):
			for c in range(len(crr[2])):
				for d in range(len(crr[3])):
					for e in range(len(crr[4])):
						if count == n:
							return crr[0][a]+crr[1][b]+crr[2][c]+crr[3][d]+crr[4][e]
						count += 1
	return None
num = int(input())
for i in range(num):
	n = int(input())
	arr = []
	brr = []
	for _ in range(6):
		arr.append(input())
	for _ in range(6):
		brr.append(input())
	crr = [[],[],[],[],[]]
	valid = True
	for j in range(5):
		c1 = set(arr[k][j] for k in range(6))
		c2 = set(brr[k][j] for k in range(6))	
		crr[j] = sorted(c1 & c2)
		if len(crr[j]) == 0:
			valid = False
			break
	if not valid:
		print('NO')
	else:
		ans = cal(crr)
		if ans is None:
			ans = 'NO'
		print(ans)
