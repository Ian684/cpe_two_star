def cal(arr , brr):
        global valid
        result = [0]*(len(arr)+len(brr))
        for a in range(len(arr)):
                for b in range(len(brr)):
                        result[a + b] += arr[a]*brr[b]
        for k in range(len(arr)+len(brr)-1):
                if result[k] // 10 >= 1:
                        result[k + 1] += result[k] // 10
                        result[k] %= 10
        while result[0] == 0 and valid:
                result = result[1:]
        return result
while True:
        try:
                r , n = input().split()
                n = int(n)
                idx = 0
                left = True
                valid = True
                for i in range(5 , -1 , -1):
                        if r[i] == '0':
                                r = r[:i]
                        elif r[i] == '.':break
                        else:break
                if r[0] == '0':
                        left = False
                        r = r[1:]
                if len(r[r.index('.')+1:]) == 0:
                        valid = False
                for i in range(len(r)-1 , -1 , -1):
                        if r[i] == '.':
                                idx = n*(len(r) - 1 - i) - 1
                                break
                r = r.replace('.' , '')
                arr = []
                brr = []
                for i in range(len(r)-1 , -1 , -1):
                        arr.append(int(r[i]))
                        brr.append(int(r[i]))
                for i in range(n-1):
                        brr = cal(arr , brr)
                if not left:
                        print('.',end="")
                        for i in brr[::-1]:
                                print(i , end="")
                else:
                        while brr[len(brr)-1] == 0:
                                brr = brr[:len(brr)-1]
                        for i in range(len(brr)-1 , idx , -1):
                                print(brr[i] , end="")
                        if idx >= 0:
                            print('.' , end="")
                        for i in range(idx , -1 , -1):
                                try:
                                        print(brr[i] , end="")
                                except:
                                        break
                print()
        except EOFError:
                break