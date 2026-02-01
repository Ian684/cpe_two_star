def ext_gcd(a: int, b: int):
    if b == 0:
        if a >= 0:
            return abs(a), 1, 0
        else:
            return abs(a), -1, 0
    g, x1, y1 = ext_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


if __name__ == "__main__":
    while True:
        try:
            a , b = map(int , input().split())
            g, x, y = ext_gcd(a, b)
            print(x , y , g)

        except EOFError:break
