def solve(d , rat):
    bomb = [[0]*1025 for _ in range(1025)]
    ans = [-1 , -1 , -1]
    for x , y , i in rat:
        for nx in range(x-d , x+d+1):
            for ny in range(y-d , y+d+1):
                if nx < 0 or nx >= 1025 or ny < 0 or ny >= 1025:continue
                bomb[nx][ny] += i
                if ans[2] < bomb[nx][ny]:
                    ans = [nx , ny , bomb[nx][ny]]
    return ans
def main():
    m = int(input())
    while m != 0:
        line = input()
        if line == "":continue
        d = int(line)
        n = int(input())
        rat = []
        for a in range(n):
            x , y , i = map(int , input().split())
            rat.append([x , y , i])
        ans = solve(d , rat)
        print(' '.join(map(str , ans)))
        m -= 1
if __name__ == "__main__":
    main()
