def main():
    while True:
        try:
            first , operator , second = input().split()
            first , second = int(first) , int(second)
        except EOFError:break
        if operator == "%":
            print(first % second)
        else:
            print(first // second)
if __name__ == '__main__':
    main()
