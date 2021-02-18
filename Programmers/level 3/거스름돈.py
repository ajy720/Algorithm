def solution(n, money):
    answer = 0

    money.sort()
    dp = [[0] * (n+1) for _ in ' '*len(money)]

    for i in range(len(money)):
        dp[i][0] = 1
        for j in range(1, n+1):
            if j >= money[i]:
                dp[i][j] += dp[i][j-money[i]]
            if i > 0:
                dp[i][j] += dp[i-1][j]

    return dp[-1][-1]


if __name__ == '__main__':
    print(solution(5, [1, 2, 5]))
