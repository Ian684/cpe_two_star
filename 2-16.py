from collections import deque
while True:
        m , n = map(int , input().split())
        if m == 0 or n == 0:
                break
        all = set()
        arr = [input() for _ in range(m)]
        for i in range(m):
                for j in range(n):
                        if arr[i][j] == '@':
                                all.add((i , j))
        count = 0
        dir = ((-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1))
        while all:
                sx , sy = all.pop()
                q = deque([(sx , sy)])
                while q:
                        x , y = q.popleft()
                        for dx , dy in dir:
                                nx , ny = dx + x , dy + y
                                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                                        continue
                                if arr[nx][ny] == '@' and (nx , ny) in all:
                                        q.append((nx , ny))
                                        all.remove((nx , ny))
                count += 1
        print(count)