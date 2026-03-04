from math import *
def sieve():
    limit = int(sqrt(10**9))+1
    sieves = [True]*limit
    sieves[0] = sieves[1] = False
    for i in range(2 , int(sqrt(limit))+1):
        if sieves[i]:
            for j in range(i*i , limit , i):
                sieves[j] = False
    prime = []
    for k , v in enumerate(sieves):
        if v:
            prime.append(k)
    return prime
def phi(n,prime):
    ans = n
    nq = int(sqrt(n))+1
    for i in prime:
        if i > nq:break
        if n % i == 0:
            while n % i == 0:
                n //= i
            ans -= ans // i
        if n == 1:break
    if n > 1:
        ans -= ans // n
    return ans
def main():
    prime = sieve()
    while True:
        n = int(input())
        if n == 0:break
        if n == 1:
            print(0)
            continue
        ans = phi(n,prime)
        print(ans)
if __name__ == "__main__":
    main()
