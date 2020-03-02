def nCm(n, m):
    if m == 0: return 1
    if m > n or m < 0: return 0

    if m > n//2: m = n-m

    son = mom = 1

    for i in range(n, n-m, -1): son *= i
    for i in range(1, m+1, 1): mom *= i

    return son//mom

if __name__ == "__main__":
    n, m = map(int, input().split())

    c = nCm(n, m)
    ans = 0
    while c % 10 == 0:
        ans += 1
        c//=10
        
    print(ans)