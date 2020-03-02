def nCm(n, m):
    if m == 0: return 1
    if m > n or m < 0: return 0

    if m > n//2: m = n-m

    son = mom = 1

    for i in range(0, m): 
        son *= n-i
        mom *= i+1

    return son//mom

if __name__ == "__main__":
    n, m = map(int, input().split())

    c = nCm(n, m)

    print(c)