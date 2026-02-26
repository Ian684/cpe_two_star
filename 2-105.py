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
def dgk


while True:
    m , c = map(int , input().split())
    if m == 0 and c == 0:break
    starta , a = set_data(m)
    startb , b = set_data(c)
    a = make(starta , a)
    b = make(startb , b)
    if dgk(a , b):
        print("yes")
    else:print("no")
