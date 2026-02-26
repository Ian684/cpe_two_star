from math import *
def cal(x , y , last):
    lx , ly = last
    a = (ly - y) / (lx - x)
    c = y - (x * a)
    b = -1
    return [a , b , c]
def distance(line , xm , ym):
    a , b , c = line
    return abs(a * xm + b * ym + c) / sqrt(a**2 + b**2)
def point(mi , lines , xm , ym):
    



while True:
    try:
        xm = int(input())
        ym = int(input())
        n = int(input())
    except EOFError:break
    mi = 1 << 20
    lines = [0 , 0 , 0]
    #ax + by + c = 0 [a , b , c]
    last = None
    for i in range(n + 1):
        x = int(input())
        y = int(input())
        if last is None:continue
        line = cal(x , y , last)
        l = distance(line , xm , ym)
        if l < mi:
            mi = l
            lines = line[:]
        last = [x , y]
    ans = point(mi , lines , xm , ym)
    print(f"ans[0]:.4f")
    print(f"ans[1]:.4f")
