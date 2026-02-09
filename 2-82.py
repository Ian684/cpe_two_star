from math import sqrt
while True:
    n = int(input())
    if n == 0:break
    line = int(sqrt(n))
    if line**2 != n:
        line += 1
    total = 2 * line - 1
    bottom = (line - 1)**2
    medium = bottom + total // 2 + 1
    if line & 1:
        if n == medium:
            print(line , line)
        elif n > medium:
            print(line - (n - medium) , line)
        else:
            print(line , line - (medium - n))
    else:
        if n == medium:
            print(line , line)
        elif n > medium:
            print(line , line - (n - medium))
        else:
            print(line - (medium - n)  , line)
