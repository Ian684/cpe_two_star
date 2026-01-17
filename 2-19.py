all = [1,5,10,25,50]
dp = [0]*7500
dp[0] = 1
for i in all:
	for j in range(i , 7500):
		dp[j] += dp[j - i]
while True:
	try:
		num = int(input())
		print(dp[num])		
	except EOFError:
		break
