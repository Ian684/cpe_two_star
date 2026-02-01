def mul(a , b):
    l = len(a) + len(b)
    arr = [0]*l
    for i in range(len(a)):
        for j in range(len(b)):
            arr[i+j] += (a[i] * b[j])
            arr[i+j+1] += arr[i+j] // 10
            arr[i+j] %= 10
    arr = arr[::-1]
    i = 0
    while i < len(arr)-1:
        if arr[i] != 0:break
        i += 1
    arr = arr[i:]
    return ''.join(map(str , arr))
while True:
    try:
        a = list(map(int , input()[::-1]))
        b = list(map(int , input()[::-1]))
        result = mul(a , b)
        print(result)
    except EOFError:
        break
