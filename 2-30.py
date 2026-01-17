num = int(input())
for i in range(num):
	aim = int(input())
	if aim == 0:
		print(0)
		continue
	if aim == 1:
		print(1)
		continue
	d = 9
	arr = []
	while d != 1:
		if aim % d == 0:
			arr.append(str(d))
			aim //= d
		else:
			d -= 1
	if aim == 1:
		print(''.join(sorted(arr)))
	else:
		print(-1)
		
