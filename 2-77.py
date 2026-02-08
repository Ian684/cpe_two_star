n = int(input())
trash = input()
for i in range(n):
    m = int(input())
    arr = [input() for _ in range(m)]
    vote = {}
    for j in range(1 , m+1):
        vote[j] = []
    c = 0
    while True:
        try:
            t = input()
        except EOFError:break
        if t == "":break
        t = list(map(int , t.split()))
        vote[t[0]].append(t)
        c += 1
    min_vote = c / 2
    valid = False
    while True:
        d = 1 << 60
        lowest = []
        for k , v in vote.items():
            if len(v) > min_vote:
                print(arr[k-1])
                valid = True
                break
            if len(v) < d:
                lowest = [k]
                d = len(v)
            elif len(v) == d:
                lowest.append(k)
        if valid:break
        if len(lowest) == len(vote):
            lowest = sorted(lowest)
            for j in lowest:
                print(arr[j-1])
            break
        for j in lowest:
            for x in vote[j]:
                for y in range(1 , len(x)):
                    if x[y] not in vote:continue
                    vote[x[y]].append(x[y:])
                    break
            del vote[j]
    if i != n - 1:print()
