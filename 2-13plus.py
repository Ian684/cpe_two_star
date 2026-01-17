# Prim minimax MST
import math
count = 1
while True:
    num = input()
    if not num:
        continue
    num = int(num)
    if num == 0:
        break
    arr = []
    for i in range(num):
        arr.append(list(map(int , input().split())))
    check = [[0]*num for _ in range(num)]
    for i in range(num-1):
        for j in range(i , num):
            temp = (arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2
            check[i][j] = temp
            check[j][i] = temp
    in_mst = [False]*num
    best = check[0][:]
    for _ in range(num):
        u = 0
        bu = 1 << 60
        for v in range(num):
            if not in_mst[v] and best[v] < bu:
                bu = best[v]
                u = v
        in_mst[u] = True



        for v in range(num):
            if not in_mst[v]:
                best[v] = min(best[v] , max(bu, check[u][v]))
    ans = math.sqrt(best[1])



    print(f"Scenario #{count}")
    print(f"Frog Distance = {ans:.3f}\n")
    count += 1
