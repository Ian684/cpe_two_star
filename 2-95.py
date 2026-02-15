from math import *
def isprime(x):
    for i in range(2 , int(sqrt(x))+1):
        if x % i == 0:
            return 0
    return 1
sum_ = [0]*10001
sum_[0] = 1
for k in range(1 , 10001):
    sum_[k] = sum_[k-1] + isprime(k**2+k+41)
while True:
    try:
        a , b = map(int , input().split())
    except EOFError:break
    if a == 0:
        result = sum_[b]
    else:
        result = sum_[b]-sum_[a-1]
    print(f"{((result*100/(b-a+1))+0.0000001):.2f}")
