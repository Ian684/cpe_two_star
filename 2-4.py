# 質數表!!
# 埃拉托斯特篩法
import math
n = int(input())


prime = [True]*(int(math.sqrt(1000000000))+1)
# 只需要根號1e9，因為所有數都能被分解，但如果被除完是質數且太大，超過根號1e9，就需要特別再乘一次
prime[0] = prime[1] = False
for i in range(2 , int(math.sqrt(int(math.sqrt(1000000000))+1))):
    # 驗整根號1e9內的質數，用特殊篩法，利用質數去反覆加自己來剔除合數
    #兩次根號的意義是只需要檢查到這(最大i***2==最大j)，反覆加自己最就會加到根號1e9了
    if prime[i]: 
        for j in range(i *i , int(math.sqrt(1000000000))+1 , i):
            prime[j] = False
check = []
for i , j in enumerate(prime):
    if j:
        check.append(i)
for _ in range(n):
    l , h = map(int , input().split())
    result = [0 , 0]
    for i in range(l , h+1):
        i_plus = i
        ans = 1
        for p in check:
            count = 0
            if i_plus == 1:
                break
            while True:
                if i_plus % p != 0:
                    break
                i_plus //= p
                count += 1
            ans *= (count + 1)
        if i_plus >1:
            ans *= 2
            # 因為前面有縮小質數範圍，如果剩下的質數很大，會檢查不到
        if ans > result[1]:
            result[0] , result[1] = i , ans
    print(f"Between {l} and {h}, {result[0]} has a maximum of {result[1]} divisors.")
