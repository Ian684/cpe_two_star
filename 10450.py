def generate():
    arr = [2 , 3]
    for i in range(2 , 51):
        arr.append(arr[i-1]+arr[i-2])
    return arr
def main():
    arr = generate()
    n = int(input())
    for i in range(1 , n + 1):
        aim = int(input())
        print(f"Scenario #{i}:")
        print(arr[aim-1])
        print()
if __name__ == "__main__":
    main()
