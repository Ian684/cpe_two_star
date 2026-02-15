history = {0:[0],1:[1]}
while True:
    try:
        n = int(input())
    except EOFError:break
    if n == 0:
        print(0)
        continue
    elif n == 1:
        print(1)
        continue
    for i in range(n , 0 , -1):
        if i in history:
            result = history[i]
            k = i + 1
            break
    for i in range(k , n+1):
        j = 0
        carry = 0
        while j < len(result):
            result[j] *= i
            result[j] += carry
            carry = result[j] // 10
            result[j] %= 10
            j += 1
        while carry != 0:
            carryt = carry % 10
            carry //= 10
            result.append(carryt)
        if i not in history:
            history[i] = result[:]
    ans = 0
    for a in result:
        ans += a
    print(ans)
