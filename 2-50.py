n = int(input())
line = input()
for i in range(n):
    time = input()
    last = [time[0:4] , time[4:6] , time[6:8]]
    history = [[last[:] , 0 , 0]]
    demerit = 0
    merit = 0
    while True:
        try:
            line = input()
            if line == "":break
            time , bad = line.split()
            bad = int(bad)
            now = [time[0:4] , time[4:6] , time[6:8]]
        except EOFError:
            break
        plus = 0
        while True:
            last[0] = str(int(last[0])+1)
            last[0] = '0'*(4-len(last[0])) + last[0]
            if last[0] > now[0]:
                break
            if last[0] == now[0] and last[1] > now[1]:
                break
            if last[0] == now[0] and last[1] == now[1] and last[2] > now[2]:
                break
            if demerit > 0:
                demerit = min(int(demerit / 2) , max(0 , demerit - 2))
                history.append([last[:] , merit , demerit])
            elif demerit == 0:
                plus += 1
                if not (plus & 1):
                    merit = min(5 , merit+1)
                    history.append([last[:] , merit , demerit])
        demerit += bad
        if demerit > 2*merit:
            demerit -= 2*merit
            merit = 0
        else:
            merit -= demerit / 2
            merit = int(merit)
            demerit = 0
        history.append([now[:] , merit , demerit])
        last = now[:]
    plus = 0
    while True:
        last[0] = str(int(last[0])+1)
        last[0] = '0'*(4-len(last[0])) + last[0]
        if merit >= 5:break
        if demerit > 0:
            demerit = min(int(demerit / 2) , max(0 , demerit - 2))
            history.append([last[:] , merit , demerit])
        elif demerit == 0:
            plus += 1
            if not (plus & 1):
                merit += 1
                history.append([last[:] , merit , demerit])
    last_merit , last_demerit = -1 , -1
    for time , merit , demerit in history:
        if merit == last_merit and demerit == last_demerit:continue
        print(f"{time[0]}-{time[1]}-{time[2]}" , end=" ")
        if merit == 0 and demerit == 0:
            print("No merit or demerit points.")
        elif merit == 0:
            print(f"{demerit} demerit point(s).")
        elif demerit == 0:
            print(f"{merit} merit point(s).")
        last_merit , last_demerit = merit , demerit
    if i != n - 1:print()
