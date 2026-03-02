def number():
    numbers = set()
    for i in range(1 , 9):
        numbers.add(str(i))
    return numbers
numbers = number()
def generate_chess(line):
    global numbers
    chess = {}
    hinders = set()
    x = 0
    for l in line:
        y = 0
        for i in l:
            if i not in numbers:
                if i not in chess:
                    chess[i] = []
                chess[i].append([x , y])
                hinders.add((x , y))
                y += 1
                continue
            y += int(i)
        x += 1
    return chess , hinders
def check_margin(nx , ny):
    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
        return False
    return True
def cal1(x , y , check , chess , hinders):
    for dx in range(1 , 8):
        nx , ny = x + dx , y
        if not check_margin(nx , ny):
            break
        if (nx , ny) in hinders:break
        if check[nx][ny]:
            continue
        check[nx][ny] = True
    for dx in range(-1 , -8 , -1):
        nx , ny = x + dx , y
        if not check_margin(nx , ny):
            break
        if (nx , ny) in hinders:break
        if check[nx][ny]:
            continue
        check[nx][ny] = True
    for dy in range(1 , 8):
        nx , ny = x , y + dy
        if not check_margin(nx , ny):
            continue
        if (nx , ny) in hinders:break
        if check[nx][ny]:
            continue
        check[nx][ny] = True
    for dy in range(-1 , -8 , -1):
        nx , ny = x , y + dy
        if not check_margin(nx , ny):
            break
        if (nx , ny) in hinders:break
        if check[nx][ny]:
            continue
        check[nx][ny] = True
    return check
def cal2(x , y , check , chess , hinders):
    for d in range(1 , 8):
        nx , ny = x + d , y + d
        if not check_margin(nx , ny):
            break
        if (nx , ny) in hinders:break
        if check[nx][ny]:
            continue
        check[nx][ny] = True
    for d in range(-1 , -8 , -1):
        nx , ny = x + d , y + d
        if not check_margin(nx , ny):
            break
        if (nx , ny) in hinders:break
        if check[nx][ny]:
            continue
        check[nx][ny] = True
    for d in range(1 , 8):
        nx , ny = x + d , y - d
        if not check_margin(nx , ny):
            break
        if (nx , ny) in hinders:break
        if check[nx][ny]:
            continue
        check[nx][ny] = True
    for d in range(-1 , -8 , -1):
        nx , ny = x + d , y - d
        if not check_margin(nx , ny):
            break
        if (nx , ny) in hinders:break
        if check[nx][ny]:
            continue
        check[nx][ny] = True
    return check
def solve(chess , hinders):
    check = [[False]*8 for _ in range(8)]
    for k , v in chess.items():
        for x , y in v:
            if not check[x][y]:check[x][y] = True
            if k.lower() == 'k':
                for dx in range(-1 , 2):
                    for dy in range(-1 , 2):
                        nx , ny = x + dx , y + dy
                        if not check_margin(nx , ny):
                            continue
                        if check[nx][ny]:
                            continue
                        check[nx][ny] = True
            elif k.lower() == 'r':
                check = cal1(x , y , check , chess , hinders)
            elif k.lower() == 'b':
                check = cal2(x , y , check , chess , hinders)
            elif k.lower() == 'q':
                check = cal1(x , y , check , chess , hinders)
                check = cal2(x , y , check , chess , hinders)
            elif k.lower() == 'n':
                for dx , dy in ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-2,-1),(-1,-2)):
                    nx , ny = x + dx , y + dy
                    if not check_margin(nx , ny):
                        continue
                    if check[nx][ny]:
                        continue
                    check[nx][ny] = True
            elif k == 'P':
                for dy in (-1,1):
                    nx , ny = x - 1 , y + dy
                    if not check_margin(nx , ny):
                        continue
                    if check[nx][ny]:
                        continue
                    check[nx][ny] = True
            elif k == 'p':
                for dy in (-1,1):
                    nx , ny = x + 1 , y + dy
                    if not check_margin(nx , ny):
                        continue
                    if check[nx][ny]:
                        continue
                    check[nx][ny] = True
    return check
def main():
    while True:
        try:
            line = input().split('/')
        except EOFError:break
        chess , hinders= generate_chess(line)
        check = solve(chess , hinders)
        c = 0
        for i in range(8):
            for j in range(8):
                if check[i][j]:continue
                c += 1
        print(c)
if __name__ == "__main__":
    main()
