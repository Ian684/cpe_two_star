# while會超時
def cal1(b , p  , m):
	if b % m == 0:
		return 0
	if p == 0:
		b = 1
	more = 1
	b %= m
	while True:
		if p == 1:
			return ((b*more) % m)
		if p % 2 == 0:
			p //= 2
		else:
			p //= 2	
			more = (more * b) % m
		b = (b * b) % m
# 遞迴不會超時，
def cal(b , p , m):
    if p == 0:
        return 1 % m
    elif p == 1:
        return b % m
    elif p % 2 == 0:
        temp = cal(b , p//2 , m)%m
        return (temp * temp) % m
    else:
        temp = cal(b , p//2 , m)%m
        return (temp * temp *(b % m)) % m
while True:
	try:
		b = int(input())
		p = int(input())
		m = int(input())
		print(cal(b , p , m))
		trash = input()
	except EOFError:
		break
