def generate_alph():
    alph = set()
    index = {}
    j = 0
    for i in range(65 , 91):
        alph.add(chr(i))
        index[chr(i)] = j
        j += 1
    for i in range(97 , 123):
        alph.add(chr(i))
        index[chr(i)] = j
        j += 1
    alph.add("+")
    index["+"] = 62
    alph.add("/")
    index["/"] = 63
    return alph , index
def main():
    alph , index = generate_alph()
    while True:
        flag = True
        stop = True
        arr = []
        last = ''
        while flag:
            line = input()
            line = last + line
            for l in range(len(line)):
                if line[l] == "#":
                    last = line[l+1:]
                    flag = False
                    break
                if line[l] in alph:
                    stop = False 
                    arr.append(line[l])
        if stop or last == "#":
            break
        temp = ''

if __name__ == "__main__":
    main()
