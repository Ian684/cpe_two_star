import math
limit = 2**15+1
prime = [True]*limit
prime[0] = prime[1] = False
for i in range(int(math.sqrt(limit))+1):
	if prime[i]:
		for j in range(i*2 , limit, i):
			prime[j] = False
while True:
	num = int(input())
	if num == 0:break
	count = 0
	for i in range(2 , num//2 + 1):
		if prime[num - i] and prime[i]:
			count += 1
	print(count)			
