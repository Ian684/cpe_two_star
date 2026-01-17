import sys
input = sys.stdin.readline
num = int(input())
for i in range(num):
        trash = input()
        n = int(input())
        first = float(input())
        end = float(input())
        sum = n*first + end
        for j in range(n):
                temp = float(input())
                sum -= 2*((n-j)*temp)
        sum /= (n+1)
        print(f"{sum:.2f}")
        if i != num - 1:print()