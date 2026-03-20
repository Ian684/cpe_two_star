def solve(n , c , points , alph):
    ans = {}
    for al in alph:
        ans[al] = 0
    for color1 in alph:
        if color1 not in points:continue
        current_set = points[color1]
        for x1 , y1 in current_set:
            for x2 , y2 in current_set:
                if x1 == x2 and y1 == y2:continue
                dx , dy = y2-y1 , x2-x1
                x3 , y3 = -dx + x1 , dy + y1
                x4 , y4 = -dx + x2 , dy + y2
                if 0 <= x3 < n and 0 <= y3 < n and 0 <= x4 < n and 0 <= y4 < n:
                    if (x3 , y3) in current_set and (x4 , y4) in current_set:
                        ans[color1] += 1
    return ans
def main():
    first = True
    while True:
        while True:
            n = input()
            if n != "":
                n = int(n)
                break
        if n == 0:break
        if first:
            first = False
        else:
            print()
        while True:
            c = input()
            if c != "":
                c = int(c)
                break
        alph = []
        points = {}
        i = 0
        while i < n:
            t = input()
            if t == "":continue
            for j in range(n):
                if t[j] not in points:
                    points[t[j]] = set()
                points[t[j]].add((i , j))
            i += 1
        i = 0
        while i < c:
            t = input()
            if t == "":continue
            alph.append(t)
            i += 1
        ans = solve(n , c , points , alph)
        for al in alph:
            print(al , ans[al]//4)
if __name__ == "__main__":
    main()
