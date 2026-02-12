from math import gcd
n = int(input())
for i in range(n):
    s1 = int(input() , 2)
    s2 = int(input() , 2)
    if gcd(s1 , s2) > 1:
        print(f"Pair #{i+1}: All you need is love!")
    else:
        print(f"Pair #{i+1}: Love is not all you need!")
