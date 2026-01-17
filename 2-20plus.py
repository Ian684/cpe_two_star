import sys
def cal(d , i):
        current = 1
        for _ in range(d-1):
                if i & 2:
                        current <<= 1
                        i = (i + 1) >> 1
                else:
                        current = (current << 1) | 1
                        i >>= 1
        return current
data = list(map(int , sys.stdin.read().split()))
num = data[0]
index = 1
for _ in range(num):
        d , i = data[index:index+2]
        index += 2
        sys.stdout.write(str(cal(d , i)) + "\n")