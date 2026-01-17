# floyd warshall algorithm
count = 1
import math
while True:
        num = input()
        if num == "":
                continue
        if num == "0":
                break
        num = int(num)
        arr = []
        for i in range(num):
                arr.append(list(map(int , input().split())))
        check = [[0]*num for _ in range(num)]
        for i in range(num-1):
                for j in range(i , num):
                        temp = (arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2
                        check[i][j] = temp
                        check[j][i] = temp
        for k in range(num):
                for i in range(num):
                        for j in range(num):
                                check[i][j] = min(check[i][j] , max(check[i][k] , check[k][j]))
        ans = math.sqrt(check[0][1])
        print(f"Scenario #{count}")
        print(f"Frog Distance = {ans:.3f}")
        print()
        count += 1