from math import *
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
if __name__ == "__main__":
    main()
