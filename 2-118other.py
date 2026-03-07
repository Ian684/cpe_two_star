def computelps(target):
    lps = [0]*len(target)
    prevlps = 0
    i = 1
    while i < len(target):
        if target[i] == target[prevlps]:
            prevlps += 1
            lps[i] = prevlps
            i += 1
        else:
            if prevlps != 0:
                prevlps = lps[prevlps-1]
            else:
                lps[i] = 0
                i += 1
    return lps
# =================練習kmp 可省略 ================
def kmp(mainstr , target):
    lps = computelps(target)
    i = 0
    j = 0
    while i < len(mainstr):
        if mainstr[i] == target[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == len(target):
            return i - j
    return -1
# ================================================
def main():
    while True:
        target = input()
        if target == ".":break
        lps = computelps(target)
        n = len(target)
        base = lps[-1]
        if n % (n - base) == 0:
            print(n // (n - base))
        else:
            print(1)
if __name__ == "__main__":
    main()
    #python 會 memory limit exceed
