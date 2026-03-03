def main():
    m , n = map(int , input().split())
    scores = {}
    for i in range(m):
        t = input().split()
        temp , score = t[0] , int(t[1])
        scores[temp] = score
    i = 0
    c = 0
    while i < n:
        line = input()
        if line == '.':
            print(c)
            c = 0
            i += 1
        for l in line.split():
            if l in scores:
                c += scores[l]
if __name__ == "__main__":
    main()
