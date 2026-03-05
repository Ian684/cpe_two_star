def dfs(check , line , ans , start):
    point = start
    def cal(point):
        nonlocal ans , check
        for next in line[point]:
            if check[next]:continue
            check[next] = True
            cal(next)
        ans.append(point+1)
    cal(point)
    return check , ans
def main():
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        line = {}
        check = [False]*n
        for k in range(n):
            line[k] = []
        for _ in range(m):
            i , j = map(int , input().split())
            i -= 1
            j -= 1
            line[i].append(j)
        ans = []
        for start in range(n):
            if check[start]:continue
            check[start] = True
            check , ans = dfs(check , line , ans , start)
        print(' '.join(map(str , ans[::-1])))
if __name__ == "__main__":
    main()
