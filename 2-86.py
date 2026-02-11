while True:
    try:
        n = ''
        while True:
            temp = input()
            n += temp
            if temp[-1] == "#":break
        n = n[:-1]
    except EOFError:break
    i = 0
    now = 0
    while True:
        if i >= len(n):break
        now = now * 2 + int(n[i])
        if now >= 131071:
            now %= 131071
        i += 1
    if now == 0:
        print("YES")
    else:
        print("NO")
