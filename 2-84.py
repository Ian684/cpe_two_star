n = int(input())
for i in range(n):
    station , s , q = map(int , input().split())
    stations = {}
    for j in range(1 , station + 1):
        stations[j] = list(map(int , input().split()[1:]))
    ans = 0
    car = []
    now = 1
    while True:
        if now > station:now = 1
        while True:
            if len(car) == 0:break
            if len(stations[now]) >= q:
                while car:
                    if car[-1] == now:
                        car.pop()
                        ans += 1
                    else:break
                break
            ans += 1
            t = car.pop()
            if t != now:
                stations[now].append(t)
        while True:
            if len(car) >= s or len(stations[now]) == 0:break
            t = stations[now].pop(0)
            car.append(t)
            ans += 1
        if len(car) == 0:
            stop = True
            for k , a in stations.items():
                if len(a) == 0:continue
                stop = False
                break
            if stop:break
        now += 1
        ans += 2
    print(ans)
