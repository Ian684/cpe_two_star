while True:
    x , y , start = map(int , input().split())
    if x == 0 and y == 0 and start == 0:break
    check = [[-1]*y for _ in range(x)]
    arr = []
    for i in range(x):
        arr.append(input())
    m , n = 0 , start - 1
    check[m][n] = 0
    while True:
        if arr[m][n] == "N":
            dm , dn = -1 , 0
        elif arr[m][n] == "S":
            dm , dn = 1 , 0
        elif arr[m][n] == "E":
            dm , dn = 0 , 1
        elif arr[m][n] == "W":
            dm , dn = 0 , -1
        em , en = m + dm , n + dn
        if em >= x or em < 0 or en >= y or en < 0:
            result = check[m][n] + 1
            print(f"{result} step(s) to exit")
            break
        if check[em][en] >= 0:
            print(f"{check[em][en]} step(s) before a loop of {check[m][n] + 1 - check[em][en]} step(s)")
            break
        else:
            check[em][en] = check[m][n] + 1
            m , n = em , en
