import math
while True:
	try:
		num = input().split()
		if int(num[0]) < 3:break
		arr = []
		if len(num) == 1:
			num = int(num[0])
			for i in range(num):
				arr.append(list(map(float , input().split())))
		else:
			idx = 1
			while idx < len(num):
				arr.append([float(num[idx]) , float(num[idx+1])])
				idx += 2
	except:
		continue
	center = [0 , 0]
	for i , j in arr:
		center[0] += i	
		center[1] += j
	center[0] /= len(arr)
	center[1] /= len(arr)
	for i in range(len(arr)):
		arr[i].append(math.atan2((arr[i][1]-center[1]),(arr[i][0]-center[0])))
	arr = sorted(arr , key = lambda x: x[2])
	all = []
	first = arr[0]
	for i in range(1 , len(arr)-1):
		all.append([[arr[i][0],arr[i][1]],[arr[i+1][0],arr[i+1][1]]])	
	ans = []
	total = 0
	for i , j in all:
		a = math.sqrt((i[0]-j[0])**2+(i[1]-j[1])**2)
		b = math.sqrt((first[0]-j[0])**2+(first[1]-j[1])**2)
		c = math.sqrt((i[0]-first[0])**2+(i[1]-first[1])**2)
		s = (a+b+c)/2
		temp2 = s*(s-a)*(s-b)*(s-c)
		if temp2 < 0:
			temp2 = 0
		temp2 = math.sqrt(temp2)
		total += temp2
		ans.append([[(first[0]+i[0]+j[0])/3,(first[1]+i[1]+j[1])/3],temp2])
	ans1 , ans2 = 0 , 0
	for k , v in ans:
		ans1 += (k[0]*(v/total))
		ans2 += (k[1]*(v/total))
	print(f"{ans1:.3f} {ans2:.3f}")
