def main():
    cases = 1
    groups = {}
    while True:
        try:
            line = input().split()
        except EOFError:break
        for word in line:
            if word == "#":
                print("Set #" + str(cases) + ":")
                cases += 1
                result = []
                for k , v in groups.items():
                    result.append([v[0][:5] , v[-1][:5] , len(v)])
                result = sorted(result)
                for first , second , num in result:
                    print(second , num)
                print()
                groups = {}
                continue
            if len(word) > 2:
                key = word[0:2] + ' ' + word[3:]
            else:
                key = word[:]
            key = key[:5]
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
if __name__ == "__main__":
    main()
