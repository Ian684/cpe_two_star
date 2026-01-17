num = int(input())
dir = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
for i in range(num):
	trash = input()
	x , y = map(int , input().split())
	arr = []
	for j in range(x):
		arr.append(input().lower())
	q = int(input())
	for j in range(q):
		aim = input().lower()
		valid = False
		for a in range(x):
			for b in range(y):
				if aim[0] != arr[a][b]:
					continue
				for dx , dy in dir:
					valid = True
					na , nb = a , b
					for l in range(1 , len(aim)):
						na , nb = na + dx , nb + dy
						if na < 0 or nb < 0 or na >= x or nb >= y:
							valid = False
							break
						if aim[l] != arr[na][nb]:
							valid = False
							break
					if valid:
						print(a+1 , b+1)
						break
				if valid:break
			if valid:break
	if i != num - 1:
		print()
