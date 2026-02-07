import math
limit = int(math.sqrt(2**31)) + 10
prime = [True]*limit
prime[0] = prime[1] = False
for i in range(2 , int(math.sqrt(limit))+1):
    if prime[i]:
        for j in range(i * i , limit , i):
            prime[j] = False
arr = []
for k , v in enumerate(prime):
    if v:
        arr.append(k)
while True:
    try:
        a , b = map(int , input().split())
    except EOFError:break
    big = [-1 , -1 , -1]
    small = [1 << 60 , -1 , -1]
    last = -1
    count = 0
    check = [True]*(b-a+1)
    if a == 1:
        check[0] = False
    for p in arr:
        if p * p > b:break
        temp = (a // p) * p
        if a % p != 0:temp += p
        if a // p == 0:temp = 2*p
        elif a // p == 1:temp = 2*p
        for j in range(temp, b + 1 , p):
            check[j - a] = False
    for i in range(a , b + 1):
        if check[i-a]:
            count += 1
            if last == -1:
                last = i
                continue
            t = i - last
            if t > big[0]:
                big = [t , last , i]
            if t < small[0]:
                small = [t , last , i]
            last = i
    if count < 2:
        print("There are no adjacent primes.")
    else:
        print(f"{small[1]},{small[2]} are closest, {big[1]},{big[2]} are most distant.")

