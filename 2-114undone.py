from math import *
while True:
    try:
        s = float(input())
    except EOFError:break
    print(f"{s/sin(75/180*pi):.10f} {(sqrt(2/3))*s:.10f} {(4/(2*sqrt(3)+sqrt(6)))*s:.10f} {(sqrt(3)/(1+sqrt(3)))*s:.10f} {:.10f} {:.10f} {:.10f}")
    #t5???
