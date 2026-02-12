number = {1:[0,0]}
now = 1
rounds = 0
direct = [[0,1],[-1,1],[-1,0],[0,-1],[1,-1],[1,0]]
while now < 100001:
    direct[0][0]
    number[now+1] = [number[now][0] + direct[0][0] , number[now][1] + direct[0][1]]
    now += 1
    for i in range(rounds):
        number[now+1] = [number[now][0] + direct[1][0] , number[now][1] + direct[1][1]]
        now += 1
    for k in range(2 , 6):
        for i in range(rounds+1):
            number[now+1] = [number[now][0] + direct[k][0] , number[now][1] + direct[k][1]]
            now += 1
    for i in range(rounds+1):
            number[now+1] = [number[now][0] + direct[0][0] , number[now][1] + direct[0][1]]
            now += 1
    rounds += 1
while True:
    try:
        n = input()
        if n == "":continue
        n = int(n)
    except EOFError:break
    print(number[n][0] , number[n][1])
