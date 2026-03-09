from math import *
def main():
    while True:
        try:
            m , k = map(int , input().split())
        except EOFError:break
        d = (12*3600) / abs(m - k)
        n = d*(24*3600 - m)
        n %= 43200
        ho = int(n // 3600)
        n %= 3600
        mi = int(n / 60 + 0.5)
        if mi == 60:
            ho += 1
            ho %= 12
            mi = 0
        if ho == 0:
            ho = 12
        ho , mi = str(ho) , str(mi)
        print(f"{m} {k} {'0'*(2-len(ho))+ho}:{'0'*(2-len(mi))+mi}")
if __name__ == "__main__":
    main()
