def sameout(x , X):
	if len(x) == 0:
		print(f"{X}=>" , end="")	
	else:
		print(f"{X}=>  " , end="")
	for i in range(len(x)):
		print(' ' , end="")
		print(x[i] , end="")
	print()
def out(a , b , c):
	sameout(a , 'A')		
	sameout(b , 'B')		
	sameout(c , 'C')
	print()
def move(all , A , B , C):
	temp = all[A].pop()
	all[C].append(temp)
	out(all['A'] , all['B'] , all['C'])
def dfs(l , ans , all , A , B , C):
	global count
	if l == 1:
		if count + 1 > ans:
			return
		move(all , A , B , C)
		count += 1
		return
	if ans <= count:
		return
	dfs(l-1 , ans , all , A , C , B)
	if count + 1 > ans:return
	move(all , A , B , C)
	count += 1
	dfs(l-1 , ans , all , B , A , C)
now = 0
while True:
	now += 1
	l , ans = map(int , input().split())
	if l == 0 and ans == 0:break
	print(f"Problem #{now}")
	print()
	all = {'A':[] , 'B':[] , 'C':[]}
	for i in range(l , 0 , -1):
		all['A'].append(i)
	out(all['A'] , all['B'] , all['C'])
	count = 0
	dfs(l , ans , all ,  'A' , 'B' , 'C')
