if __name__ == "__main__":
    n = int(input())
    dp = [1, 2] + [0] * (n-1)

    for i in range(2, n):
        dp[i] =  (dp[i-1] + dp[i-2]) % 10007

    print(dp[n-1])
