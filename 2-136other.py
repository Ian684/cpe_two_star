import sys
from itertools import permutations

def solve():
    input_data = sys.stdin.read().splitlines()
    for line in input_data:
        nums = list(map(int, line.split()))
        if not any(nums):
            break
        found = False
        for p in permutations(nums):
            if dfs(p, 1, p[0]):
                found = True
                break
        print("Possible" if found else "Impossible")
def dfs(p, index, current_ans):
    if index == 5:
        return current_ans == 23
    next_num = p[index]
    if dfs(p, index + 1, current_ans + next_num): return True
    if dfs(p, index + 1, current_ans - next_num): return True
    if dfs(p, index + 1, current_ans * next_num): return True
    return False
if __name__ == "__main__":
    solve()
