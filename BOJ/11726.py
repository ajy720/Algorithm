def nCm(n, m):
    if m == 0: return 1
    if m > n or m < 0: return 0

    if m > n // 2: m = n - m

    son = mom = 1

    for i in range(0, m):
        son = son * (n - i)
        mom = mom * (i + 1)

    return son // mom


if __name__ == "__main__":
    n = int(input())
    ans = 0

    for i in range(0, n + 1, 2):
        v, h = i // 2, n - i
        ans += nCm(v + h, min(v, h))
        ans %= 10007

    print(f'{n} : {ans}')
