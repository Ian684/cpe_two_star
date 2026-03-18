import sys
def solve(d, rat):
    bomb = [[0]*1027 for _ in range(1027)]
    for x, y, i in rat:
        x1, y1 = max(x-d, 0) + 1, max(y-d, 0) + 1
        x2, y2 = min(x+d, 1024) + 1, min(y+d, 1024) + 1
        bomb[x1][y1] += i
        bomb[x1][y2+1] -= i
        bomb[x2+1][y1] -= i
        bomb[x2+1][y2+1] += i
    ans = [0, 0, -1]
    for a in range(1, 1026):
        row = bomb[a]
        prev_row = bomb[a-1]
        for b in range(1, 1026):
            row[b] += row[b-1] + prev_row[b] - prev_row[b-1]
            if row[b] > ans[2]:
                ans = [a-1, b-1, row[b]]
    return ans
def main():
    data = sys.stdin.read().split()
    it = iter(data)
    num_test_cases = int(next(it))
    for _ in range(num_test_cases):
        d = int(next(it))
        n = int(next(it))
        rat = []
        for _ in range(n):
            rat.append((int(next(it)), int(next(it)), int(next(it))))
        res = solve(d, rat)
        print(f"{res[0]} {res[1]} {res[2]}")
if __name__ == "__main__":
    main()
