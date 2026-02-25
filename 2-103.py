while True:
    try:
        faces , times , need = map(int , input().split())
    except EOFError:break
    if times == 0 and need == 0:
        print("1/1")
        continue
    elif times == 0 and need > 0:
        print("0/1")
        continue
    elif times > 0 and need == 0:
        print(f"{0}/{faces**times}")
    dp = [[0]*(need) for _ in range(times)]
    for i in range(faces):
        if i >= need:break
        dp[0][i] = 1
    for t in range(1 , times):
        window_value = 0
        for k in range(1 , need):
            window_value += dp[t-1][k-1]
            if k > faces:
                window_value -= dp[t-1][k - faces - 1]
            dp[t][k] = window_value
    print(f"{dp[-1][-1]}/{faces**times}")
