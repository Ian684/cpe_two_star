def cal(d , i):
        sum = 0
        for a in range(d):
                sum += 2**a
        arr = [0]*sum
        result = []
        for _ in range(2**(d-1)):
                current = 0
                for b in range(d-1):
                        if arr[current] == 0:
                                arr[current] = 1
                                current = current*2 + 1
                        else:
                                arr[current] = 0
                                current = current*2 + 2
                result.append(current)
        return result[i%(2**(d-1))-1]
num= int(input())
for i in range(num):
        d , i = map(int , input().split())
        print(cal(d , i)+1)
end = int(input())