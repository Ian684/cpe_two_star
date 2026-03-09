def generatefac():
    numbers = [[1],[1]]
    for i in range(2 , 21):
        t = numbers[i-1][:]
        posi = 0
        carry = 0
        while True:
            if posi >= len(t):
                if carry == 0:
                    break
                t.append(0)
            t[posi] *= i
            t[posi] += carry
            carry = t[posi] // 10
            t[posi] %= 10
            posi += 1
        numbers.append(t)
    return numbers
def divide(ans , divisor):
    now = 0
    for div in divisor:
        flag = True
        i = now
        carry = 0
        while i < len(ans):
            ans[i] += carry * 10  
            carry = ans[i] % div
            ans[i] //= div
            if flag and ans[i] != 0:
                flag = False
            if ans[i] == 0 and flag:
                ans[i] = -1
                now = i+1
            i += 1
    if carry == 0:
        return ans
    return "???"
def main():
    numbers = generatefac()
    n = int(input())
    for i in range(1 , n + 1):
        text = input()
        c = {}
        divisor = []
        for t in text:
            if t not in c:
                c[t] = 0
            c[t] += 1
            if c[t] != 1:
                divisor.append(c[t])
        ans = numbers[len(text)]
        ans = divide(ans[::-1] , divisor)
        print(f"Data set {i}: " , end="")
        for a in ans:
            if a == -1:continue
            print(a , end="")
        print()
if __name__ == "__main__":
    main()
