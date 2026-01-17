arr = [0]
for i in range(1 , 11):
	temp = 1
	for j in range(2*i , i + 1,-1):
		temp *= j
	for j in range(2 , i+1):
		temp //= j
	arr.append(temp)
cal = []
while True:
	try:	
		num = input()
		if num == "":continue
		cal.append(int(num))
	except EOFError:
		break
for i in range(len(cal)):
	print(arr[cal[i]])
	if i != len(cal)-1:
		print()
