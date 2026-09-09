from math import log

def main():
    t = int(input())
    for _ in range(t):
        n , x = map(int , input().split())
        if x == 0:
            print(1 , 1)
            continue
        total = 2 ** n
        left , right = 1 , total
        tx = x
        count = 0
        while not (tx & 1):
            tx //= 2
            right -= 2 ** count
            count += 1
        for i in range(n):
            if x & 1:
                left += 1
            x //= 2
        print(left , right)

if __name__ == "__main__":
    main()
