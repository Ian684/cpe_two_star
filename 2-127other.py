from math import gcd
def generate_lcm(a , b):
    return a//gcd(a , b)*b
result = 0
def dfs(n , m , numbers , now , lcm ,  count):
    global result
    if lcm > n:return
    for i in range(now , m):
        next_lcm = generate_lcm(lcm , numbers[i])
        if lcm <= n:
            if count & 1:
                result += n // next_lcm
            else:
                result -= n // next_lcm
            dfs(n , m , numbers , i+1 , next_lcm ,  count + 1)
    return 
def main():
    global result
    while True:
        try:
            n , m = map(int , input().split())
            numbers = list(map(int , input().split()))
        except EOFError:break
        result = 0
        dfs(n , m , numbers , 0 , 1 , 1)
        print(n - result)
if __name__ == "__main__":
    main()
