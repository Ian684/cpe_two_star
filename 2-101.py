from math import *

def cal(aim):
    stage = int(sqrt(aim))
    x , y = 0 , 0
    y += stage * sqrt(3) / 2
    start = stage ** 2
    t = aim - start
    if not (t & 1):
        y += sqrt(3) / 3
    else:
        y += sqrt(3) / 6
    x = 0.5 * (aim - (start + stage))
    return x , y
while True:
    try:
        a , b = map(int , input().split())
    except EOFError:break
    ax , ay = cal(a)
    bx , by = cal(b)
    ans = sqrt((ax - bx)**2 + (ay - by)**2)
    print(f"{ans:.3f}")
