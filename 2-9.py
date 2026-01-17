import math
prime = [True]*(1001)
prime[0] = prime[1] = False
for i in range(int(math.sqrt(1001))+1):
        if prime[i]:
                for j in range(i*i , 1001 , i):
                        prime[j] = False
arr = [1]
for i , p in enumerate(prime):
        if p:
                arr.append(i)
while True:
        try:
                n , c = map(int , input().split())
                print(f"{n} {c}:" , end="")
                count = 0
                for i in range(len(arr)):
                        if n < arr[i]:
                                break
                        count += 1
                if count % 2 == 0:
                        for i in range(count//2 - c , count//2 + c):
                                if i >= count or i < 0:
                                        continue
                                print(f" {arr[i]}" , end="")
                else:
                        for i in range(count//2 - c + 1 , count//2 + c):
                                if i >= count or i < 0:
                                        continue
                                print(f" {arr[i]}" , end="")
                print()
                print()
        except EOFError:
                break