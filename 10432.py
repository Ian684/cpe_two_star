from math import *
def main():
    while True:
        try:
            r , n = input().split()
            r = float(r)
            n = int(n)
        except EOFError:break
        print(f"{n*r*r*sin((n-2)/(2*n)*pi)*cos((n-2)/(2*n)*pi):.3f}")
if __name__ == "__main__":
    main()
