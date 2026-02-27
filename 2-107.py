while True:
    try:
        n = int(input())
    except EOFError:break
    m = 2**n
    w = []
    p = [0]*m
    for i in range(m):
        w.append(int(input()))
    for i in range(m):
        for j in range(n):
            p[i] += w[i^(1 << j)]
    bigest = -1
    for i in range(m):
        c = 0
        for j in range(n):
            bigest = max(bigest , p[i] + p[i^(1 << j)])
    print(bigest)
