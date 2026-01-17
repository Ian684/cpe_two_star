def cal(gg):
        result = 0
        current = 0
        for current in range(len(gg)):
                for c in range(current+1,len(gg)):
                        if gg[current] > gg[c]:
                                result += 1
        return result
num = int(input())
for i in range(num):
        trash = input()
        n , m = map(int , input().split())
        arr = {}
        for j in range(m):
                temp = input()
                arr[j] = [temp , cal(temp)]
        arr = sorted(arr.items() , key=lambda x:(x[1][1] , x[0]))
        for a , b in arr:
                print(b[0])
        if i != num - 1:
            print()