def topo(check , line , n):
    





def main():
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        line = {}
        check = [False]*n
        for k in range(n):
            line[k] = []
        for _ in range(m):
            i , j = map(int , input().split())
            i -= 1
            j -= 1
            line[i].append(j)
        ans = topo(check , line , n)
        print(' '.join(map(str , ans)))
if __name__ == "__main__":
    main()
