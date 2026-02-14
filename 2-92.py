from math import *
while True:
    try:
        a , b , c = map(float , input().split())
    except EOFError:break
    if a == 0.0 or b == 0.0 or c == 0.0:
        total = 0.0
    else:
        C = (b**2 + a**2 - c**2) / (2*b*a)
        C = max(-1.0 , min(1.0 , C))
        C = acos(C)
        total = a * b * sin(C)
        total /= (a + b + c)
    print(f"The radius of the round table is: {total:.3f}")
