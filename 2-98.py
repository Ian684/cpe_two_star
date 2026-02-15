#(2n)! / ((n)!*(n+1)!)
limit = 4294967295
kata = {}
i = 1
while True:
    a = 2*i
    b = i+1
    up = 1
    down = 1
    for j in range(i):
        up *= a
        down *= b
        a -= 1
        b -= 1
    t = up // down
    if t > limit:break
    kata[t] = i
    i += 1
while True:
    try:
        n = int(input())
    except EOFError:break
    print(kata[n])
