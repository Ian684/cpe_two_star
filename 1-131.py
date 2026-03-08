from collections import deque
def bfs(arr , a , b , check):
    q = deque([[a , b]])
    check[a][b] = True
    center = arr[a][b]
    directions = ((0,1),(0,-1),(1,0),(-1,0))
    while q:
        x1 , y1 = q.popleft()
        for dx , dy in directions:
            nx , ny = x1 + dx , y1 + dy
            if nx < 0 or nx >= len(arr) or ny < 0 or ny >= len(arr[0]):
                continue
            if check[nx][ny]:continue
            if arr[nx][ny] == center:
                check[nx][ny] = True
                q.append([nx , ny])
    return check
def main():
    n = int(input())
    for i in range(1 , n+1):
        x , y = map(int , input().split())
        arr = [input() for _ in range(x)]
        check = [[False]*y for _ in range(x)]
        ans = {}
        for a in range(x):
            for b in range(y):
                if check[a][b]:continue
                if arr[a][b] not in ans:
                    ans[arr[a][b]] = 0
                ans[arr[a][b]] += 1
                check = bfs(arr , a , b , check)
        print(f"World #{i}")
        for k , v in sorted(ans.items() , key = lambda o: (-o[1] , o[0])):
            print(f"{k}: {v}")
if __name__ == "__main__":
    main()
