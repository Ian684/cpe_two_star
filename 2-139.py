def cross(a , b , c):
    return (b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])

def isonline(aim , b , c):
    if aim[0] <= max(b[0] , c[0]) and aim[0] >= min(b[0] , c[0]) and aim[1] <= max(b[1] , c[1]) and aim[1] >= min(b[1] , c[1]) :
        return True
    return False

def intersect(line , polygon):
    n = polygon[0]
    polygon = polygon[1:]
    flag = False
    
    for i in range(n):
        next = (i + 1) % n
        o1 = cross(line[0] , line[1] , polygon[i])
        o2 = cross(line[0] , line[1] , polygon[next])
        o3 = cross(polygon[i] , polygon[next] , line[0])
        o4 = cross(polygon[i] , polygon[next] , line[1])
        if o1 * o2 < 0 and o3 * o4 < 0:flag = True

        if o1 == 0 and isonline(polygon[i] , line[0] , line[1]):flag = True
        if o2 == 0 and isonline(polygon[next] , line[0] , line[1]):flag = True
        if o3 == 0 and isonline(line[0] , polygon[i] , polygon[next]):flag = True
        if o4 == 0 and isonline(line[0] , polygon[i] , polygon[next]):flag = True

        if flag:
            break
    return flag

def inpolygon(point , polygon):
    n = polygon[0]
    if n <= 2:return False
    polygon = polygon[1:]
    
    flag = False
    for i in range(n):
        j = (i + 1) % n
        yflag = False
        xflag = False
        if (polygon[i][1] > point[1]) != (polygon[j][1] > point[1]):yflag = True
        if yflag and point[0] < ((polygon[j][0] - polygon[i][0]) * (point[1] - polygon[i][1]) / (polygon[j][1] - polygon[i][1]) + polygon[i][0]):xflag = True
        if xflag and yflag:flag = True ^ flag
    return flag

def solve(submarines , areas , submarine , area):

    for s in range(submarine):
        sub = submarines[s]

        intersection = False
        for ar in areas:
            if intersect(sub , ar):
                intersection = True
                break
        if intersection:
            print(f"Submarine {s+1} is partially on land.")
            continue

        completeland = False
        for ar in areas:
            if inpolygon(sub[0] , ar) and inpolygon(sub[1] , ar):
                completeland = True
                break
        if completeland:
            print(f"Submarine {s+1} is completely on land.")
        else:
            print(f"Submarine {s+1} is still in water.")
def main():
    submarine = int(input())
    submarines = []
    for _ in range(submarine):
        x1 , y1 , x2 , y2 = map(int , input().split())
        submarines.append([[x1 , y1] , [x2 , y2]])
    area = int(input())
    areas = []
    for _ in range(area):
        points = int(input())
        areas.append([points])
        for p in range(points):
            x , y = map(int , input().split())
            areas[-1].append([x , y])
    solve(submarines , areas , submarine , area)
if __name__ == "__main__":
    main()
