number = ['0','1','2','3','4','5','6','7','8','9']
while True:
	try:
		text , num = input().split()
		num = int(num)
		current = 0
		left = 0
		right = 0
		arr = [-1]*num
		srr = [-1]*num
		while True:
			if len(text) == 0:break
			if text[current] == '[':
				left = current
			elif text[current] == ']':
				right = current
				current = -1
				if '+' in text[left:right+1]:
					c = int(text[left+1:right-1])
					srr[0] = c
					for i in range(1 , num):
						srr[i] = arr[i-1] + srr[i-1]
					arr = srr[:]
					srr = [-1]*num
				elif '*' in text[left:right+1]:
					c = int(text[left+1:right-1])
					srr[0] = c * arr[0]
					for i in range(1 , num):	
						srr[i] = srr[i-1] * arr[i]
					arr = srr[:]
					srr = [-1]*num
				else:
					for i in range(num):
						arr[i] = int(text[left+1:right])
				text = text[:left] + text[right+1:]
			current += 1
		print(' '.join(map(str , arr)))
	except EOFError:
		break
