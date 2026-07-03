class DSU:
    def __init__(self , n):
        self.size = [1]*n
        self.parents = list(range(n))
    def find(self , x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self , a , b):
        roota , rootb = self.find(a) , self.find(b)
        if roota != rootb:
            if self.size[roota] < self.size[rootb]:
                roota , rootb = rootb , roota
            self.size[roota] += self.size[rootb]
            self.parents[rootb] = roota
            return True
        return False
def main():
    t = int(input())
    for c in range(t):
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        dsu = DSU(n)
        for i in range(m):
            a , b = map(int , input().split())
            a -= 1
            b -= 1
            dsu.union(a , b)
        result = {}
        ans = -1
        for i in range(n):
            temp = dsu.find(i)
            if temp not in result:
                result[temp] = 0
            result[temp] += 1
            ans = max(ans , result[temp])
        print(ans)
if __name__ == "__main__":
    main()
