letter = []
low = ord('a')
_low = ord('A')
for i in range(26):
    letter.append(chr(low+i))
    letter.append(chr(_low+i))
for i in range(10):
    letter.append(str(i))
def get(a , b):
    arr = []
    brr = []
    a , b = a + ' ' , b + ' '
    if len(a) < len(b):
        a , b = b , a
    sa = ''
    sb = ''
    for i in range(len(b)):
        if a[i] not in letter:
            if sa != '':
                arr.append(sa)
                sa = ''
        else:
            sa += a[i]
        if b[i] not in letter:
            if sb != '':
                brr.append(sb)
                sb = ''
        else:
            sb += b[i]
    for i in range(len(b) , len(a)):
        if a[i] not in letter:
            if sa != '':
                arr.append(sa)
                sa = ''
        else:
            sa += a[i]
    return [arr , brr]
def cal(a , b):
    arr , brr = get(a , b)
    la , lb = len(arr) , len(brr)
    dp = [[0]*(la+1) for _ in range(lb+1)]
    for i in range(1 , lb+1):
        for j in range(1 , la+1):
            if arr[j-1] == brr[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1] , dp[i-1][j])
    return dp[lb][la]
now = 0
while True:
    now += 1
    try:
        a = input()
        b = input()
        if a == "" or b == "":
            if now//10 == 0:
                print(f" {now}. Blank!")
            else:
                print(f"{now}. Blank!")
            continue
        result = cal(a , b)
        if now//10 == 0:
            print(f" {now}. Length of longest match: {result}")
        else:
            print(f"{now}. Length of longest match: {result}")
    except EOFError:break
