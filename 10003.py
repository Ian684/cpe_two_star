while True:
	num = int(input())
	if num == 0:break
	n = int(input())
	arr = list(map(int , input().split()))
	dp = [[1 << 60]*(n+2) for _ in range(n+2)]
	for i in range(n+1):
		dp[i][i+1] = 0
	arr.insert(0 , 0)
	arr.append(num)
	for l in range(2 , n+2):
		for i in range(n+2-l):
			j = i + l
			m = 1 << 60
			for k in range(i+1 , j):
				temp = dp[i][k]+dp[k][j]
				if temp < m:
					m = temp
			dp[i][j] = m + arr[j] - arr[i]
	print(f"The minimum cutting is {dp[0][n+1]}.")
