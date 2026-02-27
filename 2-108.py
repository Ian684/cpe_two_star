import sys
from collections import deque
input = sys.stdin.readline

def main():
    try:
        line = input().strip()
        if not line: return
        n = int(line)
    except EOFError: return

    for case_idx in range(n):
        while True: # 跳過空行
            line = input().strip()
            if line: break
        k, m = map(int, line.split())
        x, y = map(int, input().split())
        
        arr = [[None]*(m+1) for _ in range(k+1)]
        difference = [[[] for _ in range(m+1)] for _ in range(k+1)]
        
        while True:
            line_str = input().strip()
            if not line_str: break
            nums = list(map(int, line_str.split()))
            for i in range(0, len(nums) - 3, 3):
                u_x, u_y, u_h = nums[i], nums[i+1], nums[i+2]
                v_x, v_y, v_h = nums[i+3], nums[i+4], nums[i+5]
                diff = v_h - u_h
                difference[u_x][u_y].append([v_x, v_y, diff])
                difference[v_x][v_y].append([u_x, u_y, -diff])

        result = bfs([x, y], k, m, arr, difference)
        
        ok = 1
        for i in range(1, k+1):
            if None in arr[i][1:]:
                ok = 0
                break
        
        for i in range(1, k+1):
            for j in range(1, m+1):
                if arr[i][j] is None:
                    if bfs([i, j], k, m, arr, difference) == 1:
                        result = 1
        
        if result == 1: print("conflicting measurements")
        elif ok == 0: print("the lack of measurements")
        else:
            for i in arr[1:]:
                print(*(i[1:]))
        
        if case_idx < n - 1: print()

def bfs(start, k, m, arr, difference):
    x, y = start
    if arr[x][y] is None: arr[x][y] = 0
    q = deque([[x, y]])
    while q:
        nx, ny = q.popleft()
        for dx, dy, diff in difference[nx][ny]:
            if arr[dx][dy] is not None:
                if arr[nx][ny] + diff != arr[dx][dy]:
                    return 1
                continue
            arr[dx][dy] = arr[nx][ny] + diff
            q.append([dx, dy])
    return -1

if __name__ == "__main__":
    main()
