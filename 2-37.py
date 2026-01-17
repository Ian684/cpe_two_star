def search(mid):
	global arr , t
	all = 0
	for d , s in arr:
		if s+mid <= 0:return 0
		all += d/(s+mid)
	if all <= t:return 1
	else:return 0
while True:
	try:
		n , t = map(int , input().split())
		arr = []
		for i in range(n):
			arr.append(list(map(int , input().split())))
		r = 20000000
		l = -20000000
		for _ in range(200):
			mid = (l+r)/2
			if search(mid):
				r = mid
			else:
				l = mid
		print(f"{r:.9f}")
	except EOFError:
		break
