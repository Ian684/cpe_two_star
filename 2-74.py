n = int(input())
trash = input()
for l in range(n):
    charge = input()
    if charge == "":continue
    charge = list(map(int , charge.split()))
    time = {}
    result = {}
    all_ = []
    while True:
        try:
            t = input()
        except EOFError:
            break
        if t == "":break
        name , clock , dir_ , far = t.split()
        far = int(far)
        if name not in result:
            result[name] = 0
        if name not in time:
            time[name] = []
        if name not in all_:
            all_.append(name)
        day , hour , minute = int(clock[3:5]) , int(clock[6:8]) , int(clock[9:11])
        time[name].append([day , hour , minute , far , dir_])
    all_ = sorted(all_)
    for aim in all_:
        time[aim] = sorted(time[aim])
        i = 0
        t_hour = -1
        t_far = -1
        while i < len(time[aim]):
            if time[aim][i][4] == "enter":
                t_hour = time[aim][i][1]
                t_far = time[aim][i][3]
            elif time[aim][i][4] == "exit" and t_hour != -1:
                ans = abs(time[aim][i][3] - t_far) * charge[t_hour] + 100
                result[aim] += ans
                t_hour = -1
                t_far = -1
            i += 1
    for aim in all_:
        if result[aim] != 0:
            print(f"{aim} ${(result[aim] + 200) / 100:.2f}")
    if l != n - 1:print()
