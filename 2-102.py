from math import *
limit = 300000
prime = [True]*limit
prime[0] = prime[1] = False
for i in range(2 , int(sqrt(limit))+1):
    if prime[i]:
        for j in range(i**2 , limit , i):
            prime[j] = False
arr = [3 , 4]
for k , v in enumerate(prime):
    if k <= 4:continue
    if v:
        arr.append(k)
fa = [0]*250000
fa[1] = 1
fa[2] = 1
a , b = 1 , 1
for i in range(3 , 250000):
    a , b = b , a + b
    if b >= 10**18:
        b //= 10
        a //= 10
    fa[i] = str(b)[:9]
while True:
    try:
        aim = int(input())
        aim -= 1
    except EOFError:break
    print(fa[arr[aim]])
