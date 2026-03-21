def main():
    while True:
        try:
            n , a = map(int , input().split())
        except EOFError:break
        sum = 0
        for i in range(1 , n+1):
            sum += (a**i)*i
        print(sum)
if __name__ == "__main__":
    main()
