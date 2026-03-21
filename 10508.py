def main():
    while True:
        try:
            h , w = map(int , input().split())
        except EOFError:break
        result = {}
        for i in range(w+1):
            result[i] = []
        first = input()
        result[w].append(first)
        last = input()
        result[0].append(last)
        for i in range(h-2):
            temp = input()
            count = 0
            for j in range(w):
                if temp[j] == first[j]:
                    count += 1
            result[count].append(temp)
        for i in range(w , -1 , -1):
            for s in result[i]:
                print(s)
if __name__ == '__main__':
    main()
