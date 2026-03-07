from math import gcd
def generate_lcm(a , b):
    return a//gcd(a , b)*b
def solve(n , m , numbers):
    ans = 0
    for i in range(1 , 1 << m):
        lcm = 1
        flag = True
        count = 0
        for j in range(0 , m):
            if i & (1 << j):
                lcm = generate_lcm(lcm , numbers[j])
                if lcm > n:
                    flag = False
                    break
                count += 1
        if flag:
            if count & 1:
                ans += n // lcm
            else:
                ans -= n // lcm
    return n - ans
def main():
    while True:
        try:
            n , m = map(int , input().split())
            numbers = list(map(int , input().split()))
        except EOFError:break
        ans = solve(n , m , numbers)
        print(ans)
if __name__ == "__main__":
    main()
