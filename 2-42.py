def bfs(new_check , line , s , e):
        from collections import deque
        q = deque([[s , s[0]]])
        new_check[s] = True
        while q:
                site , result = q.popleft()
                if site == e:
                        return result
                for l in line[site]:
                        if new_check[l]:continue
                        q.append([l,result+l[0]])
                        new_check[l] = True
import copy
num = int(input())
for i in range(num):
        trash = input()
        road , t = map(int , input().split())
        line = {}
        check = {}
        for _ in range(road):
                a , b = input().split()
                if a not in line:
                        check[a] = False
                        line[a] = []
                if b not in line:
                        check[b] = False
                        line[b] = []
                line[a].append(b)
                line[b].append(a)
        for j in range(t):
                new_check = copy.deepcopy(check)
                start , end = input().split()
                print(bfs(new_check , line , start , end))
        if i != num-1:print()