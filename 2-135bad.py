import sys
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
    line = sys.stdin.readlines()
    line = ''.join(line)
    l = 0
    while True:
        arr = []
        while True:
            if line[l] == "#":
                l += 1
                break
            if line[l] not in alph:
                l += 1
                continue
            arr.append(line[l])
            l += 1
        if len(arr) == 0:break
        temp = ''
        for a in arr:
            temp +=  bin(index[a])[2:].zfill(6)
        output_buffer = bytearray()
        for i in range(0 , len(temp) // 8 * 8 , 8):
            output_buffer.append(int(temp[i:i+8] , 2))
        sys.stdout.buffer.write(output_buffer)
        sys.stdout.buffer.write(b"#")
if __name__ == "__main__":
    main()
