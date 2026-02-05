arr = []
while True:
    try:
        a = int(input())
        arr.append(a)
        arr = sorted(arr)
        if len(arr) & 1:
            print(arr[len(arr) // 2])
        else:
            print((arr[len(arr) // 2] + arr[len(arr) // 2 - 1])// 2)
    except EOFError:
        break
