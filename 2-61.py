def dfs(temp):
    brr = []
    aim = len(temp)
    def cal(temp , l , now):
        if l == aim:
            brr.append(now)
        for k in range(len(temp)):
            if temp[k] != -1:
                t = temp[k]
                temp[k] = -1
                cal(temp , l+1 , now + t)
                temp[k] = t
    cal(temp , 0 , "")
    return brr

num = int(input())

for i in range(num):
    try:
        temp = list(input())
        if len(temp) == 0:
            print()
            print()
            continue
        arr = dfs(temp)
        arr = sorted(list(set(arr)))
        for j in arr:
            print(j)
        print()
    except EOFError:break
