while True:
        try:
                arr = input()
                if arr == '':
                        continue
                arr = list(map(float , arr.split()))
                if arr[0] <= 0:
                        print(-1)
                        continue
                n = arr[0]
                arr = arr[1:]
                s1 = sum(arr)/n
                s2 = sorted(arr)[(len(arr)+1)//2-1]
                print(f"{s1:.2f} {s2:.2f}")
        except EOFError:break