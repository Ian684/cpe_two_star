import math
limit = int(math.sqrt(32767))+1
prime = [True]*limit
prime[0] = prime[1] = False
for i in range(2 , int(math.sqrt(limit))+1):
        if prime[i]:
                for j in range(i**2 , limit , i):
                        prime[j] = False
arr = []
for i , p in enumerate(prime):
        if p:
                arr.append(i)
while True:
        num = input()
        if num == "0":break
        num = list(map(int , num.split()))
        count = 0
        sum = 1
        while True:
                if count >= len(num):break
                sum *= (num[count]**num[count+1])
                count += 2
        sum -= 1
        p = 0
        ans = []
        while True:
                if sum == 1 or p >= len(arr):break
                if sum % arr[p] == 0:
                        c = 1
                        sum //= arr[p]
                        while True:
                                if sum % arr[p] != 0:break
                                sum //= arr[p]
                                c += 1
                        ans.append(c)
                        ans.append(arr[p])
                p += 1
        if sum != 1:
                ans.append(1)
                ans.append(sum)
        for a in range(len(ans)-1 , -1 , -1):
                if a == 0:
                        print(ans[a])
                        break
                print(ans[a] , end=" ")