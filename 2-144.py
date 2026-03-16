from math import *
def main():
    while True:
        try:
            n = int(input())
        except EOFError:break
        points = []
        now = 0
        lasty = -1
        for i in range(n):
            y , x = map(float , input().split())
            points.append([now , max(y , lasty)])
            lasty = y
            now += x
        lastx , lasty = now , lasty
        ans = 0
        for x , y in points[1:]:
            times = lastx**2 / x**2
            t = atan2(y*times-lasty , x*times - lastx)
            if abs(t) > abs(ans):
                ans = t
        t = sqrt((4.9*lastx**2)/((tan(ans)*lastx-lasty)*cos(ans)**2))
        print(f"{ans*180/pi:.2f} {t:.2f}")
if __name__ == "__main__":
    main()
