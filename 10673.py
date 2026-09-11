from math import *

def ex_gcd(a , b):
    
    if b == 0:
        return a , 1 , 0

    g , x1 , y1 = ex_gcd(b , a % b)

    x = y1
    y = x1 - (a//b) * y1

    return g , x , y


def main():
    t = int(input())
    for _ in range(t):
        x , k = map(int , input().split())
        g , p , q = ex_gcd(floor(x/k) , ceil(x/k))
        p *= x//g
        q *= x//g
        print(p , q)

if __name__ == "__main__":
    main()
