def cal(n , k , all , all_index , l , check , stack):
        if n == 1:
                return '01'
        result = []
        while stack:
                now , next , back = stack.pop()
                if next == 2:
                        if back is not None:
                                result.append(back)
                        continue
                stack.append([now , next+1 , back])
                if check[all_index[now]][next]:continue
                check[all_index[now]][next] = True
                stack.append([now[1:] + str(next), 0 , str(next)])
        return ''.join(result[::-1])
num = int(input())
history = {}
for i in range(num):
        n , k = map(int , input().split())
        if n in history:
                result = history[n]
        else:
                l = 2**(n-1)
                all = []
                all_index = {}
                for j in range(l):
                        temp = bin(j)[2:]
                        temp = (n - 1 - len(temp))*'0' + temp
                        all.append(temp)
                        all_index[temp] = j
                check = [[False , False] for j in range(l)]
                stack = [[all[l-1] , 0 , None]]
                result = cal(n , k , all , all_index , l , check , stack)
                result = (2**n - len(result))*'0' + result
                history[n] = result
        result += result
        print(int(result[k:k+n] , 2))
# 可隨機生成合法snake再用booth算法找最小字串