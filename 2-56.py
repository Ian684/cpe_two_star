import sys
input = sys.stdin.readline
def prim(n , arr):
	import heapq
	from math import sqrt
	pq = []
	heapq.heappush(pq , [0 , 0])
	dp = [1 << 60]*n
	dp[0] = 0
	check = [False]*n
	while pq:
		l , s = heapq.heappop(pq)
		if check[s]:continue
		check[s] = True
		for k in range(n):
			if check[k]:continue
			temp = sqrt((arr[s][0]-arr[k][0])**2+(arr[s][1]-arr[k][1])**2)
			if temp < dp[k]:
				dp[k] = temp
				heapq.heappush(pq , [temp , k])
	return f"{sum(dp):.2f}"
num = int(input())
for i in range(num):
	trash = input()
	n = int(input())
	arr = []
	for j in range(n):
		arr.append(list(map(float , input().split())))
	print(prim(n , arr))
	if i != num - 1:print()
