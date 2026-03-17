from math import *
def main():
    while True:
        line = input()
        if line == "0":break
        line = list(map(int , line.split()))
        line = line[:-1]
        m = line[0]
        arr = []
        for l in line[1:]:
            if m == l:continue
            arr.append(abs(m-l))
        g = arr[0]
        for a in arr[1:]:
            g = gcd(g , a)
        print(g)
if __name__ == "__main__":
    main()
