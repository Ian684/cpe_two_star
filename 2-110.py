from math import *
while True:
    try:
        radius , n = map(int , input().split())
    except EOFError:break
    if n == 1:
        print(f"{radius:.10f} {0:.10f} {0:.10f}")
        continue
    cita = (180 / n) * pi / 180
    r = (sin(cita) * radius) / (sin(cita) + 1)
    print(f"{r:.10f}" , end=" ")

    angle = 90 - (180 / n)
    little = (angle / 360) * (r**2) * pi
    third_line = sqrt((radius - r)**2 - r**2)
    big = 0.5 * third_line * r
    ans1 = (big - little) * 2 * n
    print(f"{ans1:.10f}" , end=" ")
    
    circle = r**2 * pi * n
    big_circle = radius**2 * pi
    ans2 = big_circle - ans1 - circle
    print(f"{ans2:.10f}")
