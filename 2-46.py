import math
limit = 40000
prime = [True]*limit
prime[0] = prime[1] = False
for i in range(2 , int(math.sqrt(limit))+1):
        if prime[i]:
                for j in range(i**2 , limit , i):
                        prime[j] = False
check = []
for k , v in enumerate(prime):
        if v:
                check.append(k)
import sys
while True:
        n = int(sys.stdin.readline())
        if n == 0:break
        arr = [i for i in range(n)]
        ans = 0
        for i in range(2 , n+1):
                ans = (ans + check[n-i])%i
        print(arr[ans]+1)