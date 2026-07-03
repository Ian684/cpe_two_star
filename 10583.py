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
    now = 1
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        dsu = DSU(n)
        for i in range(m):
            a , b = map(int , input().split())
            a -= 1
            b -= 1
            dsu.union(a , b)
        ans = set()
        for i in range(n):
            ans.add(dsu.find(i))
        print(f"Case {now}: {len(ans)}")
        now += 1
if __name__ == "__main__":
    main()
