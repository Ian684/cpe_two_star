from math import *
def main():
    while True:
        try:
            n , l , w = map(int , input().split())
        except EOFError:break
        circles = []
        for i in range(n):
            p , r = map(int , input().split())
            if r < w/2:
                continue
            first = p - sqrt(r**2 - (w/2)**2)
            second = p + sqrt(r**2 - (w/2)**2)
            circles.append([first , second])    
        circles = sorted(circles)
        now = 0
        c = 0
        i = -1
        last_first = -1 * 1 << 60
        last_second = 0
        while i < len(circles) and now < l:
            m = [1 << 60 , -1]
            u = -1
            for j in range(i+1 , len(circles)):
                first , second = circles[j]
                if last_first <= first <= last_second:
                    if second > m[1]:
                        m = [first , second]
                        u = j
                    continue
                break
            last_first , last_second = m
            now = last_second
            if u == -1:
                break
            c += 1
            i = u
        if now < l:
            print(-1)
        else:
            print(c)
if __name__ == "__main__":
    main()
