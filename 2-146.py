from math import *
<<<<<<< HEAD
def distance(a , b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
def main():
    while True:
        line = input().split()
        if len(line) == 2 and line[0] == "0" and line[1] == "0":break
        w = float(line[0])
        n = int(line[1])
        line = list(map(float , line[2:]))
        points = []
        first = 0
        second = 0
        for i in range(0 , len(line) , 2):
            points.append([line[i] , line[i+1]])
            first += line[i]*line[(i+3)%len(line)]
            second += line[i+1]*line[(i+2)%len(line)]
        bigest = 0.5*abs(first-second)
        for i in range(n):
            j = (i+1)%n
            bigest -= w * distance(points[i] , points[j])
        for i in range(n):
            j = (i+1)%n
            k = (i-1)%n
            angle = ((points[j][0]-points[i][0])*(points[k][0]-points[i][0])+(points[j][1]-points[i][1])*(points[k][1]-points[i][1]))/(distance(points[i] , points[j])*distance(points[i] , points[k]))
            angle = max(-1.0, min(1.0, angle))
            angle = acos(angle)
            bigest += (w**2)*(1/tan(angle/2))
        print(f"{bigest:.3f}")
=======
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
>>>>>>> e72dd16bcf1a21f57ce77e21d9039d38669d67f6
if __name__ == "__main__":
    main()
