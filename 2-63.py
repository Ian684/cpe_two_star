from collections import deque

def bfs(arr , f):
    q = deque([f])
    check = [[False]*len(arr) for _ in range(len(arr))]
    while q:
        x , y , step = q.popleft()
        check[x][y] = True
        if arr[x][y] == '3':
            return step
        for dx , dy in ((-1,0),(0,-1),(1,0),(0,1)):
            nx , ny = x + dx , y + dy
            if 0 <= nx < len(arr) and 0 <= ny < len(arr):
                if not check[nx][ny]:
                    q.append([nx , ny , step + 1])
    return 0
while True:
    try:
        arr = []
        first = []
        m = int(input())
        for i in range(m):
            t = input()
            arr.append(t)
            for j in range(m):
                if t[j] == '1':
                    first.append([i , j , 0])
        result = -1
        for f in first:
            t = bfs(arr , f)
            if result < t:
                result = t
        print(result)
    except EOFError:break
