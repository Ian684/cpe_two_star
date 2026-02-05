while True:
    n = int(input())
    if n == 0:break
    arr = []
    for i in range(n):
        a = input()
        b = input()
        arr.append([a , b])
    aim = input()
    i = 0
    for k , v in arr:
        i = 0
        while i < len(aim):
            valid = True
            for j in range(len(k)):
                if i + j >= len(aim):
                    valid = False
                    break
                if k[j] != aim[i+j]:
                    valid = False
                    break
            if valid:
                aim = aim[:i] + v + aim[i + len(k):]
                i = -1
            i += 1
    print(aim)


