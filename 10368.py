def solve():
    while True:
        a , b = map(int , input().split())
        if a == 0 and b == 0:
            break
        if a < b:
            a, b = b, a
        stan_wins = True
        while True:
            if a % b == 0 or a // b >= 2:
                break
            if a < b:
                a, b = b, a
            a , b = b , a % b
            stan_wins = not stan_wins
        if stan_wins:
            print("Stan wins")
        else:
            print("Ollie wins")
if __name__ == "__main__":
    solve()
