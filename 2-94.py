#搞那個特殊字元搞超久...
import sys
sys.stdout.reconfigure(encoding='latin-1')

number = {"ar":['o', 'as', 'a', 'amos', 'ais', 'am'],
          "er":['o', 'es', 'e', 'emos', 'eis', 'em'],
          "ir":['o', 'es', 'e', 'imos', 'is', 'em']}

first = True
while True:
    try:
        n, m = input().split()
    except EOFError:
        break
    
    if not first:
        print()
    first = False
    
    print(f"{n} (to {m})")
    con = n[-2:]
    
    if con not in number:
        print("Unknown conjugation")
        continue
    
    root = n[:-2]
    temp = number[con]
    
    print(f"{'eu':<10}{root+temp[0]}")
    print(f"{'tu':<10}{root+temp[1]}")
    print(f"{'ele/ela':<10}{root+temp[2]}")
    print(f"{'n'+chr(243)+'s':<10}{root+temp[3]}")
    print(f"{'v'+chr(243)+'s':<10}{root+temp[4]}")
    print(f"{'eles/elas':<10}{root+temp[5]}")
