def cal(num , q , line):
	def dfs(line , color , check , current):
		global num
		for x in line[current]:
			if x in check:
				if color == check[x]:
					return 0
				continue
			if color == 1:
				check[x] = 0
				if dfs(line , 0 , check , x) == 0:
					return 0
			elif color == 0:
				check[x] = 1
				if dfs(line , 1 , check , x) == 0:
					return 0
		return 1
	check = {}
	check[0] = 0
	if dfs(line , 0 , check , 0):
		return 1
	return 0
while True:
	num = int(input())
	if num == 0:break
	q = int(input())
	line = {}
	for _ in range(q):
		temp1 , temp2 = map(int , input().split())
		if temp1 not in line:
			line[temp1] = []
		if temp2 not in line:
			line[temp2] = []
		line[temp1].append(temp2)	
		line[temp2].append(temp1)	
	if cal(num , q , line):
		print("BICOLORABLE.")
	else:
		print("NOT BICOLORABLE.")
