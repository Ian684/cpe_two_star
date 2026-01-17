def check(num):
	for A in range(2 , num):
		remain = 1
		a = A
		d = num
		while d != 1:
			if d % 2 == 0:
				a = (a**2)%num
				d //= 2
			else:
				remain *= a%num
				a = (a**2)%num
				d //= 2
		remain %= num
		if (remain*a)%num != A: 
			return 0
	return 1
import math
limit = 65000
prime = [True]*limit
prime[0] = prime[1] = False
for i in range(2 , int(math.sqrt(limit))+1):
	if prime[i]:
		for j in range(i**2 , limit , i):
			prime[j] = False
while True:
	num = int(input())
	if num == 0:break
	if not prime[num]:
		if check(num):
			print(f"The number {num} is a Carmichael number.")
		else:
			print(f"{num} is normal.")
	else:
		print(f"{num} is normal.")
	
