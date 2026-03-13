import math, sys

def cnt(lcm, sgn, i):
    if i == m:
        return n // lcm * sgn
    return cnt(lcm, sgn, i+1) + \
           cnt(lcm*r[i]//math.gcd(lcm, r[i]), -sgn, i+1)

for n, m in (map(int, s.split()) for s in sys.stdin):
    r = list(map(int, sys.stdin.readline().split()))
    print(cnt(1, 1, 0))
