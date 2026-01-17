def cal(x , xstring , y , ystring):
    dp = [[0]*(y+1) for _ in range(x+1)]
    for j in range(y+1):
        dp[0][j] = j
    for i in range(x+1):
        dp[i][0] = i
    for i in range(1 , x+1):
        for j in range(1 , y+1):
            if xstring[i-1] == ystring[j-1]:
                dp[i][j] = min(dp[i-1][j]+1 , dp[i][j-1]+1 , dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i-1][j]+1 , dp[i][j-1]+1 , dp[i-1][j-1]+1)
    return dp[i][j]
while True:
    try:
        x , xstring = input().split()
        y , ystring = input().split()
        print(cal(int(x) , xstring , int(y) , ystring))
    except EOFError:
        break