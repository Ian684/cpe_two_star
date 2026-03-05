def solve(x):
    return (x*(x+1)//2)**2
def main():
    while True:
        try:
            x = int(input())
        except EOFError:break
        ans = solve(x)
        print(ans)
if __name__ == "__main__":
    main()
