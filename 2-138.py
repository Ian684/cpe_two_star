from math import *
def cal(a , b , c):
    s = (a + b + c) / 2
    t = s*(s-a)*(s-b)*(s-c) 
    if t <= 0:
        return -1
    return 4*sqrt(t)/3
def main():
    while True:
        try:
            a , b , c = map(float , input().split())
        except EOFError:break
        print(f"{cal(a , b , c):.3f}")
if __name__ == "__main__":
    main()
