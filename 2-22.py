while True:
	m , n = map(int , input().split())
	b = max(m , n)
	a = min(m , n)
	if a == 0 and b == 0:
		break
	ans = 0
	if a == 1:
		ans += b
	elif a == 2:
		ans += (b // 4)*4
		b %= 4
		if b == 1:
			ans += 2
		elif 2 <= b <= 3:
			ans += 4
	else:
		ans += (a*b)//2 + (a*b)%2
	print(f"{ans} knights may be placed on a {m} row {n} column board.")
		
