n = int(input())
for i in range(n):
    m = int(input())
    arr = []
    brr = []
    for j in range(m):
        arr.append(input())
    for j in range(m):
        brr.append(input())
    i , j = m - 1 , m - 1
    while i >= 0 and j >= 0:
        if arr[i] == brr[j]:
            i -= 1
            j -= 1
        else:
            i -= 1
    for j in range(j , -1 , -1):
        print(brr[j])
    if i != n - 1:print()
