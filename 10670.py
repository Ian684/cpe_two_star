def main():

    t = int(input())
    for c in range(t):
        main_start , end , q = map(int , input().split())
        ans = []
        for i in range(q):
            start = main_start
            agency , line = input().split(":")
            one , half = map(int , line.split(","))
            cost = 0
            while int(start) > end:
                if half > one * (start - start // 2):
                    break
                if start / 2 < end:
                    break
                cost += half
                start /= 2
            cost += one * (int(start) - end)

            ans.append([agency , cost])


        print(f"Case {c+1}")
        for k , v in sorted(ans , key = lambda x : (x[1] , x[0])):
            print(k , v)

if __name__ == "__main__":
    main()
