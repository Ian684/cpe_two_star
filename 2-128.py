def main():
    while True:
        try:
            m = input()
            if m == "":continue
            m = int(m)
            if m <= 0:continue
            numbers = []
            while len(numbers) < m:
                line = input().split()
                for l in line:
                    numbers.append(int(l))
        except EOFError:break
        c = 0
        for i in range(m):
            for j in range(i + 1, m):
                if numbers[i] > numbers[j]:
                    c += 1
        print(f"Minimum exchange operations : {c}")
if __name__ == "__main__":
    main()
