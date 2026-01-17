def cal(t):
        from collections import deque
        global dist , num
        count = {0:-1}
        check = [False]*num
        check[t] = True
        q = deque([[0 , t]])
        while q:
                day , em = q.popleft()
                if day not in count:
                        count[day] = 0
                count[day] += 1
                for x in dist[em]:
                        if check[x]:continue
                        q.append([day+1 , x])
                        check[x] = True
        result = -float('inf')
        ans = -1
        for k , v in count.items():
                if result < v:
                        ans = k
                        result = v
        if ans == 0:
                return '0'
        return f'{result} {ans}'
num = int(input())
dist = {}
for i in range(num):
        temp = list(map(int , input().split()))[1:]
        dist[i] = temp
q = int(input())
for i in range(q):
        t = int(input())
        print(cal(t))