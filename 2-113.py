from math import sqrt
while True:
    try:
        s = float(input())
    except EOFError:break
    print(f"{s*sqrt(3)/2:.10f} {(sqrt(3)*s)/(2+sqrt(3)):.10f} {s*sqrt(3)/4:.10f} {(-1*(7/sqrt(3))*s+sqrt(((7/sqrt(3))*s)**2+(35/3)*(s**2)))/(10/3):.10f}")
