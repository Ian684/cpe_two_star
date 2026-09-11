import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0

    while idx < len(data):
        n = data[idx]
        idx += 1

        if n == 0:
            break

        nums = data[idx:idx+n]
        idx += n

        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])

        ans = max(dp)

        if ans <= 0:
            print("Losing streak.")
        else:
            print(f"The maximum winning streak is {ans}.")

if __name__ == "__main__":
    main()
