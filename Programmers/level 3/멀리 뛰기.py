def solution(n):
    dp = [0] * (n+3)
    dp[0] = 1

    for i in range(n+1):
        dp[i+1] = (dp[i+1] + dp[i]) % 1234567
        dp[i+2] = (dp[i+2] + dp[i]) % 1234567

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
