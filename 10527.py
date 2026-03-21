def main():
    while True:
        n = int(input())
        if n == -1:break
        if n < 10:
            print(10+n)
            continue
        result = []
        for i in range(9 , 1 , -1):
            while n % i == 0:
                n //= i
                result.append(i)
        if n != 1:
            print("There is no such number.")
        else:
            print(''.join(map(str , result[::-1])))
if __name__ == "__main__":
    main()
