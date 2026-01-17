num = int(input())
for i in range(num):
	trash = input()
	m = int(input())
	arr = []
	current = 0
	for j in range(m):
		a , b = map(int , input().split())
		temp = a + b
		if temp >= 10:
			temp %= 10
			d = current
			while d > 0:
				arr[d - 1] += 1
				if arr[d-1] < 10:
					break
				arr[d-1] %= 10
				d -= 1
		arr.append(temp)
		current += 1
	for j in arr:
		print(j , end="")
	if i != num - 1:print()
# 全部讀完再進位
# import sys
# sys.stdin.readline()
# sys.stdin.read()
# sys.stdin.readlines()
# sys.stdout.write()