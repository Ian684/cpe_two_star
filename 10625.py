rules = {}

def solve(tran , s , aim , times):

    global rules
    base = {}
    dp = {}
    for start , trash in tran.items():
        dp[start] = 0
        base[start] = 0
        if aim == start:
            dp[start] += 1

    for i in range(times):
        newdp = base.copy()
        for k1 , v1 in tran.items():
            for c in v1:
                if c in dp:
                    newdp[k1] += dp[c]
                elif c == aim:
                    newdp[k1] += 1

        dp = newdp.copy()
    ans = 0
    for c in s:
        if c in dp:
            ans += dp[c]
        elif c == aim:
            ans += 1
    return ans

def main():

    global rules
    t = int(input())
    for _ in range(t):
        r = int(input())
        rules = [[0]*94 for i in range(94)]
        tran = {}
        for i in range(r):
            a , b = input().split("->")
            a = ord(a) - 33
            tmp = []
            for j in range(len(b)):
                temp = ord(b[j])-33
                rules[a][temp] += 1
                tmp.append(temp)
            tran[a] = tmp
        q = int(input())
        for i in range(q):
            s , aim , times = input().split()
            times = int(times)
            aim = ord(aim)-33
            temp = []
            for start in s:
                temp.append(ord(start)-33)
            print(solve(tran , temp , aim , times))

if __name__ == "__main__":
    main()
