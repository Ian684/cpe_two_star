num = int(input())
#1=up-down
#2=left-right
#3=rightup-leftdown
#4=leftup-rightdown
for i in range(num):
        n = int(input())
        arr = []
        for j in range(n):
                arr.append(list(map(int , input().split())))
        t = (n+1)//2
        for j in range(t-1 , -1 , -1):
                temp = list(map(int , input().split()))
                q , check = temp[0] , temp[1:]
                start = t-j-1
                end = n-start
                for c in check:
                        if c == 1:
                                for k2 in range(start , end):
                                        arr[start][k2] , arr[end-1][k2] = arr[end-1][k2] , arr[start][k2]
                                for k2 in range(start+1 , n//2):
                                        arr[k2][start] , arr[n-k2-1][start] = arr[n-k2-1][start] , arr[k2][start]
                                        arr[k2][end-1] , arr[n-k2-1][end-1] = arr[n-k2-1][end-1] , arr[k2][end-1]
                        elif c == 2:
                                for k2 in range(start , end):
                                        arr[k2][start] , arr[k2][end-1] = arr[k2][end-1] , arr[k2][start]
                                for k2 in range(start+1 , n//2):
                                        arr[start][k2] , arr[start][n-k2-1] = arr[start][n-k2-1] , arr[start][k2]
                                        arr[end-1][k2] , arr[end-1][n-k2-1] = arr[end-1][n-k2-1] , arr[end-1][k2]
                        elif c == 3:
                                for k2 in range(start , end):
                                        arr[start][k2] , arr[k2][start] = arr[k2][start] , arr[start][k2]
                                for k2 in range(end-1 , start , -1):
                                        arr[end-1][k2] , arr[k2][end-1] = arr[k2][end-1] , arr[end-1][k2]
                        elif c == 4:
                                for k2 in range(start , end):
                                        arr[start][k2] , arr[n-1-k2][n-1-start] = arr[n-1-k2][n-1-start] , arr[start][k2]
                                for k2 in range(start , end-1):
                                        arr[end-1][k2] , arr[n-1-k2][start] = arr[n-1-k2][start] , arr[end-1][k2]
        for a in range(len(arr)):
                for b in range(len(arr[0])):
                        if b == len(arr[0])-1:
                                print(arr[a][b])
                                break
                        print(arr[a][b] , end=" ")