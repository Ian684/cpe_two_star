while True:
    n = int(input())
    if n == 0:break
    arr = []
    all_ = {}
    for i in range(n):
        arr.append(int(input()))
    arr = sorted(arr)
    for i in range(n):
        for j in range(i + 1 , n):
            t = arr[i] + arr[j]
            if t not in all_:
                all_[t] = []
            all_[t].append((arr[i] , arr[j]))
    valid = False
    for i in range(n - 1 , -1 , -1):
        for j in range(i - 1 , -1 , -1):
            t = arr[i] - arr[j]
            if t not in all_:
                continue
            for k in all_[t]:
                if arr[i] in k or arr[j] in k:
                    continue
                valid = True
                print(arr[i])
                break
            if valid:
                break
        if valid:
            break
    if not valid:
        print("no solution")
