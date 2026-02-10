def cal(n , line):
    check = {}
    ans = 1 << 60
    maxn = {}
    for i in range(1 , n+1):
        check[i] = 0
        maxn[i] = i
        for l in line[i]:
            maxn[i] = max(l , maxn[i])
    def dfs(now , ok , c):
        nonlocal ans , maxn , n
        if c >= ans:return
        if ok >= n:
            ans = min(c , ans)
            return
        if now > n:return
        for i in range(1 , now):
            if check[i] == 0 and maxn[i] < now:
                return
        dfs(now+1 , ok , c)
        if check[now] == 0:temp = 1
        else:temp = 0
        check[now] += 1
        for next_ in line[now]:
            if check[next_] == 0:
                temp += 1
            check[next_] += 1
        if temp > 0:
            dfs(now+1 , ok + temp , c + 1)
        for next_ in line[now]:
            check[next_] -= 1
        check[now] -= 1
    dfs(1 , 0 , 0)
    return ans
while True:
    try:
        n , m = map(int , input().split())
    except EOFError:break
    if n == 0 and m == 0:break
    line = {}
    for i in range(n):
        line[i+1] = []
    for i in range(m):
        a , b = map(int , input().split())
        line[a].append(b)
        line[b].append(a)
    print(cal(n , line))
