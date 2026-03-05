def solve():
    limit = 100000000
    sieve_size = (limit // 2) + 1
    is_prime_odd = bytearray([1]) * sieve_size
    is_prime_odd[0] = 0

    for i in range(3, int(limit**0.5) + 1, 2):
        if is_prime_odd[i // 2]:
            start = (i * i) // 2
            is_prime_odd[start : sieve_size : i] = bytearray((sieve_size - 1 - start) // i + 1)

    def check(num):
        if num < 2: return False
        if num == 2: return True
        if num % 2 == 0: return False
        return is_prime_odd[num // 2]
    while True:
        try:
            n = int(input())
        except EOFError:break
        found = False
        if n % 2 == 1:
            p1, p2 = 2, n - 2
            if p2 > 2 and check(p2):
                print(f"{n} is the sum of {p1} and {p2}.")
                found = True
        else:
            start_p1 = (n - 1) // 2
            if start_p1 > 1:
                if start_p1 % 2 == 0: start_p1 -= 1
                
                for p1 in range(start_p1, 2, -2):
                    p2 = n - p1
                    if is_prime_odd[p1 // 2] and check(p2):
                        print(f"{n} is the sum of {p1} and {p2}.")
                        found = True
                        break
                if not found and check(n - 2):
                    print(f"{n} is the sum of 2 and {n - 2}.")
                    found = True
        if not found:
            print(f"{n} is not the sum of two primes!")

if __name__ == "__main__":
    solve()
