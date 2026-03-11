from math import *
def main():
    a = [1/sqrt(2) , sqrt(5)/2 , 5*sqrt(17)/16 , sqrt(2) , sqrt(10)/2 , 1.6885429682141935]
    n = int(input())
    for i in range(n):
        aim = float(input())
        for j in a[:-1]:
            print(f"{j*aim:.11f}" , end=" ")
        print(f"{a[-1]*aim:.11f}")
if __name__ == "__main__":
    main()
