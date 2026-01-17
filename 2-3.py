def calculate_legal():
    if king_[0] == queen_[0]:
        if king_[1] < queen_[1]:
            for x in range(king_[1] + 1, 8):
                legal.append([queen_[0] , x])
        else:
            for x in range(king_[1]):
                legal.append([queen_[0] , x])
        for x in range(8):
            legal.append([x , queen_[1]])
    elif king_[1] == queen_[1]:
        if king_[0] < queen_[0]:
            for x in range(king_[0] + 1, 8):
                legal.append([x , queen_[1]])
        else:
            for x in range(king_[0]):
                legal.append([x , queen_[1]])
        for x in range(8):
            legal.append([queen_[0] , x])
    else:
        for x in range(8):
            legal.append([x , queen_[1]])
            legal.append([queen_[0] , x])
    return legal
check = ["Illegal state" , "Illegal move" , "Move not allowed" , "Continue" , "Stop"]
side = {}
i = 0
for a in range(8):
    for b in range(8):
        side[i] = [a , b]
        i += 1
while True:
    try:
        king , queen , moveside = map(int , input().split())
        if king == queen:
            print(check[0])
            continue
        if 63 < king or king < 0 or queen < 0 or 63 < queen:
            print(check[1])
            continue
        king_ , queen_ = side[king] , side[queen]
        legal = []
        if moveside > 63 or queen_ == side[moveside] or king_ == side[moveside]:
            print(check[1])
            continue
        legal = calculate_legal()
        if side[moveside] not in legal:
            print(check[1])
            continue
        kinglegal = [[king_[0]+1 , king_[1]] , [king_[0]-1 , king_[1]] , [king_[0] , king_[1]+1] , [king_[0] , king_[1]-1]]
        valid = True
        for x in kinglegal:
            if 0 <= x[0] < 8 and 0 <= x[1] < 8:
                if x in legal and x == side[moveside]:
                    valid = False
                    break
        if not valid:
            print(check[2])
            continue
        queen_ = side[moveside]
        valid = True
        legal = []
        for x in range(8):
            legal.append([x , queen_[1]])
            legal.append([queen_[0] , x])
        for x in kinglegal:
            if 0 <= x[0] < 8 and 0 <= x[1] < 8:
                if x not in legal:
                    valid = False
                    print(check[3])
                    break
        if valid:
            print(check[4])
            continue
    except EOFError:
        break