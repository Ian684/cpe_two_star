while True:
    n , m = map(int , input().split())
    if n == 0 and m == 0:break
    line = {}
    check = {}
    for i in range(n):
        line[i+1] = set()
        check[i+1] = -1
    for i in range(m):
        start , end = map(int , input().split())
        line[start].add(end)
        line[end].add(start)
    bad = []
    count = 0
    all_ = 0
    ok = set()
    while True:
        u = -1
        bigest = -1
        for j in range(1 , n+1):
            if check[j] == 1:continue
            for k in bad:
                if k not in line[j]:continue
                line[j].remove(k)
            if len(line[j]) > bigest:
                u = j
                bigest = len(line[j])
        bad = [u]
        check[u] = 1
        count += 1
        ok.add(u)
        for j in line[u]:
            bad.append(j)
            if check[j] != -1:continue
            check[j] = 0
            ok.add(j)
        if len(ok) >= n:break
    print(count)

