while True:
    try:
        a = input()
        b = input()
    except EOFError:break
    arr = []
    history = {}
    for i in range(len(a)):
        if a[i] not in history:
            history[a[i]] = 0
        history[a[i]] += 1
    for i in range(len(b)):
        if b[i] in history and history[b[i]] > 0:
            history[b[i]] -= 1
            arr.append(b[i])
    print(''.join(sorted(arr)))
