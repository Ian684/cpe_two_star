import math
limit = 1000001
prime = [True]*limit
prime[0] = prime[1] = False
for i in range(2 , int(math.sqrt(limit))+1):
        if prime[i]:
                for j in range(i**2 , limit , i):
                        prime[j] = False
def check(target , arr = (2,4,6,8,0)):
        if not prime[target]:return False
        d = 0
        temp = target
        while temp:
                if temp % 10 in arr:return False
                temp //= 10
                d += 1
        temp = 10**(d-1)
        while True:
                if d == 1:break
                target = (target%temp)*10 + target // temp
                if not prime[target]:return False
                d -= 1
        return True
while True:
        num = input()
        if num == '-1':break
        numi , numj = map(int , num.split())
        count = 0
        for target in range(numi , numj+1):
                if check(target):
                        count += 1
        if count == 0:
                print(f'No Circular Primes.')
        elif count == 1:
                print(f'{count} Circular Prime.')
        else:
                print(f'{count} Circular Primes.')