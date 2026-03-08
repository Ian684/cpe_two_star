def solve(n):
    i = 1
    left = []
    while True:
        if n < i:
            break
        left.append(i)
        n -= i
        i += 1
    left[-1] += n
    w = 0
    space = len(left)*2
    for h in range(len(left)-1):
        space -= 2
        print(" "*space , end="")
        print("#**" + "."*w + "**#")
        for dh in range(left[h]-1):
            print(" "*space , end="")
            print("#" + "."*(w + 4) + "#")
        w += 4
    print("#**" + "."*w + "#")
    for dh in range(left[-1]-1):
        print("#" + "."*(w + 2) + "#")
def main():
    now = 1
    while True:
        try:
            n = int(input())
        except EOFError:break
        print(f"Tower #{now}")
        now += 1
        solve(n)
        print()
if __name__ == "__main__":
    main()
