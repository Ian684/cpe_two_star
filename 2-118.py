from math import *
def solve(s):
    l = len(s)
    ans = 1 << 60
    for i in range(1 , int(sqrt(l))+1):
        if l % i != 0:continue
        j = l//i
        if s[:i]*j == s:
            ans = min(i , ans)
        if s[:j]*i == s:
            ans = min(j , ans)
    return ans
def main():
    while True:
        s = input()
        if s == '.':break
        ans = len(s) // solve(s)
        print(ans)
if __name__ == "__main__":
    main()
