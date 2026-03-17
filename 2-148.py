from math import gcd
def main():
    while True:
        try:
            n , aim = map(int , input().split())
        except EOFError:break
        arr = []
        for i in range(1 , n+1):
            for j in range(i , n+1):
                if gcd(i , j) == 1:
                    arr.append([i/j,i,j])
        arr = sorted(arr)
        print(f"{arr[aim-1][1]}/{arr[aim-1][2]}")
if __name__ == "__main__":
    main()
