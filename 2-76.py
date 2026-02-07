now = 0
while True:
    n , p = map(int , input().split())
    if n == 0 and p == 0:break
    if now != 0:
        print()
    arr = []
    for _ in range(n):
        trash = input()
    for i in range(p):
        name = input()
        price , amount = input().split()
        amount = int(amount)
        for _ in range(amount):
            trash = input()
        arr.append([-1 * amount , float(price) , i , name])
    arr = sorted(arr)
    now += 1
    print(f"RFP #{now}")
    print(arr[0][3])
