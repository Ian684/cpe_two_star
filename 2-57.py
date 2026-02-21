import sys

tokens = sys.stdin.read().split()
t_idx = 0

while t_idx < len(tokens):
    try:
        n = int(float(tokens[t_idx]))
        t_idx += 1
        
        if n <= 0:
            print("-1")
            continue
            
        arr = []
        for _ in range(n):
            arr.append(float(tokens[t_idx]))
            t_idx += 1
        
        s1 = sum(arr) / n
        
        arr.sort()
        s2 = arr[(len(arr) + 1) // 2 - 1]
        
        print(f"{s1:.2f} {s2:.2f}")
        
    except (EOFError, IndexError):
        break
