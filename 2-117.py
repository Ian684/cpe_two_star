from math import *
def main():
    while True:
        D , v = map(int , input().split())
        if D == 0 and v == 0:break
        ans = ((D**3*pi-6*v)/pi)**(1/3)
        print(f"{ans:.3f}")
if __name__ == "__main__":
    main()
