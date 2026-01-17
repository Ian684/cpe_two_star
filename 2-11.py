while True:
        num = int(input())
        if num == 0:break
        while True:
                arr = input()
                if arr == "0":
                        print()
                        break
                arr = list(map(int , arr.split()))
                station = []
                valid = True
                current = 1
                for a in arr:
                        while True:
                                if len(station) != 0 and station[-1] == a:
                                        station.pop()
                                        break
                                elif current > len(arr):
                                        valid = False
                                        break
                                station.append(current)
                                current += 1
                        if not valid:break
                if valid:
                        print("Yes")
                else:
                        print("No")