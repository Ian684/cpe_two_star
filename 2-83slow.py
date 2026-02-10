import math
while True:
    n = int(input())
    if n == 0:break
    arr = []
    for i in range(n * 2):
        x , y = map(int , input().split())
        arr.append([x , y])
    valid = False
    for a in range(-500 , 501):
        for b in range(-500 , 501):
            if a == 0 and b == 0:continue
            up , down = 0 , 0
            for x , y in arr:
                ans = a * x + b * y
                if ans == 0:
                    up , down = 1 , 2
                    break
                elif ans > 0:
                    up += 1
                else:
                    down += 1
            if up == down:
                valid = True
                print(a , b)
                break
        if valid:break
