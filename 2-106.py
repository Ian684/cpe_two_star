import sys
from math import *

input_data = sys.stdin.read().split()

it = iter(input_data)

def check(last, x, y, ans):
    x1, y1 = last
    tx, ty = ans
    return (min(x1, x) - 1e-9 <= tx <= max(x1, x) + 1e-9 and 
            min(y1, y) - 1e-9 <= ty <= max(y1, y) + 1e-9)

def cal(x, y, last):
    lx, ly = last
    if lx == x:
        return [1, 0, -x]
    a = (ly - y) / (lx - x)
    c = y - (x * a)
    b = -1
    return [a, b, c]

def distance(line, xm, ym):
    a, b, c = line
    return abs(a * xm + b * ym + c) / sqrt(a**2 + b**2)

def point(lines, xm, ym):
    a, b, c = lines
    t = (-a * xm - b * ym - c) / (a**2 + b**2)
    x = xm + t * a
    y = ym + t * b
    return [x, y]

while True:
    try:
        xm = float(next(it))
        ym = float(next(it))
        n = int(next(it))
    except StopIteration:
        break

    mi = 1e18
    last = None
    ans = [0.0, 0.0]

    for i in range(n + 1):
        x = float(next(it))
        y = float(next(it))
        if last is None:
            last = [x, y]
            ans = [x, y]
            continue

        line = cal(x, y, last)
        l_line = distance(line, xm, ym)
        t = point(line, xm, ym)
        
        if check(last, x, y, t):
            if l_line < mi:
                mi = l_line
                ans = t
        else:
            l1 = sqrt((last[0]-xm)**2 + (last[1]-ym)**2)
            l2 = sqrt((x-xm)**2 + (y-ym)**2)
            if l1 < mi:
                mi = l1
                ans = last[:]
            if l2 < mi:
                mi = l2
                ans = [x, y]
        last = [x, y]

    print(f"{ans[0]:.4f}")
    print(f"{ans[1]:.4f}")
