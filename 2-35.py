import math
limit = 1300000
prime = [True]*limit
prime[0] = prime[1] = False
for i in range(2 , int(math.sqrt(limit))+1):
	if prime[i]:
		for j in range(i**2 , limit , i):
			prime[j] = False
while True:
	num = int(input())
	if num == 0:break
	left = right = num
	while True:
		if prime[left] and prime[right]:
			break
		if not prime[left]:
			left -= 1
		if not prime[right]:
			right += 1
	print(right - left)
