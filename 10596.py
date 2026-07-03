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
        try:
            n , m = map(int , input().split())
            dsu = DSU(n)
            lines = {}
            points = set()
            for i in range(m):
                a , b = map(int , input().split())
                if a not in lines:
                    lines[a] = 0
                if b not in lines:
                    lines[b] = 0
                lines[a] += 1
                lines[b] += 1
                points.add(a)
                points.add(b)
                dsu.union(a , b)
            ans = set()
            for i in points:
                ans.add(dsu.find(i))
            if len(ans) != 1:
                print("Not Possible")
            else:
                valid = True
                for i in range(n):
                    if i not in lines:continue
                    if lines[i] & 1:
                        valid = False
                        break
                if valid:
                    print("Possible")
                else:
                    print("Not Possible")
            now += 1
        except EOFError:break
if __name__ == "__main__":
    main()
