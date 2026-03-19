def main():
    t = int(input())
    for _ in range(t):
        n , b = map(int , input().split())
        count = 0
        for i in range(b):
            line = list(map(int , input().split()))[1:]
            temp = 1
            for l in line:
                temp *= l
            count += temp
        print(count % n)
if __name__ == "__main__":
    main()
