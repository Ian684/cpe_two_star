while True:
    n = int(input())
    if n == 0:break
    arr = []
    total = 0
    for i in range(n):
        t = int(round(float(input().strip()) * 100))
        total += t
        arr.append(t)
    arr = sorted(arr)
    count1 = total // n
    count2 = count1 if total % n == 0 else count1 + 1
    result1 = 0
    result2 = 0
    for a in arr:
        if a < count1:
            result1 += count1 - a           
        if a > count2:
            result2 += a - count2
    result = max(result1 , result2)
    print(f"${result / 100:.2f}")

# float 誤差
# 超出cent , 多判斷
# 判斷當有超出cent時 , 付出(會有兩個結果,但count大的一定會更大)跟收到(會有兩個結果,但count大的一定會更小)哪個大(因為這是要達到均分的流動錢)
