while True:
    try:
        n = int(input())
        i = 1
        now = 1
        while True:
            now %= n
            if now % n == 0:
                print(i)
                break
            now *= 10
            now += 1
            i += 1
    except EOFError:break
