num = int(input())
print("INTERSECTING LINES OUTPUT")
for i in range(num):
    arr = list(map(int , input().split()))
    if arr[0]-arr[2] == 0 and arr[4]-arr[6] == 0:
        if arr[0] == arr[4]:
            print("LINE")
        else:
            print("NONE")
    elif arr[0]-arr[2] == 0:
        a2 = (arr[5]-arr[7])/(arr[4]-arr[6])
        b2 = arr[5] - a2*arr[4]
        ansx = arr[0]
        ansy = a2*ansx + b2
        print(f"POINT {ansx:.2f} {ansy:.2f}")
    elif arr[4]-arr[6] == 0:
        a1 = (arr[1]-arr[3])/(arr[0]-arr[2])
        b1 = arr[1] - a1*arr[0]
        ansx = arr[4]
        ansy = a1*ansx + b1
        print(f"POINT {ansx:.2f} {ansy:.2f}")
    else:
        a1 = (arr[1]-arr[3])/(arr[0]-arr[2])
        b1 = arr[1] - a1*arr[0]
        a2 = (arr[5]-arr[7])/(arr[4]-arr[6])
        b2 = arr[5] - a2*arr[4]
        if a1 == a2:
            if b1 == b2:
                print("LINE")
            else:
                print("NONE")
        else:
            ansx = (b1 - b2)/(a2 - a1)
            ansy = a1*ansx + b1
            print(f"POINT {ansx:.2f} {ansy:.2f}")
print("END OF OUTPUT")