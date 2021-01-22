def solution(land):
    n = len(land)
    dp = [[0] * 4 for i in range(n)]
    dp[0] = land[0]

    for i in range(1, n):
        for j in range(4):
            dp[i][j] = max([dp[i-1][k] + land[i][j]
                            for k in range(4) if j != k])

    return max(dp[-1])


if __name__ == "__main__":
    print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
