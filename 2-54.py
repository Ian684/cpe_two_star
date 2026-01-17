import math
def cal(a):
	t1 = a.pop(0)
	s1 = 0
	s2 = 0
	for i in range(0 , len(a)-2 , 2):
		s1 += a[i]*a[i+3]
	for i in range(1 , len(a)-1 , 2):
		s2 += a[i]*a[i+1]
	return (abs(s1-s2)/2)*t1
while True:
	num = int(input())
	if num == 0:break
	arr = []
	for i in range(num):
		temp = input().split()
		arr.append(list(map(float , temp)))
	r , t = map(float , input().split())
	area = t * (r**2) * math.pi
	total = 0
	for a in arr:
		total += cal(a)
	print(int(total//area))
