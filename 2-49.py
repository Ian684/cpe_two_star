num = int(input())
c = 0
while c < num:
	aim = input()
	if aim == '':continue
	aim = int(aim)
	c += 1
	result = 0
	count = 0
	old_arr = []
	arr = []
	valid = True
	while True:
		x , y = map(int , input().split())
		if x == 0 and y == 0:break
		if x <= 0 and y <= 0:continue
		elif x >= aim and y >= aim:continue
		elif x <= 0 and y >= aim:
			valid = False
			x1 , y1 = x , y
			continue
		arr.append([x , y])
	if not valid:
		print(1)
		print(x1 , y1)
		print()
		continue
	ans = []
	while count < aim:
		u = -1
		m = -1
		for a in range(len(arr)):
			if arr[a][0] <= count and arr[a][1] - count > m:
				u = a
				m = arr[a][1] - count
		if u == -1:
			valid = False
			break
		count = arr[u][1]
		result += 1
		ans.append(arr[u])
		del arr[u]
	if not valid:
		print(0)
	else:
		print(result)
		arr = sorted(arr , key=lambda x: x[0])
		for a , b in ans:
			print(a , b)
	if c != num - 1:
		print()
