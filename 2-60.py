from math import gcd
def cmp(x ,y):
    if x[0]/x[1] > y[0]/y[1]:
        return 1
    elif x[0]/x[1] < y[0]/y[1]:
        return -1
    else:
        return 0
while True:
    n , m = map(int , input().split())
    if n == 1 and m == 1:break
    arr = [[0,1] , [1,1] , [1,0]]
    ans = []
    while True:
        tmp = cmp([n,m] , arr[1])
        if tmp == 0:
            break
        elif tmp > 0:
            arr[0] = arr[1][:]
            arr[1] = [arr[1][0] + arr[2][0] , arr[1][1] + arr[2][1]]
            ans.append('R')
        else:
            arr[2] = arr[1][:]
            arr[1] = [arr[1][0] + arr[0][0] , arr[1][1] + arr[0][1]]
            ans.append('L')
        arr[1][0] //= gcd(arr[1][0] , arr[1][1])
        arr[1][1] //= gcd(arr[1][0] , arr[1][1])
    print(''.join(ans))