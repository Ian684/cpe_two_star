from math import *
while True:
    try:
        s = float(input())
    except EOFError:break
    a , b , c = 0.554579157314856 , 0.525783423063208 , 0.476627109438971
    print(f"{s/sin(75/180*pi):.10f} {(sqrt(2/3))*s:.10f} {(4/(2*sqrt(3)+sqrt(6)))*s:.10f} {(sqrt(3)/(1+sqrt(3)))*s:.10f} {s*a:.10f} {s*b:.10f} {s*c:.10f}")
