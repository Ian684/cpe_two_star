from math import *
def solve(n , lines , center):
    angles = []
    cx , cy = center
    for x1 , y1 , x2 , y2 in lines:
        angle = [atan2(y1-cy , x1-cx) , atan2(y2-cy , x2-cx)]
        if angle[0] < 0:
            angle[0] += 2*pi
        if angle[1] < 0:
            angle[1] += 2*pi
        first , second = min(angle) , max(angle)
        if second - first > pi:
            angles.append([second , 0])
            angles.append([2*pi , 1])
            angles.append([0 , 0])
            angles.append([first , 1])
        else:
            angles.append([first , 0])
            angles.append([second , 1])
    angles = sorted(angles)
    ans = -1
    count = 0
    for angle , flag in angles:
        if flag == 0:
            count += 1
            ans = max(ans , count)
        else:
            count -= 1
    print(ans)
    return
def main():
    while True:
        n = int(input())
        if n == 0:break
        lines = []
        for i in range(n):
            lines.append(list(map(int , input().split())))
        center = list(map(int , input().split()))
        solve(n , lines , center)
if __name__ == "__main__":
    main()
