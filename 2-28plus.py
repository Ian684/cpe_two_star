arr = (113,131,197,199,311,337,373,719,733,919,971,991,1193,1931,3119,3779,7793,7937,9311,9377,11939,19391,19937,37199,39119,71993,91193,93719,93911,99371,193939,199933,319993,331999,391939,393919,919393,933199,939193,939391,993319,999331)
while True:
        num = input()
        if num == '-1':break
        numi , numj = map(int , num.split())
        count = 0
        for i in arr:
                if numi <= i <= numj:
                        count += 1
        if count == 0:
                print(f'No Circular Primes.')
        elif count == 1:
                print(f'{count} Circular Prime.')
        else:
                print(f'{count} Circular Primes.')