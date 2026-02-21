def inset(screen , row , column , x , mode):
    if mode > -1:
        if mode == 0:
            screen[row].insert(column , x)
        elif mode == 1:
            screen[row][column] = x
        if column < 9:
            column += 1
    return [screen , row , column]
now = 0
while True:
    now += 1
    n = int(input())
    if n == 0:break
    print(f"Case {now}")
    mode = 1
    row = 0
    column = 0
    screen = [[' ']*10 for _ in range(10)]
    for i in range(n):
        t = input()
        j = 0
        while j < len(t):
            if t[j] == "^":
                j += 1
                if t[j] == 'b':
                    column = 0
                elif t[j] == 'c':
                    screen = [[' ']*10 for _ in range(10)]
                elif t[j] == 'd':
                    if row < 9:
                        row += 1
                elif t[j] == 'e':
                    screen[row] = screen[row][:column] + ' '*(10-column)
                elif t[j] == 'h':
                    row = 0
                    column = 0
                elif t[j] == 'i':
                    mode = 0
                elif t[j] == 'l':
                    if column > 0:
                        column -= 1
                elif t[j] == 'o':
                    mode = 1
                elif t[j] == 'r':
                    if column < 9:
                        column += 1
                elif t[j] == 'u':
                    if row > 0:
                        row -= 1
                elif t[j] == '^':
                    screen , row , column = inset(screen , row , column , t[j] , mode)
                else:
                    if len(t[j:len(t)]) >= 2:
                        row = int(t[j])
                        j += 1
                        column = int(t[j])
            else:
                screen , row , column = inset(screen , row , column , t[j] , mode)
            j += 1
    print("+----------+")
    for r in range(10):
        print('|' , end="")
        for c in range(10):
            print(screen[r][c] , end="")
        print('|')
    print("+----------+")
            
