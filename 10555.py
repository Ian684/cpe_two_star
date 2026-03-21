from math import *
def main():
    while True:
        line = input()
        if line == "0":break
        smallest = [1 << 60 , 1 << 60]
        a = line[:-3]
        a = a[2:]
        for l in range(1 , len(a)+1):
            b = int(a+a[len(a)-l:])
            t = 10**(len(a))
            b -= int(a)
            c = int('9'*l)*t
            g = gcd(b , c)
            b //= g
            c //= g
            if c < smallest[1]:
                smallest = [b , c]
        print(f"{smallest[0]}/{smallest[1]}")
if __name__ == "__main__":
    main()
