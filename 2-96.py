n = int(input())
line = input()
check = {}
k = 1
for i in ['Clubs','Diamonds','Hearts','Spades']:
    for j in ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']:
        check[k] = j + ' of ' + i
        k += 1
for i in range(n):
    m = int(input())
    shuffles = []
    for j in range(m):
        t = []
        count = 0
        while count < 52:
            for a in list(map(int , input().split())):
                t.append(a)
                count += 1
        shuffles.append(t)
    result = [i for i in range(1 , 53)]
    while True:
        try:
            temp = input()
        except EOFError:break
        if temp == "":break
        shuffle = shuffles[int(temp)-1]
        t = []
        for sh in shuffle:
            t.append(result[sh-1])
        result = t[:]
    for a in result:
        print(check[a])
    if i != n - 1:print()
