import math
limit = 10001
prime = [True]*limit
prime[0] = prime[1] = False
for i in range(2 , int(math.sqrt(limit)) + 1):
        if prime[i]:
                for j in range(i**2 , limit , i):
                        prime[j] = False
arr = []
for k , v in enumerate(prime):
        if v:
                arr.append(k)
while True:
        num = int(input())
        if num == 0:break
        idx = 0
        while True:
                if num <= arr[idx] or idx == len(arr)-1:
                        break
                idx += 1
        count = 0
        for i in range(idx , -1 , -1):
                temp = num
                temp -= arr[i]
                if temp == 0:
                        count += 1
                        continue
                elif temp < 0:
                        continue
                for j in range(i-1 , -1 , -1):
                        temp -= arr[j]
                        if temp == 0:
                                count += 1
                                break
                        elif temp < 0:break
        print(count)