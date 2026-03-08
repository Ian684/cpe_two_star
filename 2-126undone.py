from math import *
def main():
    while True:
        try:
            a , b , c = map(float , input().split())
        except EOFError:break
        ra , rb , rc = sqrt(a/pi) , sqrt(b/pi) , sqrt(c/pi)
        ka , kb , kc = 1/ra , 1/rb , 1/rc
        sr = (ka + kb + kc) + 2*sqrt(ka*kb + kb*kc + ka*kc)
        sr = 1/sr
        R = (ka + kb + kc) - 2*sqrt(ka*kb + kb*kc + ka*kc)
        R = 1/R
        R = abs(R)
        t = sqrt((ra + rb + rc)*ra*rb*rc)
        an = t * (2*ra*rb*rc / ((ra+rb)*(rb+rc)*(ra+rc)))
        print(f"{R:.10f} {sr:.10f} {an:.10f}")
if __name__ == "__main__":
    main()
