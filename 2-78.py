n = int(input())
for i in range(n):
    try:
        trash = input()
    except EOFError:break
    block = set()
    check = {}
    while True:
        try:
            t = input()
        except EOFError:break
        if t == "#":break
        t = t.split()
        lock = t[0] 
        transaction = int(t[1])
        item = int(t[2])
        if transaction in block:
            print("IGNORED")
            continue
        if item not in check:
            check[item] = [set() , set()]
            if lock == "X":
                check[item][0].add(transaction)
            else:
                check[item][1].add(transaction)
            print("GRANTED")
            continue
        valid = True
        if lock == "S":
            for j in check[item][0]:
                if j != transaction:
                    print("DENIED")
                    block.add(transaction)
                    valid = False
                    break
            if valid:
                print("GRANTED")
                check[item][1].add(transaction)
        elif lock == "X":
            for k in range(2):
                for j in check[item][k]:
                    if j != transaction:
                        print("DENIED")
                        block.add(transaction)
                        valid = False
                        break
                if not valid:break
            if valid:
                print("GRANTED")
                check[item][0].add(transaction)
    if i != n - 1:print()
