import math 
def bsgs(a , c , P):
    right = {}
    m = int(math.ceil(math.sqrt(P)))
    start = c % P
    for q in range(m+1):
        right[start] = q
        start = start * a % P
    am = a ** m % P
    left = 1
    for p in range(m+1):
        if left in right:
            q = right[left]
            ans = m * p - q
            if ans >= 0:return ans
        left = left * am % P 
    return -1
if __name__ == "__main__":
    while True:
        try:
            P , a , c = map(int , input().split())
        except EOFError:break
        ans = bsgs(a , c , P)
        if ans == -1:print("no solution")
        else:print(ans)
