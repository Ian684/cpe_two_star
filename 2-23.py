def bfs(x , y , arr ,check , m , n):
	from collections import deque
	dir = ((1,0),(0,1),(-1,0),(0,-1))
	queue = deque([])
	queue.append([x,y])	
	count = 1
	check[x][y] = -1
	while queue:
		ax , ay = queue.popleft()
		for dx , dy in dir:
			nx , ny = ax + dx , ay + dy
			if nx < 0 or nx >= n or ny < 0 or ny >= m:
				continue
			if check[nx][ny] == -1:
				continue
			check[nx][ny] = -1
			queue.append([nx,ny])
			count += 1
	return count
num = int(input())
trash = input()
for _ in range(num):
	arr = []
	x , y = input().split()
	if x[0] == '0':
		x = int(x[1])
	else:
		x = int(x)
	if y[0] == '0':
		y = int(y[1])
	else:
		y = int(y)
	arr.append(input())
	x -= 1
	y -= 1
	m = len(arr[0])
	check = []
	check.append([0]*m)
	for i in range(m):
		if arr[0][i] == '1':
			check[0][i] = -1
	j = 1
	while True:
		try:
			temp = input()
		except EOFError:break
		if temp == '':break
		arr.append(temp)
		check.append([0]*m)
		for i in range(0 , m):
			if arr[j][i] == '1':
				check[j][i] = -1
		j += 1
	n = len(arr)
	print(bfs(x , y , arr , check , m , n))
	if _ == num - 1:break
	print()
