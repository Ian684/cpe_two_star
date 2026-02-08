n = int(input())
trash = input()
for i in range(n):
    arr = []
    while True:
        try:
            t = input()
        except EOFError:break
        if t == "":break
        arr.append(t)
    same = 0
    last_space = 0
    last = ""
    for a in range(len(arr)):
        if len(arr[a]) <= last_space:
            last_space = len(arr[a]) - 1
        for j in range(last_space+1 , -1 , -1):
            if arr[a][:j] == last[:j]:
                print(f"{j*' '}{arr[a]}")
                last = arr[a]
                last_space = j
                break
    if i != n - 1:
        print()
