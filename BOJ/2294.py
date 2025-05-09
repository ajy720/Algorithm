from sys import maxsize

if __name__ == "__main__":
    n, k = map(int, input().split())

    arr = sorted([int(input()) for _ in range(n)])

    dp = [0] + [maxsize] * (k)

    for i in range(1, k + 1):
        for x in arr:
            if i - x >= 0:
                dp[i] = min(dp[i], dp[i - x] + 1)

    print(dp[k] if dp[k] != maxsize else -1)
