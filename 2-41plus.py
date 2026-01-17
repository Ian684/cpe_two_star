arr = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973]
while True:
    num = int(input())
    if num == 0:break
    if num in arr:
        print(f"The number {num} is a Carmichael number.")
    else:
        print(f"{num} is normal.")