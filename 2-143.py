def main():
    time = {"utc":0,"gmt":0,"bst":1,"ist":1,"wet":0,"west":1,"cet":1,"cest":2,"eet":2,"eest":3,"msk":3,"msd":4,"ast":-4,"adt":-3,"nst":-3.5,"ndt":-2.5,"est":-5,"edt":-4,"cst":-6,"cdt":-5,"mst":-7,"mdt":-6,"pst":-8,"pdt":-7,"hst":-10,"akst":-9,"akdt":-8,"aest":10,"aedt":11,"acst":9.5,"acdt":10.5,"awst":8}
    n = int(input())
    for i in range(n):
        line = input().split()
        if len(line) == 3:
            if line[0] == "noon":
                t = 12*60
            else:
                t = 24*60
            first , second = line[1:]
        else:
            t , s , first , second = line
            t = t.split(":")
            t = int(t[0])*60 + int(t[1])
            if s == "p.m." and t // 60 != 12:
                t += 12*60
            elif s == "a.m." and t // 60 == 12:
                t -= 12*60
        first , second = first.lower() , second.lower()
        difference = time[second] - time[first]
        t += 60*difference
        t = int(t)
        if t < 0:
            t += 24*60
        t %= 24*60
        hour = t // 60
        minute = t % 60
        s = ""
        if hour >= 12:
            s = "p.m."
            if hour != 12:
                hour -= 12
            elif minute == 0:
                s = "noon"
        else:
            s = "a.m."
            if hour == 0:
                hour = 12
                if minute == 0:
                    s = "midnight"
        if s == "noon" or s == "midnight":
            print(s)
        else:
            print(f"{hour}:{str(minute).zfill(2)} {s}")
if __name__ == "__main__":
    main()
