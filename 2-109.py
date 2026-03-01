from collections import deque
def fill(m , n , picture , x , y ,c):
    x , y = x - 1 , y - 1
    center = picture[y][x]
    q = deque([[x , y]])
    direction = ((1,0),(-1,0),(0,1),(0,-1))
    check = [[False]*m for _ in range(n)]
    check[y][x] = True
    while q:
        x , y = q.popleft()
        picture[y][x] = c
        for dx , dy in direction:
            nx , ny = x + dx , y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:continue
            if check[ny][nx]:continue
            if picture[ny][nx] == center:
                check[ny][nx] = True
                q.append([nx , ny])
    return picture
while True:
    try:
        line = input().split()
    except EOFError:break
    command , line = line[0] , line[1:]
    if command == "X":break
    elif command == "I":
        m , n = map(int , line)
        picture = [["O"]*m for _ in range(n)]
    elif command == "C":
        picture = [["O"]*m for _ in range(n)]
    elif command == "L":
        x , y = map(int , line[:2])
        c = line[2]
        picture[y-1][x-1] = c
    elif command == "V":
        x , y1 , y2 = map(int , line[:3])
        y1 , y2 = min(y1 , y2) , max(y1 , y2)
        c = line[3]
        for i in range(y1-1 , y2):
            picture[i][x-1] = c
    elif command == "H":
        x1 , x2 , y = map(int , line[:3])
        x1 , x2 = min(x1 , x2) , max(x1 , x2)
        c = line[3]
        picture[y-1] = picture[y-1][:x1-1] + [c]*(x2-x1+1) + picture[y-1][x2:]
    elif command == "K":
        x1 , y1 , x2 , y2 = map(int , line[:4])
        x1 , x2 = min(x1 , x2) , max(x1 , x2)
        y1 , y2 = min(y1 , y2) , max(y1 , y2)
        c = line[4]
        for j in range(y1-1 , y2):
            picture[j] = picture[j][:x1-1] + [c]*(x2-x1+1) + picture[j][x2:]
    elif command == "F":
        x , y = map(int , line[:2])
        c = line[2]
        picture = fill(m , n , picture , x , y , c)
    elif command == "S":
        name = line[0]
        print(name)
        for i in range(n):
            print(''.join(picture[i]))
    else:continue
