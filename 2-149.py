def main():
    i = 1
    count = 1
    now = 0
    arr = []
    while now < 100000000:
        arr.append([now+1 , 9*i , count])
        now += 9*i*count
        i *= 10
        count += 1
    while True:
        try:
            n = int(input())
        except EOFError:break
        for i in range(1 , len(arr)):
            if arr[i][0] > n:
                start = arr[i-1][0]
                quantity = arr[i-1][1]
                count = arr[i-1][2]
                break
        t1 = str((n - start) // count + 10**(count-1))
        t2 = (n - start) % count 
        print(t1[t2])
if __name__ == "__main__":
    main()
