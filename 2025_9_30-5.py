def check(arr , days , mid):
    current = 1
    count = 0
    for i in arr:
        if count+i <= mid:
            count += i
        else:
            current += 1
            count = i
            if current > days:
                return False
    return True
# 驗證，累加天數並控制在mid以下，一超過就換下一天並重製距離和驗證天數
# 因為把每個都壓在一定距離下，天數會更多
def search(arr , days):
    low , high = max(arr) , sum(arr)
    while True:
        if low >= high:
            break
        mid = (low + high)//2
        if check(arr , days , mid):
            high = mid
        else:
            low = mid + 1
    return low
# 二分搜去逼近答案並驗證mid是否可行
# 可行代表數字可以更小，相反數字要比mid更大
while True:
    try:
        a , b = map(int , input().split())
        arr = []
        a , b = a + 1 , b + 1
        for i in range(a):
            arr.append(int(input()))
        print(search(arr , b))
    except EOFError:
        break