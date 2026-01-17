arr = [0 , 1]
for i in range(2 , 5001):
        arr.append(arr[i-1]+arr[i-2])
while True:
        try:
                n = int(input())
                print(f"The Fibonacci number for {n} is {arr[n]}")
        except EOFError:
                break