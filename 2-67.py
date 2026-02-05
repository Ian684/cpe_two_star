from math import sqrt
while True:
    n = int(input())
    if n == 0:break
    if int(sqrt(n))**2 == n:
        print("yes")
    else:
        print("no")

    #flag = 0
    #for i in range(1 , int(sqrt(n)) +4):
     #   if n % i == 0:
      #      print(i)
       #     flag += 1
    #if flag & 1:
     #   print("yes")
    #else:
     #   print("no")
