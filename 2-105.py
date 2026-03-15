from math import *
def lenn(aa , bb):
    return sqrt((aa[0] - bb[0])**2 + (aa[1] - bb[1])**2)
def set_data(num):
    a = []
    starty = 2**16
    startx = 2**16
    for i in range(num):
        x , y = map(int , input().split())
        if y < starty:
            startx , starty = x , y
        elif y == starty and x < startx:
            startx , starty = x , y
        a.append([x , y])
    b = []
    for nx , ny in a:
        if nx == startx and ny == starty:continue
        angle = atan2(ny - starty , nx - startx)
        b.append([angle , nx , ny])
    b = sorted(b , key = lambda x: (x[0] , lenn([x[1] , x[2]] , [startx , starty])))
    return [startx , starty] , b
def compare(aa , bb , cc):
    t = (bb[0] - aa[0])*(cc[1] - aa[1]) - (cc[0] - aa[0])*(bb[1] - aa[1])
    if t <= 0:
        return False
    return True
def make(start , temp):
    if len(temp) == 0:
        return [start]
    arr = [start , temp[0][1:]]
    for angle , x , y in temp[1:]:
        arr.append([x , y])
        while True:
            if len(arr) < 3:break
            if compare(arr[-3] , arr[-2] , arr[-1]):break
            arr.pop(-2)
    return arr
def cross(a , b , c):
    return (b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])
def isonline(aim , b , c):
    if aim[0] <= max(b[0] , c[0]) and aim[0] >= min(b[0] , c[0]) and aim[1] <= max(b[1] , c[1]) and aim[1] >= min(b[1] , c[1]) :
        return True
    return False
def intersection(a1 , a2 , b1 , b2):
    o1 = cross(a1 , a2 , b1)
    o2 = cross(a1 , a2 , b2)
    o3 = cross(b1 , b2 , a1)
    o4 = cross(b1 , b2 , a2)
    if o1 * o2 < 0 and o3 * o4 < 0:return True

    if o1 == 0 and isonline(b1 , a1 , a2):return True
    if o2 == 0 and isonline(b2 , a1 , a2):return True
    if o3 == 0 and isonline(a1 , b1 , b2):return True
    if o4 == 0 and isonline(a2 , b1 , b2):return True

    return False
def inpolygon(aim , polygon):
    n = len(polygon)
    if n <= 2:return False
    flag = False
    for i in range(n):
        j = (i+1)%n
        if (polygon[i][1] > aim[1]) != (polygon[j][1] > aim[1]):
            if aim[0] < ((polygon[j][0]-polygon[i][0])*(aim[1]-polygon[i][1])/(polygon[j][1]-polygon[i][1])+polygon[i][0]):
                flag = flag ^ True
    return flag
def solve(a , b):
    an , bn = len(a) , len(b)
    for i in range(an):
        if inpolygon(a[i] , b):
            print("No")
            return
    for i in range(bn):
        if inpolygon(b[i] , a):
            print("No")
            return
    for i in range(an):
        for j in range(bn):
            if intersection(a[i] , a[(i+1)%an] , b[j] , b[(j+1)%bn]):
                print("No")
                return 
    print("Yes")
    return
def main():
    while True:
        m , c = map(int , input().split())
        if m == 0 and c == 0:break
        starta , a = set_data(m)
        startb , b = set_data(c)
        a = make(starta , a)
        b = make(startb , b)
        solve(a , b)
if __name__ == "__main__":
    main()
