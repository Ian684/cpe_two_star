def cal(n):
    for i in range(1 , 100000):
        check = [0]*n
        check[0] = 1
        current = 0
        while True:
            if current == 12:
                if sum(check) == n:
                    return i
                else:
                    break
            count = 0
            while True:
                if count == i:
                    break
                current += 1
                current %= n
                if check[current] == 0:
                    count += 1
                else:
                    continue
            check[current] = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(cal(n))