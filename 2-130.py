def generate():
    arr = [0]*1003
    arr[0] = 1
    arr[1] = 2
    arr[2] = 3
    for i in range(3 , 1003):
        arr[i] = arr[i-1] + arr[i-2]
    return arr
def main():
    arr = generate()
    while True:
        try:
            n = int(input())
        except EOFError:break
        print(arr[n])
if __name__ == "__main__":
    main()
