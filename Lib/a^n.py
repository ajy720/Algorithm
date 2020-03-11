def pow(a, n):
    if n == 0: return 1

    if n % 2 == 0: return pow(a, n//2)**2
    else: return a*pow(a, n-1)

if __name__ == "__main__":
    a, n = map(int, input().split())

    p = pow(a, n)

    print(p)