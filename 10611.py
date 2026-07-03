import sys

def find(aim, arr):
    n = len(arr)
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= aim:
            right = mid
        else:
            left = mid + 1
    shorter = arr[left - 1] if left > 0 else 'X'
    
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > aim:
            right = mid
        else:
            left = mid + 1
    taller = arr[left] if left < n else 'X'
    return shorter, taller

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    q = int(input_data[n+1])
    queries = [int(x) for x in input_data[n+2:n+2+q]]
    for aim in queries:
        a, b = find(aim, arr)
        print(a, b)

if __name__ == "__main__":
    main()
