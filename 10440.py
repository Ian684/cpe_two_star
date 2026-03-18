def main():
    c = int(input())
    for _ in range(c):
        n , t , m = map(int , input().split())
        cars = []
        for i in range(m):
            cars.append(int(input()))
        cars = sorted(cars)
        remain = m % n
        if remain == 0:
            ans = 0
            ans2 = m//n
        else:
            ans = cars[remain-1] + 2 * t
            ans2 = m//n + 1
        for i in range(remain , m , n):
            bigest = cars[i+n-1]
            if bigest > ans:
                ans = bigest + t * 2
            else:
                ans += t * 2
        print(ans-t , ans2)
if __name__ == "__main__":
    main()
