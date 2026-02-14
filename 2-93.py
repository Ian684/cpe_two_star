#中間想到可以以國王去判斷....
#但懶得改了..
now = 0
def down(arr , i , j , t , k):
    for u in range(1,9):
        if i + u >= 8:
            return t
        if arr[i+u][j] == k:
            return True
        if arr[i+u][j] != '.':
            return t
def up(arr , i , j , t , k):
    for u in range(1,9):
        if i - u < 0:
            return t
        if arr[i-u][j] == k:
            return True
        if arr[i-u][j] != '.':
            return t
def left(arr , i , j , t , k):
    for u in range(1,9):
        if j - u < 0:
            return t
        if arr[i][j-u] == k:
            return True
        if arr[i][j-u] != '.':
            return t
def right(arr , i , j , t , k):
    for u in range(1,9):
        if j + u >= 8:
            return t
        if arr[i][j+u] == k:
            return True
        if arr[i][j+u] != '.':
            return t
def left_up(arr , i , j , t , k):
    for u in range(1,9):
        if i - u < 0 or j - u < 0:
            return t
        if arr[i-u][j-u] == k:
            return True
        if arr[i-u][j-u] != '.':
            return t
def left_down(arr , i , j , t , k):
    for u in range(1,9):
        if i + u >= 8 or j - u < 0:
            return t
        if arr[i+u][j-u] == k:
            return True
        if arr[i+u][j-u] != '.':
            return t
def right_up(arr , i , j , t , k):
    for u in range(1,9):
        if i - u < 0 or j + u >= 8:
            return t
        if arr[i-u][j+u] == k:
            return True
        if arr[i-u][j+u] != '.':
            return t
def right_down(arr , i , j , t , k):
    for u in range(1,9):
        if i + u >= 8 or j + u >= 8:
            return t
        if arr[i+u][j+u] == k:
            return True
        if arr[i+u][j+u] != '.':
            return t
while True:
    now += 1
    arr = []
    flag = False
    for i in range(8):
        try:
            t = input().strip()
        except EOFError:
            arr = None
            break
        arr.append(t)
        for j in range(8):
            if t[j] != '.':
                flag = True
    if arr is None:break
    if not flag:break
    try:
        trash = input()
    except EOFError:pass
    w = False
    b = False
    for i in range(8):
        for j in range(8):
            if arr[i][j] == 'P':
                if i - 1 >= 0 and j + 1 < 8 and arr[i-1][j+1] == "k":
                    b = True
                if i - 1 >= 0 and j - 1 >= 0 and arr[i-1][j-1] == 'k':
                    b = True
            elif arr[i][j] == 'p':
                if i + 1 < 8 and j + 1 < 8 and arr[i+1][j+1] == "K":
                    w = True
                if i + 1 < 8 and j - 1 >= 0 and arr[i+1][j-1] == "K":
                    w = True
            elif arr[i][j] == 'R':
               b = down(arr , i , j , b , 'k')
               b = up(arr , i , j , b , 'k')
               b = left(arr , i , j , b , 'k')
               b = right(arr , i , j , b , 'k')
            elif arr[i][j] == 'r':
               w = down(arr , i , j , w , 'K')
               w = up(arr , i , j , w , 'K')
               w = left(arr , i , j , w , 'K')
               w = right(arr , i , j , w , 'K')
            elif arr[i][j] == 'B':
               b = left_up(arr , i , j , b , 'k')
               b = left_down(arr , i , j , b , 'k')
               b = right_up(arr , i , j , b , 'k')
               b = right_down(arr , i , j , b , 'k')
            elif arr[i][j] == 'b':
               w = left_up(arr , i , j , w , 'K')
               w = left_down(arr , i , j , w , 'K')
               w = right_up(arr , i , j , w , 'K')
               w = right_down(arr , i , j , w , 'K')
            elif arr[i][j] == 'Q':
               b = left_up(arr , i , j , b , 'k')
               b = left_down(arr , i , j , b , 'k')
               b = right_up(arr , i , j , b , 'k')
               b = right_down(arr , i , j , b , 'k')
               b = down(arr , i , j , b , 'k')
               b = up(arr , i , j , b , 'k')
               b = left(arr , i , j , b , 'k')
               b = right(arr , i , j , b , 'k')
            elif arr[i][j] == 'q':
               w = left_up(arr , i , j , w , 'K')
               w = left_down(arr , i , j , w , 'K')
               w = right_up(arr , i , j , w , 'K')
               w = right_down(arr , i , j , w , 'K')
               w = down(arr , i , j , w , 'K')
               w = up(arr , i , j , w , 'K')
               w = left(arr , i , j , w , 'K')
               w = right(arr , i , j , w , 'K')
            elif arr[i][j] == 'N':
                for u in (-2 , 2):
                    for m in (-1 , 1):
                        if i + u >= 8 or i + u < 0 or j + m >= 8 or j + m < 0:continue
                        if arr[i+u][j+m] == 'k':
                            b = True
                for u in (-1 , 1):
                    for m in (-2 , 2):
                        if i + u >= 8 or i + u < 0 or j + m >= 8 or j + m < 0:continue
                        if arr[i+u][j+m] == 'k':
                            b = True
            elif arr[i][j] == 'n':
                for u in (-2 , 2):
                    for m in (-1 , 1):
                        if i + u >= 8 or i + u < 0 or j + m >= 8 or j + m < 0:continue
                        if arr[i+u][j+m] == 'K':
                            w = True
                for u in (-1 , 1):
                    for m in (-2 , 2):
                        if i + u >= 8 or i + u < 0 or j + m >= 8 or j + m < 0:continue
                        if arr[i+u][j+m] == 'K':
                            w = True

    if w:
        print(f"Game #{now}: white king is in check.")
    elif b:
        print(f"Game #{now}: black king is in check.")
    else:
        print(f"Game #{now}: no king is in check.")
