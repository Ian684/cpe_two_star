import sys
import bisect

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    heights = [int(x) for x in input_data[1:N+1]]
    
    Q = int(input_data[N+1])
    queries = [int(x) for x in input_data[N+2:N+2+Q]]
    
    results = []
    for q in queries:
        low_idx = bisect.bisect_left(heights, q)
        shorter = str(heights[low_idx - 1]) if low_idx > 0 else 'X'
        high_idx = bisect.bisect_right(heights, q)
        taller = str(heights[high_idx]) if high_idx < N else 'X'
        results.append(f"{shorter} {taller}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
