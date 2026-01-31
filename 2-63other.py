while True:
    try:
        all_1 = []
        all_3 = []
        m = int(input())
        for i in range(m):
            t = input()
            for j in range(m):
                if t[j] == '1':
                    all_1.append([i , j])
                elif t[j] == '3':
                    all_3.append([i , j])
        result = -1
        for i in all_1:
            temp = 1 << 60
            for j in all_3:
                temp = min(abs(i[0] - j[0]) + abs(i[1] - j[1]) , temp)
            result = max(temp , result)
        print(result)
    except EOFError:break
