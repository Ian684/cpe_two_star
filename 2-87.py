#修好久....精度要注意
from math import *
n = int(input())
for _ in range(n):
    try:
        line = input().split()
        x1, y1, x2, y2, r = map(float, line)
    except EOFError:
        break
    if x1 == x2 and y1 == y2:
        print(f"{0.0:.3f}")
        continue
    if x1 == x2:
        a_line = -1.0
        b_line = 0.0
    else:
        a_line = (y1-y2) / (x1-x2)
        b_line = -1.0
    c_line = -1*(a_line*x1+b_line*y1)
    long = abs(c_line) / (sqrt(a_line**2+b_line**2))
    if long >= r - 1e-12:
        print(f"{sqrt((y2-y1)**2 + (x2-x1)**2):.3f}")
        continue
    else:
        temp1 = (-1*x1)*(x2-x1) + (-1*y1)*(y2-y1)
        temp2 = (-1*x2)*(x1-x2) + (-1*y2)*(y1-y2)
        if temp1 <= 1e-12 or temp2 <= 1e-12:
            print(f"{sqrt((y2-y1)**2 + (x2-x1)**2):.3f}")
            continue
    ans = 0
    a_side = sqrt(max(0.0, x1**2+y1**2-r**2))
    b_side = sqrt(max(0.0, x2**2+y2**2-r**2))
    ans += a_side
    ans += b_side

    i, j, k = a_side, r, sqrt(x1**2+y1**2)
    value1 = (j**2+k**2-i**2) / (2*j*k)
    angle1 = acos(max(-1.0, min(1.0, value1)))

    i, j, k = b_side, r, sqrt(x2**2+y2**2)
    value2 = (j**2+k**2-i**2) / (2*j*k)
    angle2 = acos(max(-1.0, min(1.0, value2)))

    i, j, k = sqrt((y2-y1)**2 + (x2-x1)**2), sqrt(x1**2+y1**2), sqrt(x2**2+y2**2)
    value3 = (j**2+k**2-i**2) / (2*j*k)
    angle3 = acos(max(-1.0, min(1.0, value3)))

    angle = max(0.0, angle3 - angle2 - angle1)
    ans += angle * r

    print(f"{ans:.3f}")
