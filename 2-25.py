def cal(c , arr , check):
	dis = [[float('inf')]*c for _ in range(c)]
	for a , b in arr:
		dis[check[b]][check[a]] = 1
	for k in range(c):
		for i in range(c):
			for j in range(c):
				if i == j:continue
				else:	
					dis[i][j] = min(dis[i][j] , dis[i][k] + dis[k][j])
	result = 0
	for i in dis:
		for j in i:
			if j != float('inf'):
				result += j
	return result
now = 0
while True:
	now += 1
	temp = input().split()
	if temp[0] == '0' and temp[1] == '0':break
	arr = []
	check = {}	
	current = 0
	for i in range(0 , len(temp) , 2):
		if temp[i] == '0' and temp[i+1] == '0':break
		if int(temp[i]) not in check:
			check[int(temp[i])] = current
			current += 1
		if int(temp[i+1]) not in check:
			check[int(temp[i+1])] = current
			current += 1
		arr.append([int(temp[i]) , int(temp[i+1])])
	avg = current*(current-1)
	result = cal(current , arr , check)
	print(f"Case {now}: average between pages = {(result/avg):.3f} clicks")
	
