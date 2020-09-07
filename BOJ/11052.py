if __name__ == "__main__":
    n = int(input())
    t = [0] + [*map(int, input().split())]
    dp = [0]

    for i in range(1, n+1):
        dp.append(max([dp[j] + t[i-j] for j in range(i)]))

    print(dp[n])
