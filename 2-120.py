# 並查集、廣深度搜尋
from math import *
class kruskal:
    def __init__(self , n , circles):
        self.__n = n
        self.__parent = list(range(n))
        self.__size = [1]*n
        self.__circles = circles[:]
    def find(self , x):
        if self.__parent[x] != x:
            self.__parent[x] = self.find(self.__parent[x])
        return self.__parent[x]
    def union(self , a , b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota != rootb:
            if self.__size[roota] < self.__size[rootb]:
                roota , rootb = rootb , roota
            self.__size[roota] += self.__size[rootb]
            self.__parent[rootb] = roota
            return True
        return False
    def distance(self , a , b):
        return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    def _kruskal(self):
        for i in range(self.__n):
            for j in range(i+1 , self.__n):
                if self.distance(self.__circles[i] , self.__circles[j]) > self.__circles[i][2] + self.__circles[j][2]:
                    continue
                if self.distance(self.__circles[i] , self.__circles[j]) < abs(self.__circles[i][2] - self.__circles[j][2]):
                    continue
                if self.find(i) != self.find(j):
                    valid = self.union(i , j)
        ans = -1
        for i in range(self.__n):
            ans = max(self.__size[i] , ans)
        return ans
def main():
    while True:
        n = int(input())
        if n == -1:break
        if n == 0:
            print(f"The largest component contains {0} rings.")
            continue
        circles = []
        for i in range(n):
            circles.append(list(map(float , input().split())))
        k = kruskal(n , circles)
        ans = k._kruskal()
        if ans == 1:
            print(f"The largest component contains {ans} ring.")
        else:
            print(f"The largest component contains {ans} rings.")
if __name__ == "__main__":
    main()
