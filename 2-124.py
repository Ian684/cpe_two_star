def generate_catalan():
    catalan = [1]*(28)
    supercatalan = [1]*(28)
    for i in range(3 , 28):
        catalan[i] = catalan[i-1]*(4*i-6) // i
        supercatalan[i] = (3*(2*i-3)*supercatalan[i-1] - (i-3)*supercatalan[i-2])// i
    return catalan , supercatalan
def main():
    catalan , supercatalan = generate_catalan()
    while True:
        try:
            n = int(input())
        except EOFError:break
        print(supercatalan[n]-catalan[n])
if __name__ == "__main__":
    main()
