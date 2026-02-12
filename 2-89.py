now = 0
while True:
    now += 1
    a = input()
    if a == "#":break
    b = input()
    la , lb = len(a) , len(b)
    dp = [[0]*(lb+1) for _ in range(la+1)]
    for i in range(la):
        for j in range(lb):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                if dp[i][j+1] > dp[i+1][j]:
                    dp[i+1][j+1] = dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
    ans = dp[la][lb]
    print(f"Case #{now}: you can visit at most {ans} cities.")
