arr = []
arr.append(0)
arr.append(1)
arr.append(2)
for i in range(3 , 51):
        arr.append(arr[i-1] + arr[i-2])
while True:
        num = int(input())
        if num == 0:break
        print(arr[num])