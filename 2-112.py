from math import *
while True:
    try:
        n = float(input())
    except EOFError:break
    print(f"{sin(108*pi/180) * (n/sin(63*pi/180)):.10f}")
