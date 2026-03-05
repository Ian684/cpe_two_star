from collections import deque
def topo(in_ , line , n):
    q = deque([])
    for i in range(n):
        if not in_[i]:q.append(i)
    ans = []
    while q:
        now = q.popleft()
        ans.append(now+1)
        for next in line[now]:
            in_[next] -= 1
            if not in_[next]:q.append(next)
    return ans
def main():
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        line = {}
        in_ = [0]*n
        for k in range(n):
            line[k] = []
        for _ in range(m):
            i , j = map(int , input().split())
            i -= 1
            j -= 1
            line[i].append(j)
            in_[j] += 1
        ans = topo(in_ , line , n)
        print(' '.join(map(str , ans)))
if __name__ == "__main__":
    main()
