def cal(a1 , a2 , a3 , a4 , a5):
    operators = ('+','-','*')
    flag = False
    for o1 in operators:
        for o2 in operators:
            for o3 in operators:
                for o4 in operators:
                    ans = a1
                    for i , j in [[o1 , a2], [o2 , a3] , [o3 , a4] , [o4 , a5]]:
                        if i == '-':
                            ans -= j
                        elif i == '+':
                            ans += j
                        else:
                            ans *= j
                    if ans == 23:
                        flag = True
                        break
                if flag:break
            if flag:break
        if flag:break
    return flag
def main():
    while True:
        a = list(map(int , input().split()))
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0 and a[4] == 0:break
        flag = False
        for a1 in range(5):
            for a2 in range(5):
                for a3 in range(5):
                    for a4 in range(5):
                        for a5 in range(5):
                            if len(set([a1 , a2 , a3 , a4 , a5])) != 5:continue
                            flag = cal(a[a1] , a[a2] , a[a3] , a[a4] , a[a5])
                            if flag:break
                        if flag:break
                    if flag:break
                if flag:break
            if flag:break
        if flag:
            print("Possible")
        else:
            print("Impossible")
if __name__ == "__main__":
    main()
