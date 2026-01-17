def a(arr):
	if arr[-1] == 0 and arr[-2] == 0:
		arr.pop()
		arr.pop()
		i = 0
		carry = 0
		while i < len(arr):
			arr[i] = arr[i] + carry * 10
			carry = arr[i] % 4
			arr[i] //= 4
			i += 1
		if carry != 0:
			return False
		else:
			return True
	else:
		i = 0
		carry = 0
		while i < len(arr):
			arr[i] = arr[i] + carry * 10
			carry = arr[i] % 4
			arr[i] //= 4
			i += 1
		if carry != 0:
			return False
		else:
			return True
def b(arr):
	i = 0
	carry = 0
	while i < len(arr):
		arr[i] = arr[i] + carry * 10
		carry = arr[i] % 3
		arr[i] //= 3
		i += 1
	if carry != 0:
		return False
	i = 0
	carry = 0
	while i < len(arr):
		arr[i] = arr[i] + carry * 10
		carry = arr[i] % 5
		arr[i] //= 5
		i += 1
	if carry != 0:
		return False
	else:
		return True
def c(arr):
	i = 0
	carry = 0
	while i < len(arr):
		arr[i] = arr[i] + carry * 10
		carry = arr[i] % 5
		arr[i] //= 5
		i += 1
	if carry != 0:
		return False
	i = 0
	carry = 0
	while i < len(arr):
		arr[i] = arr[i] + carry * 10
		carry = arr[i] % 11
		arr[i] //= 11
		i += 1
	if carry != 0:
		return False
	else:
		return True
now = 0
while True:
	try:
		from copy import deepcopy 
		n = input()
		nrr = []
		for i in range(len(n)):
			nrr.append(int(n[i]))
		arr = deepcopy(nrr)
		count = 0
		valid = False
		if a(arr):
			valid = True
			count += 1
			print("This is leap year.")
		arr = deepcopy(nrr)
		if b(arr):
			count += 1
			print("This is huluculu festival year.")
		arr = deepcopy(nrr)
		if valid:
			if c(arr):
				count += 1
				print("This is bulukulu festival year.")
		if count == 0:
			print("This is an ordinary year.")
		print()
	except EOFError:
		break
