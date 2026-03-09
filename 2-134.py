import math
def cal(mid , p , q , r , s , t , u):
    return p*(math.exp(-mid)) + q*math.sin(mid) + r*math.cos(mid) + s*math.tan(mid) + t*(mid**2) + u
def solve(p , q , r , s , t , u):
    l = 0
    r1 = 1
    for i in range(500):
        mid = (l + r1) / 2
        ans = cal(mid , p , q , r , s , t , u)
        if ans > 0:
            l = mid
        else:
            r1 = mid
    return mid
def main():
    while True:
        try:
            p , q , r , s , t , u = map(int , input().split())
        except EOFError:break
        if cal(0 , p , q, r, s , t ,u) * cal(1 , p , q , r , s , t , u) > 0:
            print(f"No solution")
            continue
        x = solve(p , q , r , s , t , u)
        print(f"{x:.4f}")
if __name__ == "__main__":
    main()
