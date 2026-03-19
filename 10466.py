from math import *
def main():
    while True:
        try:
            n , T = map(int , input().split())
        except EOFError:break
        ans = [[0 , 0 , 0]]
        for i in range(n):
            r , t = map(int , input().split())
            cita = (T % t / t) * 2 * pi
            deltax = r * max(-1.0 , min(1.0 , cos(cita)))
            deltay = r * max(-1.0 , min(1.0 , sin(cita)))
            deltax += ans[-1][0]
            deltay += ans[-1][1]
            ans.append([deltax , deltay , sqrt(deltax**2+deltay**2)])
        print(f"{ans[1][2]:.4f}" , end="")
        for a in ans[2:]:
            print(f" {a[2]:.4f}" , end="")
        print()
if __name__ == "__main__":
    main()
