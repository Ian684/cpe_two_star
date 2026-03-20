def generate():
    arr = [0 , 0 , 1]
    for i in range(3 , 801):
        arr.append((i-1)*(arr[i-1]+arr[i-2]))
    return arr
def main():
    arr = generate()
    while True:
        n = int(input())
        if n == -1:break
        print(arr[n])
if __name__ == "__main__":
    main()
