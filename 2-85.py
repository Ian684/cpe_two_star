while True:
    try:
        n = input().split()
        if len(n) > 1:
            x , y = map(int , n)
            for i in range(4):
                if (x + i - 2) % 4 == 0:x += i
                if (y - i - 2) % 4 == 0:y -= i
            print((y - x) // 4 + 1)
            continue
        else:
            t = int(n[0])
            n = abs(t)
        if (n - 2) % 4 == 0:
            print("Bachelor Number.")
            continue
        elif n & 1:
            a , b = (n + 1) // 2 , (n - 1) // 2
        else:
            a , b = (n // 2 + 2) // 2 , (n // 2 - 2) // 2
        if t == 0:print(2 , 2)
        elif t > 0:print(a , b)
        else:print(b , a)
    except EOFError:break
