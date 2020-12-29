
def solution(n):
    dp = [1] * (n + 1)

    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    return dp[n]


if __name__ == "__main__":
    n = 4
    print(solution(n))
    n = 12412
    print(solution(n))
    n = 5903
    print(solution(n))
    n = 60000
    print(solution(n))
