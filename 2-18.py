import sys
sys.setrecursionlimit(1_000_000)
def cal1(x1 , y1):
	if x1 < 0 or y1 < 0 or x1 >= m or y1 >= n:return
	if arr[x1][y1] == '.':return
	if arr[x1][y1] == '*':return
	elif arr[x1][y1] == 'X':
		arr[x1] = arr[x1][:y1] + '*' + arr[x1][y1+1:]
		for dx , dy in dir:
			cal1(x1+dx , y1+dy)
def cal(x , y):
	global count
	if x < 0 or y < 0 or x >= m or y >= n:return
	if arr[x][y] == '.':return
	if arr[x][y] == '*':
		arr[x] = arr[x][:y] + '.' + arr[x][y+1:]
		for dx , dy in dir:
			cal(x+dx , y+dy)
	elif arr[x][y] == 'X':
		cal1(x , y)
		count += 1
		arr[x] = arr[x][:y] + '.' + arr[x][y+1:]
		for dx , dy in dir:
			cal(x+dx , y+dy)
dir = ((1,0),(0,1),(-1,0),(0,-1))
now = 0
while True:
	temp = input()
	if temp == '':continue
	n , m = map(int , temp.split())
	if n == 0 and m == 0:
		break
	now += 1
	idx = 0
	arr = []
	while idx < m:
		temp = input()
		if temp == '':continue
		arr.append(temp)
		idx += 1
	result = []
	for i in range(m):
		for j in range(n):
			if arr[i][j] == '.':continue
			count = 0
			cal(i , j)
			if count:
				result.append(count)
	print(f"Throw {now}")
	if result:
		print(' '.join(map(str , sorted(result))))
	else:
		print()
	print()
