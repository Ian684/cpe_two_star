n = int(input())
trash = input()
for i in range(n):
    people = {}
    a , b = map(int , input().split())
    for j in range(1 , a+1):
        people[j] = set()
    while True:
        try:
            line = input()
            if line == "":break
            man , tree = map(int , line.split())
        except EOFError:break
        people[man].add(tree)
    all_ = []
    c = 0
    for j in range(1 , a+1):
        if people[j] in all_:
            continue
        else:
            c += 1
            all_.append(people[j])
    print(c)
    if i != n - 1:print()
