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
    for i in range(10):
        alph.add(str(i))
        index[str(i)] = j
        j += 1
    alph.add("+")
    index["+"] = 62
    alph.add("/")
    index["/"] = 63
    return alph , index
def main():
    alph , index = generate_alph()
    last = ''
    while True:
        flag = True
        stop = True
        arr = []
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
        for a in arr:
            t = bin(index[a])[2:]
            temp += (6-len(t))*'0'+t
        for i in range(0 , len(temp) // 8 * 8 , 8):
            print(chr(int(temp[i:i+8] , 2)),end="")
        print("#",end="")
if __name__ == "__main__":
    main()
