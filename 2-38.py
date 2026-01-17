def cal(n , l , aim):
	check = ['000','001','010','011','100','101','110','111']
	zero = []
	one = []
	n = bin(n)[2:]
	if len(n) != 8:
		n = '0'*(8-len(n)) + n
	for i in range(7 , -1 ,-1):
		if n[i] == '1':
			one.append(check[7-i])
		else:
			zero.append(check[7-i])
	def dfs(zero , one , aim , current, now):
		if current == len(aim):
			if now[-1][1:3] == now[0][0:2]:
				return True
			else:
				return False
		if aim[current] == '0':
			for i in range(len(zero)):
				if current != 0 and zero[i][0:2] != now[current-1][1:3]:
					continue
				now.append(zero[i])
				if dfs(zero , one , aim , current+1 , now):
					return True
				now.pop()
			return False	
		elif aim[current] == '1':
			for i in range(len(one)):
				if current != 0 and one[i][0:2] != now[current-1][1:3]:
					continue
				now.append(one[i])
				if dfs(zero , one , aim , current+1 , now):
					return True
				now.pop()
			return False
	if not dfs(zero , one , aim , 0 , []):
		return 0
	else:
		return 1
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
