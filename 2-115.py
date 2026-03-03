def main():
    spl = ('.',',','!','?',' ')
    while True:
        try:
            ans = {}
            line = ''
            count = 0
            while True:
                if len(line) > 0 and line[-1] != '-' and count != 0:
                    if count not in ans:
                        ans[count] = 0
                    ans[count] += 1
                    count = 0
                line = input()
                if line == "#":break
                for i in range(len(line)):
                    if line[i] in spl and count != 0:
                        if count not in ans:
                            ans[count] = 0
                        ans[count] += 1
                        count = 0
                    if 65 <= ord(line[i]) <= 90 or 97 <= ord(line[i]) <= 122:
                        count += 1
        except EOFError:break
        for k , v in sorted(ans.items() , key = lambda x : x[0]):
            print(k , v)
        print()
if __name__ == "__main__":
    main()
